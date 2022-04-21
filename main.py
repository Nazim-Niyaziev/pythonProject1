# per_cent = {'ТКБ': 5.6, 'СКБ': 5.9,
#             'ВТБ': 4.28, 'СБЕР': 4.0}
# money = int(input("Введите сумму вклада: "))
# list_p = per_cent.values()
# L = list(list_p) #формируем список из значений процентных ставок
#
# p_money = {'ТКБ': int((L[0] * money)/100), 'СКБ': int((L[1] * money)/100),
#            'ВТБ': int((L[2] * money)/100), 'СБЕР': int((L[3] * money)/100)}
# list_money = list(p_money.values())
# print("ТКБ - " + str(list_money[0]) + ", CКБ - " + str(list_money[1]) + ", ВТБ - " + str(list_money[2]) + ", СБЕР - " + str(list_money[3]))
#
# deposit_max = str(max(p_money.values())) #выбираем максимальное значение депозита
# print("Максимальное начисление средств: " + deposit_max + "руб.")

def merge_sort(L):  # "разделяй"
    if len(L) < 2:  # если кусок массива равен 2,
        return L[:]  # выходим из рекурсии
    else:
        middle = len(L) // 2  # ищем середину
        left = merge_sort(L[:middle])  # рекурсивно делим левую часть
        right = merge_sort(L[middle:])  # и правую
        return merge(left, right)  # выполняем слияние


def merge(left, right):  # "властвуй"
    result = []  # результирующий массив
    i, j = 0, 0  # указатели на элементы

    # пока указатели не вышли за границы
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # добавляем хвосты
    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result
