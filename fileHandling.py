file = open("abc.txt", "r+")
file.write("dbdbdbddb")

string = file.read()
print(string)


file.close()


print(string)
