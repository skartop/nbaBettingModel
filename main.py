import csv
from datetime import datetime

from predictSpreads import findTeam, predictGame

predictions = []
date = "2020-09-04"

team1 = findTeam("rockets")
team2 = findTeam("lakers")

predictions.append(predictGame(team1, team2, 6))

team1 = findTeam("bucks")
team2 = findTeam("heat")

predictions.append(predictGame(team1, team2, -5.5))

fileName = 'predictions/spreads/%s.txt' % date

with open(fileName, 'w') as f:
    f.writelines(predictions)
f.close()