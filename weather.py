def get_temperature():
    while True:
        try:
            temperature = float(input("Введите температуру (-50 до 50): "))
            if -50 <= temperature <= 50:
                return temperature
            else:
                print("Ошибка: введите число в диапазоне от -50 до 50.")
        except ValueError:
            print("Ошибка: введите числовое значение.")

def get_binary_input(prompt):
    while True:
        try:
            print(prompt)
            choice = int(input("Введите 1 (да) или 2 (нет): "))
            if choice == 1 or choice == 2:
                return choice - 1
            else:
                print("Ошибка: введите только 1 или 2.")
        except ValueError:
            print("Ошибка: введите только 1 или 2.")

temperature = get_temperature()

if 20 < temperature < 30:
    has_osadki = get_binary_input("Есть осадки?")
    if not has_osadki:
        print("Наденьте футболку, шорты и дождевик.")
    else:
        print("Наденьте футболку и шорты.")
elif 0 < temperature <= 20:
    has_osadki = get_binary_input("Есть осадки?")
    if not has_osadki:
        heavy_osadki = get_binary_input("Осадки сильные?")
        if not heavy_osadki:
            print("Наденьте пальто, резиновые сапоги и зонт.")
        else:
            print("Наденьте пальто и дождевик.")
    else:
        print("Наденьте пальто.")
else:
    if temperature >= 30:
        print("Можете ничего не надевать")
    else:
        print("Наденьте пуховик.")
