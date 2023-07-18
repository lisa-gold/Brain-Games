from random import randint


RULES = 'What is the result of the expression?'


def give_question():
    random_number_1 = randint(0, 99)
    random_number_2 = randint(0, 99)
    random_operation_index = randint(1, 3)
    match random_operation_index:
        case 1:
            random_operation = '+'
            right_answer = random_number_1 + random_number_2
        case 2:
            random_operation = '-'
            right_answer = random_number_1 - random_number_2
        case 3:
            random_operation = '*'
            right_answer = random_number_1 * random_number_2

    return random_number_1, random_operation, random_number_2, right_answer
