CountkEven = lambda no :(no % 2 == 0)

def main():

    count = 0

    n = int(input("How many elements? "))

    Data = []

    for i in range(n):
        x = int(input("Enter element: "))
        Data.append(x)

    print("org list ",Data)

    FData = list(filter(CountkEven,Data))
    print("list after filter : ",FData)
    print("number if even elements : ",len(FData))

if __name__ == "__main__":
    main()
