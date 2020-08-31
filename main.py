import csv
from datetime import datetime

from predictSpreads import findTeam, predictGame

predictions = []
date = "2020-08-31"

team1 = findTeam("heat")
team2 = findTeam("bucks")

predictions.append(predictGame(team1, team2, 5.5))

team1 = findTeam("rockets")
team2 = findTeam("thunder")

predictions.append(predictGame(team1, team2, -5.5))

fileName = 'predictions/spreads/%s.txt' % date

with open(fileName, 'w') as f:
    f.writelines(predictions)
f.close()