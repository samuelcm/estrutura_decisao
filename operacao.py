#Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
#O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
#par ou ímpar;
#positivo ou negativo;
#inteiro ou decimal.

num1=float(input("Digite o primeiro numero:\n"))
num2=float(input("Digite o segundo numero:\n"))

operacao = input("Qual operacao deseja usar?")

if operacao == 'soma':
    resultado = num1 + num2
elif operacao == 'diminuicao':
    resultado = num1-num2
elif operacao == 'multiplicacao':
    resultado = num1*num2
elif operacao == 'divisao':
    resultado = num1/num2

def par (a):
    if resultado %2==0:
        return 'Par'
    else:
        return 'Impar'

res_par = par(resultado)

def pos_neg (a):
    if resultado > 0:
        return 'positivo'
    elif resultado == 0:
        return 'zero'
    else:
        return 'negativo'

res_pos = pos_neg (resultado)

def dec_int (a):
    if resultado == round(resultado):
        return 'inteiro'
    else:
        return 'decimal'

res_dec = dec_int(resultado)

print(f"O número resultado da {operacao} é {res_par}, {res_pos} e {res_dec}")
