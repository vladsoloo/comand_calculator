def main():
    print("Простой калькулятор")
    print("Доступные операции: +, -, *, /")

    while True:
        try:

            num1 = float(input("Введите первое число: "))
            operator = input("Введите оператор (+, -, *, /): ")
            num2 = float(input("Введите второе число: "))

            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("Ошибка: Деление на ноль!")
                    continue
                result = num1 / num2
            else:
                print("Ошибка: Неверный оператор!")
                continue

            print(f"Результат: {num1} {operator} {num2} = {result}")

            again = input("Хотите выполнить еще одно вычисление? (да/нет): ")
            if again.lower() != 'да':
                print("Спасибо за использование калькулятора!")
                break

        except ValueError:
            print("Ошибка: Пожалуйста, введите корректное число!")
            continue


if __name__ == 'main':
    main()
