import requests
import json
from enum import Enum

# Define scraping URLs
BASE_URL = 'https://www.roadtonationals.com/'
RESULTS_URL = 'api/%s/results/%s/%s/%s/%s'
FINAL_RESULTS_URL = 'api/%s/finalresults/%s'
CURRENT_WEEK_URL = 'api/%s/currentweek/%s'
HA_DIFF_URL = 'api/%s/homeaway/%s'
ROSTER_URL = 'api/%s/rostermain/%s/%s/1'
GYMNAST_RESULTS_URL = 'api/%s/gymnast/%s/%s'

class ScraperConstants(Enum):
	'''Constants useful for making scraping calls'''
	Team = 0
	Individual = 1
	Mens = 'men'
	Womens = 'women'
	FloorExercise_Mens = 1
	PommelHorse = 2
	StillRings = 3
	Vault_Mens = 4
	ParallelBars = 5
	HighBar = 6
	AllAround_Mens = 7
	Vault_Womens = 1
	UnevenBars = 2
	BalanceBeam = 3
	FloorExercise_Womens = 4
	AllAround_Womens = 5

class Scraper(object):
	'''Scraper of RoadToNationals website'''

	def __init__(self):
		# Create HTTP session for making requests
		self.create_new_session()

	def create_new_session(self):
		self.session = requests.Session()
		self.session.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}

	def get_current_and_max_week(self, gender, year):
		'''
		Gets current season week and maximum week number given the current season year.
		@params
			gender: "men" or "women"
			year: season year
		@returns
			A JSON object with "week" and "max" keys that represent the current season week and max season week
		'''

		response = self.session.get(BASE_URL + (CURRENT_WEEK_URL % (gender.value, year)))
		return json.loads(response.text)

	def get_results(self, gender, year, week_number, team_or_individual, event):
		'''
		Gets team or individual results for certain gender, season, week, and event.
		@params
			gender: "men" or "women"
			year: season year
			week_number: week number of season
			team_or_individual: 0 for team results or 1 for individual results
			event: numerical value depending on gender chosen.
				if "men" specified for gender:
					1->FX, 2->PH, 3->SR, 4->VT, 5->PB, 6->HB, 7->AA
				if "women" specified for gender:
					1->VT, 2->UB, 3->BB, 4->FX, 5->AA
		@returns
			A JSON object with the "data" and "schema" keys. "data" is a dictionary and "schema" is an object. "schema" contains various information about the available years to look through, 
			the current year, the number of weeks available to look through for each year, list of teams, and list of conferences.
			Each element of the "data" array represents the results and has the following keys:
				"rank", "name", "tid", "rqs", "usag", "reg", "con", "ave", and "high"
			The "schema" object has the following keys:
				"year", "years", "weeks", "cons", "teams", and "yearweeks"
		'''
		response = self.session.get(BASE_URL + (RESULTS_URL % (gender.value, year, week_number, team_or_individual.value, event.value)))
		return json.loads(response.text)

	def get_final_results(self, gender, year):
		'''
		Gets final results for the season.
		@params
			gender: "men" or "women"
			year: season year
		@returns
			A JSON object where only key is "data" array. Each element of the "data" array represents a team's final results and is an object containing the following keys:
				"rank", "team_name", "team_id", "ncaa_final", "ncaa", "nqa", "average_score", and "high_score"
		'''
		response = self.session.get(BASE_URL + (FINAL_RESULTS_URL % (gender.value, year)))
		return json.loads(response.text)
	
	def get_home_away_diff(self, gender, year):
		'''
		Gets H/A diff for all teams, useful for obtaining list of all teams.
			@params
				gender: "men" or "women"
				year: season year
			@returns
				Returns JSON array where all teams are an object in the array with the following keys:
					"team_name", "team_id", "avgteam", "maxteam", "homeavg", "awayavg", "counthome", "countaway", and "diff"
		'''
		response = self.session.get(BASE_URL + (HA_DIFF_URL % (gender.value, year)))
		return json.loads(response.text)

	def get_roster(self, gender, year, team_id):
		'''
		Gets roster for a team.
			@params
				gender: "men" or "women"
				year: season year
				team_id: numerical team id
			@returns
				JSON dictionary where each element is an object representing a person on the roster. Each object has the following keys:
					"id", "tid", "lname", "fname", "hometown", "fx", "ph", "sr", "v", "pb", "hb", "school_year", "events"
				where the keys representing events are either "1" or null depending on whether the person does them.
		'''
		response = self.session.get(BASE_URL + (ROSTER_URL % (gender.value, year, team_id)))
		return json.loads(response.text)

	def get_gymnast_meet_results(self, gender, year, gymnast_id):
		'''
		Gets all meet results for a gymnast.
			@params
				gender: "men" or "women"
				year: season year
				gymnast_id: RTN gymnast id
			@returns
				JSON object with "team" and "meets" keys. "team" is a JSON object with information about the team of the gymnast and contains the following keys:
					"fname" == "0", "lname" == "1", "team_name" == "2"
				"meets" is an array where each element is a JSON object representing a meet that contains the following keys for both men and women:
					"fname", "lname", "all_around", "vault", "floor", "meet_date", "date", "home", "opponent", "meet_desc", "vt_url", "fx_url"
				the following keys for men:
					"phorse", "rings", "pbars", "highbar", "ph_url", "sr_url", "pb_url", "hb_url"
				and the following keys for women:
					"bars", "beam", "ub_url", "bb_url"
		'''
		response = self.session.get(BASE_URL + (GYMNAST_RESULTS_URL % (gender.value, year, gymnast_id)))
		return json.loads(response.text)

class ScraperExpection(Exception):
	pass