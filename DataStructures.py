#LIST


x=[10,False,20.5]
y=[10,20,30,40,50,60,70,80,90]
y.pop()
print(y)
y.pop(2)
print(y)
y.insert(1,22)
print(y)
y.remove(22)
print(y)
y.append(1)
print(y)
print(y.count(10))
print(y.index(10))
y.reverse()
print(y)
y.sort()
print(y)
#print(x.sort())  ----- cannot sort an heterogenous list
y.sort(reverse=True)
print(y)
x.sort(reverse=True)
print(x)
print(x+y)


print()
print()


#Tuple  -> kind of immutable list (as it is immutable, adding and removing element methods are not provided)
t1 = (10,20,30,40,50,60,70,80,90)
print(t1.count(10))
print(t1.index(10))

print()
print()
print()
print()


#Set  ->  duplicacy not allowed and has elements in ascending order

s1={1,3,5,7,9}
s2={2,4,6,8,10}
print(s1)

s1.add(20)
print(s1)
s1.union(s2)
print(s1)
s2.intersection(s1)
print(s1)
s1.difference(s2)
print(s1)
s1.update(s2)
print(s1)
s1.difference(s2)
print(s1)
s1.difference_update(s2)
print(s1)








