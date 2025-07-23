class a:

    def meth1(self):
        print("meth1 aaa")

    def meth2(self):
        print("meth2 aaa")

class b:#(a):
        def meth3(self):
            print("meth3 bbb")



class c(a,b):
    def meth2(self):
        print("meth2 ccc")


# b1=b()
# b1.meth1()
# b1.meth2()

c1=c()
c1.meth1()
c1.meth2()
c1.meth3()
