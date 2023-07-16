import prompt


# number of correct answers needed
NUMBER_OF_TRIES = 3


def greet(introduce_rules):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    introduce_rules()
    return name


def is_integer(data):
    if (data.isnumeric() is True
            or (data[0] == '-' and data[1:].isnumeric() is True)):
        return int(data)
    return data


def check_answer(give_question, right_answer, users_name):
    i = 1
    while i <= NUMBER_OF_TRIES:
        question = give_question()
        user_answer = is_integer(prompt.string('Your answer: '))
        correct_answer = right_answer(question)

        if correct_answer == user_answer:
            print('Correct!')
            i = i + 1
            continue
        else:
            print(f'''
'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'
Let\'s try again, {users_name}!
            ''')
            return
            break
    return print(f'Congratulations, {users_name}!')
