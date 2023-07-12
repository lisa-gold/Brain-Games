from brain_games.all_games import greet
from brain_games.cli import welcome_user
from brain_games.games.brain_gcd_game import introduce_rules
from brain_games.games.brain_gcd_game import check_answer


def main():
    greet()
    name = welcome_user()
    introduce_rules()
    check_answer(name)


if __name__ == '__main__':
    main()
