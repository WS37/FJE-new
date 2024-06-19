from iterators.JSONIterator import JSONIterator

class Context():
    def __init__(self, style_strategy, icon_family_strategy):
        self.style_strategy = style_strategy
        self.icon_family_strategy = icon_family_strategy

    def setStrategy(self):
        self.style = self.style_strategy()
        self.icon_family = self.icon_family_strategy()

    def doSomething(self, data):
        iterator = JSONIterator()
        root = iterator.getNext(data)
        print(root.display(self.style, self.icon_family))