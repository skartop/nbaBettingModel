import os

from DataPullers.matchupPuller import pullMatchups
from DataPullers.spreadPuller import updateSpreads
from DataPullers.teamStatPuller import PullTeamStats

yearList = range(2008, 2021)

for year in yearList:
    try:
        os.remove("../data/teams/%d.csv" % year)
    except:
        pass
    league = PullTeamStats(year)
    for team in league:
        team.printMatchupToCSV(year)

    try:
        os.remove("../data/matchups/%d.csv" % year)
    except:
        pass
    matchups = pullMatchups(year, league)
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
    writepath = "../data/matchups/%d.csv" % year
    mode = 'a' if os.path.exists(writepath) else 'w'
    with open(writepath, mode) as fd:
        fd.write(header)
    for matchup in matchups:
        matchup.printMatchupToCSV(year)

    updateSpreads(year)
