from random import randint
from random import choice

RULES = 'What is the result of the expression?'


def give_question():
    random_number_1 = randint(0, 99)
    random_number_2 = randint(0, 99)
    random_operator = choice('+-*')
    right_answer = random_number_1
    match random_operator:
        case 1:
            random_operator = '+'
            right_answer = right_answer + random_number_2
        case 2:
            random_operator = '-'
            right_answer = right_answer - random_number_2
        case 3:
            random_operator = '*'
            right_answer = right_answer * random_number_2
    expression = f'{random_number_1} {random_operator} {random_number_2}'
    return expression, str(right_answer)
