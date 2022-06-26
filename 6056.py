a, b = input().split()
a = int(a)
b = int(b)

a = bool(a)
b = bool(b)

print(bool ((a and (not b)) or ((not a) and b)))
