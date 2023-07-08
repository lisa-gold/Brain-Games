from random import randint
from brain_games.all_games import number_of_tries
from brain_games.all_games import accept_users_answer


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


def check_answer(users_name):
    i = 1
    while i <= number_of_tries:
        question = give_question()
        number_1 = question[0]
        number_2 = question[2]
        operator = question[1]
        answer = int(accept_users_answer())

        match operator:
            case '+':
                right_answer = number_1 + number_2
            case '-':
                right_answer = number_1 - number_2
            case '*':
                right_answer = number_1 * number_2

        if right_answer == answer:
            print('Correct!')
            i = i + 1
            continue
        else:
            print(f'''
            {answer} is wrong answer ;(. Correct answer was {right_answer}
            Let\'s try again, {users_name}!
            ''')
            i = 1
            continue

    return print(f'Congratulations, {users_name}!')
