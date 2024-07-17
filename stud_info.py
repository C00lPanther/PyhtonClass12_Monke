#

import pickle
def data_entry():                                                           
    f = open("student.txt","wb")
    num = int(input('enter the number of students in your class: '))

    for i in range(num):    
        print('enter the information for student number: {}'.format(i+1))           

        name = input('enter your name: ')
        rno = int(input('enter your roll number: '))
        marks = eval(input('enter your marks: '))

        student = { 'Rno':rno, 'Name':name, 'Marks':marks}
        pickle.dump(student,f)
    f.close()

def data_receive_all():
    f = open("student.txt","rb")        
    while True:                                                             
        try:
            val = pickle.load(f)
            print(" %2d | %20s | %3d"%(val['Rno'], val['Name'].ljust(20," "), val['Marks']))
        except EOFError:
            print('No more records available \n')
            f.close()
            break

def data_receive():
    f = open("student.txt","rb")
    r = int(input('enter the roll number for student info: '))
    found = False
    while True:
        try:
            val = pickle.load(f)
            if val['Rno'] == r:
                print(" %2d | %20s | %3d"%(val['Rno'], val['Name'].ljust(20," "), val['Marks']))
                found = True
        except EOFError:
            break
    f.close()
    if found == False:
        print('No records available for the given roll number \n')

def data_update():
    f = open("student.txt","rb")
    val_list=[]
    while True:
        try:
            val = pickle.load(f)
            val_list.append(val)
        except EOFError:
            break
    f.close()

    r = int(input('enter the record to be updated: '))
    for i in range(len(val_list)):
        if val_list[i]['Rno'] == r:
            val = val_list[i]
            print('OLD RECORD:')
            print(' %2d | %20s | %3d'%(val['Rno'], val['Name'].ljust(20," "), val['Marks']))
            resp = input('do you want to change the record (y/n) : ')
            if resp.lower() == 'y':
                marks = eval(input('enter the updated marks: '))
                val_list[i]['Marks'] = marks

                f = open('student.txt','wb')
                for data in val_list:
                    pickle.dump(data,f)
                print('RECORDS UPDATED \n')
                f.close()
                break
        
    else:
        print('record not found')

def data_delete():
    val_list = []
    f = open('student.txt','rb')
    while True:
        try:
            val = pickle.load(f)
            val_list.append(val)
        except EOFError:
            break
    f.close()

    f = open('student.txt','wb')
    r = int(input('Enter the record to be deleted: '))
    for i in range(len(val_list)):
        if val_list[i]['Rno'] == r:
            val = val_list[i]
            print('OLD RECORD:')
            print(' %2d | %20s | %3d'%(val['Rno'], val['Name'].ljust(20," "), val['Marks']))
            resp = input('do you want to delete the record (y/n): ')
            if resp.lower() == 'y':
                continue
            else :
                pickle.dump(val_list[i],f)
        else :
            pickle.dump(val_list[i],f)
    f.close

    



while True:
    ans=int(input(""" 
STUDENT RECORDS -
enter the resp number for the following action
    1)Enter data
    2)Revieve all data
    3)Recieve data for a specific student
    4)Update data for a specific student
    5)Delete data
    6)EXIT 
response: """))
    print()
    if ans == 1:
        data_entry()
    elif ans == 2:
        data_receive_all()
    elif ans == 3:
        data_receive()
    elif ans == 4:
        data_update()
    elif ans==5:
        data_delete()
    elif ans==6:
        break
    else:
        print('WRONG INPUT')
    
