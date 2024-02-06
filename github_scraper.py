# This version is probably better than the API method
import requests
import util.SMS as SMS
from datetime import date
from bs4 import BeautifulSoup


USERNAME = 'smalldrew'  # put your username here
PHONE_NUMBER = 0000000000  # put your phone number here

def check_code_today(username: str) -> bool:
    """Check if a user with the given username has made any commits on GitHub today."""

    url = f'https://github.com/{username}' 
    response = requests.get(url)

    if response.status_code == 200:
        web_scrape = BeautifulSoup(response.content, 'html.parser')
        commit_box = web_scrape.find('td', {'data-date': str(date.today())})      
        data_level = commit_box['data-level']

        return False if data_level == '0' else True
    return None


def check(username: str, phone_number: int) -> None:
    """Sends a message if you didn't code. Otherwise, it sends a good job message."""
    if check_code_today(username):
        print(f'{username} coded today.')
        SMS.send_text('Good job. You coded today.', phone_number)
        print('Sent good job message.\n')
    else:
        print(f'{username} did not code today')
        SMS.send_text('You did not code today. Go code right now.', phone_number)
        print('Sent a reminder\n')


if __name__ == '__main__':
    check(USERNAME, PHONE_NUMBER)
