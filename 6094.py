n = int(input())
a = input().split()

for i in range(n):
  a[i] = int(a[i])

mini = a[0]

for i in range(1, n, 1):
  
  if mini>a[i]:
    mini = a[i]
  
print(mini)
