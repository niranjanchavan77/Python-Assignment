import threading

def DisplayNum():

    for i in range(1,51):
        print(i)

def DisplayRevNum():

    for i in range(50,0,-1):
        print(i)

def main():

    Thread1 = threading.Thread(target=DisplayNum)
    Thread2 = threading.Thread(target=DisplayRevNum)

    Thread1.start()
    Thread1.join()
    print("Thread1 is completed \n")

    Thread2.start()
    Thread2.join()
    print("Thread2 is completed \n")



if __name__ == "__main__":
    main()