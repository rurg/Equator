

class No_token(Exception):# Класс обработки исключения - первый введенный символ - не операнд
    def __init__(self, text, num):
        self.txt = text
        self.n = num

OPERATORS = {'+': (lambda x, y: x + y), '-': (lambda x, y: x - y),
             '*': (lambda x, y: x * y), '/': (lambda x, y: x / y)}

def polish():
    expression = input('Введите выражение в прямой польской нотации (н-р: + 2 2)').split()
    token = expression[0]

    try:
        if token in OPERATORS:
            y, x = int(expression.pop()), int(expression.pop())  # забираем 2 числа -  последние элементы всегда числа
            result = OPERATORS[token](x,y) # вычисление значения выражения
            print(f'Значение введенного выражения: {result}')
        else:
            raise No_token('Ошибка: Вы ввели что-то не то, какую то возмутительную билиберду:',token)
    except No_token as Nt:
        print(Nt)
    except ZeroDivisionError:
        print('Ошибка: Деление на "0"')
    except ValueError:
        print('Ошибка: Введены буквы вместо цифр')


polish()
"""
try:
    numb = 100/0

except ZeroDivisionError:
    print('на ноль не делит')
    numb = 100
print(numb)

price = '2'
try:
    if price < 3:
        print('zer gut valdemar')

#except :
#    print ('huyston we have any problrm')
except Exception as e:
    print(e)

print('by')"""
