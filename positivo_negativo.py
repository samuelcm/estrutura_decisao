#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

numero = input("digite um valor")
if "." in numero:
    numero = float(numero)
else:
    numero = int(numero)

if numero > 0:
    print("o numero é positivo")
elif numero<0:
    print("o numero é negativo")
else:
    print ("zero não é positivo nem negativo")
