import prompt


# number of correct answers needed
number_of_tries = 3


def greet():
    print('Welcome to the Brain Games!')


def accept_users_answer():
    user_answer = prompt.string('Your answer: ')
    return user_answer
