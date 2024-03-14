class Button:
    type: str = "Knopka"
    def __init__(self, text, link):
        self.text = text
        self.link = link
home = Button("Domoy", "/home")
catalog_msk = Button("Katalog", "/msk/catalog")

print(home.text)
print("Knopka " + home.text + " imeet ssilku " + home.link)

print("\n")

print(catalog_msk.text)
print("Knopka " + catalog_msk.text + " imeet ssilku " + catalog_msk.link)

class ButtonTwo:
    def __init__(self, text, link, loc):
        self.text = text
        self.link = link
        self.loc = loc
    def click(self):
        return "Kilik po lokatoru - {}".format(self.loc)
home_two = ButtonTwo("Domoy", "/home", "button#home")
print(home_two.click())

 