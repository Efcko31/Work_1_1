
import math
# Лабораторная работа №3


# 1) Найти все простые делители данного натурального числа
n = int(input())
answer = []
for i in range(1, n + 1):
    if n % i == 0:
        total_answer = 0
        for j in range(1, i + 1):
            if i % j == 0:
                total_answer += 1
        if total_answer == 2:
            answer.append(i)
print(*answer)


 2) С клавиатуры вводятся целые числа. Признак конца ввода — ноль.
    Определить число, следующее за последним из введённых минимальных значений.
n = 1
minimum_n = 9999999999
minimum_n_1 = 9999999999
flag_stop_program = False
while flag_stop_program != True:
    n = int(input())
    if n != 0:
        if minimum_n_1 > n:
            minimum_n = n
            minimum_n, minimum_n_1 = minimum_n_1, minimum_n
        elif minimum_n > n:
            minimum_n = n
    elif n == 0:
        flag_stop_program = True
print(minimum_n)

# У меня вопрос по этому заданию. Я написал программу так, чтобы она выводила воторое минимальное значение после самого минимального.
# Если не правильно понял, то переделаю сейчас так:

n = 1
minimum_n = 9999999999
answer = 1
flag_stop_program = False
flag_the_next_number_after_the_minimum = False
while flag_stop_program != True:
    n = int(input())
    if flag_the_next_number_after_the_minimum == True:
        answer = n
        flag_the_next_number_after_the_minimum = False
    if n != 0:
        if minimum_n > n:
            minimum_n = n
            flag_the_next_number_after_the_minimum = True
    elif n == 0:
        flag_stop_program = True
print(answer)
# В данном варианте, вводятся числа и выводится число, которое по порядку ввода идет за минимальным числом при вводе.
# То есть, при вводе: 1 2 3 -12 -14 7 8, выведет 7.


# 3) Дано целое число n, удовлетворяющее условию 0 < |n| <= 2 * 10 ** 9
#  Найти максимальную цифру в записи этого числа.
n = input()
answer = 0
for i in range(len(n)):
    if int(n[i]) > answer:
        answer = int(n[i])
print(answer)


# 4) Определить, является ли данное натуральное число простым числом.
n = int(input())
number_of_divisors = 0
for i in range(1, n + 1):
    if n % i == 0:
        number_of_divisors += 1
if number_of_divisors == 2:
    print('YES')
else:
    print("NO")


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

symbol_users = list(input())
total_symbols = 0
maximum_symbols = 0
for i in range(1, len(symbol_users)):
    if symbol_users[i] != '.':
        if symbol_users[i] == symbol_users[i - 1]:
            total_symbols += 1
        else:
            if maximum_symbols < total_symbols + 1:
                maximum_symbols = total_symbols + 1
            total_symbols = 0
    else:
        break
if maximum_symbols < total_symbols + 1:
    maximum_symbols = total_symbols + 1
print(maximum_symbols)


# 8) не понял как ....


# 9) С клавиатуры вводятся целые числа. Признак конца ввода — ноль.
# Определить число, предшествующее первому из введённых максимальных значений.

symbol_users = list(input())
maximum_number = int(symbol_users[0])
flag_stop = 0
answer = 0
for i in range(1, len(symbol_users)):
    if int(symbol_users[i]) != flag_stop:
        if maximum_number < int(symbol_users[i]):
            maximum_number = int(symbol_users[i])
            answer = symbol_users[i - 1]
    else:
        break
print(answer)

# 10) Дано целое число n, удовлетворяющее условию 0 < |n| <= 2 * 10 ** 9
# Найти максимальную цифру в записи этого числа.

number = list(input())
answer = 1
for i in range(len(number)):
    if int(number[i]) != 0:
        answer *= int(number[i])
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
