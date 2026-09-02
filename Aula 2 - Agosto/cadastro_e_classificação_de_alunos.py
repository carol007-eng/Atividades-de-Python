# Programa para cadastrar e classificar alunos

# Cria uma lista vazia para armazenar os alunos
alunos = []

# Pergunta quantos alunos serão cadastrados
quantidade = int(input("Quantos alunos deseja cadastrar? "))

# Repete o cadastro de acordo com a quantidade informada
for i in range(quantidade):

    # Mostra qual aluno está sendo cadastrado
    print("\nCadastro do aluno", i + 1)

    # Pede o nome do aluno
    nome = input("Digite o nome: ")

    # Pede a média do aluno
    media = float(input("Digite a média: "))

    # Verifica a situação do aluno
    if media >= 7:
        situacao = "Aprovado"
    elif media >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    # Cria um dicionário com os dados do aluno
    aluno = {
        "nome": nome,
        "media": media,
        "situacao": situacao
    }

    # Adiciona o aluno à lista
    alunos.append(aluno)


# Cria os contadores
aprovados = 0
recuperacao = 0
reprovados = 0

# Percorre todos os alunos cadastrados
for aluno in alunos:

    # Verifica a situação do aluno
    if aluno["situacao"] == "Aprovado":
        aprovados = aprovados + 1

    elif aluno["situacao"] == "Recuperação":
        recuperacao = recuperacao + 1

    else:
        reprovados = reprovados + 1


# Mostra os resultados
print("\n===== RESULTADO =====")

# Percorre novamente a lista de alunos
for aluno in alunos:

    # Mostra os dados de cada aluno
    print(
        aluno["nome"],
        "- Média:",
        aluno["media"],
        "-",
        aluno["situacao"]
    )

# Mostra a quantidade de alunos em cada situação
print("\nTotal de alunos:", quantidade)
print("Aprovados:", aprovados)
print("Recuperação:", recuperacao)
print("Reprovados:", reprovados)