 # range function is not count last number (Ending number)
 # only 1 to 100 is counted
 #999983, 143141
# importing the multiprocessing module


# multiple core with multiple process
# parallel programming
# gives output much faster

import multiprocessing

def print_cube():
    for i in range(2,69317): 
        for j in range(2,69317):
            if i%j == 0:
                break
        if i == j:
            print(i,end=",")

    print("its completed_1 \n")

def print_square():
    for i in range(2,69317): 
        for j in range(2,69317):
            if i%j == 0:
                break
        if i == j:
            print(i,end=",")
    print("its completed_2 \n")
            
def print_third():
    for i in range(2,69317): 
        for j in range(2,69317):
            if i%j == 0:
                break
        if i == j:
            print(i,end=",")
    print("its completed_3 \n")
    
    
if __name__ == "__main__":
    # creating processes
    p1 = multiprocessing.Process(target=print_square)
    p2 = multiprocessing.Process(target=print_cube)
    p3 = multiprocessing.Process(target=print_third)
    
    
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