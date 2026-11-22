import threading

def Even(no):

    print("first 10 even numbers are : ")

    for i in range(2,no+1):
        if(i % 2 == 0):
            print(i)

def Odd(no):

    print("first 10 odd numbers are : ")

    for i in range(1,no+1):
        if(i % 2 != 0):
            print(i)

def main():

    Num = int(input("enter the number : "))

    t1 = threading.Thread(target=Even , args=(Num,))
    t2 = threading.Thread(target=Odd , args=(Num,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()