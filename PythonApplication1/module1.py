#1

def arithmetic(a: float,b:float,c:float):
    """Lihtne kalkulaator
    + - liitmine
    - - lahutamine
    * - korrustamine
    / - jagamine
    :param float a:Esimine arv
    :param float b:Teine arv
    :param str c: Aritmeetiline tehing
    :rtype var: Märamata tüüb
    """   
    if c=="+":
        r=a+b
    elif c=="-":
        r=a-b 
    elif c=="*":
        r=a*b 
    elif c== "/":
         if b!=0:
             r=a/b 
         else:
             print("Div0")
             r=0.0 

    else:
        print("Viga")
        r=0.0
    return r

#2
def arithmetic(a: float,b:float,c:str):
 def is_year_leap(aasta: int):
    """Liigaasta leidmine
    Tagastab true kui aasta on liigaasta ja False kui ei ole
    :param int aasta: Aasta number
    :rtype bool: Funktsioni vastus loogilises formaadis
    """
    if aasta%4==0:
        vastus=True
    else:
        vastus=False
    return vastus
#3
def square(a):
	p = 4*a
	s = a*a
	d = (a**2) / 2
	d = d**0.5
	
	k = (p, s, d)
	
	return k
	
print(square(16))
#4
def season(num):

   if num == 12 or 1 <= num <= 2:

       print("Talv")

   elif  3 <= num <= 5:

       print("Kevad")

   elif 6 <= num <= 8:

       print("Suvi")

   elif 9 <= num <= 11:

       print("Sügis")

   else:

       print("Sisestatud vale kuu number!")

n = int(input("Sisestage kuu number (1-12): "))

season(n)
#5

n = int(input())
m = int(input())
y = int(input())

def bank(n, m, y):
        nal = n
        year = y
        def money():
            if year >0:
                nal = n*1.1+m
                year = year -1
                return money()
            else:
                return nal

print (nal)


print (nal)
#6
from cmath import sqrt


def is_prime(number):
    # Kõik paarisarvud peale 2 ei ole lihtsad
    if number % 2 == 0 and number != 2:
        return False
    # 0 ja 1 ei ole lihtsad
    if number == 0 or number == 1:
        return False
    # Kordame numbreid 3-st sisestatud juureni, samm - 2
    for n in range(3, int(sqrt(number).real) + 1, 2):
        if number % n == 0:  # Kui arv jagub võrdselt, siis pole see lihtne
            return False
    return True  # Ülejäänud arvud on algarvud

n = int(input('Sisestage number: '))
print(is_prime(n))
#7

import datetime
d=int(input("Sisestage päev"))# пример - 15
m=int(input("Sisestage kuu"))# пример - 5
y=int(input("Sisestage aasta"))# пример - 2018
try:
    data=datetime.date(y,m,d)
    print(data)
    print("Olemasolev kuupäev")
    print("Sellist kuupäeva pole")
#8

def str_xor(string,key):
    return "".join([chr(ord(c1) ^ ord(c2)) for (c1,c2) in zip(string,key)])
 
str1=""
key=""
arr=['a','б','в','г','д','a','b','c','d','e']
f=open("in.txt","r",encoding="utf-8")
for line in f:
    str1=str1+line
f.close()
 
 
for i in range(len(str1)):
    if str1[i]==" ":
        continue
    key=key+str(i+5*(i%2))+arr[i%10]
  
print('\n Lähtetekst: '+str1+'\n')
print('\n Võti: '+key)
encoded = str_xor(str1,key)
print('\n Šifreeritud tekst: '+encoded+'\n')
decoded = str_xor(encoded,key)
print('\n Dekrüpteeritud tekst: '+decoded+'\n')