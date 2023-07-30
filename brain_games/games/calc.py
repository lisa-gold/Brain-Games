from random import randint
from random import choice

RULES = 'What is the result of the expression?'


def generate_question_and_answer():
    random_number_1 = randint(0, 99)
    random_number_2 = randint(0, 99)
    random_operator = choice('+-*')
    match random_operator:
        case '+':
            right_answer = random_number_1 + random_number_2
        case '-':
            right_answer = random_number_1 - random_number_2
        case '*':
            right_answer = random_number_1 * random_number_2
    expression = f'{random_number_1} {random_operator} {random_number_2}'
    return expression, str(right_answer)
