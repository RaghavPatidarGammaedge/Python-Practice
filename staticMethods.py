class A:
    @staticmethod
    def meth1():
        print("static method")

    @classmethod
    def meth2(cls):
        print("class method")

A.meth1()
A.meth2()