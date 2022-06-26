a, b = input().split()

a = int(a)
b = int(b)
c = bool(a)
d = bool(b)

print (bool((a and b) or ((not a) and (not b))))
