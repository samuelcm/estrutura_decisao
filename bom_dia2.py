#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
#Imprima a mensagem "Bom Dia!",  "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.


print("Em que turno você estuda?")
turno = input("Digite:\n 'M' se voce estuda de manhã.\n 'V' se estuda de tarde. \n 'N' se estuda a noite\n")

def saudacao (a):
    if a == 'M':
        return 'Bom dia'
    elif a == 'V':
        return 'Boa tarde'
    elif a == 'N':
        return'Boa noite'
    else:
        return 'Valor inválido'

saudacao2 = saudacao(turno)

print ("{}". format(saudacao2))
