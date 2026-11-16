CheckOdd = lambda no :(no % 2 != 0)

def main():

    n = int(input("How many elements? "))

    Data = []

    for i in range(n):
        x = int(input("Enter element: "))
        Data.append(x)

    print("org list ",Data)

    FData = list(filter(CheckOdd,Data))
    print("list after filter : ",FData)

if __name__ == "__main__":
    main()
