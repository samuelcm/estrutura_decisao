#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a
#participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve
#ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário,
#ele será classificado como "Inocente".


pontos = []

pergunta1 = input("Telefonou para a vítima?")
pergunta2 = input("Esteve no local do crime?")
pergunta3= input("Mora perto da vítima?")
pergunta4= input("Devia para a vítima?")
pergunta5 = input("Já trabalhou com a vítima?")

if pergunta1== 'sim':
    pontos.append(pergunta1)
if pergunta2 == 'sim':
    pontos.append(pergunta2)
if pergunta3 == 'sim':
    pontos.append(pergunta3)
if pergunta4 == 'sim':
    pontos.append(pergunta4)
if pergunta5 == 'sim':
    pontos.append(pergunta5)

pontuacao = len(pontos)

if pontuacao<=2:
    print ("Suspeita")
elif pontuacao >2 and pontuacao<=4:
    print ("Cumplice")
elif pontuacao == 5:
    print ("Assassino")
