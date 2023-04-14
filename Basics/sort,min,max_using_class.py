class num:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def add(self):
        print(f"sum of {self.a} + {self.b} + {self.c} is {self.a+self.b+self.c}")
        pass
    def min(self):
        print(f"min of {self.a} ,{self.b} , {self.c} is {min(self.a,self.b,self.c)}")
        pass
    def max(self):
        print(f"max of {self.a} ,{self.b} , {self.c} is {max(self.a,self.b,self.c)}")
        pass
obj=num(10,20,30)
obj.add()
obj.min()
obj.max()
 