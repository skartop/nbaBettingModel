import os

import pandas as pd


def updateSpreads(year):
    spreadData = pd.read_csv("../data/spreads/%d.csv" % year)
    matchupData = pd.read_csv("../data/matchups/%d.csv" % year)

    for i in range(int(len(spreadData) / 2)):
        team1_spread = spreadData.iloc[(i * 2)]
        team2_spread = spreadData.iloc[(i * 2 + 1)]
        favorite = team1_spread if float(team1_spread['ML']) < 0 else team2_spread
        dog = team1_spread if float(team1_spread['ML']) > 0 else team2_spread

        if str(favorite['Close']).lower() == 'pk':
            closingTotal = dog['Close']
            closingSpread = 0
        elif str(dog['Close']).lower() == 'pk':
            closingTotal = favorite['Close']
            closingSpread = 0
        elif float(favorite['Close']) < float(dog['Close']):
            closingTotal = dog['Close']
            closingSpread = favorite['Close']
        else:
            closingTotal = favorite['Close']
            closingSpread = dog['Close']

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
                closingSpread = 0 - float(closingSpread)

            matchupData.loc[team1_matchup, 'favorite'] = favorite_name
            matchupData.loc[team1_matchup, 'spread'] = closingSpread
            matchupData.loc[team1_matchup, 'total'] = closingTotal
            if closingSpread != 0:
                matchupData.loc[team1_matchup, 'cover'] = 1 if float(
                    matchupData.loc[team1_matchup, 'winner'].iloc[0]) + float(closingSpread) >= 0 else 0
            else:
                matchupData.loc[team1_matchup, 'cover'] = 1 if float(
                    matchupData.loc[team1_matchup, 'winner'].iloc[0]) >= 0 else 0
            matchupData.loc[team1_matchup, 'over'] = 1 if float(
                matchupData.loc[team1_matchup, 'home_points'].iloc[0]) + float(
                matchupData.loc[team1_matchup, 'visitor_points'].iloc[0]) >= float(closingTotal) else 0

    matchupData.to_csv("../data/matchups/%d.csv" % year)


def convertXlsxToCsv(year):
    #2010 = nba odds 2009-10.xlsx
    read_file = pd.read_excel('../data/spreads/xlsx/nba odds 20%s-%s.xlsx' % (str(year - 2001).zfill(2), str(year - 2000).zfill(2)))
    read_file.to_csv('../data/spreads/%d.csv' % year, index=None, header=True)
