class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def sqare_A(self):
        return self.a * self.b
    def perimeter_A(self):
        return (self.a + self.b) * 2
obj_1 = Rectangle(10, 16)
obj_2 = Rectangle(88, 26)
obj_3 = Rectangle(69,74)
print(obj_1.sqare_A())
print(obj_1.perimeter_A())
print(obj_2.sqare_A())
print(obj_2.perimeter_A())
print(obj_3.sqare_A())
print(obj_3.perimeter_A())

class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def addition(self):
        return self.a + self.b
    def multiplication(self):
        return self.a * self.b
    def division(self):
        return self.a / self.b
    def subtraction(self):
        return self.a - self.b
obj_4 = Math(5,6)
print(obj_4.addition())
print(obj_4.multiplication())
print(obj_4.division())
print(obj_4.subtraction())

class Buttons:
    def __init__(self, text, type, loc, url):
        self.text = text
        self.type = type
        self.loc = loc
        self.url = url
    def click(self):
        return "Клик по кнопке - {}".format(self.text)
text_box = Buttons("Текстовое окно", "Кнопка", "", "https://demoqa.com/text-box")
Check_box = Buttons("Флажок", "Кнопка", "", "https://demoqa.com/checkbox")
Radio_Button = Buttons("Переключатель", "Кнопка", "", "https://demoqa.com/radio-button")
Web_Tables = Buttons("Вэб-таблицы", "Кнопка", "", "https://demoqa.com/webtables")
Buttons_Box = Buttons("Кнопки", "Кнопка", "", "https://demoqa.com/buttons")
Links = Buttons("Ссылки", "Кнопка", "", "https://demoqa.com/links")
Broken_Links_Images = Buttons("Неработающие ссылки — изображения", "Кнопка", "", "https://demoqa.com/broken")
Upload_and_Download = Buttons("Загрузить и скачать", "Кнопка", "", "https://demoqa.com/upload-download")
Dynamic_Properties = Buttons("Динамические свойства", "Кнопка", "", "https://demoqa.com/dynamic-properties")
print(text_box.click())
print(Check_box.click())
print(Radio_Button.click())
print(Web_Tables.click())
print(Buttons_Box.click())
print(Links.click())
print(Broken_Links_Images.click())
print(Upload_and_Download.click())
print(Dynamic_Properties.click())






