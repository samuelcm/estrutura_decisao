#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao
#longo de um semestre, e calcule a sua média. A atribuição de conceitos
#obedece à tabela abaixo:
#O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e
#a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

nota1 = input("qual sua primeira nota?\n")
nota2= input("qual a segunda nota?\n")
try:
    nota1 = float(nota1)
    nota2 = float(nota2)
except:
    print("Dados invalidos")

media = (nota1+ nota2)/2


if media >= 6:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

print ("Nota 1: {}. Nota2: {}. Media: {}".format(nota1, nota2, media))

if media >= 9:
    print("Conceito A")
elif media >=7.5 and media<9:
    print ("Conceito B")
elif media >=6.0 and media <7.5:
    print("Conceito C")
elif media >=4 and media <6:
    print("Conceito D")
else:
    print("Conceito E")


print(situacao)
