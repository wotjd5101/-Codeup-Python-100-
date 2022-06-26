a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)

l = list()

l.append(a)
l.append(b)
l.append(c)

for i in range(len(l)):
  if l[i]%2 == 0: 
    print(l[i])
