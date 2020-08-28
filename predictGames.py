from main import findTeam, predictGame

team1 = findTeam("clippers")
team2 = findTeam("dallas")

predictGame(team1, team2, -8.5)

team2 = findTeam("denver")
team1 = findTeam("utah")

predictGame(team1, team2, 3)
