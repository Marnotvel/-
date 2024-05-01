from load_random_word import load_random_word
from Player import Player
from BasicWord import BasicWord


def main():
    username = input('Введите имя игрока: ')
    user_player = Player(username)
    basic_word = load_random_word()

    print(basic_word)

    print(f'Привет, {username}!')
    print(f'Составьте {basic_word.subword_counting()} слов из слова {basic_word}')
    print('Слова должны быть не короче 3 букв')
    print('Чтобы закончить игру, угадайте все слова или напишите "stop"')
    print('Поехали, ваше первое слово?')

    while user_player.word_count() < basic_word.subword_counting():
        answer = input()

        if answer in ('stop', 'стоп'):
            break

        if len(answer) < 3:
            print('слишком короткое слово')
            continue

        if not basic_word.examination(answer):
            print('неверно')
            continue

        if user_player.usage_check(answer):
            print('уже использовано')
            continue

        print('верно! дальше ')
        user_player.adding_word(answer)

    print(f'Игра завершена! Вы угадали {user_player.word_count()} слов!')


if __name__ == "__main__":
    main()
