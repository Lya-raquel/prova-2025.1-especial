def main():
    ganho = float(input('Total do ganho: '))
    colaboracao = float(input('Quanto colaborou?(Digite 0 para parar) '))
    imposto = (20/100) * ganho
    total_ganho = ganho - imposto

    colaboracoes = []

    while colaboracao != 0:
        colaboracoes.append(colaboracao)
        colaboracao = float(input('Quanto colaborou?(Digite 0 para parar) '))

    soma = sum(colaboracoes)

    maior_ganho = None
    menor_ganho = None

    print("\nDistribuição do prêmio (após imposto):")

    i = 0
    while i < len(colaboracoes):
        divisao = (colaboracoes[i] / soma) * total_ganho

        if maior_ganho is None or divisao > maior_ganho:
            maior_ganho = divisao

        if menor_ganho is None or divisao < menor_ganho:
            menor_ganho = divisao

        i += 1

    print(f"\nMaior ganho: R$ {maior_ganho:.2f}")
    print(f"Menor ganho: R$ {menor_ganho:.2f}")
        

main()
# inicio: 24/05/2025 hora: 18:00
# fim: 24/05/2025    hora: 19:00
