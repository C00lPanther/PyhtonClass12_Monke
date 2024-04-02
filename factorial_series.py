n = int(input('enter the number of terms'))
deno = 1 
sum = 0
for i in range(1,n+1,1):
    deno = deno * i
    t = 1/deno
    sum = sum + t
print(sum)

