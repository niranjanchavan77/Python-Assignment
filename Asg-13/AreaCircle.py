def Area(R,PI):
    area = PI * R * R
    return area

def main():

    radius = int(input("enter the radius : "))

    ret = Area(radius,3.14)

    print("area of circle is : ",ret)

if __name__ == "__main__":
    main()
