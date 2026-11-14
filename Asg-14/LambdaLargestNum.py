Largest = lambda a,b : max(a , b)

def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    Ret = Largest(Value1,Value2)  
    
    print("largest num is : ",Ret)

if __name__ == "__main__":
    main()