from brain_games.all_games import greet
from brain_games.games.brain_calc_game import introduce_rules
from brain_games.games.brain_calc_game import check_answer


def game(name):
    introduce_rules()
    check_answer(name)


def main():
    name = greet()
    game(name)


if __name__ == '__main__':
    main()
