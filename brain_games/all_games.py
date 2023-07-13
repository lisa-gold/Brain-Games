import prompt
from brain_games.cli import welcome_user


# number of correct answers needed
NUMBER_OF_TRIES = 3


def greet():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    return name


def accept_users_answer():
    user_answer = prompt.string('Your answer: ')
    return user_answer


def is_integer(data):
    if (data.isnumeric() is True
            or (data[0] == '-' and data[1:].isnumeric() is True)):
        return True
