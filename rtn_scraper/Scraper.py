import requests
import json
from enum import Enum

# Define constant URLs
BASE_URL = 'https://www.roadtonationals.com/'
RESULTS_URL = 'api/%s/results/%s/%s/%s/%s'
FINAL_RESULTS_URL = 'api/%s/finalresults/%s'
CURRENT_WEEK_URL = 'api/%s/currentweek/%s'
HA_DIFF_URL = 'api/%s/homeaway/%s'
ROSTER_URL = 'api/%s/rostermain/%s/%s/1'

class ScraperEnums(Enum):
	'''Constants used to make scraping calls'''
	TEAM = 0
	INDIVIDUAL = 1
	MENS = 'men'
	WOMENS = 'women'

class Events(Enum):
	'''Events used to make scraping calls'''
	FX_Mens = 1
	PH = 2
	SR = 3
	VT_Mens = 4
	PB = 5
	HB = 6
	AA_Mens = 7
	VT_Womens = 1
	UB = 2
	BB = 3
	FX_Womens = 4
	AA_Womens = 5

# Main scraper object
class Scraper(object):
	'''Scraper of RoadToNationals website'''

	def __init__(self):
		# Create HTTP session for making requests
		self.session = requests.Session()
		# TODO: Add User-Agent randomization to avoid detection
		self.session.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}

	def get_current_and_max_week(self, gender, year):
		response = self.session.get(BASE_URL + (CURRENT_WEEK_URL % (gender.value, year)))
		return json.loads(response.text)

	def get_results(self, gender, year, week_number, team_or_individual, event):
		response = self.session.get(BASE_URL + (RESULTS_URL % (gender.value, year, week_number, team_or_individual.value, event.value)))
		return json.loads(response.text)

	def get_final_results(self, gender, year):
		response = self.session.get(BASE_URL + (FINAL_RESULTS_URL % (gender.value, year)))
		return json.loads(response.text)
	
	def get_home_away_diff(self, gender, year):
		response = self.session.get(BASE_URL + (HA_DIFF_URL % (gender.value, year)))
		return json.loads(response.text)

	def get_roster(self, gender, year, team_id):
		response = self.session.get(BASE_URL + (ROSTER_URL % (gender.value, year, team_id)))
		return json.loads(response.text)
