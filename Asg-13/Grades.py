def Greades(num):

    if(num >= 75):
        print("Distinction")
    elif(num >= 60):
        print("first class")
    elif(num >= 55):
        print("second class")
    elif(num < 50):
        print("fail")
    else:
        print("detained")

def main():

    number = int(input("entr the correct number : "))

    Greades(number)

if __name__ == "__main__":
    main()