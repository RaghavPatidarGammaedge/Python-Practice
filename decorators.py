def myDecorator(func):
    def wrapper():
        print("myDecorator1")
        func()
        print("myDecorator2")

    return wrapper

@myDecorator
def myFunc():
    print("myFunc")


myFunc()

class A:
    @myDecorator
    def meth1(self):
        print("meth1")

a=A()
a.meth1()