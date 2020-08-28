from predictSpreads import findTeam, predictGame

team1 = findTeam("clippers")
team2 = findTeam("dallas")

predictGame(team1, team2, -8.5)

team1 = findTeam("denver")
team2 = findTeam("utah")

predictGame(team1, team2, 3)