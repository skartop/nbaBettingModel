import os

from DataPullers.matchupPuller import PullMatchups
from DataPullers.spreadPuller import updateSpreads
from DataPullers.teamStatPuller import PullTeamStats

yearList = range(2009, 2021, 1)
# yearList = [2015]
for year in yearList:
    if (year == 2012):
        continue
    try:
        os.remove("teams/%dteams.csv" % year)
    except:
        pass
    league = PullTeamStats(year)
    for team in league:
        team.printMatchupToCSV(year)

    try:
        os.remove("matchups/%dmatchups.csv" % year)
    except:
        pass
    matchups = PullMatchups(year, league)
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
             "opp_ft_rate_diff"+'\n'
    with open('matchups/%dmatchups.csv' % year, 'a') as fd:
        fd.write(header)
    for matchup in matchups:
        matchup.printMatchupToCSV(year)

    # try:
    updateSpreads(year)
    # except:
    # # except Exception as w:
    # #     print(str(w))
    #     pass
