class demo:
    company_name="gammaedge"
    def __init__(self, name, contact, email):
        self.name = name
        self.contact = contact
        self.email = email

    def display (self):
        print(self.name)
        print(self.contact)
        print(self.email)
        print(self.company_name)
        print()

d1 = demo("ram",12345,"ram@gmail.com")
d2 = demo("shyam",54321,"shyam@gmail.com")

d1.display()
d2.display()

d1.company_name="xyz"

d1.display()
d2.display()


d2.company_name="abc"

d1.display()
d2.display()

d1.contact=9090
d2.contact=8080

d1.display()
d2.display()
