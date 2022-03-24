
c = int(input("Введите количество билетов: "))
N = []
L = []
order = []
for i in range(1, c+1):
    N.append(i)
    age = int(input(f"Введите возвраст покупателя билета № {i} : "))
    L.append(age)
    if age < 18:
        cost = 0
    elif 18 <= age < 25:
        cost = 990
    elif age >= 25:
        cost = 1390
    order.append(cost)
print("Полная стоимость билетов - ",sum(order))
if c > 3:
    print("Стоимость билетов со скидкой 10% - ", sum(order)*0.9)