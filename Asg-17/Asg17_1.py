from ModuleArithmatic import Addition, Substraction, Multiplication, Division

def main():

    value1 = int(input("enter the first number : "))
    value2 = int(input("enter the second number : "))

    ret = Addition(value1,value2)
    print("addition is : ",ret)

    ret = Substraction(value1,value2)
    print("Substraction is : ",ret)

    ret = Multiplication(value1,value2)
    print("Multiplication is : ",ret)

    ret = Division(value1,value2)
    print("Division is : ",ret)

if __name__ == "__main__":
    main()

