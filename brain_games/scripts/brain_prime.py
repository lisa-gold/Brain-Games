from brain_games.all_games import greet
from brain_games.games.brain_prime_game import introduce_rules
from brain_games.games.brain_prime_game import check_answer


def main():
    name = greet()
    introduce_rules()
    check_answer(name)


if __name__ == '__main__':
    main()
