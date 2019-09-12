#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
#Imprima a mensagem "Bom Dia!",  "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.


print("Em que turno você estuda?")
turno = input("Digite:\n 'M' se voce estuda de manhã.\n 'V' se estuda de tarde. \n 'N' se estuda a noite\n")

if turno == 'M':
    print("Bom dia!")
elif turno == 'V':
    print('Boa tarde')
elif:
    print('Boa noite')
else:
    print('Valor inválido')
