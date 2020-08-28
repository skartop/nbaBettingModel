class Matchup():
    def __init__(self, team1, team2, team1points=0, team2points=0, date=0, spread=0):
        self.visitor_team = team2
        self.home_team = team1
        self.home_points = team1points
        self.visitor_points = team2points
        self.winner = int(team1points) - int(team2points)

        self.age_diff = float(self.home_team.age) - float(self.visitor_team.age)
        self.sos_diff = float(self.home_team.sos) - float(self.visitor_team.sos)
        self.srs_diff = float(self.home_team.srs) - float(self.visitor_team.srs)
        self.off_rtg_diff = float(self.home_team.off_rtg) - float(self.visitor_team.off_rtg)
        self.def_rtg_diff = float(self.home_team.def_rtg) - float(self.visitor_team.def_rtg)
        self.net_rtg_diff = float(self.home_team.net_rtg) - float(self.visitor_team.net_rtg)
        self.pace_diff = float(self.home_team.pace) - float(self.visitor_team.pace)
        self.fta_per_fga_pct_diff = float(self.home_team.fta_per_fga_pct) - float(self.visitor_team.fta_per_fga_pct)
        self.fg3a_per_fga_pct_diff = float(self.home_team.fg3a_per_fga_pct) - float(self.visitor_team.fg3a_per_fga_pct)
        self.ts_pct_diff = float(self.home_team.ts_pct) - float(self.visitor_team.ts_pct)
        self.efg_pct_diff = float(self.home_team.efg_pct) - float(self.visitor_team.efg_pct)
        self.tov_pct_diff = float(self.home_team.tov_pct) - float(self.visitor_team.tov_pct)
        self.orb_pct_diff = float(self.home_team.orb_pct) - float(self.visitor_team.orb_pct)
        self.ft_rate_diff = float(self.home_team.ft_rate) - float(self.visitor_team.ft_rate)
        self.opp_efg_pct_diff = float(self.home_team.opp_efg_pct) - float(self.visitor_team.opp_efg_pct)
        self.opp_tov_pct_diff = float(self.home_team.opp_tov_pct) - float(self.visitor_team.opp_tov_pct)
        self.drb_pct_diff = float(self.home_team.drb_pct) - float(self.visitor_team.drb_pct)
        self.opp_ft_rate_diff = float(self.home_team.opp_ft_rate) - float(self.visitor_team.opp_ft_rate)

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
        with open('matchups/%dmatchups.csv' % year, 'a') as fd:
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
               str(self.age_diff) + "," + \
               str(self.sos_diff) + "," + \
               str(self.srs_diff) + "," + \
               str(self.off_rtg_diff) + "," + \
               str(self.def_rtg_diff) + "," + \
               str(self.net_rtg_diff) + "," + \
               str(self.pace_diff) + "," + \
               str(self.fta_per_fga_pct_diff) + "," + \
               str(self.fg3a_per_fga_pct_diff) + "," + \
               str(self.ts_pct_diff) + "," + \
               str(self.efg_pct_diff) + "," + \
               str(self.tov_pct_diff) + "," + \
               str(self.orb_pct_diff) + "," + \
               str(self.ft_rate_diff) + "," + \
               str(self.opp_efg_pct_diff) + "," + \
               str(self.opp_tov_pct_diff) + "," + \
               str(self.drb_pct_diff) + "," + \
               str(self.opp_ft_rate_diff) + '\n'
