#Faça um programa para a leitura de duas notas parciais de um aluno.
#O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota1 = input("digite a primeira nota")
nota2 = input("digite a segunda nota")

nota1 = float(nota1)
nota2 = float(nota2)

if nota1>10 or nota1 <0:
    print("digite uma nota entre zero e 10")
else:
    if (nota1 + nota2)/2 >= 7 and (nota1 + nota2)/2 <10 :
        print ('aprovado')
    elif (nota1 + nota2)/2 == 10:
        print("aprovado com distinção")
    else:
        print("reprovado")
