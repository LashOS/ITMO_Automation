class Input:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text
search = Input("input#search")
a = Input("input#a")
print(search.loc)
print(a.text)
class Button:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text
b = Button("Button#b")
c = Button("button#c")
print(b.loc)
print(c.text)
class Title:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text
d = Title("Title#d")
e = Title("Title#e")
print(d.loc)
print(e.text)
class Link:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text
f = Link("Link#f")
g = Link("Link#g")
print(f.loc)
print(g.text)
