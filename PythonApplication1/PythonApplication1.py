from keyboard import *
from math import *
from random import *
while True:
    print("Funktsioonid".center(50,"+"))
    print("arithmetic- A,\nis_year_leap-Y,\nsquare-S \nseason-Z \nbank-B \nis_prime-I \ndate-D \nXOR_cipher-X \nXOR_uncipher-X2 ")
    v=input()
    if v.upper()=="A":
        arv1=float(input("Arv 1:"))
        arv2=float(input("Arv 2:"))
        sym=input("Tehe:")
        rezult=arithmetic(arv1,arv2,sym)
        print(rezult)
    elif v.upper()=="Y":
        rezult=is_year_leap(int(input("Sisesta aasta: ")))
        print(rezult)
    elif v.upper()=="S":
        rezult=square(int(input("Sisesta piirkond: ")))
        print(rezult)
    elif v.upper()=="Z":
        rezult=season(int(input("Sisestage kuupäev: ")))
        print(rezult)

    elif v.upper()=="B":
        rezult=bank(int(input("Kui palju raha soovite laenata: ")))
        print(rezult)
    elif v.upper()=="I":
        rezult=is_prime(int(input("Sisesta ARG  : ")))
        print(rezult)
    elif v.upper()=="D":
        rezult=date(int(input("Sisesta kuupäev: ")))
        print(rezult)
    elif v.upper()=="X":
        rezult=XOR_cipher(int(input("Sisesta F: ")))
        print(rezult)
    elif v.upper()=="X2":
        rezult=XOR_uncipher(int(input("Sisesta F2: ")))
        print(rezult)
