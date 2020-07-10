import unittest
from rtn_scraper import Scraper, ScraperConstants, ScraperException, MensEvents, WomensEvents

class Test_ScraperException(unittest.TestCase):
    def test_get_current_and_max_week_invalid_gender(self):
        scraper = Scraper()
        self.assertRaises(ScraperException, scraper.get_current_and_max_week, 'Invalid gender', 2018)

    def test_get_current_and_max_week_men_year_too_low(self):
        scraper = Scraper()
        self.assertRaises(ScraperException, scraper.get_current_and_max_week, ScraperConstants.Men, 2010)

    def test_get_current_and_max_week_women_year_too_low(self):
        scraper = Scraper()
        self.assertRaises(ScraperException, scraper.get_current_and_max_week, ScraperConstants.Women, 1990)

    def test_get_current_and_max_week_year_too_high(self):
        scraper = Scraper()
        self.assertRaises(ScraperException, scraper.get_current_and_max_week, ScraperConstants.Men, 10000)

    def test_get_results_invalid_gender(self):
        scraper = Scraper()
        self.assertRaises(ScraperException, scraper.get_results, 'Invalid gender', 2018, 1, ScraperConstants.Team, MensEvents.Vault)

    def test_get_results_men_year_too_low(self):
        scraper = Scraper()
        self.assertRaises(ScraperException, scraper.get_results, ScraperConstants.Men, 2010, 1, ScraperConstants.Team, MensEvents.Vault)

    def test_get_results_women_year_too_low(self):
        scraper = Scraper()
        self.assertRaises(ScraperException, scraper.get_results, ScraperConstants.Women, 1990, 1, ScraperConstants.Team, WomensEvents.Vault)

    def test_get_results_year_too_high(self):
        scraper = Scraper()
        self.assertRaises(ScraperException, scraper.get_results, ScraperConstants.Women, 10000, 1, ScraperConstants.Team, WomensEvents.Vault)

    def test_get_results_invalid_event_men(self):
        scraper = Scraper()
        self.assertRaises(ScraperException, scraper.get_results, ScraperConstants.Men, 2018, 1, ScraperConstants.Team, WomensEvents.Vault)

    def test_get_results_invalid_event_women(self):
        scraper = Scraper()
        self.assertRaises(ScraperException, scraper.get_results, ScraperConstants.Women, 2018, 1, ScraperConstants.Team, MensEvents.Vault)

    def test_get_results_invalid_week_number_men(self):
        scraper = Scraper()
        self.assertRaises(ScraperException, scraper.get_results, ScraperConstants.Men, 2018, 100, ScraperConstants.Team, MensEvents.Vault)

    def test_get_results_invalid_week_number_women(self):
        scraper = Scraper()
        self.assertRaises(ScraperException, scraper.get_results, ScraperConstants.Women, 2018, 100, ScraperConstants.Team, WomensEvents.Vault)

    def test_get_final_results_invalid_gender(self):
        scraper = Scraper()
        self.assertRaises(ScraperException, scraper.get_final_results, 'Invalid gender', 2018)

    def test_get_final_results_men_year_too_low(self):
        scraper = Scraper()
        self.assertRaises(ScraperException, scraper.get_final_results, ScraperConstants.Men, 2010)

    def test_get_final_results_women_year_too_low(self):
        scraper = Scraper()
        self.assertRaises(ScraperException, scraper.get_final_results, ScraperConstants.Women, 1990)

    def test_get_final_results_year_too_high(self):
        scraper = Scraper()
        self.assertRaises(ScraperException, scraper.get_final_results, ScraperConstants.Men, 10000)

    def test_get_home_away_diff_invalid_gender(self):
        scraper = Scraper()
        self.assertRaises(ScraperException, scraper.get_home_away_diff, 'Invalid gender', 2018)

    def test_get_home_away_diff_men_year_too_low(self):
        scraper = Scraper()
        self.assertRaises(ScraperException, scraper.get_home_away_diff, ScraperConstants.Men, 2010)

    def test_get_home_away_diff_women_year_too_low(self):
        scraper = Scraper()
        self.assertRaises(ScraperException, scraper.get_home_away_diff, ScraperConstants.Women, 1990)

    def test_get_home_away_diff_year_too_high(self):
        scraper = Scraper()
        self.assertRaises(ScraperException, scraper.get_home_away_diff, ScraperConstants.Men, 10000)

    def test_get_roster_invalid_gender(self):
        scraper = Scraper()
        self.assertRaises(ScraperException, scraper.get_roster, 'Invalid gender', 2018, 51)

    def test_get_roster_invalid_year(self):
        scraper = Scraper()
        self.assertRaises(ScraperException, scraper.get_roster, ScraperConstants.Men, 1990, 51)

    def test_get_roster_invalid_team_id(self):
        scraper = Scraper()
        self.assertRaises(ScraperException, scraper.get_roster, ScraperConstants.Men, 1990, -1)

    def test_get_gymnast_meet_results_invalid_gender(self):
        scraper = Scraper()
        self.assertRaises(ScraperException, scraper.get_gymnast_meet_results, 'Invalid gender', 2018, 6838)

    def test_get_gymnast_meet_invalid_year(self):
        scraper = Scraper()
        self.assertRaises(ScraperException, scraper.get_gymnast_meet_results, ScraperConstants.Men, 2014, 6838)

    def test_get_gymnast_meet_invalid_gymnast_id(self):
        scraper = Scraper()
        self.assertRaises(ScraperException, scraper.get_gymnast_meet_results, ScraperConstants.Men, 2018, -1)

if __name__ == '__main__':
    unittest.main()
