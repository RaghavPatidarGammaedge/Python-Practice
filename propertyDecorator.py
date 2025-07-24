class A:
    def __init__(self, n):
        self.__n = n

    @property
    def n(self):
        print("value of n is = ",end='')
        return self.__n

    @n.setter
    def n(self, n1):
        print("setting n = ",n1)
        self.__n = n1

    @n.deleter
    def n(self):
        del self.__n
        print("n deleted sucess")


a = A(5)
print(a.n)
a.n = 10
print(a.n)
del a.n
