import prompt


# number of correct answers needed
NUMBER_OF_TRIES = 3


def play(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULES)
    for _ in range(0, NUMBER_OF_TRIES):
        question, correct_answer = game.generate_question_and_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if correct_answer != user_answer:
            print(f'''
'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'
Let\'s try again, {name}!
            ''')
            break
        print('Correct!')

    else:
        print(f'Congratulations, {name}!')
