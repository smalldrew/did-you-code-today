# This version is probably better than the API method
import requests
import util.SMS as SMS
from datetime import date
from bs4 import BeautifulSoup


USERNAME = 'smalldrew'  # put your username here

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


def check(username: str) -> None:
    """Sends a message if you didn't code. Otherwise, it sends a good job message."""
    if check_code_today(username):
        print('LOG: Sent good job message.')
        SMS.send_text('Good job. You coded today.')
    else:
        print('LOG: Sent angry message.')
        SMS.send_text('GO CODE RIGHT NOW OR YOU WILL DIE.')


if __name__ == '__main__':
    check(USERNAME)
