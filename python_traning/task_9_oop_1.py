from task_9_checks import Checks
class Input(Checks):
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc
search = Input("input#search", "input#search")
print(search.loc)
class Button(Checks):
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc
click = Button("Button#click", "Title#date")
print(click.loc)
class Title(Checks):
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc
date = Title("Title#date", "Title#date")
print(date.loc)
class Link(Checks):
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc
url = Link("Link#url", "input#text")
print(url.loc)

