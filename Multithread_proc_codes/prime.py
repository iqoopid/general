 # range function is not count last number (Ending number)
 # only 1 to 100 is counted
 #999983, 143141
for i in range(2,69317): 
    for j in range(2,69317):
        if i%j == 0:
            break
    if i == j:
        print(i,end=",")

print("its completed_1")
        
for i in range(2,69317): 
    for j in range(2,69317):
        if i%j == 0:
            break
    if i == j:
        print(i,end=",")

print("its completed_2")
        
for i in range(2,69317): 
    for j in range(2,69317):
        if i%j == 0:
            break
    if i == j:
        print(i,end=",")
        
print("its completed_3")