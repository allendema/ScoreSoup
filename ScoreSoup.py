#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests

query = input("Do you want to see just the live results? [y/n] ")

if query == "y":
	mix = "https://www.livescores.com/soccer/live/"
else:
	mix = "https://www.livescores.com/"



headers = {
    'User-Agent': '"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0',
}

r = requests.get(mix, headers = headers)

if r.status_code == 200:
	print("\033[33mFetching results... \n")
	
else:
	print("Connection with Livescores.com not established. \n")

html = r

soup = BeautifulSoup(html.content, "html.parser")

home_team = soup.find_all(class_="ply tright name")
away_team = soup.find_all(class_="ply name")
score = soup.find_all(class_="scorelink")

# Next update should be with .string.strip() from home_team etc. without lists.

homes = []
aways = []
goals = []

for home in home_team:
	#print(home.string)
	homes.append(home.string)

for i in score:
	#print(i.string)
	goals.append(i.string)

for away in away_team:
	#print(away.string)
	aways.append(away.string)
	

	
for home, score, away in zip(homes, goals, aways):
	print("{0} {1} {2}".format(home, score, away))
	
print("\033[33m \n Good luck to your team.")
