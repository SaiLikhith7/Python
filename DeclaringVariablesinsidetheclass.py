#Declaring Varaibles inside the class


class MyClass:
    a,b=100,200

    def add(self):
        print(self.a+self.b)
    def mul(self):
        print(self.a*self.b)

mc=MyClass()
mc.add()
mc.mul()