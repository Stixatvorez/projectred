from math import *
from random import *

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
def square(a):
	p = 4*a
	s = a*a
	d = (a**2) / 2
	d = d**0.5
	
	k = (p, s, d)
	
	return k
	
print(square(16))
def season(num):

   if num == 12 or 1 <= num <= 2:

       print("Зима")

   elif  3 <= num <= 5:

       print("Весна")

   elif 6 <= num <= 8:

       print("Лето")

   elif 9 <= num <= 11:

       print("Осень")

   else:

       print("Неверно введён номер месяца!")

n = int(input("Введите номер месяца (1-12): "))

season(n)
