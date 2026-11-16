from functools import reduce        #  important to import reduce

Addition = lambda a,b : (a + b)

def main():

    n = int(input("how many elements want in list : "))

    Data = []

    for i in range(n):
        i = int(input("enter the numbers : "))
        Data.append(i)

    print("org list ",Data)

    RData = reduce(Addition,Data)
    print("list after reduce ",RData)

if __name__ == "__main__":
    main()