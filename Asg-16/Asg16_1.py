def CheckNo(no):

    if(no == 0):
        print("zero")
    elif(no > 0):
        print("positive")
    elif(no < 0):
        print("negative")
    else:
        print("incorrect")
    
num = int(input("enter the number : "))
CheckNo(num)