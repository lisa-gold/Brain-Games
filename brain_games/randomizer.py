from random import randint


def give_question():
    random_number = randint(0, 999)
    print(f'Question: {random_number}')
    return random_number
