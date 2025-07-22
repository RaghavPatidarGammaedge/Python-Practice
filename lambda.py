x=lambda a: print(a)
y=lambda a,b: print(a+b)
z=lambda a,b,c: print(a+b+c)

x(10)
y(10,20)
z(10,20,30)



def func1():
    return lambda a:a**2

p=func1()(10)
print(p)