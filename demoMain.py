print("CALCULATOR")
print("1. +")
print("2. -")
print("3. *")
print("4. /")
print("5. **")
print("6. /")
choice = input("Enter your choice->")
num1 = int(input("Enter first number->"))
num2 = int(input("Enter second number->"))
print("Your Answer is",end=' ')

# if choice == "+": print(num1 + num2)
# elif choice == "-": print(num1 - num2)
# elif choice == "*": print(num1 * num2)
# elif choice == "/": print(num1 / num2)
# elif choice == "**": print(num1 ** num2)

match choice:
    case '+':   print(num1 + num2)
    case '-':   print(num1 - num2)
    case '*': print(num1 * num2)
    case '/': print(num1 / num2)
    case '**': print(num1 ** num2)
    case '//': print(num1 // num2)


