#To create a box
def box(a,b,c):
    for i in range(a):
        print(b*c)
hig = int(input('enter the height of the box:'))
bre = int(input('etner the breadth of the box:'))
char = input('enter the character of the box:')
for i in range(hig):
    print(char*bre)

box(hig,bre,char)
'''
enter the height of the box:4
etner the breadth of the box:3
enter the character of the box:#
###
###
###
###
###
###
###
###
'''