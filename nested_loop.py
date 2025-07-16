#nested loops in python
# start pattern number row print the star

row = int(input("Enter the nubmer row"))
for i in range(1 ,row + 1):
    for j in range(0,i):
        print("*",end=" ")
    print("")
