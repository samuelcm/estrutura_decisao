#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos
#são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e
#3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado
#(é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos.
#O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações,
#dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

hr = int(input("Quantas horas de trabalho neste mês?"))
pgto_hr = float(input("Quanto é sua hora de trabalho?"))

sal_bruto = hr * pgto_hr

def IR (a):
    if a <=900:
        return 0
    elif a >900 and a <=1500:
        return 0.05
    elif a>1500 and a<= 2500:
        return 0.1
    else:
        return 0.2

pgto_IR = IR (sal_bruto)
INSS = sal_bruto*0.10
Sindicato= sal_bruto*0.03
FGTS = sal_bruto*0.11
descontos = pgto_IR+ INSS+Sindicato
sal_liquido = sal_bruto-descontos


print("Salário bruto: (", pgto_hr,"*", hr, "): R$",sal_bruto)
print("(-) IR ( {aliquota} %): R$ {pgto}". format(aliquota=pgto_IR*100, pgto = pgto_IR*sal_bruto))
print("(-) INSS (10%):R$", INSS)
print ("FGTS (11%):R$", FGTS)
print ("Total de descontos: R$",descontos)
print ("Salário líquido: R$", sal_liquido)
