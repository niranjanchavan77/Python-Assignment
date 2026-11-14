Maximum = lambda a,b : a > b

def main():

    no1 = int(input("enter the first number : "))
    no2 = int(input("enter the second number : "))

    ret = Maximum(no1,no2)

    if(ret == True):
        print(f"{no1} is greater then {no2} ")
    else:
        print(f"{no2} is greater then {no1} ")

if __name__ == "__main__":
    main()