num = -1
if num > 0:
    print("Число больше")
elif(num == 0):
    print("Число равно 0")
else:
    print("Число отрицательное")

def str_yes_no(str_1, str_2):
    if str_1 == str_2:
        print("Равно")
    else:
        print("Не равно")
str_yes_no(str_1 = "test", str_2 = "test1")

permit_print = True

if num > 0 and permit_print:
    print("num - положительное число")

def education(year: int):
    if year >= 1 and year <= 4:
        print("Бакалавр 1-4 курс")
    elif year >= 5 and year <= 6:
        print("Магистр 5-6 курс")
    elif year >= 7 and year <= 9:
        print("Асптрант 7-9 курс")
    else:
        print("Введите корректный год обучения")
education(year = 5)

def noumber(num):
    if num in range(1, 101):
        print("+")
    elif num in range(-100, 0):
        print("-")
    elif num == 0:
        print("0")
    else:
        print("Enter correct noumber")
noumber(num = 56)