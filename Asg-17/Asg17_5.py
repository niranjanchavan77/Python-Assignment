n = int(input("enter the number : "))

for i in range(n,0,-1):
    for j in range(i):          # run i times
        print("*", end = " ")  
    print( )
    