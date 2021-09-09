from dataclasses import dataclass


@dataclass
class Race:
    name: str
    distance: int
    empty_gates: int
    fee: float
    race_url: str = 'https://zed.run/race/'

    def __init__(self, single_race: dict) -> None:
        self.name = single_race['name']
        self.distance = single_race['length']
        self.empty_gates = 12 - len(single_race['gates'])
        self.fee = float(single_race['fee'])
        self.race_url += single_race['race_id']

