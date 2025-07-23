class A:
    def __init__(self, name , contact , email):
        self.name = name
        self._contact = contact
        self.__email = email

    def getter(self):
        print(self.__email)
    def setter(self,value):
        self.__email = value
        print("setter")

a1=A("abc",1234,"abc@gmail.com" )
a1.getter()
a1.setter(12345)
a1.getter()
# print(a1.email) throws error
print(a1.name)
print(a1._contact)
