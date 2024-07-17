#make range functionality
def rng(start,stop,step):
    z = start
    while z<stop :
        print(z)
        z = z + step


a=int(input('etner the integer form which ou want to start'))
b= int(input('ente the integer before which the function stops'))
c = int(input('enter the step of the function'))
x = a
while x<b :
    print(x)
    x = x + c
rng(a,b,c)
'''
etner the integer form which ou want to start3
ente the integer before which the function stops9
enter the step of the function2
3
5
7

3
5
7
'''