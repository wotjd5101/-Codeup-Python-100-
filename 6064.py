a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

mini = 0

if a>b:
  if b>c:
    mini = c
    
  else:
    mini = b

else:
  if a>c:
    mini = c
  else:
    mini = a

print("{0}" .format(mini))

print()

