# text = str(input("Введите текст:"))
# m = len(list(set(text)))
# print("Количество уникальных символов: ", m)
#
# def is_leap_year(x):
#     return (x % 400 == 0) or ((x % 4 == 0) and (x % 100 != 0))

# N = 1239287
# print('5' in str(N) and '3' in str(N))

# is_rainy = True  # дождь будет
#
# if is_rainy:
#     print("Брать зонт")
# else:
#     print("Не брать зонт")
#
# a = 7
# b = 9 + a
# print("a=F(",b,")")

# s = 5
# a = 10
# if a > 0:
#    s = s + a
# else:
#    s = s - a
#
# print(s)

# is_rainy = False  # дождь будет
# heavy_rain = False  # не сильный дождь
#
# if is_rainy:
#     # в данный блок дописали ещё один условный оператор
#     if heavy_rain:
#         print("Брать зонт")
#     else:
#         print("Надеть дождевик")
# else:
#     print("Не брать зонт")

# print(bool(None))

# try:  # Добавляем конструкцию try-except для отлова нашей ошибки
#     print("Перед исключением")
#     # теперь пользователь сам вводит числа для деления
#     a = int(input("a: "))
#     b = int(input("b: "))
#     c = a / b  # здесь может возникнуть исключение деления на ноль
#     print(c)  # печатаем c = a / b если всё хорошо
# except ZeroDivisionError as e:  # Добавляем тип именно той ошибки которую хотим отловить.
#     print(e)  # Выводим информацию об ошибке
#     print("После исключения")
#
# print("После После исключения")

# print("Перед исключением")
# # теперь пользователь сам вводит числа для деления
# a = int(input("a: "))
# b = int(input("b: "))
# c = a / b # здесь может возникнуть исключение деления на ноль
# print(c) # печатаем c = a / b если всё хорошо
# print(e) # Выводим информацию об ошибке
# print("После исключения")

# try:
#     print("Перед исключением")
#     a = int(input("a: "))
#     b = int(input("b: "))
#     c = a / b
#     print(c)  # печатаем c = a / b, если всё хорошо
# except ZeroDivisionError as e:
#     print("Деление на ноль")
# else:  # код в блоке else выполняется только в том случае, если код в блоке try выполнился успешно (т.е. не вылетело никакого исключения).
#     print("Всё ништяк")
# finally:  # код в блоке finally выполнится в любом случае при выходе из try-except
#     print("Finally на месте")
#
# print("После После исключения")

# print('Скорость ветра от 1 до разумного')
# speed = int(input())
# if speed >= 0 and speed <=4:
#     print('weak')
# elif speed <= 10:
#     print('moderate')
# elif speed <= 18:
#     print('strong')
# elif speed >= 19:
#     print('hurricane')

# try:
#     age = int(input("How old are you?"))
#     if age > 100 or age <= 0:
#         raise ValueError("Тебе не может быть столько лет")
# except ValueError as error:
#     print(error)
#     print("Неправильный возраст")
# else:
#     print(f"You are {age} years old!") # Возраст выводится только в случае, если пользователь ввёл правильный возраст.

# try:
#     stroka = int(input("Введите строку: "))
# except ValueError as error:
#     print("Вы ввели неправильное число")
# else:
#     print("Вы ввели " + str(stroka))
# finally:
#     print("Выход из программы")

# password = input("Enter the password ")
# if not password:  # password строка содержащая пароль, введенный пользователем
#    print("Вы забыли ввести пароль! Повторите попытку ещё раз")

# if x > 0 and y > 0:  # x > 0, y > 0
#     print("Первая четверть")
# if x > 0 and y < 0:  # x > 0, y < 0
#     print("Четвертая четверть")
# if x < 0 and y > 0:  # x < 0, y > 0
#     print("Вторая четверть")
# if x < 0 and y < 0:  # x < 0, y < 0
#     print("Третья четверть")

# A = int(input('Введите первое число A\n'))
# B = int(input('Введите второе число B\n'))
# C = int(input('Введите третье число C\n'))
# if A < 45 and B >= 45 and C >= 45:
#     print("Число А единственное меньше 45")
# elif A >= 45 and B < 45 and C  >= 45:
#     print("Число B единственное меньше 45")
# elif A >= 45 and B >= 45 and C < 45:
#     print("Число C единственное меньше 45")
# else:
#     print("Числа меньше 45 нет или их несколько")
#
# A = int(input('Введите число A\n'))
# if -10 < A < -1 or 2 < A < 15:
#     print("Число принадлежит указанным интервалам")
# else:
#     print("Число не принадлежит указанным интервалам")

# a = int(input('Введите первое число'))
# b = int(input('Введите второе число'))
# c = int(input('Введите третье число'))
#
# if a<45:
#     if b>45 and c>45:
#         result = True
#     else:
#         result = False
# else:
#     if b > 45:
#         result = True
#     else:
#         if c>45:
#             result = True
#         else:
#             result = False
# print(result)

# S = 1  # заводим переменную-счетчик
# N = 5
#
# for i in range(1, N + 1):
#     print("Значение произведения на предыдущем шаге: ", S)
#     print("Текущее число: ", i)
#     S *= i
#     print("Значение произведения после сложения: ", S)
#     print("---")
# print("Конец цикла")
# print()
# print("Ответ: произведение равно = ", S)

# S = 1  # заводим переменную-счетчик
# N = int(input("Введите число звездочек "))
#
# for i in range(1, N + 1):
#     print("*" * i)

# S = 0  # заводим переменную-счетчик, в которой мы будем считать сумму
# n = 1  # текущее натуральное число
#
# # заводим цикл while, который будет работать, пока сумма не превысит 500
# while S < 500:  # делай пока ...
#     S += n  # увеличиваем сумму, равносильно S = S + n
#     n += 1  # так как сумма ещё не достигла нужного значения, то увеличиваем переменную-счетчик
#     print("Ещё считаю ...")
#
# print("Сумма равна: ", S)
# print("Количество чисел: ", n)

# S = 1
#
# # заводим цикл while, который будет работать, пока произведение не превысит 1000
# while S ** 2 < 1000:  # делай пока ...
#     S += 1
#     print(S)
#
#
# print("main " + str(S - 1))

# n = 1
# while True:
#    if n ** 2 >= 1000:
#        print("Последнее число", n - 1)
#        break
#    n += 1

# random_matrix = [
#     [9, 2, 1],
#     [2, 5, 3],
#     [4, 8, 5]
# ]
#
# mean_value_rows = []  # здесь будут храниться средние значения для каждой строки
# min_value_rows = []  # здесь будут храниться минимальные значения для каждой строки
# min_index_rows = []  # здесь будут храниться индексы минимальных значений для каждой строки
# max_value_rows = []  # здесь будут храниться максимальные значения для каждой строки
# max_index_rows = []  # здесь будут храниться индексы максимальных значений для каждой строки
#
# for row in random_matrix:  # здесь мы целиком берем каждую сроку
#     min_index = 0  # в качестве минимального значения возьмем первый элемент строки
#     max_index = 0
#     min_value = row[min_index]  # начальное минимальное значение для каждой строки будет новое
#     max_value = row[max_index]  # для максимального значения тоже самое
#     for index_col in range(len(row)):
#         if row[index_col] < min_value:
#             min_value = row[index_col]
#             min_index = index_col
#         if row[index_col] > max_value:
#             max_value = row[index_col]
#             max_index = index_col
#     min_value_rows.append(min_value)
#     min_index_rows.append(min_index)
#     max_value_rows.append(max_value)
#     max_index_rows.append(max_index)
#
# print(min_value_rows)
# print(min_index_rows)
# print(max_value_rows)
# print(max_index_rows)
# print(type(row))

# list_ = [-5, 2, 4, 8, 12, -7, 5]
#
# for i in range(len(list_)):  # равносильно выражению for i in [0, 1, 2, 3, 4, 5, 6]:
#     print("Индекс элемента: ", i)
#     print("Значение элемента: ", list_[i])  # с помощью индекса получаем значение элемента
#     print("---")
# print("Конец цикла")

# list_ = [-5, 2, 4, 8, 12, -7, 5]
# # Объявим переменную, в которой будем хранить индекс отрицательного элемента
# index_negative = None
#
# for i, value in enumerate(list_):
#     if value < 0:
#         print("Отрицательное число: ", value)
#         index_negative = i  # перезаписываем значение индекса
#         print("Новый индекс отрицательного числа: ", index_negative)
#     else:
#         print("Положительное число: ", value)
#     print("---")
# print("Конец цикла")
# print()
# print("Ответ: индекс последнего отрицательного элемента = ", index_negative)

text = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо -- песнь заводит,
Налево -- сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух... там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# text = text.lower()
# text = text.replace(" ", "")
# text = text.replace("\n", "")
# print(text)
# count = {}  # для подсчета символов и их количества
# for char in text:
#    if char in count:  # если символ уже встречался, то увеличиваем его количество на 1
#        count[char] += 1
#    else:
#        count[char] = 1
# print(count)
# for char, cnt in count.items():
#    print(f"Символ {char} встречается {cnt} раз")

# if n % 2 == 0:
#     n = n // 2
# else:
#     n = (n * 3 + 1) // 2

# n = int(input("Введите число\n"))
#
# while True:
#     if n % 2 == 0:
#         n = int(n / 2)
#     else:
#         n = int((n * 3 + 1) / 2)
#     print(n)
#
#     if n == 1:
#         print("Done")
#         break

# heads = 35  # количество голов
# legs = 94  # количество ног
#
# for r in range(heads + 1):  # количество кроликов
#     for ph in range(heads + 1):  # количество фазанов
#         #  если суммарное количество голов превышено или ног превышено, то переходим на следующий шаг цикла
#         if (r + ph) > heads or \
#             (r * 4 + ph * 2) > legs:
#             continue
#         if (r + ph) == heads and (r * 4 + ph * 2) == legs:
#             print("Количество кроликов", r)
#             print("Количество фазанов", ph)
#             print("---")

# n = int(input("Введите число\n"))
# for x in range(1, n + 1):
#     print("*" * x)

# some_var = (2,)
# if some_var is None:
#     print("NoneType")
# else:
#     print(type(some_var))

# a = "foo"
# b = "bar"
#
# print(1 and a or b)

# a = int(input("Введите число "))
#
# if type(a) == int and 100 <= a <= 999 and a % 2 == 0 and a % 3 == 0:
#     print("Это число нам подходит")

# if all([type(a) == int,
#         100 <= a <= 999,
#         a % 2 == 0,
#         a % 3 == 0]):
#     print("Число удовлетворяет условиям")

# L = list(map(int, input().split()))
#
# print(all(L))

# M = [[i*j for j in range(1,11)] for i in range(1,11)]
# print(M)

# L = [int(input()) for i in range(5)]

# L = [int(input()) % 2 == 0 for i in range(5)]
# print(any(L) or not any(L))

# L = [i for i in range(10)]
# # 0 1 2 3 4 5 6 7 8 9
# M = [i for i in range(10,0,-1)]
# # 10 9 8 7 6 5 4 3 2 1
# # N = [ ]
# #
# # for i in range(10):
# #     N.append(L[i] * M[i])
# #
# # print(N)
# for a, b in zip(L,M):
#     print('a =', a, 'b =', b)
# N = [a*b for a,b in zip(L,M)]
# print(N)

# text = input("Введите строку: ")
#
# f_letter = text[0]
# count = 0
# result = ""
# for letter in text:
#    if letter == f_letter:
#        count += 1
#    else:
#        result += f_letter + str(count)
#        f_letter = letter
#        count = 1
# result += f_letter + str(count)
# print(result)
#
#
# print(count)

# def char_frequency():
#    text = """
#    У лукоморья дуб зелёный;
#    Златая цепь на дубе том:
#    И днём и ночью кот учёный
#    Всё ходит по цепи кругом;
#    Идёт направо -- песнь заводит,
#    Налево -- сказку говорит.
#    Там чудеса: там леший бродит,
#    Русалка на ветвях сидит;
#    Там на неведомых дорожках
#    Следы невиданных зверей;
#    Избушка там на курьих ножках
#    Стоит без окон, без дверей;
#    Там лес и дол видений полны;
#    Там о заре прихлынут волны
#    На брег песчаный и пустой,
#    И тридцать витязей прекрасных
#    Чредой из вод выходят ясных,
#    И с ними дядька их морской;
#    Там королевич мимоходом
#    Пленяет грозного царя;
#    Там в облаках перед народом
#    Через леса, через моря
#    Колдун несёт богатыря;
#    В темнице там царевна тужит,
#    А бурый волк ей верно служит;
#    Там ступа с Бабою Ягой
#    Идёт, бредёт сама собой,
#    Там царь Кащей над златом чахнет;
#    Там русский дух... там Русью пахнет!
#    И там я был, и мёд я пил;
#    У моря видел дуб зелёный;
#    Под ним сидел, и кот учёный
#    Свои мне сказки говорил.
#    """
#
#    text = text.lower()
#    text = text.replace(" ", "")
#    text = text.replace("\n", "")
#
#    count = {}  # для подсчета символов и их количества
#    for char in text:
#        if char in count:  # если символ уже встречался, то увеличиваем его количество на 1
#            count[char] += 1
#        else:
#            count[char] = 1
#
#    for char, cnt in count.items():
#        print(f"Символ {char} встречается {cnt} раз")
#
# ...
#
# # вызвали функцию в любом месте программы
# char_frequency()

# def print_2_add_2():
#     a = 2 + 2
#     print(a)
#
# print_2_add_2()

# def hello_world():
#     print("Hello World")
#
# hello_world()

# # объявили функцию для подсчета количества символов в неком абстрактном тексте
# def char_frequency(text):
#    text = text.lower()
#    text = text.replace(" ", "")
#    text = text.replace("\n", "")
#
#    count = {}  # для подсчета символов и их количества
#    for char in text:
#        if char in count:  # если символ уже встречался, то увеличиваем его количество на 1
#            count[char] += 1
#        else:
#            count[char] = 1
#
#    for char, cnt in count.items():
#        print(f"Символ {char} встречается {cnt} раз")

# # функция, которая возводит любое число в квадрат
# def pow_func(base):
#    print(base ** 2)
#
# pow_func(3)  # 9
# pow_func(5)  # 25

# def del_na(n,a):
#     if a % n == 0:
#         print(f"Число {n} является делителем числа {a}")
#     else:
#         print(f"Число {n} не является делителем числа {a}")
#
# del_na(4,2)
# del_na(5,2)

# def stairs():
#     for x in range(n , 0, -1):
#         print("*" * x)

# def pow_func(base, n=2):
#    print(base ** n)
#
# print(pow_func(3))

# def pow_func(base, n=2):
#     inside_result = base ** n
#     return inside_result
#
# print(pow_func(3))

# def koldel(a):
#     count = 0
#     for i in range(1, n+1):
#         if a % i == 0:
#             count += 1
#     return count
#
# koldel(4)

# def get_multipliers(a):
#    count = 0
#    for n in range(1, a + 1):
#        if a % n == 0:
#            count += 1
#
#    return count
#
# get_multipliers(40)

# x = 3
# def func():
#    global x
#    print(x)
#    x = 5
#    x += 5
#    return x
# print(func())

# def get_my_func():
#    def hello_world():
#        print("Hello")
#    return hello_world
#
# hello_world_func = get_my_func()  # получить функцию в качестве результата
#
# print(type(hello_world_func))  # <class 'function'>
# hello_world_func()  # Hello

# def get_mul_func(m):
#    nonlocal_m = m
#
#    def local_mul(n):
#       return n * nonlocal_m
#
#    return local_mul
#
#
# two_mul = get_mul_func(2)  # возвращаем функцию, которая будет умножать числа на 2
# print(two_mul(6))  # 5 * 2

# x = 3
#
# def func():
#    global x # объявляем, что переменная является глобальной
#    print(x)
#    x = 5
#    x += 5
#    return x

# func()
# print(x)

# def adder(*nums):
#    prz_ = 1
#    for n in nums:
#       prz_ *= n
#
#    return prz_
#
#
# print(adder())  # 0
# print(adder(1))  # 1
# print(adder(1, 2))  # 3
# print(adder(1, 2, 3))  # 6
# установим аргумент name_arg пустым а внутри функции будем проверять его

# def correct_func(name_arg=None):
#    if name_arg is None:
#        name_arg = []
#    print("Аргумент до изменения", name_arg)
#    name_arg.append(1)
#    print("Аргумент после изменения", name_arg)
#
# # вызовем два раза одну и ту же функцию
# correct_func()
# print('-----')
# correct_func()
# print('-----')
# correct_func([123])
# print('-----')
# correct_func(name_arg=[123])

# def reverse_str(string):
#     if len(string) == 0:
#         return ''
#     else:
#         return string[-1] + reverse_str(string[:-1])
#
#
# print(reverse_str('rest'))

# def fib():
#     a = 0
#     while True:
#         a += 2
#         yield a
#
#
# for num in fib():
#     print(num)

# def count(start=1, step=1):
#     counter = start
#     while True:
#         yield counter
#         counter += step

# def repeat_list(list_):
#     c = list_.copy()
#     while True:
#         value = c.pop(0)
#         c.append(value)
#         yield value
#
#
# for i in repeat_list([1, 2, 3]):
#     print(i)

# iter(int)  # TypeError: 'type' object is not iterable

# def createGenerator():
#     mylist = range(10)
#     for i in mylist:
#         yield i * i
#
#
# mygenerator = createGenerator()  # создаём генератор
# print(mygenerator)  # mygenerator является объектом!
#
# for i in mygenerator:
#     print(i)

# str_ = "my tst"
# str_iter = iter(str_)
# a = {'dylan': 1,'bob': 211}
# a_iter = iter(a)
#
# print(type(a))  # строка
# print(type(a_iter))
# print(type(str_))  # строка
# print(type(str_iter))
# print(next(str_iter))
# print(next(str_iter))  # y
# print(next(str_iter))  #
# print(next(str_iter))  # t
# print(next(str_iter))  # s
# print(next(str_iter))
# print(next(str_iter))

# def my_decorator(a_function_to_decorate):
#     # Здесь мы определяем новую функцию - «обертку». Она нам нужна, чтобы выполнять
#     # каждый раз при вызове оригинальной функции, а не только один раз
#     def wrapper():
#         # здесь поместим код, который будет выполняться до вызова, потом вызов
#         # оригинальной функции, потом код после вызова
#         print("Я буду выполнен до основного вызова!")
#
#         result = a_function_to_decorate()  # не забываем вернуть значение исходной функции
#
#         print("Я буду выполнен после основного вызова!")
#         return result
#
#     return wrapper
#
# def my_function():
#    print("Я - оборачиваемая функция!")
#    return 0
#
# print(my_function())
# # Я - оборачиваемая функция!
# # 0
#
# decorated_function = my_decorator(my_function)  # декорирование функции
# print(decorated_function())
# # Я буду выполнен до основного вызова!
# # Я - оборачиваемая функция!
# # Я буду выполнен после основного вызова!
# # 0

# import time
#
#
# def decorator_time(fn):
#     def wrapper():
#         print(f"Запустилась функция {fn}")
#         t0 = time.time()
#         result = fn()
#         dt = time.time() - t0
#         print(f"Функция выполнилась. Время: {dt:.10f}")
#         return dt  # задекорированная функция будет возвращать время работы
#
#     return wrapper
#
#
# def pow_2():
#     print('----')
#     return 10000000 ** 2
#
#
# def in_build_pow():
#     print('----')
#     return pow(10000000, 2)
#
#
#
# pow_2 = decorator_time(pow_2)
# in_build_pow = decorator_time(in_build_pow)
#
# pow_2()
# # Запустилась функция <function pow_2 at 0x7f938401b158>
# # Функция выполнилась. Время: 0.0000011921
#
# in_build_pow()
# # Запустилась функция <function in_build_pow at 0x7f938401b620>
# # Функция выполнилась. Время: 0.0000021458

# import time
#
# N = 100
#
#
# def decorator_time(fn):
#    def wrapper():
#        t0 = time.time()
#        result = fn()
#        dt = time.time() - t0
#        return dt
#    return wrapper
#
#
# def pow_2():
#    return 10000000 ** 2
#
#
# def in_build_pow():
#    return pow(10000000, 2)
#
#
# pow_2 = decorator_time(pow_2)
# in_build_pow = decorator_time(in_build_pow)
#
# mean_pow_2 = 0
# mean_in_build_pow = 0
# for _ in range(N):
#    mean_pow_2 += pow_2()
#    mean_in_build_pow += in_build_pow()
#
# print(f"Функция {pow_2} выполнялась {N} раз. Среднее время: {mean_pow_2 / N:.10f}")
# print(f"Функция {in_build_pow} выполнялась {N} раз. Среднее время: {mean_in_build_pow / N:.10f}")

# def counter(func):
#    count = 0
#    def wrapper(*args, **kwargs):
#        nonlocal count
#        func(*args, **kwargs)
#        count += 1
#        print(f"Функция {func} была вызвана {count} раз")
#    return wrapper
#
# @counter
# def say_word(word):
#    print(word)
#
# say_word("Oo!!!")
# # Oo!!!
# # Функция <function say_word at 0x7f93836d47b8> была вызвана 1 раз
#
# say_word("Oo!!!")
# # Oo!!!
# # Функция <function say_word at 0x7f93836d47b8> была вызвана 2 раз

# def cache(func):
#    cache_dict = {}
#    def wrapper(num):
#        nonlocal cache_dict
#        if num not in cache_dict:
#            cache_dict[num] = func(num)
#            print(f"Добавление результата в кэш: {cache_dict[num]}")
#        else:
#            print(f"Возвращение результата из кэша: {cache_dict[num]}")
#        print(f"Кэш {cache_dict}")
#        return cache_dict[num]
#    return wrapper
#
# @cache
# def f(n):
#    return n * 123456789
#
# f(-1)

# # def linear_solve(a, b):
# #     return b/a
# def linear_solve(a, b):
#     if a:
#         return b/a
#     elif not a and not b: # снова используем числа в логических выражениях
#         return "Бесконечное количество корней"
#     else:
#         return "Нет корней"
#
# print(linear_solve(0, 0))

# def D(a, b, c):
#     return b ** 2 - 4 * a * c
#
#
# def quadratic_solve(a, b, c):
#     if D(a, b, c) < 0:
#         return print("Нет вещественных корней")
#     elif D(a, b, c) == 0:
#         return print(f'Единственный корень {-b / (2 * a)}')
#     else:
#         return print(
#             f'Первый корень {(-b - D(a, b, c) ** 0.5) / (2 * a)}\nВторой корень {(-b + D(a, b, c) ** 0.5) / (2 * a)}')
#
#
# print(quadratic_solve(1, 5, 1))


# def min_list(L):
#     if len(L) == 1:
#         return L[0]
#     return L[0] if L[0] < min_list(L[1:]) else min_list(L[1:])

# def e():
#     n = 1
#
#     while True:
#         yield (1 + 1 / n) ** n
#         n += 1
#
#
# last = 0
# for a in e(): # e() - генератор
#     if (a - last) < 0.00000001: # ограничение на точность
#         print(a)
#         break # после достижения которого - завершаем цикл
#     else:
#         last = a # иначе - присваиваем новое значение

# yesno = input("""Введите Y, если хотите авторизоваться или N,
#              если хотите продолжить работу как анонимный пользователь: """)
#
# auth = yesno == "Y"
#
#
# def is_auth(func):
#     def wrapper():
#         if auth:
#             print("Пользователь авторизован")
#             func()
#         else:
#             print("Пользователь неавторизован. Функция выполнена не будет")
#
#     return wrapper
#
#
# @is_auth
# def from_db():
#     print("some data from database")
#
#
# @is_auth
# def change_profile():
#     print("Profile has been changed")
#
# change_profile()
# from_db()


# USERS = ['admin', 'guest', 'director', 'root', 'superstar']
#
# yesno = input("""Введите Y, если хотите авторизоваться или N,
#              если хотите продолжить работу как анонимный пользователь: """)
#
# auth = yesno == "Y"
#
# if auth:
#     username = input("Введите ваш username:")
#
#
# def is_auth(func):
#     def wrapper():
#         if username in USERS:
#             print("Пользователь авторизован")
#             func()
#         else:
#             print("Пользователь неавторизован. Функция выполнена не будет")
#
#     return wrapper
#
#
# @is_auth
# # @has_access
# def from_db():
#     print("some data from database")
#
#
# from_db()

# L = ['THIS', 'IS', 'LOWER', 'STRING']
#
# print(list(map(str.lower, L)))
# # ['this', 'is', 'lower', 'string']


# # Из заданного списка вывести только положительные элементы
# def positive(x):
#     return x % 2 == 0  # функция возвращает только True или False
#
# result = filter(positive, [-2, -1, 0, 1, -3, 2, -3])
#
# # Возвращается итератор, т.е. перечисляйте или приводите к списку
# print(list(result))   # [1, 2]


# map + filter
# some_list = [i - 10 for i in range(20)]
#
#
# def pow2(x): return x ** 2
#
#
# def positive(x): return x > 0
#
#
# print(some_list)
# print(list(map(pow2, filter(positive, some_list))))


# d = {2: "c", 1: "d", 4: "a", 3: "b"}
#
# # Чтобы отсортировать его по ключам, нужно сделать так:
# print(dict(sorted(d.items())))
# # {1: 'd', 2: 'c', 3: 'b', 4: 'a'}
#
# print(dict(sorted(d.items(), key=lambda x: x[1])))  # сортировка по значению словаря


# a = ["asd", "bbd", "ddfa", "mcsa"]
#
# print(list(map(len,a)))
#
# b = ["это", "маленький", "текст", "обидно"]
#
# print(list(map(str.upper, b)))

# myFile = open('ReadMe.txt', encoding="utf8")
# print("--")
# for line in myFile:
#     print(line)
#
# print("--")
# for line in myFile:
#     print(line)

# myFile = open('namefile.txt', 'w')
# myFile.write('tttt')
# myFile.write('\n')
# myFile.write('tttt')
# print('zzzz', file=myFile)


# def changeText(text):
#
#     # Функция принимает строку с текстом.
#     # Убирает все знаки препинания и возвращает
#     # список, состоящий из слов текста.
#
#
# for i in '!"\'#$%&()*+-,/:;<=>?@[\\]^_{|}~':
#     text = text.replace(i, '')
#
# return text.split()
#
#
# def mostCommon(text, lenght=0):
#
#     # Функция принимает список и ограничение по длине.
#     # Возвращает самый часто встречающийся элемент.
#     # Если есть несколько элементов с одинаковой самой большой частотой, то вернёт их все.
#
#
# most_common = []
# qty_most_common = 0
#
# for item in text:
#     if len(item) > lenght:
#         qty = text.count(item)
#         if qty > qty_most_common and qty > 2:
#             qty_most_common = qty
#             most_common = [item]
#         elif qty == qty_most_common:
#             most_common.append(item)
#
# return list(set(most_common))
#
#
# def mostLenght(text):
#     """
#     Функция принимает список.
#     Возвращает самый длинный элемент.
#     Если есть несколько элементов с одинаковой самой большой длиной, то вернёт их все.
#     """
#
#
# most_lenght = []
# qty_most_lenght = 0
# alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# for item in text:
#     for char in item:
#         if char not in alphabet:
#             charEn = False
#         else:
#             charEn = True
#
#     if charEn:
#         qty = len(item)
#         if qty > qty_most_lenght:
#             qty_most_lenght = qty
#             most_lenght = [item]
#         elif qty == qty_most_lenght:
#             most_lenght.append(item)
#
# return list(set(most_lenght))
#
# nameFile = input('Название файла: ')
#
# with open(nameFile, encoding='utf8') as f:
#     fileText = f.read()
#
# fileText = changeText(fileText)
# print(f'Список самых частых слов длинной более трёх символов: {mostCommon(fileText, 3)}')
# print(f'Список самых длинных английских слов: {mostLenght(fileText)}')

# class User:
#     pass
#
# peter = User()
# peter.name = "Peter Robertson"
#
# julia = User()
# julia.name = "Julia Donaldson"
#
# # print(peter.name)
# # print(julia.name)
#
# peter.email = "peterrobertson@mail.com"
# print(peter.email)
# print('\n')
# print(julia.email)

# class User:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#
# peter = User(name="Peter Robertson", email="peterrobertson@mail.com")
# julia = User(name="Julia Donaldson", email="juliadonaldson@mail.com")
#
# print(peter.name)
# print(julia.email)

# class Product:
#     def __init__(self, name, category, quantity_in_stock):
#         self.name = name
#         self.category = category
#         self.quantity_in_stock = quantity_in_stock
#
#     def is_available(self):
#         return True if self.quantity_in_stock > 0 else False
#
#
# eggs = Product("eggs", "food", 12)
# print(eggs.is_available())

# class Event:
#     def __init__(self, timestamp=0, event_type="", session_id=""):
#         self.timestamp = timestamp
#         self.type = event_type
#         self.session_id = session_id
#
#     def init_from_dict(self, event_dict):
#         self.timestamp = event_dict.get("timestamp")
#         self.type = event_dict.get("type")
#         self.session_id = event_dict.get("session_id")
#
# events = [
#     {
#      "timestamp": 1554583508000,
#      "type": "itemViewEvent",
#      "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
#     },
#     {
#      "timestamp": 1555296337000,
#      "type": "itemViewEvent",
#      "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
#     },
#     {
#      "timestamp": 1549461608000,
#      "type": "itemBuyEvent",
#      "session_id": "0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct",
#     },
# ]
#
# # for event in events:
# #     event_obj = Event(timestamp=event.get("timestamp"),
# #                       event_type=event.get("type"),
# #                       session_id=event.get("session_id"))
# #     print(event_obj.timestamp)
# for event in events:
#     event_obj = Event()
#     event_obj.init_from_dict(event)
#     print(event_obj.timestamp)

# import datetime
#
#
# class Product:
#     max_quantity = 100000
#
#     def __init__(self, name, category, quantity_in_stock):
#         self.name = name
#         self.category = category
#         self.quantity_in_stock = quantity_in_stock
#
#     def is_available(self):
#         return True if 0 < self.quantity_in_stock < 100000 else False
#
#
# class Food(Product):
#     is_critical = True
#     needs_to_be_refreshed = True
#     refresh_frequency = datetime.timedelta(days=1)
#
#
# eggs = Food(name="eggs", category="food", quantity_in_stock=100005)
# print(eggs.max_quantity)
# print(eggs.is_available())

# class Event:
#     def __init__(self, timestamp=0, event_type="", session_id=""):
#         self.timestamp = timestamp
#         self.type = event_type
#         self.session_id = session_id
#
#     def init_from_dict(self, event_dict):
#         self.timestamp = event_dict.get("timestamp")
#         self.type = event_dict.get("type")
#         self.session_id = event_dict.get("session_id")
#
#     def show_description(self):
#         print("This is generic event.")
#
#
# class ItemViewEvent(Event):
#     type = "itemViewEvent"
#
#     def __init__(self, timestamp=0, session_id="", number_of_views=0):
#         self.timestamp = timestamp
#         self.session_id = session_id
#         self.number_of_views = number_of_views
#
#     def show_description(self):
#         print("This event means someone has browsed an item.")
#
#
# if __name__ == "__main__":
#     test_view_event = ItemViewEvent(timestamp=1549461608000, session_id="0:NynteeXG:MYlskrqZbcmXNSFEJaZIsNVGeDLLpmct", number_of_views=6)
#     test_view_event.show_description()
#     print(test_view_event.type)

# string = str(input(""))
#
#
# def par_checker(string):
#     stack = []  # инициализируем стек
#
#     for s in string:  # читаем строку посимвольно
#         if s == "(":  # если открывающая скобка,
#             stack.append(s)  # добавляем её в стек
#         elif s == ")":
#             # если встретилась закрывающая скобка, то проверяем
#             # пуст ли стек и является ли верхний элемент — открывающей скобкой
#             if len(stack) > 0 and stack[-1] == "(":
#                 stack.pop()  # удаляем из стека
#             else:  # иначе завершаем функцию с False
#                 return False
#     # если стек пустой, то незакрытых скобок не осталось
#     # значит, возвращаем True, иначе — False
#     return len(stack) == 0
#
#
# print(par_checker(string))

# pars = {")": "(", "]": "["}
#
# string = str(input(""))
#
# def par_checker_mod(string):
#     stack = []
#
#     for s in string:
#         if s in "([":
#             stack.append(s)
#         elif s in ")]":
#             if len(stack) > 0 and stack[-1] == pars[s]:
#                 stack.pop()
#             else:
#                 return False
#     return len(stack) == 0
#
# print(par_checker_mod(string))


# N_max = int(input("Определите размер очереди:"))
#
# queue = [0 for _ in range(N_max)]  # инициализируем список с нулевыми элементами
# order = 0  # будем хранить сквозной номер задачи
# head = 0  # указатель на начало очереди
# tail = 0  # указатель на элемент следующий за концом очереди
#
#
# def is_empty():  # очередь пуста?
#     # да, если указатели совпадают и в них содержится ноль
#     return head == tail and queue[head] == 0
#
#
# def size():  # получаем размер очереди
#     if is_empty():  # если она пуста
#         return 0  # возвращаем ноль
#     elif head == tail:  # иначе, если очередь не пуста, но указатели совпадают
#         return N_max  # значит очередь заполнена
#     elif head > tail:  # если хвост очереди сместился в начало списка
#         return N_max - head + tail
#     else:  # или если хвост стоит правее начала
#         return tail - head
#
#
# def add():  # добавляем задачу в очередь
#     global tail, order
#     order += 1  # увеличиваем порядковый номер задачи
#     queue[tail] = order  # добавляем его в очередь
#     print("Задача №%d добавлена" % (queue[tail]))
#
#     # увеличиваем указатель на 1 по модулю максимального числа элементов
#     # для зацикливания очереди в списке
#     tail = (tail + 1) % N_max
#
#
# def show():  # выводим приоритетную задачу
#     print("Задача №%d в приоритете" % (queue[head]))
#
#
# def do():  # выполняем приоритетную задачу
#     global head
#     print("Задача №%d выполнена" % (queue[head]))
#     queue[head] = 0  # после выполнения зануляем элемент по указателю
#     head = (head + 1) % N_max  # и циклично перемещаем указатель
#
#
# while True:
#     cmd = input("Введите команду:")
#     if cmd == "empty":
#         if is_empty():
#             print("Очередь пустая")
#         else:
#             print("В очереди есть задачи")
#     elif cmd == "size":
#         print("Количество задач в очереди:", size())
#     elif cmd == "add":
#         if size() != N_max:
#             add()
#         else:
#             print("Очередь переполнена")
#     elif cmd == "show":
#         if is_empty():
#             print("Очередь пустая")
#         else:
#             show()
#     elif cmd == "do":
#         if is_empty():
#             print("Очередь пустая")
#         else:
#             do()
#     elif cmd == "exit":
#         for _ in range(size()):
#             do()
#         print("Очередь пустая. Завершение работы")
#         break
#     else:
#         print("Введена неверная команда")


# G = {"Адмиралтейская":
#          {"Садовая": 4},
#      "Садовая":
#          {"Сенная площадь": 3,
#           "Спасская": 3,
#           "Адмиралтейская": 4,
#           "Звенигородская": 5},
#      "Сенная площадь":
#          {"Садовая": 3,
#           "Спасская": 3},
#      "Спасская":
#          {"Садовая": 3,
#           "Сенная площадь": 3,
#           "Достоевская": 4},
#      "Звенигородская":
#          {"Пушкинская": 3,
#           "Садовая": 5},
#      "Пушкинская":
#          {"Звенигородская": 3,
#           "Владимирская": 4},
#      "Владимирская":
#          {"Достоевская": 3,
#           "Пушкинская": 4},
#      "Достоевская":
#          {"Владимирская": 3,
#           "Спасская": 4}}
#
# D = {k: 100 for k in G.keys()}
# start_k = 'Адмиралтейская'  # стартовая вершина
# D[start_k] = 0  # расстояние от неё до самой себя равно нулю
# U = {k: False for k in G.keys()}
#
# for _ in range(len(D)):
#     # выбираем среди непросмотренных наименьшее по расстоянию
#     min_k = min([k for k in U.keys() if not U[k]], key=lambda x: D[x])
#
#     for v in G[min_k].keys():  # проходимся по всем смежным вершинам
#         D[v] = min(D[v], D[min_k] + G[min_k][v])  # минимум
#     U[min_k] = True  # просмотренную вершину помечаем
#
# D = {k : 100 for k in G.keys()} # расстояния
# start_k = 'Адмиралтейская' # стартовая вершина
# D[start_k] = 0 # расстояние от нее до самой себя равно нулю
# U = {k : False for k in G.keys()} # флаги просмотра вершин
# P = {k : None for k in G.keys()} # предки
#
# for _ in range(len(D)):
#     # выбираем среди непросмотренных наименьшее по расстоянию
#     min_k = min([k for k in U.keys() if not U[k]], key = lambda x: D[x])
#
#     for v in G[min_k].keys(): # проходимся по всем смежным вершинам
#          if D[v] > D[min_k] + G[min_k][v]: # если расстояние от текущей вершины меньше
#             D[v] = D[min_k] + G[min_k][v] # то фиксируем его
#             P[v] = min_k # и записываем как предок
#     U[min_k] = True # просмотренную вершину помечаем
#
# pointer = "Владимирская" # куда должны прийти
# while pointer is not None: # перемещаемся, пока не придём в стартовую точку
#     print(pointer)
#     pointer = P[pointer]
# print(P)


# class BinaryTree:
#     def __init__(self, value):
#         self.value = value
#         self.left_child = None
#         self.right_child = None
#
#
#     def insert_left(self, next_value):
#         if self.left_child is None:
#             self.left_child = BinaryTree(next_value)
#         else:
#             new_child = BinaryTree(next_value)
#             new_child.left_child = self.left_child
#             self.left_child = new_child
#         return self
#
#
#     def insert_right(self, next_value):
#         if self.right_child is None:
#             self.right_child = BinaryTree(next_value)
#         else:
#             new_child = BinaryTree(next_value)
#             new_child.right_child = self.right_child
#             self.right_child = new_child
#         return self
#
#     def post_order(self):
#         if self.left_child is not None:  # если левый потомок существует
#             self.left_child.post_order()  # рекурсивно вызываем функцию
#
#         if self.right_child is not None:  # если правый потомок существует
#             self.right_child.post_order()  # рекурсивно вызываем функцию
#
#         print(self.value)  # процедура обработки
#
#     def in_order(self):
#         if self.left_child is not None:  # если левый потомок существует
#             self.left_child.in_order()  # рекурсивно вызываем функцию
#
#         print(self.value)  # процедура обработки
#
#         if self.right_child is not None:  # если правый потомок существует
#             self.right_child.in_order()  # рекурсивно вызываем функцию
#
# # создаём корень и его потомков /7|2|5\
# node_root = BinaryTree(2).insert_left(7).insert_right(5)
# # левое поддерево корня /2|7|6\
# node_7 = node_root.left_child.insert_left(12).insert_right(6)
# # правое поддерево предыдущего узла /5|6|11\
# node_6 = node_7.right_child.insert_left(15).insert_right(11)
# # правое поддерево корня /|5|9\
# node_5 = node_root.right_child.insert_right(9)
# # левое поддерево предыдущего узла корня /4|9|\
# node_9 = node_5.right_child.insert_left(4)
#
# print(node_root.in_order())


# class Node:  # класс элемента
#     def __init__(self, value=None, next_=None):  # инициализируем
#         self.value = value  # значением
#         self.next = next_  # и ссылкой на следующий элемент
#
#     def __str__(self):
#         return "Node value = " + str(self.value)
#
#
# class LinkedList:  # класс списка
#     def __init__(self):  # инициализируем пустым
#         self.first = None
#         self.last = None
#
#     def clear(self):  # очищаем список
#         self.__init__()
#
#     def __str__(self):  # функция печати
#         R = ''
#
#         pointer = self.first  # берем первый указатель
#         while pointer is not None:  # пока указатель не станет None
#             R += str(pointer.value)  # добавляем значение в строку
#             pointer = pointer.next  # идем дальше по указателю
#             if pointer is not None:  # если он существует добавляем пробел
#                 R += ' '
#         return R
#
#     def pushleft(self, value):
#         if self.first is None:
#             self.first = Node(value)
#             self.last = self.first
#         else:
#             new_node = Node(value, self.first)
#             self.first = new_node
#
#     def pushright(self, value):
#         if self.first is None:
#             self.first = Node(value)
#             self.last = self.first
#         else:
#             new_node = Node(value)
#             self.last.next = new_node
#             self.last = new_node
#
#     def popleft(self):
#         if self.first is None:  # если список пустой, возвращаем None
#             return None
#         elif self.first == self.last:  # если список содержит только один элемент
#             node = self.first  # сохраняем его
#             self.__init__()  # очищаем
#             return node  # и возвращаем сохраненный элемент
#         else:
#             node = self.first  # сохраняем первый элемент
#             self.first = self.first.next  # меняем указатель на первый элемент
#             return node  # возвращаем сохраненный
#
#     def popright(self):
#         if self.first is None:  # если список пустой, возвращаем None
#             return None
#         elif self.first == self.last:  # если список содержит только один элемент
#             node = self.first  # сохраняем его
#             self.__init__()  # очищаем
#             return node  # и возвращаем сохраненный элемент
#         else:
#             node = self.last  # сохраняем последний
#             pointer = self.first  # создаем указатель
#             while pointer.next is not node:  # пока не найдем предпоследний
#                 pointer = pointer.next
#             pointer.next = None  # обнуляем указатели, чтобы
#             self.last = pointer  # предпоследний стал последним
#             return node  # возвращаем сохраненный
#
#         def __iter__(self):  # объявляем класс как итератор
#             self.current = self.first  # в текущий элемент помещаем первый
#             return self  # возвращаем итератор
#
#         def __next__(self):  # метод перехода
#             if self.current is None:  # если текущий стал последним
#                 raise StopIteration  # вызываем исключение
#             else:
#                 node = self.current  # сохраняем текущий элемент
#                 self.current = self.current.next  # совершаем переход
#                 return node  # и возвращаем сохраненный
#
#         def __len__(self):
#             count = 0
#             pointer = self.first
#             while pointer is not None:
#                 count += 1
#                 pointer = pointer.next
#             return count
#
#
#
#
# LL = LinkedList()
#
# LL.pushright(1)
# LL.pushleft(2)
# LL.pushright(3)
# LL.popright()
# LL.pushleft(4)
# LL.pushright(5)
# LL.popleft()
#
# print(__len__(LL))

# array = str(input("Введите последовательность чисел через пробел: "))
#
# try:
#     test3num = map(int(array))
#     print("Это правильный ввод! Ваше счастливое число: ", test3num)
# except ValueError:
#     print("Это не правильный ввод. Это не число вообще! Это строка")

#
# import requests
#
# r = requests.get(
#     'https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=html')  # делаем запрос на сервер по переданному адресу
# print(r.content)

#
# import requests
#
# r = requests.get('https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=html')
# print(r.status_code)  # узнаем статус полученного ответа

# import requests
#
# r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')  # попробуем поймать json ответ
# print(r.content)

# import requests
# import json  # импортируем необходимую библиотеку
#
# r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
# texts = json.loads(r.content)  # делаем из полученных байтов python объект для удобной работы
# print(type(texts))  # проверяем тип сконвертированных данных
#
# for text in texts:  # выводим полученный текст. Но для того чтобы он влез в консоль оставим только первые 50 символов.
#     print(text)


# import requests
# import json
#
# r = requests.get('https://api.github.com')
#
# d = json.loads(r.content)  # делаем из полученных байтов python объект для удобной работы
#
# print(type(d)) print(d['followers_url'])  # обращаемся к полученному объекту как к словарю и попробуем напечатать
# одно из его значений


# import requests
#
# r = requests.post('https://httpbin.org/post', data={'key': 'value'})  # отправляем пост запрос
# print(r.content)  # содержимое ответа и его обработка происходит так же, как и с гет-запросами, разницы никакой нет


# import requests
# import json
#
# data = {'key': 'value'}
#
# r = requests.post('https://httpbin.org/post', json=json.dumps(
#     data))  # отправляем пост запрос, но только в этот раз тип передаваемых данных будет JSON
# print(r.content)

# import lxml.html
# from lxml import etree
#
# # создадим объект ElementTree. Он возвращается функцией parse()
# tree = etree.parse('Welcome to Python.org.html',
#                    lxml.html.HTMLParser())  # попытаемся спарсить наш файл с помощью HTML-парсера. Сам HTML — это то,
# # что мы скачали и поместили в папку из браузера.
#
# ul = tree.findall(
#     'body/div/div[3]/div/section/div[3]/div[1]/div/ul/li')  # помещаем в аргумент методу findall скопированный xpath.
# # Здесь мы получим все элементы списка новостей. (Все заголовки и их даты)
#
# # создаём цикл? в котором будем выводить название каждого элемента из списка
# for li in ul:
#     a = li.find(
#         'a')  # в каждом элементе находим, где хранится заголовок новости. У нас это тег <a>. Т.е. гиперссылка,
#     # на которую нужно нажать, чтобы перейти на страницу с новостью. Гиперссылки в HTML — это всегда тэг <a>.
#     print(a.text)  # из этого тега забираем текст — это и будет нашим названием

# import requests  # импортируем наш знакомый модуль
# import lxml.html
# from lxml import etree
#
# html = requests.get('https://www.python.org/').content  # получим html главной странички официального сайта python
#
# # создадим объект ElementTree. Он возвращается функцией parse()
# tree = etree.parse('Welcome to Python.org.html',
#                    lxml.html.HTMLParser())  # попытаемся спарсить наш файл с помощью html парсера
#
# ul = tree.findall(
#     'body/div/div[3]/div/section/div[3]/div[1]/div/ul/li')  # помещаем в аргумент методу findall скопированный xpath
#
# # создаём цикл в котором мы будем выводить название каждого элемента из списка
# for li in ul:
#     a = li.find('a')  # в каждом элементе находим где хранится название. У нас это тег <a>
#     time = li.find('time')
#     print(time.get('datetime'), a.text)  # из этого тега забираем текст - это и будет нашим названием


import redis
# import json  # так-так-так, кто это тут у нас? Наш старый друг Джейсон заглянул на огонёк! Ну привет, чем ты сегодня нас порадуешь?
#
# red = redis.Redis(
#     host='localhost',
#     port=6379,
# )
#
# red.delete('dict1') # удаляются ключи с помощью метода .delete()
# print(red.get('dict1'))

red = redis.Redis(
    host='localhost',
    port=6379
)

cont = True

while cont:
    action = input('action:\t')
    if action == 'write':
        name = input('name:\t')
        phone = input('phone:\t')
        red.set(name, phone)
    elif action == 'read':
        name = input('name:\t')
        phone = red.get(name)
        if phone:
            print(f'{name}\'s phone is {str(phone)}')
    elif action == 'delete':
        name = input('name:\t')
        phone = red.delete(name)
        if phone:
            print(f"{name}'s phone is deleted")
        else:
            print(f"Not found {name}")
    elif action == 'stop':
        break