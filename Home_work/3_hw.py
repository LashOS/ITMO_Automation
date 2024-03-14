def task_1(a, b):
    if a > b:
        print(a)
    elif a < b:
        print(b)
    elif a == b:
        print("Равны")
    else:
        print("Введите корректное число")
task_1(a = 1, b = 2)

def task_2(a, b):
    if a - b == 135 or b - a == 135:
        print("Yes")
    else:
        print("No")
task_2(a = 235, b = 100)
def task_3(a, b = ("Зима", "Весна", "Лето", "Осень")):
    if a == 12 and a >= 2:
        print(b[0])
    elif a in range(3, 6):
        print(b[1])
    elif a in range(6, 9):
        print(b[2])
    elif a in range(9, 12):
        print(b[3])
task_3(a = 6)

def task_4(a, b, c):
    if a > 10 and b > 10 and c > 10:
        print("yes")
    else:
        print("No")
task_4(a = 10, b = 11, c = 12)

def task_5(a, pos_count = 0, neg_count = 0):
    for num in a:
        if num >= 0:
            pos_count += 1
        else:
            neg_count += 1
    print("Положительных чисел в списке ", pos_count)
    print("Отрицательных чисел в списке ", neg_count)
task_5(a = [23, -34, 34, -43, 324])

def task_6(a, b, month = 29):
    print((a * (month * 12)) + (b * month))
task_6(a = 2, b = 4)


