class Demo:
    def __init__(self,val1,val2) -> None:
        self.val1=val1
        self.val2=val2

    def fun(self):
        print(f"{self.val1} {self.val2}")
    def gun(self):
        print(f"{self.val1} {self.val2}")
obj1=Demo(11,21)
obj2=Demo(51,101)
obj1.fun()
obj1.gun()
obj2.fun()
obj2.gun()