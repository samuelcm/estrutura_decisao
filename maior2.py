#Faça um Programa que leia três números e mostre o maior deles.

num1 = input("digite um numero.\n")
num2 = input("digite outro numero.\n")
num3 =input("digite o terceiro numero.\n")

num1 = float(num1)
num2 = float(num2)
num3 = float(num3)

def maior_numero(a,b,c):
    if a> b and a>c:
        print("o maior numero é ", a)
    elif b>a and b>c:
        print("o maior numero é ", b)
    else:
        print("o maior numero é ", c)


maior_numero(num1, num2, num3)
