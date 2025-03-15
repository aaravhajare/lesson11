
row = int(input("enter n.o of rows"))
n = 1

for i in range(1 , row+1):

    for j in range(1,i+1):
        print(n , end=" ")
        n = n+1
    print()