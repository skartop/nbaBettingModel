import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from pyquery import PyQuery

from team import Team

url = 'https://www.basketball-reference.com/leagues/NBA_%d.html'


def PullTeamStats(year):
    response = requests.get(url%year)
    soup = BeautifulSoup(response.text, "html.parser")
    soup.prettify()

    stats_table = soup.find('div', {"id": "all_misc_stats"})
    rows = BeautifulSoup(stats_table.contents[5], "html.parser").findAll('td')
    #30 teams and 24 stat categories
    rank = 1
    league = []
    for i in range(30):
        row = rows[i*27:(i+1)*27]
        team = Team(row)
        league.append(team)
        rank = rank+1
    return league
