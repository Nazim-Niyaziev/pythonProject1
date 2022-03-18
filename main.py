per_cent = {'ТКБ': 5.6, 'СКБ': 5.9,
            'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму вклада: "))
list_p = per_cent.values()
L = list(list_p) #формируем список из значений процентных ставок

p_money = {'ТКБ': int((L[0] * money)/100), 'СКБ': int((L[1] * money)/100),
           'ВТБ': int((L[2] * money)/100), 'СБЕР': int((L[3] * money)/100)}
list_money = list(p_money.values())
print("ТКБ - " + str(list_money[0]) + ", CКБ - " + str(list_money[1]) + ", ВТБ - " + str(list_money[2]) + ", СБЕР - " + str(list_money[3]))

deposit_max = str(max(p_money.values())) #выбираем максимальное значение депозита
print("Максимальное начисление средств: " + deposit_max + "руб.")