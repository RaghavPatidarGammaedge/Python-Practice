d2={1:'65',2:{3:'c',4:'awa'}}

s2=[]
for i in d2.keys():
        s2.append(int(i))
        if i==2:
              for j in d2.get(i).keys():
                      s2.append(int(j))

print(s2)
# print(d2.get(2).get(4).get(22))
# print(d2[2][4][22])


