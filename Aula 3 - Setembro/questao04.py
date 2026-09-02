produtos = []

for i in range(5):
    nome = input(f"Nome do produto {i+1}: ")
    preco = float(input("Preço: "))
    qtd = int(input("Quantidade: "))
    produtos.append({"nome": nome, "preco": preco, "qtd": qtd})

mais_caro = max(produtos, key=lambda p: p["preco"])
mais_barato = min(produtos, key=lambda p: p["preco"])
total_estoque = sum(p["preco"] * p["qtd"] for p in produtos)

print("Produto mais caro:", mais_caro["nome"])
print("Produto mais barato:", mais_barato["nome"])
for p in produtos:
    print(f"{p['nome']} - Valor estoque: {p['preco']*p['qtd']}")
print("Valor total do estoque:", total_estoque)