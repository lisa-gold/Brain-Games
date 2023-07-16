from brain_games.all_games import greet
from brain_games.games.brain_gcd_game import introduce_rules
from brain_games.games.brain_gcd_game import give_question
from brain_games.games.brain_gcd_game import right_answer
from brain_games.all_games import check_answer


def main():
    name = greet(introduce_rules)
    check_answer(give_question, right_answer, name)


if __name__ == '__main__':
    main()
