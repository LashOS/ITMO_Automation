class Car:
    def __init__(self, color, type, year, start: bool):
        self.color = color
        self.type = type
        self.year = year
        self.start = start
    def start_engine(self):
        if self.start:
            print("Автомобиль заведен")
        else:
            print("Автомобиль заглушен")
    def get(self):
        print(self.color, self.type, self.year)

car_1 = Car("green", "crossover", "2015", False)
car_1.get()
car_1.start_engine()