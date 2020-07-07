from rtn_scraper import Scraper
from rtn_scraper import Events
from rtn_scraper import ScraperEnums
from rtn_scraper import Team
from rtn_scraper import Gymnast
from rtn_scraper import MeetScore

import pickle, os

import time

start = time.time()

teams = []

scraper = Scraper()
results = scraper.get_home_away_diff(ScraperEnums.MENS, 2020)

for team in results:
	teams.append(Team(team['team_id'], team['team_name']))

counter = 1
num_gymnasts = 0
for team in teams:
	print('[%s/%s] Getting roster for %s' % (counter, len(teams), team.name))
	counter = counter + 1
	results = scraper.get_roster(ScraperEnums.MENS, 2020, team.id)
	for gymnast in results:
		team.roster.append(Gymnast(gymnast['id'], gymnast['tid'], gymnast['fname'].strip() + ' ' + gymnast['lname']))
	num_gymnasts = num_gymnasts + len(team.roster)

counter = 1
for team in teams:
	for gymnast in team.roster:
		print('[%s/%s] Getting results for %s' % (counter, num_gymnasts, gymnast.name))
		counter = counter + 1
		results = scraper.get_gymnast_results(ScraperEnums.MENS, 2020, gymnast.id)['meets']
		for meet in results:
			gymnast.meets.append(MeetScore(meet['meet_date'], ph=meet['phorse'], fx=meet['floor'], sr=meet['rings'], vt=meet['vault'], pb=meet['pbars'], hb=meet['highbar'], aa=meet['all_around']))


pickle.dump(teams, open('teams.p', 'wb'))

print("Took %s seconds to run" % (time.time() - start))
