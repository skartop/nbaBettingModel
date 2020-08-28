import csv
from datetime import datetime

from predictSpreads import findTeam, predictGame

predictions = []
date = "2020-08-30"

team1 = findTeam("boston")
team2 = findTeam("raptors")

predictions.append(predictGame(team1, team2, 2.0))

team1 = findTeam("clippers")
team2 = findTeam("dallas")

predictions.append(predictGame(team1, team2, -9.5))

team1 = findTeam("nuggets")
team2 = findTeam("jazz")

predictions.append(predictGame(team1, team2, 2.5))

fileName = 'predictions/spreads/%s.txt' % date

with open(fileName, 'w') as f:
    f.writelines(predictions)
f.close()