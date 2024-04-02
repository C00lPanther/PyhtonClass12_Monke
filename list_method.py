l = [1,2,3,4,5,6]
n = int(input( ''' Enter the respective number for the method - 
            1.Append element
            2.Modify element
            3.Delete element from a position
            4.Sort list in asc order
       '''))
if n == 1:
    x = input('enter the new element')
    l.append(x)
elif n==2:
    x = input('enter the element index to be modified')
    y = input('enter the new element')
    l[x] = y
elif n ==3 :
    x = input('enter the element index to be deleted')
    del x
elif n ==4 :
    l.sort


