#To demonstrate the immutability of tuple
def calc(a):
    a = list(a)
    a[0] = a[0]*2
    a[1] = a[1] + 1
    print("calc :", a)
P = (100,200)
print(P)
calc(P)
print(P)
