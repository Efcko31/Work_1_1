
import math
# Лабораторная работа №3


# 1) Найти все простые делители данного натурального числа
n = int(input())
answer = []
d = 2
while d * d <= n:
    if n % d == 0:
        answer.append(d)
        n //= d
    else:
        d += 1
if n > 1:
    answer.append(n)
print(answer)


 2) С клавиатуры вводятся целые числа. Признак конца ввода — ноль.
    Определить число, следующее за последним из введённых минимальных значений.
min_n = 9999999999
answer = 0
isLastNMin = False

def error_checking(number):
    while True:
        if number[1::].isdigit() != True:
            print('ОШИБКА! Введите целое число!')
            number = input()
        else:
            return int(number)

while True:
    n = error_checking(input())
    if n != 0:
        if not f_answer:
            answer = n
        if min_n > n:
            min_n = n
            isLastNMin = True
        else:
            isLastNMin = False
    elif n == 0:
        break
print(answer)


# 3) Дано целое число n, удовлетворяющее условию 0 < |n| <= 2 * 10 ** 9
#  Найти максимальную цифру в записи этого числа.

def error_checking(n):
    while True:
        if n.isdigit() != True:
            print('ОШИБКА! Введите целое число!')
            n = input()
        else:
            if int(n) > 2 * 10 ** 9:
                print('ОШИБКА! Число не должно быть больше 2 * 10 ** 9!')
                n = input()
            else:
                return n
number = error_checking(input())
answer = int(number[0])
for i in range(1, len(number)):
    i_n = int(number[i])
    if i_n > answer:
        answer = i_n
print(answer)


# 4) Определить, является ли данное натуральное число простым числом.

answer = False
n = int(input())
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        answer = True
print('YES' if not answer else 'NO')


# 5) Даны натуральные числа a и b. Определить, могут ли эти числа быть соседними
# членами последовательности Фибоначчи.
a, b = int(input()), int(input())
stopping_the_cycle = False
if a > b:
    a, b = b, a
number_1 = 1
number_2 = 1
answer = False
while number_2 < b:
    number_3 = number_1 + number_2
    number_1, number_2 = number_2, number_3

if number_1 == a and number_2 == b:
    print('Yes')
else:
    print('NO')

# 6) Установить, является ли данное натуральное число n совершенным (равным сумме
# всех его делителей, меньших n)
n = int(input())
answer = 0
for i in range(1, n):
    if n % i == 0:
        answer += i
if answer == n:
    print('YES')
else:
    print('NO')

# 7) С клавиатуры вводятся символы. Признак конца ввода — точка. Определить максимальную длину
#    подпоследовательности одинаковых следующих друг за другом символов.
list_symbol = []
total_symbols = 1
maximum_symbols = 0
symbol_1 = input()

while '.' not in symbol_1:
    symbol_2 = input()
    if len(symbol_2) == 1:
        if symbol_2 == symbol_1:
            total_symbols += 1
        else:
            if maximum_symbols < total_symbols:
                maximum_symbols = total_symbols
            total_symbols = 1
        symbol_1 = symbol_2
    else:
        print("Ошибка! Введите 1 символ!")

print(maximum_symbols)


# 8) не понял как ....


# 9) С клавиатуры вводятся целые числа. Признак конца ввода — ноль.
# Определить число, предшествующее первому из введённых максимальных значений.
def error_checking(n):
    while n:
        if not n.isdigit():
            if not n[1::].isdigit():
                print('ОШИБКА! Введите целое число!')
                n = input()
            else:
                return int(n)
        else:
            return int(n)

symbols = error_checking(input())
maximum_number = symbols
number = symbols
previous_number = 'Нет предыдущего числа'

while symbols != 0:
    number = symbols
    symbols = error_checking(input())
    if maximum_number < symbols:
        maximum_number = symbols
        previous_number = number

print(previous_number)

# 10) Дано целое число n, удовлетворяющее условию 0 < |n| <= 2 * 10 ** 9
# Найти максимальную цифру в записи этого числа.

def error_checking(n):
    while n:
        if n.isdigit():
            if int(n) < 2 * 10 ** 9 and int(n) > 0:
                return list(n)
            else:
                print("ОШИБКА! Условие: 0 < |n| <= 2 * 10 ** 9 !!! ")
                n = input()
number = error_checking(input())
answer = number[0]
for i in range(1, len(number)):
    if answer < number[i]:
        answer = number[i]
print(answer)

# 11) С клавиатуры вводятся символы. Признак конца ввода — точка. Определить символ,
# следующий за последним вхождением цифры.

user_symbol = input()
answer = 'NOTHING'
flag_user_symbol = 'NOTHING'

while user_symbol != '.':
    flag_user_symbol = user_symbol
    user_symbol = input()
    if not user_symbol.isdigit():
        flag_user_symbol = user_symbol
    elif user_symbol.isdigit():
        answer = flag_user_symbol
print(answer)


# 12) С клавиатуры вводятся целые числа. Признак конца ввода — ноль.
# Определить количество введённых нечётных чисел после последнего отрицательного.

user_number = int(input())
total_number_for_answer = 0
counter_on_off = True
while user_number != 0:

    user_number = int(input())
    if not counter_on_off and user_number < 0:
        counter_on_off = True
        total_number_for_answer = 0

    if user_number < 0:
        counter_on_off = False

    if not counter_on_off:
        if user_number % 2 != 0 and user_number > 0:
            total_number_for_answer += 1

print(total_number_for_answer)

# 13) Дано целое неотрицательное число n, удовлетворяющее условию 0 < |n| <= 2 * 10 ** 9 Определить количество нулей,
# которыми заканчивается запись числа n. Вывести n в виде a*10^k, где a — целое, не содержащее нуля в конце записи числа;
# k — количество нулей в конце записи числа n. Например, 130 000 = 13*10^4.

def error_checking(n):
    while n:
        if n.isdigit():
            if int(n) < 2 * 10 ** 9 and int(n) > 0:
                return list(n)
            else:
                print("ОШИБКА! Условие: 0 < |n| <= 2 * 10 ** 9 !!! ")
                n = input()
number = list(error_checking(input()))
number = number[::-1]
flag_zero = True
a = []
k = 0
for i in range(len(number)):
    if number[i] == '0' and flag_zero:
        k += 1
    else:
        a.append(number[i])
        flag_zero = False
a = a[::-1]
print(*a, ' * 10 ^ ', k, sep='')

# 14) С клавиатуры вводятся целые числа. Признак конца ввода — ноль.
# Определить число, следующее за последним из отрицательных чисел.
def error_checking(n):
    while n:
        if not n.isdigit():
            if not n[1::].isdigit():
                print('ОШИБКА! Введите целое число!')
                n = input()
            else:
                return int(n)
        else:
            return int(n)

user_number = error_checking(input())
flag_negative_number = False
answer_for_number = 'NOTHING'

while user_number != 0:
    user_number = error_checking(input())
    if flag_negative_number:
        answer_for_number = user_number
        flag_negative_number = False
    if user_number < 0:
        flag_negative_number = True
print(answer_for_number)


# 15) Дано целое число n, удовлетворяющее условию 0 < |n| <= 2 * 10 ** 9
#     Найти сумму цифр числа n.

def error_checking(n):
    while n:
        if n.isdigit():
            if int(n) < 2 * 10 ** 9 and int(n) > 0:
                return list(n)
            else:
                print("ОШИБКА! Условие: 0 < |n| <= 2 * 10 ** 9 !!! ")
                n = input()

number = error_checking(input())
sum_number = 0
for i in range(len(number)):
    sum_number += int(number[i])
print(sum_number)

# 16) С клавиатуры вводятся вещественные числа. Признак конца ввода — ноль.
# Определить, является ли вводимая последовательность упорядоченной по невозрастанию или по неубыванию.
def error_checking(n):
    while n:
        if not n.isdigit():
            c = n[1::].split('.')
            if len(c) == 2:
                c = c[0] + c[1]
                if not c.isdigit():
                    print('ОШИБКА! Введите вещественное число!')
                    n = input()
                else:
                    return float(n)
            else:
                print('ОШИБКА! Введите вещественное число!')
                n = input()
        else:
            return float(n)
flag_descending = False
flag_ascending = False
user_number = error_checking(input())
previous_number = user_number
while user_number != 0:
    user_number = error_checking(input())
    if user_number != 0:
        if previous_number < user_number:
            flag_ascending = True
        elif previous_number > user_number:
            flag_descending = True
    previous_number = user_number
if flag_ascending + flag_descending != 2:
    if flag_ascending:
        print('Упорядоченна по неубыванию')
    elif flag_descending:
        print('Упорядоченна по невозврастанию')
else:
    print('Никак не упорядоченна')


# 17) С клавиатуры вводятся вещественные числа. Признак конца ввода — ноль.
# Определить, является ли вводимая последовательность арифметической прогрессией.
def error_checking(n):
    while n:
        if not n.isdigit():
            c = n[1::].split('.')
            if len(c) == 2:
                c = c[0] + c[1]
                if not c.isdigit():
                    print('ОШИБКА! Введите вещественное число!')
                    n = input()
                else:
                    return float(n)
            else:
                print('ОШИБКА! Введите вещественное число!')
                n = input()
        else:
            return float(n)

user_number = error_checking(input())
if user_number != 0:
    first_number = user_number
    user_number = error_checking(input())
    
    if user_number != 0:
        second_number = user_number
        difference = first_number - second_number
        flag_arithmetic_progression = True
        
        while user_number != 0:
            user_number = error_checking(input())
            if user_number != 0:
                first_number = user_number
                first_number, second_number = second_number, first_number
                if first_number - second_number != difference:
                    flag_arithmetic_progression = False
            else:
                break
                
        if flag_arithmetic_progression:
            print('Является арифметической прогрессией')
        elif not flag_arithmetic_progression:
            print('Не является арифметической прогрессией')
    else:
        print('NOTHING')
else:
    print('NOTHING')



# 27) Определить, в какой степени входит число 3 в разложение на простые множители
# натурального числа n.

n = int(input())
total_3 = 0
while n > 3:
    if n % 3 == 0:
        n = n // 3
        total_3 += 1
    elif n % 2 == 0:
        n = n // 2
    elif n % 5 == 0:
        n = n // 5
    elif n % 7 == 0:
        n = n // 7
    else:
        n = n / n
print(total_3)



# 29) Получить число n в семеричной системе счисления.

n = int(input())
answer = []
while n > 1:
    a = n % 7
    n = n // 7
    answer.append(a)
print(*answer, sep='')

# 30)Установить, чётным или нечётным является число цифр в записи данного натурального числа.
# Если число цифр нечётно, вывести среднюю цифру.

n = list(input())
total = 0
answer = 0

for i in range(len(n)):
    total += 1

if total % 2 == 0:
    print('Четное число цифр')
else:
    answer = n[(total - 1) // 2]
    print('Нечётное число цифр')
    print('Средняя цифра:', answer)
