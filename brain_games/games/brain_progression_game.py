from random import randint
from brain_games.all_games import NUMBER_OF_TRIES
from brain_games.all_games import accept_users_answer
from brain_games.all_games import is_integer


def introduce_rules():
    print('What number is missing in the progression?')


def show_progression(lenth, arr):
    random_place = randint(0, lenth - 1)
    arr_clone = arr[:]
    arr_clone[random_place] = '..'
    result_to_show = ''
    for i in range(lenth):
        result_to_show = result_to_show + str(arr_clone[i]) + ' '
    print(f'Question: {result_to_show}')
    return result_to_show, random_place


def positive_progression(first_number, lenth, progressor):
    result = [first_number]
    for i in range(1, lenth):
        new_value = first_number + progressor * i
        result.append(new_value)
    return result


def negative_progression(first_number, lenth, progressor):
    result = [first_number]
    for i in range(1, lenth):
        new_value = first_number - progressor * i
        result.append(new_value)
    return result


def give_question():
    number = randint(0, 99)
    random_progressor = randint(0, 9)
    random_lenth = randint(5, 15)
    random_operation_index = randint(1, 2)

    if random_operation_index == 1:
        result = positive_progression(number, random_lenth, random_progressor)
    else:
        result = negative_progression(number, random_lenth, random_progressor)

    progression = show_progression(random_lenth, result)
    place = progression[1]

    return result, place


def check_answer(users_name):
    i = 1
    while i <= NUMBER_OF_TRIES:
        question = give_question()
        random_place = question[1]
        right_answer = question[0][random_place]
        answer = accept_users_answer()

        if is_integer(answer) is True and right_answer == int(answer):
            print('Correct!')
            i = i + 1
            continue
        else:
            print(f'''
'{answer}' is wrong answer ;(. Correct answer was '{right_answer}'
Let\'s try again, {users_name}!
            ''')
            return
            break

    return print(f'Congratulations, {users_name}!')
