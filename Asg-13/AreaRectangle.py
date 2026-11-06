def Area(L,W):
    area = L * W
    return area

def main():

    length = int(input("enter the length : "))
    wedgth = int(input("enter the wedgth : "))

    ret = Area(length,wedgth)

    print("area of rectangle is : ",ret)

if __name__ == "__main__":
    main()
