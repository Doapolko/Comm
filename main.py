import ctypes
import winsound
import time

# Константы
CORRECT_PASSWORD = "1234"
CORRECT_LOCK_PASSWORD = "5678"
CHAR_LIST = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def lock_screen():
    try:
        print("Экран заблокирован")
        ctypes.windll.user32.LockWorkStation()
        print("Отправлена команда Win+L")
        winsound.Beep(500, 500)  # 500 Гц, 0.5 сек
    except Exception as e:
        print(f"Ошибка блокировки: {e}")

def unlock_signal():
    print("Введите пароль на ПК")
    winsound.Beep(500, 500)  # 500 Гц, 0.5 сек

def check_username(username):
    print(f"Проверяется username: @{username}")
    print("Откройте Telegram и введите @{username} в поиске.")
    print("Если пользователь найден, username занят. Если нет, он, вероятно, свободен.")
    winsound.Beep(500, 500)  # 500 Гц, 0.5 сек

def main():
    input_string = ""
    current_char = "0"
    char_index = 0
    mode = "password"

    while True:
        print(f"\nТекущий режим: {mode}")
        print(f"Текущий символ: {current_char}")
        print(f"Ввод: {input_string}")
        print("Действия: (1) Переключить символ, (2) Добавить символ, (3) Сбросить ввод, (4) Сменить режим, (5) Выход")
        action = input("Выберите действие (1-5): ")

        if action == "1":  # Переключить символ
            if mode == "password":
                char_index = (char_index + 1) % 10
                current_char = str(char_index)
            else:
                char_index = (char_index + 1) % 36
                current_char = CHAR_LIST[char_index]
            print(f"Символ: {current_char}")

        elif action == "2":  # Добавить символ
            input_string += current_char
            print(f"Ввод: {input_string}")
            if mode == "password" and len(input_string) == 4:
                if input_string == CORRECT_PASSWORD:
                    unlock_signal()
                elif input_string == CORRECT_LOCK_PASSWORD:
                    lock_screen()
                else:
                    print("Неверный пароль")
                input_string = ""
            elif mode == "username" and len(input_string) >= 5:
                check_username(input_string)
                input_string = ""

        elif action == "3":  # Сбросить ввод
            input_string = ""
            print("Ввод сброшен")

        elif action == "4":  # Сменить режим
            mode = "username" if mode == "password" else "password"
            input_string = ""
            current_char = "0"
            char_index = 0
            print(f"Режим изменён на: {mode}")

        elif action == "5":  # Выход
            print("Программа завершена")
            break

        else:
            print("Неверное действие, выберите 1-5")

if __name__ == "__main__":
    main()