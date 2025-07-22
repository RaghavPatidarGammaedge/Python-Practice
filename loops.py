
#for loop
for i in range(5):
    print(i)


#while loop
i=10
while i>0:
    print(i)
    i-=1


#nested for loop
for i in range(10):
    for j in range(i):
        print("*",end=' ')
    print()

#loops with data structures and else clause
list1=[10,20,30,40,50]
for i in list1:
    if(i==33):
        print(list1)
        break
else:
    print(list1)



