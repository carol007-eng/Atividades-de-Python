# Programa para calcular desconto de um produto

def calcular_desconto(preco, percentual):
    valor_desconto = preco * (percentual / 100)
    preco_final = preco - valor_desconto
    return preco_final


produto = input("Digite o nome do produto: ")

preco = float(input("Digite o preço do produto: R$ "))

percentual = float(input("Digite o percentual de desconto: "))

preco_final = calcular_desconto(preco, percentual)

valor_desconto = preco - preco_final

print("\n===== RESULTADO =====")
print("Produto:", produto)
print("Preço original: R$", round(preco, 2))
print("Valor do desconto: R$", round(valor_desconto, 2))
print("Preço final: R$", round(preco_final, 2))