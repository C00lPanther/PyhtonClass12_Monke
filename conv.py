book={'identity':'pehchaan', 
      'intelligence':'samajhdaari',
      'hello':'namaste',
      'good night':'shubhratri',
      'bye':'alvida',
      }
x = input('enter a word you need translation  for:')
for k,v in book.items() :
    if x==k:
        print('the translation is:',book[k])
        break
    elif x==v:
        print('the translation is:',k)
        break
else:
    print('the word is not present in our dictionary')
