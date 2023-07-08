import prompt
from random import randint


# number of correct answers needed
number_of_tries = 3


def give_question():
    random_number = randint(0, 999)
    print(f'Question: {random_number}')
    return random_number


def accept_users_answer():
    user_answer = prompt.string('Your answer: ')
    return user_answer


def right_answer():
    if give_question() % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return right_answer


def check_answer(users_name):
    i = 1
    while i <= number_of_tries:
        number = give_question()
        answer = accept_users_answer()

        if number % 2 == 0:
            right_answer = 'yes'
        else:
            right_answer = 'no'

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
