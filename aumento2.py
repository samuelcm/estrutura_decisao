# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores
# e lhe contrataram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
# baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salario = float(input("Parabens. Voce recebeu um aumento. Digite seu salário atual:\n"))

if salario <= 280:
    p_aumento = 0.2
elif salario > 280 and salario <700:
    p_aumento = 0.15
elif salario >= 700 and salario < 1500:
    p_aumento = 0.10
else:
    p_aumento = 0.05


aumento_real = salario*p_aumento
novo_salario = salario + (salario*p_aumento)

print ("-"*35)
print("Seu salário atual é de R$ {}.".format(salario))
print ("-"*35)
print("O percentual de reajuste do seu salário é de {percentual}%".format(percentual=p_aumento*100))
print ("-"*35)
print("Você terá um aumento de R$ {}".format(aumento_real))
print ("-"*35)
print("Seu novo salário será de R$ {}".format(novo_salario))
print ("-"*35)
