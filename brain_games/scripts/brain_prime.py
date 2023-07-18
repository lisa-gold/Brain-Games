from brain_games.games.brain_prime_game import RULES
from brain_games.games.brain_prime_game import give_question
from brain_games.all_games import play_game


def main():
    play_game(RULES, give_question)


if __name__ == '__main__':
    main()
