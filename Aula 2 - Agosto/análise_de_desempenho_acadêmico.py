# Programa para analisar o desempenho de um aluno

# Pede o nome do aluno
nome = input("Digite o nome do aluno: ")

# Pede as três notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

# Calcula a média das três notas
media = (nota1 + nota2 + nota3) / 3

# Verifica a situação do aluno
if media >= 7:
    situacao = "Aprovado"
elif media >= 5:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

# Mostra os resultados
print("\n===== RESULTADO =====")
print("Aluno:", nome)
print("Média:", round(media, 2))
print("Situação:", situacao)