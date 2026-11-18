num = int(input("enter the number : "))

sum = 0

for i in range(1,num):
    if (num % i == 0):
        sum = sum + i
        print("factor of number are",i)
    else:
        pass

print("sum of factors of number is : ",sum)
