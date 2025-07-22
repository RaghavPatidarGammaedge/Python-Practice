def func1(name='ricky',contact=1234):
    print(name)
    print(contact)
    def func2():
        print("func2 called")
    func2()
    return {'name':name,'contact':contact}

print(func1(name='tom',contact=4321),end='\n\n')
print(func1(contact=5678),end='\n\n')
print(func1(name='alex'),end='\n\n')
# print(func2(),end='\n\n')  will cause error