a = set()
b = set()

def mostrarC(a,b):
    c = a - b
    return c
    
for i in range(0,9):
    a.add(i+1)
    b.add(i+2)

print(a)
print(b)
print(mostrarC(a,b))