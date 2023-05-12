class Stack:
    def _init_(self) -> None:
        self.data = []
        self.cost = 0

    def push(self, value):
        self.cost += 1
        self.data.append(value)

    def pop(self):
        self.cost += 1
        self.data.pop()

    def multipop(self, k):
        for i in range(k):
            self.pop()

    def returnCost(self):
        return self.cost


class DyanmicTable:
    def _init_(self) -> None:
        self.table = []
        self.capacity = 1
        self.cost = 0

    def insert(self, value):
        if len(self.table) == self.capacity:
            self.cost += self.capacity
            self.capacity *= 2
        self.cost += 1
        self.table.append(value)

    def returnCost(self):
        return self.cost


s1 = Stack()
s1.push(3)
s1.push(4)
s1.push(67)
s1.pop()
s1.push(32)
s1.multipop(2)
print(s1.returnCost()/7)

d1 = DyanmicTable()
for i in range(16):
    d1.insert(1)
print(d1.returnCost()/16)