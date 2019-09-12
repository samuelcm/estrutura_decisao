#Faça um Programa que leia três números e mostre o maior e o menor deles.
num1 = input("digite um numero.\n")
num2 = input("digite outro numero.\n")
num3 =input("digite o terceiro numero.\n")

try:
    num1 = float(num1)
except:
    print("digite um numero valido")

try:
    num2 = float(num2)
except:
    print("digite numero valido")

try:
    num3 = float(num3)
except:
    print("digite numero valido")

if num1> num2 and num1>num3:
    maior = num1
elif num2>num1 and num2>num3:
    maior = num2
else:
    maior = num3

if num1< num2 and num1<num3:
    menor = num1
elif num2<num1 and num2<num3:
    menor = num2
else:
    menor = num3

print("O maior numero é {} e o menor é {}.". format(maior, menor))
