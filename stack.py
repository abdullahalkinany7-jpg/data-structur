class stack:
    def __init__(self):
        self.s=[]
    def add(self,va):
        self.s.append(va)
    def remove(self):
        if self.isEmpty():
            print("the list is empty")
        else:
         self.s.pop()
    def top(self):
        if self.isEmpty():
         print("the list is empty")
        else:
         print(self.s[-1])
    def isEmpty(self):
        return len(self.s)==0
s=stack()
s.add(6)
s.add(8)
s.remove()
