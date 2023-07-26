from random import randint


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def give_question():
    random_number = randint(0, 999)
    if random_number % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    expression = f'{random_number}'
    return expression, right_answer
