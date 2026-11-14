multiplication = lambda a,b : (a * b)

def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    Ret = multiplication(Value1,Value2)  
    
    print("multiplication is : ",Ret)

if __name__ == "__main__":
    main()