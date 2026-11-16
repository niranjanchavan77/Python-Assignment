GreaterLen = lambda data :len(data) > 5

def main():

    n = int(input("How many words "))

    Data = []

    for i in range(n):
        x = str(input("Enter element: "))
        Data.append(x)

    print("org list ",Data)

    FData = list(filter(GreaterLen,Data))
    print("list after filter : ",FData)

if __name__ == "__main__":
    main()
