import os


class Matchup():
    def __init__(self, team1, team2, team1points=0, team2points=0, date=0, spread=0):
        self.visitor_team = team2
        self.home_team = team1
        self.home_points = team1points
        self.visitor_points = team2points
        self.winner = int(team1points) - int(team2points)

        self.age_diff = round((float(self.home_team.age) - float(self.visitor_team.age)), 3)
        self.sos_diff = round((float(self.home_team.sos) - float(self.visitor_team.sos)), 3)
        self.srs_diff = round((float(self.home_team.srs) - float(self.visitor_team.srs)), 3)
        self.off_rtg_diff = round((float(self.home_team.off_rtg) - float(self.visitor_team.off_rtg)), 3)
        self.def_rtg_diff = round((float(self.home_team.def_rtg) - float(self.visitor_team.def_rtg)), 3)
        self.net_rtg_diff = round((float(self.home_team.net_rtg) - float(self.visitor_team.net_rtg)), 3)
        self.pace_diff = round((float(self.home_team.pace) - float(self.visitor_team.pace)), 3)
        self.fta_per_fga_pct_diff = round((float(self.home_team.fta_per_fga_pct) - float(self.visitor_team.fta_per_fga_pct)), 3)
        self.fg3a_per_fga_pct_diff = round((float(self.home_team.fg3a_per_fga_pct) - float(self.visitor_team.fg3a_per_fga_pct)), 3)
        self.ts_pct_diff = round((float(self.home_team.ts_pct) - float(self.visitor_team.ts_pct)), 3)
        self.efg_pct_diff = round((float(self.home_team.efg_pct) - float(self.visitor_team.efg_pct)), 3)
        self.tov_pct_diff = round((float(self.home_team.tov_pct) - float(self.visitor_team.tov_pct)), 3)
        self.orb_pct_diff = round((float(self.home_team.orb_pct) - float(self.visitor_team.orb_pct)), 3)
        self.ft_rate_diff = round((float(self.home_team.ft_rate) - float(self.visitor_team.ft_rate)), 3)
        self.opp_efg_pct_diff = round((float(self.home_team.opp_efg_pct) - float(self.visitor_team.opp_efg_pct)), 3)
        self.opp_tov_pct_diff = round((float(self.home_team.opp_tov_pct) - float(self.visitor_team.opp_tov_pct)), 3)
        self.drb_pct_diff = round((float(self.home_team.drb_pct) - float(self.visitor_team.drb_pct)), 3)
        self.opp_ft_rate_diff = round((float(self.home_team.opp_ft_rate) - float(self.visitor_team.opp_ft_rate)), 3)

        self.date = date

        self.total = 0
        self.spread = spread
        self.favorite = 0
        self.cover = 0
        self.over = 0

    def findTeam(self, league, team_name):
        if team_name[-1] == '*':
            team_name = team_name[:-1]
        for team in league:
            if team_name.lower().replace(" ","") in team.team_name.lower().replace(" ",""):
                return team

    def printMatchupToCSV(self, year):
        writepath = "../data/matchups/%d.csv" % year
        mode = 'a' if os.path.exists(writepath) else 'w'
        with open(writepath, mode) as fd:
            fd.write(self.getCSVString())

    def getCSVString(self):
        return str(self.home_team.team_name.lower().replace(' ', '').replace('losangeles', 'la')) + "," + \
               str(self.visitor_team.team_name.lower().replace(' ', '').replace('losangeles', 'la')) + "," + \
               str(self.home_points) + "," + \
               str(self.visitor_points) + "," + \
               str(self.winner) + "," + \
               str(self.favorite) + "," + \
               str(self.spread) + "," + \
               str(self.total) + "," + \
               str(self.cover) + "," + \
               str(self.over) + ", " +\
               str(self.date) + "," + \
               "{:.2f}".format(self.age_diff) + "," + \
               "{:.2f}".format(self.sos_diff) + "," + \
               "{:.2f}".format(self.srs_diff) + "," + \
               "{:.2f}".format(self.off_rtg_diff) + "," + \
               "{:.2f}".format(self.def_rtg_diff) + "," + \
               "{:.2f}".format(self.net_rtg_diff) + "," + \
               "{:.2f}".format(self.pace_diff) + "," + \
               "{:.2f}".format(self.fta_per_fga_pct_diff) + "," + \
               "{:.2f}".format(self.fg3a_per_fga_pct_diff) + "," + \
               "{:.2f}".format(self.ts_pct_diff) + "," + \
               "{:.2f}".format(self.efg_pct_diff) + "," + \
               "{:.2f}".format(self.tov_pct_diff) + "," + \
               "{:.2f}".format(self.orb_pct_diff) + "," + \
               "{:.2f}".format(self.ft_rate_diff) + "," + \
               "{:.2f}".format(self.opp_efg_pct_diff) + "," + \
               "{:.2f}".format(self.opp_tov_pct_diff) + "," + \
               "{:.2f}".format(self.drb_pct_diff) + "," + \
               "{:.2f}".format(self.opp_ft_rate_diff) + '\n'
