def Additon(data):

    sum = 0

    for i in data:
        sum = sum + i
    return sum

def main():

    n = int(input("enter the number of elements to be stored : "))

    lst = []

    for i in range(n):
        x = int(input("enter the numbers : "))
        lst.append(x)

    print("org list : ",lst) 

    ret = Additon(lst)
    print("summation of list is : ",ret)


if __name__ == "__main__":
    main()
