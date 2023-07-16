from random import randint


def introduce_rules():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def give_question():
    random_number = randint(1, 99)
    print(f'Question: {random_number}')
    return random_number


def right_answer(arr):
    number = arr
    result = 0
    for divider in range(2, int(number / 2)):
        if number % divider == 0:
            result = 1
            break
        continue

    if result == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return right_answer
