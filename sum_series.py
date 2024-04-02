n = int(input('enter the number of terms till which we want summation'))
sum1 = 0
sum2 =0
for i in range(1 ,n+1 , 1):
    for k in range(1 , i+1 ,1):
        sum2 = sum2 + k
    sum1 = sum1 + sum2
    sum2 = 0
print(sum1)
