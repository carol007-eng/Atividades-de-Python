consumos = []
for i in range(6):
    valor = float(input(f"Digite o consumo do mês {i+1}: "))
    consumos.append(valor)

media = sum(consumos) / len(consumos)
maior = max(consumos)
menor = min(consumos)
acima_media = sum(1 for c in consumos if c > media)
posicao_maior = consumos.index(maior) + 1

print("Consumo médio:", media)
print("Maior consumo:", maior, "no mês", posicao_maior)
print("Menor consumo:", menor)
print("Meses acima da média:", acima_media)