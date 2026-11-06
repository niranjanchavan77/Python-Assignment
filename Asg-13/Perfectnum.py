number = int(input("enter the number : "))

sum = 0

for i in range (1,number):
    if (number % i == 0):
        sum = sum + i

if (number == sum):
    print("num is perfect num ")
else:
    print("num is not perfect ")
