#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests

query = input("Do you want to see just the live results? [y/n] ")

if query == "y":
    mix = "https://www.livescores.com/soccer/live/"
else:
    mix = "https://www.livescores.com/"

headers = {
    'User-Agent':  'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0',
}

r = requests.get(mix, headers=headers)

if r.status_code == 200:
    print("\033[33mFetching results... \n")

else:
    print("Connection with Livescores.com not established. \n")

html = r
soup = BeautifulSoup(html.content, "html.parser")

# Define what to search for
# If on extra time - names will  be 'None'
home_team = soup.find_all(class_="FootballMatchRow_home__2jnn7")
away_team = soup.find_all(class_="FootballMatchRow_away__12Br8")

home_score = soup.find_all(class_="FootballMatchRow_score__home__2-xt3")
away_score = soup.find_all(class_="FootballMatchRow_score__away__30bhM")

homes = []
aways = []
home_goals = []
away_goals = []

# Get the text from found  results
for home in home_team:
    # print(home.string)
    homes.append(home.string)

for i in home_score:
    # print(i.string)
    home_goals.append(i.string)

for j in away_score:
    # print(j.string)
    away_goals.append(j.string)

for away in away_team:
    # print(away.string)
    aways.append(away.string)

# Format and print results
for home, home_score, away_score, away in zip(homes, home_goals, away_goals, aways):

	print(f' {home} {home_score} - {away_score} {away}')

print("\033[33m \nGood luck to your team.")
