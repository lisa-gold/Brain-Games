import prompt
from brain_games.check_users_answer import check_answer


def introduce_rules():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    introduce_rules()
    check_answer(name)


if __name__ == '__main__':
    main()
