from random import randint


RULES = 'What number is missing in the progression?'
MAX_LENGTH = 15
MIN_LENGTH = 5


def show_progression(length, arr):
    random_place = randint(0, length - 1)
    arr_clone = arr[:]
    arr_clone[random_place] = '..'
    result_to_show = ''
    for i in range(length):
        result_to_show = result_to_show + str(arr_clone[i]) + ' '
    return result_to_show, random_place


def generate_progression(first_number, length, progressor):
    result = [first_number]
    for i in range(1, length):
        new_value = first_number + progressor * i
        result.append(new_value)
    return result


def give_question():
    number = randint(-99, 99)
    random_progressor = randint(-9, 9)
    random_length = randint(MIN_LENGTH, MAX_LENGTH)
    result = generate_progression(number, random_length, random_progressor)
    progression = show_progression(random_length, result)
    place = progression[1]
    right_answer = result[place]
    expression = f'{progression[0]}'
    return expression, str(right_answer)
