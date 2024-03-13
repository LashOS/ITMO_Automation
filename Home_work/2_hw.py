def task_1(a: int, b: float, c: str, d: list, e: bool):
    print(a, "относится к типу", type (a))
    print(b, "относится к типу", type (b))
    print(c, "относится к типу", type (c))
    print(d, "относится к типу", type (d))
    print(e, "относится к типу", type (e))
task_1(a = 1, b = 2.2, c = 'Privet', d = [1, 2, 3], e = True)
def task_2(a = [1,2,3,4,5,8,13,21])->list:
    return a[0:3]
print(task_2())
# называется "список"

def task_3(a)-> int:
    return a*a
print(task_3(2))