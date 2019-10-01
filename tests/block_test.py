import sys
import pandas
import traceback

import play_scraper

class Block:
    def __init__(self, company):
        self.company = company

    def find_app_id(self, found):
        app_id = []
        for data in list(found):
            if data.has_key("app_id"):
                app_id.append(data["app_id"])

        return app_id

    def search(self):
        # Read the company name from csv url
        url = "https://raw.githubusercontent.com/connor11528/tech-companies-bay-area/master/Bay-Area-Companies-List.csv"
        content = pandas.read_csv(url)
        data = {}
        
        if "Company Name" in sorted(content):        
            for company in content["Company Name"]:
                data[company] = []
        
        for company in list(data):
            try:
                found = play_scraper.search(company, page=2)
                data[company] = self.find_app_id(found)
            except Exception as e:
                traceback.print_exc()
                data["error"] = str(e)
                continue

        return data

    def run(self):
        try:
            return self.search()
        except:
            return None
