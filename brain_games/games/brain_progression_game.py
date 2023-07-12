from random import randint
from brain_games.all_games import number_of_tries
from brain_games.all_games import accept_users_answer


def introduce_rules():
    print('What number is missing in the progression?')


def show_progression(arr):
    result_to_show = ''
    for i in range(len(arr)):
        result_to_show = result_to_show + str(arr[i]) + ' '
    return result_to_show

def give_question():
    random_number_1 = randint(0, 99)
    random_progressor = randint(0, 9)
    random_lenth = randint(5, 15)
    random_operation_index = randint(1, 2)
    result = [random_number_1]
    if random_operation_index == 1:
        for i in range(1, random_lenth):
            new_value = random_number_1 + random_progressor * i
            result.append(new_value)
    else:
        for i in range(1, random_lenth):
            new_value = random_number_1 - random_progressor * i
            result.append(new_value)
    random_place = randint(0, random_lenth - 1)
    result_clone = result[:]
    result_clone[random_place] = '..'
    result_to_show = show_progression(result_clone)
    print(f'Question: {result_to_show}')
    return result, random_place


def check_answer(users_name):
    i = 1
    while i <= number_of_tries:
        question = give_question()
        answer = int(accept_users_answer())
        random_place = question[1]
        right_answer = question[0][random_place]
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
