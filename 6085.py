w, h, b = input().split()

w = int(w)
h = int(h)
b = int(b)

result = (w*h*b)/(8*(1024**2))

print(f'{result:0.2f} MB')
