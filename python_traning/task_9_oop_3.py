class Soda:
    def __init__(self, ing=None):
        self.ing = ing

    def show_my_drink(self):
        if self.ing:
            print(f"Gazirovka i {self.ing}")
        else:
            print("Obi4naia gazirovka")
drink1 = Soda()
drink2 = Soda("Malina")
drink1.show_my_drink()
drink2.show_my_drink()
