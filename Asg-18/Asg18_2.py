def Maximum(data):

    Maximum = max(data)
    return Maximum

def main():

    n = int(input("enter the number of elements to be stored : "))

    lst = []

    for i in range(n):
        x = int(input("enter the numbers : "))
        lst.append(x)

    print("org list : ",lst) 

    ret =  Maximum(lst)
    print("maximum num in list is : ",ret)


if __name__ == "__main__":
    main()
