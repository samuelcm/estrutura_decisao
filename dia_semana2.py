#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.),
#se digitar outro valor deve aparecer valor inválido.

semana = {1: "Domingo", 2:"Segunda", 3:"Terça", 4:"Quarta", 5:"Quinta", 6:"Sexta", 7:"Sábado"}
dia= int(input("Escolha um dia da semana (1-Domingo, 2 - Segunda, 3 - Terça, 4-Quarta,5-Quinta, 6-Sexta, 7-Sabado)"))


for dias in semana:
    if dias == dia:# in semana.keys():
        print(semana[dias])
        break
    else:
        print ("Valor inválido")


#0800 7236626
#136192984179285
