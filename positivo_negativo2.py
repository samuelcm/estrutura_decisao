#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

numero = input("digite um valor")

try:
    numero = float(numero)
except:
    print("digite um numero valido")

if numero == 0:
    sinal = "zero"
elif numero>0:
    sinal = "positivo"
else:
    sinal = "negativo"

print ("o numero escolhido é {}.". format(sinal))
