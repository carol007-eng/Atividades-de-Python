# Script 1 - Classificador de desempenho acadêmico

# Entrada de dados
nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
faltas = int(input("Digite a quantidade de faltas: "))

# Cálculo da média
media = (nota1 + nota2 + nota3) / 3

# Verificação da situação
if faltas > 10:
    situacao = "Reprovado por falta"
elif media >= 7:
    situacao = "Aprovado"
elif 5 <= media < 7:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

# Saída
print("\n--- Resultado ---")
print("Aluno:", nome)
print("Média:", round(media, 2))
print("Situação:", situacao)