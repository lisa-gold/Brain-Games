from random import randint
from math import gcd


RULES = 'Find the greatest common divisor of given numbers.'


def generate_question_and_answer():
    random_number_1 = randint(1, 99)
    random_number_2 = randint(1, 99)
    right_answer = gcd(random_number_1, random_number_2)
    expression = f'{random_number_1} {random_number_2}'
    return expression, str(right_answer)
