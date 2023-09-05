
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
    fibonacci_numbers = number_1 + number_2
    number_1, number_2 = number_2, number_1
    fibonacci_numbers, number_2 = number_2, fibonacci_numbers
    if number_2 == a:
        if number_1 + number_2 == b:
            answer = True
            break
        else:
            answer = False
            break
if answer == True:
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
total_symbols = 0
maximum_symbols = 0
while True:
    symbols = input()
    if '.' in symbols:
        break
    else:
        if len(symbols) == 1:
            list_symbol.append(symbols)
        else:
            print("Ошибка! Введите 1 символ!")

for i in range(1, len(list_symbol)):
    if list_symbol[i] == list_symbol[i - 1]:
        total_symbols += 1
    else:
        if maximum_symbols < total_symbols + 1:
            maximum_symbols = total_symbols + 1
        total_symbols = 0
if maximum_symbols < total_symbols + 1:
    maximum_symbols = total_symbols + 1
print(maximum_symbols)


# 8) не понял как ....


# 9) С клавиатуры вводятся целые числа. Признак конца ввода — ноль.
# Определить число, предшествующее первому из введённых максимальных значений.
list_symbols = []
flag_stop = 0
answer = 0

def error_checking(n):
    while True:
        if not n.isdigit():
            if not n[1::].isdigit():
                print('ОШИБКА! Введите целое число!')
                n = input()
            else:
                return int(n)
        else:
            return int(n)
while True:
    symbols = error_checking(input())
    if symbols == 0:
        break
    else:
        list_symbols.append(symbols)

maximum_number = int(list_symbols[0])
for i in range(1, len(list_symbols)):
    if maximum_number < int(list_symbols[i]):
        maximum_number = int(list_symbols[i])
        answer = list_symbols[i - 1]
print(answer)

# 10) Дано целое число n, удовлетворяющее условию 0 < |n| <= 2 * 10 ** 9
# Найти максимальную цифру в записи этого числа.

def error_checking(n):
    while True:
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

user_symbol = 0
answer = 'NOTHING'
flag_user_symbol = 'NOTHING'
while user_symbol != '.':
    user_symbol = input()
    if user_symbol not in '1234567890.':
        flag_user_symbol = user_symbol

    if user_symbol == '.':
        print(answer)

    elif user_symbol in '1234567890':
        answer = flag_user_symbol
    flag_user_symbol = user_symbol


# 12) С клавиатуры вводятся целые числа. Признак конца ввода — ноль.
# Определить количество введённых нечётных чисел после последнего отрицательного.

user_number = 1
total_number_for_answer = 0
flag_negative_number = False
while user_number != 0:
    user_number = int(input())
    if flag_negative_number == True and user_number < 0:
        flag_negative_number = False
        total_number_for_answer = 0
    if user_number < 0:
        flag_negative_number = True

    if flag_negative_number == True:
        if user_number % 2 != 0 and user_number > 0:
            total_number_for_answer += 1

print(total_number_for_answer)


# 13) Дано целое неотрицательное число n, удовлетворяющее условию 0 < |n| <= 2 * 10 ** 9 Определить количество нулей,
# которыми заканчивается запись числа n. Вывести n в виде a*10^k, где a — целое, не содержащее нуля в конце записи числа;
# k — количество нулей в конце записи числа n. Например, 130 000 = 13*10^4.

number = list(input())
number = number[::-1]
flag_ziro = True
a = []
k = 0
for i in range(len(number)):
    if number[i] == '0' and flag_ziro == True:
        k += 1
    else:
        a.append(number[i])
        flag_ziro = False
a = a[::-1]
print(*a, ' * 10 ^ ', k, sep='')

# 14) С клавиатуры вводятся целые числа. Признак конца ввода — ноль.
# Определить число, следующее за последним из отрицательных чисел.

user_number = 1
flag_negative_number = False
answer_for_number = 0
while user_number != 0:
    user_number = int(input())
    if flag_negative_number == True:
        answer_for_number = user_number
        flag_negative_number = False
    if user_number < 0:
        flag_negative_number = True
print(answer_for_number)


# 15) Дано целое число n, удовлетворяющее условию 0 < |n| <= 2 * 10 ** 9
#     Найти сумму цифр числа n.

number = list(input())
sum_number = 0
for i in range(len(number)):
    sum_number += int(number[i])
print(sum_number)

# 16) С клавиатуры вводятся вещественные числа. Признак конца ввода — ноль.
# Определить, является ли вводимая последовательность упорядоченной по невозрастанию или по неубыванию.

user_number = 1
list_user_number = []
while user_number != 0:
    user_number = int(input())
    if user_number != 0:
        list_user_number.append(user_number)
total_numbers_in_descending_order = 0 # убывание
total_ascending_numbers = 0

for i in range(1, len(list_user_number)):
    if list_user_number[i] > list_user_number[i - 1]:
        total_ascending_numbers += 1
    elif list_user_number[i] < list_user_number[i - 1]:
        total_numbers_in_descending_order += 1

if total_ascending_numbers + 1 == len(list_user_number) and total_numbers_in_descending_order == 0:
    print('Упорядоченна по неубыванию')
elif total_numbers_in_descending_order + 1 == len(list_user_number) and total_ascending_numbers == 0:
    print('Упорядоченна по невозврастанию')
else:
    print('Никак не упорядоченна')


# 17) С клавиатуры вводятся вещественные числа. Признак конца ввода — ноль.
# Определить, является ли вводимая последовательность арифметической прогрессией.

user_number = 1
first_number = int(input())
second_number = int(input())
difference = first_number - second_number
flag_arithmetic_progression = True
while user_number != 0:
    user_number = int(input())
    if user_number != 0:
        first_number = user_number
        first_number, second_number = second_number, first_number
        if first_number - second_number != difference:
            flag_arithmetic_progression = False
if flag_arithmetic_progression == True:
    print('Является арифметической прогрессией')
else:
    print('Не является арифметической прогрессией')


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
total = len(n)
answer = 0
if total % 2 == 0:
    print('Четное число цифр')
else:
    answer = n[(total - 1) // 2]
    print('Четное число цифр')
    print('Средняя цифра:', answer)
