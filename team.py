import os


class Team:
    def __init__(self, row):
        if row[0].text.strip()[-1] == '*':
            self.team_name = row[0].text.strip()[:-1]
        else:
            self.team_name = row[0].text.strip()
        self.age = row[1].text.strip()
        self.sos = row[7].text.strip()
        self.srs = row[8].text.strip()
        self.off_rtg = row[9].text.strip()
        self.def_rtg = row[10].text.strip()
        self.net_rtg = row[11].text.strip()
        self.pace = row[12].text.strip()
        self.fta_per_fga_pct = row[13].text.strip()
        self.fg3a_per_fga_pct = row[14].text.strip()
        self.ts_pct = row[15].text.strip()
        self.efg_pct = row[16].text.strip()
        self.tov_pct = row[17].text.strip()
        self.orb_pct = row[18].text.strip()
        self.ft_rate = row[19].text.strip()
        self.opp_efg_pct = row[20].text.strip()
        self.opp_tov_pct = row[21].text.strip()
        self.drb_pct = row[22].text.strip()
        self.opp_ft_rate = row[23].text.strip()
        self.date = row[23].text.strip()

        self.schedule = []

    def printMatchupToCSV(self, year):
        csv_row = self.age + "," + \
                  self.sos + "," + \
                  self.srs + "," + \
                  self.off_rtg + "," + \
                  self.def_rtg + "," + \
                  self.net_rtg + "," + \
                  self.pace + "," + \
                  self.fta_per_fga_pct + "," + \
                  self.fg3a_per_fga_pct + "," + \
                  self.ts_pct + "," + \
                  self.efg_pct + "," + \
                  self.tov_pct + "," + \
                  self.orb_pct + "," + \
                  self.ft_rate + "," + \
                  self.opp_efg_pct + "," + \
                  self.opp_tov_pct + "," + \
                  self.drb_pct + "," + \
                  self.opp_ft_rate + '\n'

        writepath = "../data/teams/%d.csv" % year
        mode = 'a' if os.path.exists(writepath) else 'w'
        with open(writepath, mode) as fd:
            fd.write(csv_row)
