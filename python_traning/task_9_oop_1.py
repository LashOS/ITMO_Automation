from task_9_checks import Checks
class Input(Checks):
    def __init__(self, text):
        self.text = text
search = Checks("input#search")
search1 = Input("input#search")
print(search1.text)
print(search.loc)
class Button(Checks):
    def __init__(self, text):
        self.text = text
click = Checks("Button#click")
click1 = Button("Button#click")
print(click.loc)
print(click1.text)
class Title(Checks):
    def __init__(self, text):
        self.text = text
date = Checks("Title#date")
date1 = Title("Title#date")
print(date.loc)
print(date1.text)
class Link(Checks):
    def __init__(self, text):
        self.text = text
url = Checks("Link#url")
url1 = Link("Link#url")
print(url.loc)
print(url1.text)