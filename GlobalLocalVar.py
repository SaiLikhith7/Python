"""global_var=12

def fun():
    local_var=100
    print(global_var)

fun()

#Local variable
xy=100

def cool():
    xy=200
    print(xy)

cool()

print(xy)"""



t=1
def increment():
    global t
    t=100
    print(t)

increment()

print(t)