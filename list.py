#modifying a list
def mod(seq):
    for i in range(len(seq)):
        if seq[i]%2==0:
            seq[i] += 2
        else :
            seq[i] -= 1
            
    print(seq)



lis = eval(input('etner a list consisting of numbers'))
x = lis.copy()
for i in range(len(x)):
        if x[i]%2==0:
            x[i] += 2
        else :
            x[i] -= 1
print(x)

mod(lis)
'''
etner a list consisting of numbers[1,2,3,4,5,6]
[0, 4, 2, 6, 4, 8]
[0, 4, 2, 6, 4, 8]
'''