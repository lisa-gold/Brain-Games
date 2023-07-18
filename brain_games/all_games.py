import prompt


# number of correct answers needed
NUMBER_OF_TRIES = 3


def play_game(RULES, give_question):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(RULES)
    i = 1
    while i <= NUMBER_OF_TRIES:
        question = give_question()
        expression = ''
        for element in question[:-1]:
            expression = f'{expression}{element} '
        print(f'Question: {expression}')
        user_answer = prompt.string('Your answer: ')
        correct_answer = question[-1]

        if str(correct_answer) == user_answer:
            print('Correct!')
            i = i + 1
            continue
        else:
            print(f'''
'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'
Let\'s try again, {name}!
            ''')
            return
            break
    return print(f'Congratulations, {name}!')
