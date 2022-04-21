print("Привет! Данная программа форматирует введеные числа в отсортированный по возрастанию список.\nЗатем выдает "
      "позицию элемента этого списка, который меньше числа 'number'\nвведенного пользователем, а следующий за этим "
      "элементом больше или равен ему ")

# from random import randint
# a[]
# for i in range(10):    (((( Альтернативный способ с автоматическим вводом и сортировкой данных ))))
#     a.append(randint(1, 50))
# a.sort()
# print(a)

array = str(input("Введите последовательность чисел через пробел: "))
try:
    lis_array = list(map(int, array.split()))
    print(lis_array)
    num = int(input("Теперь введите произвольное число: "))


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


    sort_array = merge_sort(lis_array)
    print("Отсортированный список:\n", sort_array)

    if num > sort_array[-1]:
        print("Введенное число больше максимального числа из отсортированного списка.")
    else:
        def binary_search(sort_array, num, left, right):
            if left > right:  # если левая граница превысила правую,
                print("Элемент отсутствует")  # значит элемент отсутствует

            middle = (right + left) // 2  # находим середину
            if sort_array[middle] < num <= sort_array[middle + 1]:  # если элемент в середине,
                return middle  # возвращаем этот индекс
            elif num < sort_array[middle]:  # если элемент меньше элемента в середине
                # рекурсивно ищем в левой половине
                return binary_search(sort_array, num, left, middle - 1)
            else:  # иначе в правой
                return binary_search(sort_array, num, middle + 1, right)


        print("Позиция элемента в списке -", (1 + binary_search(sort_array, num, 0, (len(sort_array) - 1))))

except ValueError:
    print("Некорректный ввод данных")


