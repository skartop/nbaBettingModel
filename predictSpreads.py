import os
import keras
import pandas as pd
from matchup import Matchup
from DataPullers.teamStatPuller import PullTeamStats


def strip_first_col(fname, delimiter=None):
    with open(fname, 'r') as fin:
        for line in fin:
            try:
               yield line.split(delimiter, 2)[2]
            except IndexError:
               continue

def predictGame(team1, team2, spread):
    global fd, predictions
    matchup = Matchup(team1, team2, spread=spread)
    os.remove('predictionMatchup.csv')
    header = "home_team," + \
             "visitor_team," + \
             "home_points," + \
             "visitor_points," + \
             "winner," + \
             "favorite," + \
             "spread," + \
             "total," + \
             "cover," + \
             "over," + \
             "date," + \
             "age_diff," + \
             "sos_diff," + \
             "srs_diff," + \
             "off_rtg_diff," + \
             "def_rtg_diff," + \
             "net_rtg_diff," + \
             "pace_diff," + \
             "fta_per_fga_pct_diff," + \
             "fg3a_per_fga_pct_diff," + \
             "ts_pct_diff," + \
             "efg_pct_diff," + \
             "tov_pct_diff," + \
             "orb_pct_diff," + \
             "ft_rate_diff," + \
             "opp_efg_pct_diff," + \
             "opp_tov_pct_diff," + \
             "drb_pct_diff," + \
             "opp_ft_rate_diff" + '\n'
    with open('predictionMatchup.csv', 'a') as fd:
        fd.write(header)
        fd.write(matchup.getCSVString())
        fd.write(matchup.getCSVString())
    dataset = pd.read_csv('predictionMatchup.csv', delimiter=',')
    dataset = dataset.drop(['home_team',
                            'visitor_team',
                            'home_points',
                            'visitor_points',
                            'favorite',
                            'total',
                            'cover',
                            'winner',
                            'over',
                            'date'], axis=1)
    dataset = dataset.to_numpy()
    predictions = model.predict_classes(dataset)
    return '%s %s %s \nPick: %s\n\n' % (team1.team_name, spread, team2.team_name, team1.team_name if predictions[0] else team2.team_name)


def findTeam(team_name):
    if team_name[-1] == '*':
        team_name = team_name[:-1]
    for team in league:
        if team_name.lower().replace(" ","") in team.team_name.lower().replace(" ",""):
            return team

model = keras.models.load_model('spreadpredictionmodel')
league = PullTeamStats(2020)


