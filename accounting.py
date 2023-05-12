class accountingStack:
    def __init__(self):
        self.stack = []
        self.cost = 0
        self.balance = 0
    
    def insert(self,item):
        self.stack.append(item)
        self.cost += 1
        self.balance += 1
        self.printStack()

    def pop(self):
        self.stack.pop()
        self.cost += 1
        self.balance -= 1
        self.printStack()
    
    def multipop(self,k):
        for _ in range(k):
            self.pop()
    
    def printStack(self):
        print(self.stack,"balance : ",self.balance)
    

class accountingTable:
    def __init__(self):
        self.table = []
        self.size = 0
        self.capacity = 1
        self.balance = 0
    
    def insert(self,item):
        if self.size == self.capacity:
            self.capacity *= 2
            new_table = [None] * self.capacity
            for i in range(self.size):
                self.balance -= 1
                new_table[i] = self.table[i]
        self.table.insert(item,self.size)
        self.size += 1
        self.balance += 2
        self.printTable()
    
    def printTable(self):
        print(self.table," balance : ",self.balance)

s = accountingStack()
s.insert(10)
s.insert(20)
s.pop()
s.insert(30)
s.insert(40)
s.multipop(2)

print("\n\n")
t = accountingTable()
n = 16
for i in range(16):
    t.insert(i)