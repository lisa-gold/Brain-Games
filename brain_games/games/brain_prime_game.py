from random import randint


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def give_question():
    random_number = randint(1, 99)
    result = 0
    for divider in range(2, int(random_number / 2) + 1):
        if random_number % divider == 0:
            result = 1
            break
        continue

    if result == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'

    return random_number, right_answer
