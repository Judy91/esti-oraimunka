import random


list=[]
for i in range(10):
    list.append(random.randrange(1,10))

#Kiirom a listat
for i in list:
    print(i) 
osszeg=sum(list)
atlag=osszeg/len(list)
print("A számok átlaga",atlag)
minimum=min(list)
print(minimum)
maximum=max(list)
print (maximum)
#Eldöntés tétele
vane=False
for i in list:
    if i ==9 :
        vane=True

if vane==True :
    print("Volt benne 9-es!!!")
else:
    print( "Nincs benne 9-es!")