import random

print("git proba")
print("Ez már a második commit")
print ("Jó lesz ez")

szam1=int(input("Kérek 1 számot a felhasználótól"))
szam2=int(input("Kérek 2 számot a felhasználótól"))
osszeg=szam1+szam2
print(osszeg)


list=[]
for i in range(10):
    list.append(random.randrange(1,10))

#Kiirom a listat
for i in list:
    print(i) 