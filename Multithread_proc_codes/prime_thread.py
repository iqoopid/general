# Python program to illustrate the concept
# of threading
# importing the threading module
import threading


def print_cube():
    for i in range(2,10000): 
        for j in range(2,10000):
            if i%j == 0:
                break
        if i == j:
            print(i,end=",")

    print("its completed_1 \n")

def print_square():
    for i in range(2,10000): 
        for j in range(2,10000):
            if i%j == 0:
                break
        if i == j:
            print(i,end=",")
    print("its completed_2 \n")
            
def print_third():
    for i in range(2,10000): 
        for j in range(2,10000):
            if i%j == 0:
                break
        if i == j:
            print(i,end=",")
    print("its completed_3 \n")


#314,159   
    
if __name__ == "__main__":
    # creating processes
    p1 = threading.Thread(target=print_square)
    p2 = threading.Thread(target=print_cube)
    p3 = threading.Thread(target=print_third)
    
    
    # starting process 1
    p1.start()
    p2.start()
    p3.start()

	# wait until process 1 is finished
    p1.join()
    p2.join()
    p3.join()

	# both processes finished
    print("Done!") 