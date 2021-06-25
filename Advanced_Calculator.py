print("1.Add")
print("2.Minus")
print("3.Multiply")
print("4.Divide")
print("5.Cube")
choice = input("Enter here: ")
def add():
    number1 = input("input a number: ")
    number2 = input("input another number: ")
    result1 = float(number1) + float(number2)
    print(result1)
def minus():
    number3 = input("input a number: ")
    number4 = input("input another number: ")
    result2 = float(number3) - float(number4)
    print(result2)
def multiply():
    number5 = input("input a number: ")
    number6 = input("input another number: ")
    result3 = float(number5) * float(number6)
    print(result3)
def divide():
    number7 = input("input a number: ")
    number8 = input("input another number: ")
    result4 = float(number7) / float(number8)
    print(result4)
def cube():
    number9 = input("input a number: ")
    result5 = float(number9) * float(number9) * float(number9)
    print(result5)

if choice == "1":
    add()
elif choice == "2":
    minus()
elif choice == "3":
    multiply()
elif choice == "4":
    divide()
elif choice == "5":
    cube()
else:
    print("Invalid")