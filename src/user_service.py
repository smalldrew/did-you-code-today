from github_scraper import check

USERS = {
    'placeholder username': 0000000000,
}


def check_users(user_data: dict) -> None:
    for username, phone_number in user_data.items():
        check(username, phone_number)


if __name__ == '__main__':
    check_users(USERS)
