CheckDiv = lambda data :(data % 3 == 0) | (data % 5 == 0)

def main():

    n = int(input("How many words "))

    Data = []

    for i in range(n):
        x = int(input("Enter element: "))
        Data.append(x)

    print("org list ",Data)

    FData = list(filter(CheckDiv,Data))
    print("list after filter : ",FData)

if __name__ == "__main__":
    main()