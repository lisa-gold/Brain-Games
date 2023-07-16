from brain_games.cli import welcome_user
from brain_games.check_users_answer import check_answer


def introduce_rules():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def main():
    name = welcome_user()
    introduce_rules()
    check_answer(name)


if __name__ == '__main__':
    main()
