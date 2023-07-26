from random import randint


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
START = -99
FINISH = 99


def is_prime(number):
    if number < 1:
        return False
    for divider in range(2, int(number / 2) + 1):
        if number % divider == 0:
            return False
    return True


def give_question():
    random_number = randint(START, FINISH)
    if is_prime(random_number) is True:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    expression = f'{random_number}'
    return expression, right_answer
