

class MyClass:
    def m1(self):
        print("Instance Methods")

    @staticmethod
    def m2(self):
        print(self)

mc=MyClass()
mc.m1()

MyClass.m2(10)

