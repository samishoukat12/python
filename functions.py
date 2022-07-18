fruits = ["banana", "apple", "mango"]


def for_function():
    for x in fruits:
        if x == "banana":
            print("Found it!")
            break
    print(x[0])


def range_function():
    for x in range(2, 40, 2):
        print(x)
    if x == 10:
        print("Found it!")
    elif x == 20:
        print("forunt of it!")


def max_Num(x, y, z):
    if x > y:
        if x > z:
            print("x is greater")
        else:
            print("z is greater")
    else:
        if y > z:
            print("y is greater")
        else:
            print("z is greater")


def result(marks):
    if(marks > 80):
        print("A")
    elif(marks > 60):
        print("B")
    elif(marks > 40):
        print("C")
    else:
        print("D")


max_Num(10, 20, 30)
for_function()
range_function()
result(90)
