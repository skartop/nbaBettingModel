import os

import pandas as pd


def updateSpreads(year):
    spreadData = pd.read_csv("spreads/%dspreads.csv" % year)
    matchupData = pd.read_csv("matchups/%dmatchups.csv" % year)

    for i in range(int(len(spreadData) / 2)):
        team1_spread = spreadData.iloc[(i * 2)]
        team2_spread = spreadData.iloc[(i * 2 + 1)]
        favorite = team1_spread if float(team1_spread['ML']) < 0 else team2_spread
        dog = team1_spread if float(team1_spread['ML']) > 0 else team2_spread

        if favorite['Open'].lower() == 'pk':
            openingTotal = dog['Open']
            openingSpread = 0
        elif dog['Open'].lower() == 'pk':
            openingTotal = favorite['Open']
            openingSpread = 0
        elif float(favorite['Open']) < float(dog['Open']):
            openingTotal = dog['Open']
            openingSpread = favorite['Open']
        else:
            openingTotal = favorite['Open']
            openingSpread = dog['Open']

        date = team1_spread['Date']
        favorite_name = favorite['Team']
        dog_name = dog['Team']
        team1_matchup = matchupData.loc[matchupData['date'] == date]
        team1_matchup = team1_matchup.loc[team1_matchup['home_team'].str.contains(favorite_name.lower()) |
                                          team1_matchup['visitor_team'].str.contains(favorite_name.lower()) |
                                          team1_matchup['home_team'].str.contains(dog_name.lower()) |
                                          team1_matchup['visitor_team'].str.contains(dog_name.lower())].index.tolist()

        if len(matchupData.loc[team1_matchup, 'home_team']) > 0:
            if favorite_name.lower() in matchupData.loc[team1_matchup, 'home_team'].iloc[0]:
                openingSpread = 0 - float(openingSpread)

            matchupData.loc[team1_matchup, 'favorite'] = favorite_name
            matchupData.loc[team1_matchup, 'spread'] = openingSpread
            matchupData.loc[team1_matchup, 'total'] = openingTotal
            if openingSpread != 0:
                matchupData.loc[team1_matchup, 'cover'] = 1 if float(
                    matchupData.loc[team1_matchup, 'winner'].iloc[0]) + float(openingSpread) >= 0 else 0
            else:
                matchupData.loc[team1_matchup, 'cover'] = 1 if float(
                    matchupData.loc[team1_matchup, 'winner'].iloc[0]) >= 0 else 0
            matchupData.loc[team1_matchup, 'over'] = 1 if float(
                matchupData.loc[team1_matchup, 'home_points'].iloc[0]) + float(
                matchupData.loc[team1_matchup, 'visitor_points'].iloc[0]) >= float(openingTotal) else 0

    matchupData.to_csv("matchups/%dmatchups.csv" % year)


def convertXlsxToCsv(year):
    read_file = pd.read_excel('spreads/%dspreads.xlsx' % year)
    read_file.to_csv('spreads/%dspreads.csv' % year, index=None, header=True)
