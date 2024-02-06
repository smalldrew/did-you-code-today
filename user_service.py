from github_scraper import check

USERS = {
    'smalldrew': 0000000000,  # put your username and phone number here
}


def check_users(user_data: dict) -> None:
    for username, phone_number in user_data.items():
        check(username, phone_number)


if __name__ == '__main__':
    check_users(USERS)
