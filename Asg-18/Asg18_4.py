def SearchElement(data,ele):

    count = 0

    for i in data:
        if(i == ele):
            count = count + 1
        
    return count

def main():

    n1 = int(input("enter the number of elements to be stored : "))

    lst = []

    for i in range(n1):
        x = int(input("enter the numbers : "))
        lst.append(x)

    print("org list : ",lst) 

    n2 = int(input("enter the number to find  : "))

    ret =  SearchElement(lst,n2)
    print("frequency of num in list is : ",ret)

if __name__ == "__main__":
    main()
