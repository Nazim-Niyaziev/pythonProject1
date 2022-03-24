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

text = input("Введите строку: ")

f_letter = text[0]
count = 0
result = ""
for letter in text:
   if letter == f_letter:
       count += 1
   else:
       result += f_letter + str(count)
       f_letter = letter
       count = 1
result += f_letter + str(count)
print(result)


print(count)