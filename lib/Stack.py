class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
            return True
        else:
            return False

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None 

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        for index, item in enumerate(self.items[::-1]):
            if item == target:
                return index
        return -1
