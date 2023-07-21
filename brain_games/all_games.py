import prompt


# number of correct answers needed
NUMBER_OF_TRIES = 3


def play_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULES)
    for i in range(0, NUMBER_OF_TRIES):
        question = game.give_question()
        expression = ''
        for element in question[:-1]:
            expression = f'{expression}{element} '
        print(f'Question: {expression}')
        user_answer = prompt.string('Your answer: ')
        correct_answer = question[-1]

        if correct_answer == user_answer:
            print('Correct!')
            continue
        else:
            print(f'''
'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'
Let\'s try again, {name}!
            ''')
            return
            break
    return print(f'Congratulations, {name}!')
