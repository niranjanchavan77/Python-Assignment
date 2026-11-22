import threading

def EvenList(data):

    count = 0
    evenlst = []

    for i in range(2,data+1,2):
        if(i % 2 == 0):
            evenlst.append(i)
            count = count + i

    print("list of even number : ",evenlst)
    print("summation of even list : ",count)

def OddList(data):
    count = 0
    oddlst = []

    for i in range(1,data+1,2):
        if(i % 2 != 0):
            oddlst.append(i)
            count = count + i

    print("List of odd number : ",oddlst)
    print("summation of odd list : ",count)

def main():

    no = int(input("enter how many elements should be there in list : "))

    lst = []

    for i in range(no):
        x = int(input("enter the elements : "))
        lst.append(x)
    print("org list : ",lst)

    t1 = threading.Thread(target=EvenList, args=(no,))
    t2 = threading.Thread(target=OddList, args=(no,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    

if __name__ =="__main__":
    main()