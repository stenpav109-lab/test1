def calc(expression):
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
        result = a / b
    else:
        return f"ошибка"
    return result

print(calc("(33,2):+"))
print(calc("(3,3):*"))
print(calc("(10,5):-"))
print(calc("(8,2):/"))
