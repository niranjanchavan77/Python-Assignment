from functools import reduce

Maximum = lambda a,b:(max(a,b))

def main():

    n = int(input("how many elements wnat in list : "))

    Data = []

    for i in range(n):
        i = int(input("enter the numbers : "))
        Data.append(i)

    print("ord list ",Data)

    RData = reduce(Maximum,Data)
    print("maximum num is : ",RData)

if __name__ == "__main__":
    main()