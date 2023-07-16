from random import randint


def introduce_rules():
    print('What is the result of the expression?')


def give_question():
    random_number_1 = randint(0, 99)
    random_number_2 = randint(0, 99)
    random_operation_index = randint(1, 3)
    match random_operation_index:
        case 1:
            random_operation = '+'
        case 2:
            random_operation = '-'
        case 3:
            random_operation = '*'
    print(f'Question: {random_number_1} {random_operation} {random_number_2}')
    return random_number_1, random_operation, random_number_2


def right_answer(arr):
    number_1 = arr[0]
    operator = arr[1]
    number_2 = arr[2]
    match operator:
        case '+':
            right_answer = number_1 + number_2
        case '-':
            right_answer = number_1 - number_2
        case '*':
            right_answer = number_1 * number_2
    return right_answer
