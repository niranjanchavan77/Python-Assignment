import threading

def Even(no):

    sumeven = 0

    for i in range(2,no,2):
        sumeven = sumeven + i
    print("summation of even factor is : ",sumeven)

def Odd(no):

    sumodd = 0

    for i in range(1,no,2):
        sumodd = sumodd + i
    print("summation of odd factors is : ",sumodd)

def main():

    value = int(input("enter the number : "))

    t1 = threading.Thread(target=Even , args=(value,))
    t2 = threading.Thread(target=Odd , args=(value,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()