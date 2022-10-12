from utils import load_random_word
from player import Player
""" Импортируем функции """

DATA_SOURCE = "https://api.npoint.io/18de9dbc99f2eaae7a67"
""" Получаем адрес с словами """

user_name = input("Ввведите имя игрока: ")
""" Ввод имени игрока """

player = Player(user_name)
print(f"Привет, {player.get_name()}!")
""" Сохраняем имя через функцию """

basic_word = load_random_word(DATA_SOURCE)
print(f"Составьте {basic_word.coutnt_sub_word()} слов из слова {basic_word.get_word()}")
print("Слова должны быть не короче 3 букв")
""" Получаем случайное слово """


while player.count_used_words() < basic_word.coutnt_sub_word():
    """ Запускаем цыкл проверки слов """

    user_input = input().strip().lower()

    if user_input in ["stop", "стоп"]:
        break

    elif len(user_input) < 3:
        print("Короткое слово")
        continue

    elif not basic_word.has_sub_word(user_input):
        print("Нет такого слова")

    elif player.is_word_user(user_input):
        print("Слово уже использовано")

    else:
        print("Верно")
        player.add_word(user_input)

print(f"Игра завершена, вы угадали {player.count_used_words()} слов!")
