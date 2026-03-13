def calc1():
        operation = input("введите операцию: ")
        a = float(input("первое число: "))
        b = float(input("второе число: "))

        if operation == '+':
            result = a + b
        elif operation == '-':
            result = a - b
        elif operation == '*':
            result = a * b
        elif operation == '/':
            if b == 0:
                print("ошибка")
                return
            result = a / b
        else:
            print("ошибка")
            return

        print(f"результат: {result}")


def calc2(expression):
        numbers_part, operation = expression.split(':')
        numbers_str = numbers_part.strip('()')
        a, b = map(float, numbers_str.split(','))

        if operation == '+':
            result = a + b
        elif operation == '-':
            result = a - b
        elif operation == '*':
            result = a * b
        elif operation == '/':
            if b == 0:
                return "oшибка"
            result = a / b
        else:
            return f"шибка"

        return result


def main():
    while True:
        print("0 - exit")
        print("1 - калькулятор (ввести знак и два числа)")
        print("2 - enter line (a,b):op)")

        choice = input("выберите действие: ")

        if choice == '0':
            break

        elif choice == '1':
            print("ввод знака и двух чисел")
            calc1()

        elif choice == '2':
            print("ввод строки формата (a,b):op ---")
            expression = input("введите выражение: ")
            result = calc2(expression)
            print(f"результат: {result}")

        else:
            print("ошибка")

if __name__ == "__main__":
    main()
