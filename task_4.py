def input_error(func):
    """
    Декоратор для обробки помилок введення.
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Дайте мені ім'я та телефон, будь ласка."
        except KeyError:
            return "Контакт не знайдено."
        except IndexError:
            return "Введіть ім'я користувача."
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

@input_error
def add_contact(args, contacts):
    # Ця перевірка може викликати помилку, якщо аргументів недостатньо
    name, phone = args
    contacts[name] = phone
    return "Контакт додано."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Контакт оновлено."

@input_error
def show_phone(args, contacts):
    name = args[0]
    return contacts[name]

def show_all(contacts):
    if not contacts:
        return "Контакти не збережено."
    # Виводимо всі контакти
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    contacts = {}
    print("Ласкаво просимо до бота-помічника!")
    while True:
        user_input = input("Введіть команду: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit", "вихід"]:
            print("До побачення!")
            break
        elif command == "hello" or command == "привіт":
            print("Чим я можу допомогти?")
        elif command == "add": print(add_contact(args, contacts))
        elif command == "change": print(change_contact(args, contacts))
        elif command == "phone": print(show_phone(args, contacts))
        elif command == "all": print(show_all(contacts))
        else: print("Невірна команда.")

if __name__ == "__main__":
    main()