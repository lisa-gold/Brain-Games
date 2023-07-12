from random import randint
from brain_games.all_games import number_of_tries
from brain_games.all_games import accept_users_answer


def introduce_rules():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def give_question():
    random_number = randint(1, 99)
    print(f'Question: {random_number}')
    return random_number


def check_answer(users_name):
    i = 1
    while i <= number_of_tries:
        question = give_question()
        number = question
        answer = accept_users_answer()

        result = 0
        for divider in range(2, int(number/2)):
            if number % divider == 0:
                result = 1
                break
            else:
                continue

        if result == 0:
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
