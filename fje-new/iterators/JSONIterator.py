from iterators.Iterator import Iterator
from components.Container import Container
from components.Leaf import Leaf

class JSONIterator(Iterator):
    def hasMore(self, data):
        return isinstance(data, dict)

    def getNext(self, data):
        if (self.hasMore(data)):
            parent = Container("root")
            for key, value in data.items():
                child = self.getNext(value)
                child.name = key
                parent.add(child)
            return parent
        elif data is not None:
            return Leaf("value", data)
        return Leaf("null")
