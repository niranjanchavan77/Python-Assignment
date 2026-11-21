def ChekPrime(data):
    if (data <= 1):
        return False

    for i in range(2,data + 1):
        if (data % 2 == 0):
            return False
    return True

def PrimeSum(data):

    total = 0

    for i in data:
        if ChekPrime(i):
            total = total + i
    return total