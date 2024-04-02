'''
To display the names in dict which are longer than 5 charac
'''
def CountNow(seq):
    for k in seq :
        if len(seq[k])>5:
          print(seq[k].upper())



places = {1:'Delhi', 2:'London' , 3:'Paris', 4:'New york', 5:'Doha'}
for k in places :
    if len(places[k])>5:
        print(places[k].upper())
CountNow(places)