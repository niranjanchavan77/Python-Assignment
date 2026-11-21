from MarvellousNum import ChekPrime, PrimeSum


def main():

    n1 = int(input("enter the number of elements to be stored : "))

    lst = []

    for i in range(n1):
        x = int(input("enter the numbers : "))
        lst.append(x)

    print("org list : ",lst) 

    ret =  PrimeSum(lst)
    print("summation of prime : ",ret)

if __name__ == "__main__":
    main()