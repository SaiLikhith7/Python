
#Passing Parameters

"""def func(i,j=200):
    print(i,j)

func(100)

func(100,250)

def named_args(name,greeting):
    print(greeting+" "+name)

named_args("sadiq","Hi")

named_args(name='sadiq',greeting='Hi')"""


def my_func(a,b,c):
    print(a,b,c)

my_func(10,20,30)

my_func(10,b=20,c=30)

my_func(10,c=30,b=20)