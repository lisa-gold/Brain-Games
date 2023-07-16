from random import randint
from math import gcd


def introduce_rules():
    print('Find the greatest common divisor of given numbers.')


def give_question():
    random_number_1 = randint(1, 99)
    random_number_2 = randint(1, 99)
    print(f'Question: {random_number_1} {random_number_2}')
    return random_number_1, random_number_2


def right_answer(arr):
    number_1 = arr[0]
    number_2 = arr[1]
    right_answer = gcd(number_1, number_2)
    return right_answer
