'''
To display a tuple of the length of words in the string
'''
def lenWords(stg):
    tup = ()
    lis = stg.split()
    for i in lis:
        tup += (len(i),)
    return(tup)

s = input('enter a string:')
l = s.split()
t = ()
for i in l:
    t += (len(i),)
print(t)
print(lenWords(s))
