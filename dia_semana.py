#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
#se digitar outro valor deve aparecer valor inválido.

semana = {1: "Domingo", 2:"Segunda", 3:"Terça", 4:"Quarta", 5:"Quinta", 6:"Sexta", 7:"Sábado"}
dia= int(input("Escolha um dia da semana (1-Domingo, 2 - Segunda, 3 - Terça, 4-Quarta,5-Quinta, 6-Sexta, 7-Sabado)"))


if dia in semana.keys():
    print (semana[dia])
else:
    print("Valor inválido")
