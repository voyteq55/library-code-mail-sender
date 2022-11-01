import datetime
import os
import requests


class DateChecker:

    def __init__(self):
        sheety_api_url = os.environ["SHEETY_API_URL"]
        api_response = requests.get(url=sheety_api_url)
        table = api_response.json()["arkusz1"]

        current_year = datetime.date.today().year
        self.possible_dates = []
        for row in table:
            day = int(row["date"][:2])
            month = int(row["date"][3:5])
            year = current_year
            new_date = datetime.date(year, month, day)
            self.possible_dates.append(new_date)

    def can_send_today(self):
        todays_date = datetime.date.today()
        for possible_date in self.possible_dates:
            if todays_date == possible_date:
                return True
        return False
