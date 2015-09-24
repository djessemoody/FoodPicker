#Similar to Picking Restaurants from a hat.
#Will Keep a list of restaurants already selected and when list is empty
#Will Populate restaurant list with  places that have already been selected

import random
#print(random.choice(list(open('foodlist.txt'))))
openfoodlist =list(open('foodlist.txt','r+'))
closedfoodlist = list(open('donefood.txt','r+'))
if not openfoodlist:
    print("Gone through entire list!")
    openfoodfile = open('foodlist.txt','w')
    for a in closedfoodlist:
        openfoodfile.write(a)
    openfoodfile.close()
    openfoodlist =list(open('foodlist.txt'))
    closedfoodlist = []

openfoodfile = open('foodlist.txt','w+')
closedfoodfile = open('donefood.txt','w+')
closedfoodfile.write('')
closedfoodfile.write('')
choice = random.choice(openfoodlist)
openfoodlist.remove(choice)
closedfoodlist.append(choice)
for a in sorted(closedfoodlist):
    closedfoodfile.write(a)
for a in sorted(openfoodlist):
    openfoodfile.write(a)


print("EAT TODAY AT: " + choice.upper())
openfoodfile.close()
closedfoodfile.close()
