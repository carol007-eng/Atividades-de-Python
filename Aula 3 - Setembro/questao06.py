notas = [7.5, 8.0, 4.5, 9.0, 6.0, 5.5, 10.0, 3.5, 8.5, 7.0]

media = sum(notas) / len(notas)
maior = max(notas)
menor = min(notas)

aprovados = sum(1 for n in notas if n >= 7)
recuperacao = sum(1 for n in notas if 5 <= n < 7)
reprovados = sum(1 for n in notas if n < 5)

print("--- Relatório ---")
print("Média da turma:", media)
print("Maior nota:", maior)
print("Menor nota:", menor)
print("Aprovados:", aprovados)
print("Recuperação:", recuperacao)
print("Reprovados:", reprovados)