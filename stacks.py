#works on Last In First Out 

class stack:
    def __init__(self):
        self.items = []
        self.length = 10
    
    def isempty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
    
    def pop(self):
        if not self.isempty():
            return self.items.pop()
        else:
            print('Stack is empty')
            
    def add(self,value):
        if len(self.items) >= self.length:
            print('Stack is full')
        else:
            self.items.append(value)
            
    def print_stack(self):
        for value in self.items:
            print(value)
            
s =  stack()
s.add(3)
s.add(5)
s.add(6)

print('We popoed ',s.pop())

s.print_stack()
