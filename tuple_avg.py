t1 =((1,2), (3,4,5), (6,7,8)) 
sum1 =0 
sum2 =0
tmean =0 
for x in range(0,len(t1) ,1):
    for y in t1[x] :
        sum2 = sum2 + y
    print('Elem', x + 1 , 'mean' , sum2/len(t1[x]))
    tmean = (tmean + sum2/len(t1[x]) )
    sum2 = 0
m = tmean/ len(t1)

print('mean of mean', m)
