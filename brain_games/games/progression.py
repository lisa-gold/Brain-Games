from random import randint


RULES = 'What number is missing in the progression?'
MAX_LENGTH = 15
MIN_LENGTH = 5


def generate_progression(first_number, length, progressor):
    result = [first_number]
    for i in range(1, length):
        new_value = first_number + progressor * i
        result.append(new_value)
    return result


def give_question():
    # генерация прогрессии
    number = randint(-99, 99)
    random_progressor = randint(-9, 9)
    random_length = randint(MIN_LENGTH, MAX_LENGTH)
    progression = generate_progression(number, random_length, random_progressor)

    # скрытие элемента прогрессии
    random_place = randint(0, random_length - 1)
    progres_clone = progression[:]
    progres_clone[random_place] = '..'
    progression_to_show = ''
    for i in range(random_length):
        progression_to_show = progression_to_show + str(progres_clone[i]) + ' '

    expression = f'{progression_to_show}'
    right_answer = progression[random_place]
    return expression, str(right_answer)
