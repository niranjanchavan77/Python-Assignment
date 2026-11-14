Cube = lambda no : no * no * no

def main():

    num = int(input("enter the number : "))

    ret = Cube(num)
    print("cube of number is : ",ret)

if __name__ == "__main__":
    main()