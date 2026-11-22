import threading

def Uppercase(data):

    uppercount = 0
    upperlst = []

    for i in(data):
        if i.isupper():
            upperlst.append(i)
            uppercount = uppercount + 1
    print("Upper case ch : ",upperlst)
    print("summation of uppercase ch is : ",uppercount)
    print(f"TID of Uppercase thread ->{threading.get_ident()} \n")


def Lowercase(data):
    lowercount = 0
    lowerlst = []
    
    for i in(data):
        if i.islower():
            lowerlst.append(i)
            lowercount = lowercount + 1
    print("lower case ch : ",lowerlst)
    print("summation of lowercase ch is : ",lowercount)
    print(f"TID of lowercase thread ->{threading.get_ident()} \n")


def Digits(data):
    digitcount = 0
    digitlst = []
        
    for i in(data):
        if i.isdigit():
            digitlst.append(i)
            digitcount = digitcount + 1
    print("digit case ch : ",digitlst)
    print("summation of digits ch is : ",digitcount)
    print(f"TID of digit thread ->{threading.get_ident()} \n")


def main():

    value = input("enter the Data : ")

    t1 = threading.Thread(target=Lowercase, args=(value,))
    t2 = threading.Thread(target=Uppercase, args=(value,))
    t3 = threading.Thread(target=Digits, args=(value,))


    t1.start()
    t1.join()

    t2.start()
    t2.join()

    t3.start()
    t3.join()
    

if __name__ =="__main__":
    main()