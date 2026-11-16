SquareList = lambda No : (No * No)

def main():

    n = int(input("How many elements? "))

    Data = []

    for i in range(n):
        x = int(input("Enter element: "))
        Data.append(x)

    print("List is:", Data)


    MData = list(map(SquareList, Data))

    print("Data after map : ",MData)
    
if __name__ == "__main__":
    main()