#!/usr/bin/env python3.9
import smtplib
import ssl
from Race import Race


def create_message(race: Race) -> str:
    message = f'''
    Free Zed.Run race has been found.

    Name:                 {race.name}
    Distance:             {race.distance}
    Free Gates:          {race.empty_gates}
    Zed.Run url:         {race.race_url}
    Fee (ETH):           {race.fee}
    '''
    return message


class Notification:
    sender: str
    receiver: str
    password: str
    port: int
    context: ssl.create_default_context

    def __init__(self):
        self.sender = '**********'
        self.receiver = '********'
        self.password = '*******'
        self.port = 465
        self.context = ssl.create_default_context()

    def send_email(self, race: Race):
        message = create_message(race=race)
        with smtplib.SMTP_SSL('smtp.gmail.com', self.port, context=self.context) as server:
            server.login(self.sender, self.password)
            server.sendmail(self.sender, self.receiver, message)

