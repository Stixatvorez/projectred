from module1 import *
while True:
    print("Funktsioonid".center(50,"+"))
    v=input("arithmetic- A \nis_year_leap- B \nsquare- C \nseason- D \nbank- E \nis_prime- F \ndate- G \nxor_cipher- K")
    if v.upper()=="A":
        a=float(input("Arv 1: "))
        b=float(input("Arv 2: "))
        c=input("Tehe: ")
        result=arithmetic(a,b,c)
        print(result)
    elif v.upper()=="B":
        year=int(input("Введите год: "))
        result=is_year_leap(year)
        print(result)
    elif v.upper()=="C":
        kv=int(input("Введите сторону квадрата: "))
        result=square(kv)
        print(result)
    elif v.upper()=="D":
        kuu=int(input("Введите номер месяца: "))
        result=season(kuu)
        print(result)
    elif v.upper()=="E":
        a=float(input("Введите сумму депозита: "))
        years=int(input("Сколько лет прошло?"))
        result=bank(a,years)
        print(result)
    elif v.upper()=="F":
        a=int(input("Введите номер: "))
        result=is_prime(a)
        print(result)
    elif v.upper()=="K":
        print("Kodeerimine".center(60,"*"))
        result=xor_cipher(input("Введите текст"), input("Введите ключ :"))
        print(result)
        print("Dekodeerimine". center(60,"*"))
        de_rezult=xor_uncipher(result, input("Введите ключ:"))
        print(de_rezult)
    elif v.upper()=="G":
        day=int(input("Введите день: "))
        month=int(input("Введите месяц: "))
        year=int(input("Введите год: "))
        result=date(day,month,year)
        print(result)

