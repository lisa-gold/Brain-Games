from random import randint


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    for divider in range(2, int(number / 2) + 1):
        if number % divider == 0:
            return False
            break
        continue
    return True


def give_question():
    random_number = randint(1, 99)
    match is_prime(random_number):
        case True:
            right_answer = 'yes'
        case False:
            right_answer = 'no'
    expression = f'{random_number}'
    return expression, right_answer
