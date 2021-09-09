#! usr/bin/env python3.9
import time
import random
import requests
from Notification import Notification
from Race import Race


class RaceChecker:
    processed_races: list
    class_number: int

    def __init__(self, class_number: int) -> None:
        self.processed_races = []
        self.class_number = class_number

    def get_json_data(self) -> list:
        url = f'https://racing-api.zed.run/api/v1/races?class={self.class_number}&status=open'
        response = requests.get(url=url)
        return response.json()

    def loop_through_race_data(self):
        race_data = self.get_json_data()
        for race in race_data:
            r = Race(single_race=race)
            if r.fee == 0.0 and r.race_url not in self.processed_races:
                print('Race with free entry found: ', r.name)
                n = Notification()
                n.send_email(race=r)
                self.processed_races.append(r.race_url)


if __name__ == '__main__':
    number = int(input('Fill in class number: '))
    app = RaceChecker(class_number=number)
    while True:
        app.loop_through_race_data()
        wait_time = random.randint(a=1, b=3)
        time.sleep(wait_time)

