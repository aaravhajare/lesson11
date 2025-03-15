
rs = int(input("enter n.o of rows"))
if (rs%2)==0:
    hd = int(rs/2)

else:
    hd = int(rs/2)+1

s = hd-1

for i in range(1,hd+1):
    for j in range(1,s+1):
        print(end=" ")
    s = s-1
    num = 1
    for j in range(i*2-1):
        print(end= str(num))
        num = num+1
    print()
space = 1
for i in range(1,hd):
    for j in range(1,s-1):
        print(end=" ")
    s = s+1
    num = 1
    for j in range(1,2*(hd-i)):
        print(end= str(num))
        num = num+1
    print()