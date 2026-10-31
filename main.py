import random
import notes_data

random.seed(24762876)

def show_help():
    print(notes_data.HELP_TEXT)

def add_note(notes, text, sep=";"):
    if text == "":
        print("Ошибка: текст заметки не указан.")
        return notes

    if notes == "":
        notes = text
    else:
        notes = notes + sep + text

    print("Заметка добавлена.")

    return notes

def list_notes(notes):
    if notes == "":
        print("Заметок пока нет.")
    else:
        print("Ваши заметки:")

        current_note = ""

        for symbol in notes:
            if symbol == notes_data.DEFAULT_SEPARATOR:
                print(current_note)
                current_note = ""
            else:
                current_note = current_note + symbol

        if current_note != "":
            print(current_note)

def find_note(notes, word):
    if word == "":
        print("Ошибка: укажите слово для поиска.")
        return

    if word in notes:
        print("Найдено.")
    else:
        print("Не найдено.")

def random_tip():
    number = random.randint(1, 4)

    if number == 1:
        print(notes_data.TIP_1)
    elif number == 2:
        print(notes_data.TIP_2)
    elif number == 3:
        print(notes_data.TIP_3)
    else:
        print(notes_data.TIP_4)

notes = ""

print(notes_data.APP_NAME)
show_help()

while True:
    command = input("> ")

    if command == "exit":
        print("Программа завершена.")
        break

    elif command == "help":
        show_help()

    elif command == "list":
        list_notes(notes)

    elif command == "clear":
        notes = ""
        print("Все заметки удалены.")

    elif command == "tip":
        random_tip()

    elif command[:4] == "add ":
        text = command[4:]
        notes = add_note(notes, text)

    elif command[:5] == "find ":
        word = command[5:]
        find_note(notes, word)

    elif command == "":
        print("Ошибка: введите команду.")

    else:
        print("Неизвестная команда.")