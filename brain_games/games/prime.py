from random import randint
from math import sqrt


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number <= 1:
        return False
    for divider in range(2, int(sqrt(number) + 1)):
        if number % divider == 0:
            return False
    return True


def generate_question_and_answer():
    random_number = randint(-99, 99)
    if is_prime(random_number):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    expression = f'{random_number}'
    return expression, right_answer
