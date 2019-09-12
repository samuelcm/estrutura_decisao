#Faça um Programa que peça um número correspondente a um determinado ano e em
#seguida informe se este ano é ou não bissexto.

#São bissextos todos os anos múltiplos de 400, p.ex: 1600, 2000, 2400, 2800...
#São bissextos todos os múltiplos de 4, exceto se for múltiplo de 100 mas não de 400,
#p.ex: 1996, 2000, 2004, 2008, 2012, 2016…
#Não são bissextos todos os demais anos.

ano = int(input("Informe o ano\n"))

if ano % 400 == 0:
    print ("O ano é bissexto")
elif ano % 4 == 0:
    if ano%100 ==0:
        if ano%400 == 0:
             print("O ano é bissexto")
        else:
            print("O ano nao é bissexto")
            
    print ("O ano é bissexto")
