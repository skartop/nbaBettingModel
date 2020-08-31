import requests
from bs4 import BeautifulSoup

from matchup import Matchup

urls = ['https://www.basketball-reference.com/leagues/NBA_%d_games-october.html',
        'https://www.basketball-reference.com/leagues/NBA_%d_games-november.html',
        'https://www.basketball-reference.com/leagues/NBA_%d_games-december.html',
        'https://www.basketball-reference.com/leagues/NBA_%d_games-january.html',
        'https://www.basketball-reference.com/leagues/NBA_%d_games-february.html',
        'https://www.basketball-reference.com/leagues/NBA_%d_games-march.html',
        'https://www.basketball-reference.com/leagues/NBA_%d_games-april.html',
        'https://www.basketball-reference.com/leagues/NBA_%d_games-may.html',
        'https://www.basketball-reference.com/leagues/NBA_%d_games-june.html',
        'https://www.basketball-reference.com/leagues/NBA_%d_games-august.html',
        'https://www.basketball-reference.com/leagues/NBA_%d_games-september.html']

urls_2012 = [
        'https://www.basketball-reference.com/leagues/NBA_%d_games-december.html',
        'https://www.basketball-reference.com/leagues/NBA_%d_games-january.html',
        'https://www.basketball-reference.com/leagues/NBA_%d_games-february.html',
        'https://www.basketball-reference.com/leagues/NBA_%d_games-march.html',
        'https://www.basketball-reference.com/leagues/NBA_%d_games-april.html',
        'https://www.basketball-reference.com/leagues/NBA_%d_games-may.html',
        'https://www.basketball-reference.com/leagues/NBA_%d_games-june.html']


urls_2020 = ['https://www.basketball-reference.com/leagues/NBA_%d_games-october.html',
        'https://www.basketball-reference.com/leagues/NBA_%d_games-november.html',
        'https://www.basketball-reference.com/leagues/NBA_%d_games-december.html',
        'https://www.basketball-reference.com/leagues/NBA_%d_games-january.html',
        'https://www.basketball-reference.com/leagues/NBA_%d_games-february.html',
        'https://www.basketball-reference.com/leagues/NBA_%d_games-march.html',
        'https://www.basketball-reference.com/leagues/NBA_%d_games-july.html',
        'https://www.basketball-reference.com/leagues/NBA_%d_games-august.html',
        'https://www.basketball-reference.com/leagues/NBA_%d_games-september.html']

def getDate(param):
    param = param.split(',')[1]
    month = param.split(' ')[1]
    day = param.split(' ')[2]
    day = day if int(day) > 9 else "0%s" % day
    switcher = {
        "Jan": "1",
        "Feb": "2",
        "Mar": "3",
        "Apr": "4",
        "May": "5",
        "Jun": "6",
        "Jul": "7",
        "Aug": "8",
        "Sep": "9",
        "Oct": "10",
        "Nov": "11",
        "Dec": "12"
    }
    return switcher.get(month)+day

def pullMatchups(year, league):
    global urls
    matchups = []
    if year == 2020:
        urls = urls_2020
    elif year == 2012:
        urls = urls_2012
    for url in urls:
        response = requests.get(url % year)
        soup = BeautifulSoup(response.text, "html.parser")
        soup.prettify()
        matchup_table = soup.findAll('div', {"id": "all_schedule"})
        try:
            matchup_table = matchup_table[0].contents[3].contents[1].contents[1].contents[6]
        except IndexError:
            break

        for el in matchup_table.contents:
            if len(el) > 1:
                if el.contents[3].text.strip() != "":
                    visitor_team = findTeam(league, el.contents[2].text.strip())
                    visitor_pts = el.contents[3].text.strip()
                    home_team = findTeam(league, el.contents[4].text.strip())
                    home_pts = el.contents[5].text.strip()
                    date = getDate(el.contents[0].text.strip())
                    matchups.append(Matchup(home_team, visitor_team, home_pts, visitor_pts, date))
    return matchups


def findTeam(league, team_name):
    if team_name[-1] == '*':
        team_name = team_name[:-1]
    for team in league:
        if team.team_name == team_name:
            return team
