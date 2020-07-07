from rtn_scraper import Scraper
from rtn_scraper import Events
from rtn_scraper import ScraperEnums
from rtn_scraper import Team
from rtn_scraper import Gymnast

import time

start = time.time()

teams = []

scraper = Scraper()
results = scraper.get_home_away_diff(ScraperEnums.MENS, 2020)

for team in results:
	teams.append(Team(team['team_id'], team['team_name']))

for team in teams:
	results = scraper.get_roster(ScraperEnums.MENS, 2020, team.id)
	for gymnast in results:
		team.roster.append(Gymnast(gymnast['id'], gymnast['tid'], gymnast['fname'].strip() + ' ' + gymnast['lname']))

for team in teams:
	print('%s:' % team.name)
	for gymnast in team.roster:
		print(gymnast)
	print()

print("Took %s seconds to run" % (time.time() - start))