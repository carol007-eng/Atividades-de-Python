# Programa para analisar uma sequência de números

# Pergunta quantos números serão digitados
quantidade = int(input("Quantos números você deseja informar? "))

# Cria uma lista vazia para guardar os números
numeros = []

# Repete o processo de entrada de acordo com a quantidade escolhida
for i in range(quantidade):
    
    # Pede um número ao usuário
    numero = int(input("Digite um número: "))
    
    # Adiciona o número à lista
    numeros.append(numero)

# Calcula a soma dos números
soma = sum(numeros)

# Calcula a média
media = soma / quantidade

# Conta quantos números são pares
pares = 0

# Percorre todos os números da lista
for numero in numeros:
    
    # Verifica se o número é divisível por 2
    if numero % 2 == 0:
        
        # Aumenta o contador de números pares
        pares = pares + 1

# Encontra o maior número
maior = max(numeros)

# Encontra o menor número
menor = min(numeros)

# Mostra os resultados
print("\n===== RESULTADO =====")
print("Números digitados:", numeros)
print("Soma:", soma)
print("Média:", round(media, 2))
print("Quantidade de números pares:", pares)
print("Maior valor:", maior)
print("Menor valor:", menor)