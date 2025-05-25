def main():
    print("Digite a quantidade de alunos e tipo (ex: 10 F). Digite 'fim' para encerrar.")

    total = 0
    frontend = 0
    mobile = 0
    backend = 0
    dados = 0
    nenhum = 0

    while True:
        entrada = input().strip()

        if entrada.lower() == 'fim':
            break

        partes = entrada.split()

        if len(partes) == 0:
            print("Entrada vazia, tente novamente.")
            continue

        if len(partes) == 1:
            
            try:
                n = int(partes[0])
                if n < 0:
                    print("Quantidade negativa não é válida.")
                    continue
                total += n
                nenhum += n
                continue
            except ValueError:
                print("Entrada inválida, tente novamente.")
                continue

        if len(partes) == 2:
            try:
                n = int(partes[0])
                if n < 0:
                    print("Quantidade negativa não é válida.")
                    continue
                tipo = partes[1].upper()
                total += n

                if tipo == 'F':
                    frontend += n
                elif tipo == 'M':
                    mobile += n
                elif tipo == 'B':
                    backend += n
                elif tipo == 'D':
                    dados += n
                else:
                    print("Tipo inválido. Contabilizado como 'Nenhuma Opção'.")
                    nenhum += n
            except ValueError:
                print("Quantidade inválida, digite um número inteiro.")
                continue
        else:
            print("Entrada inválida. Use: número e letra (ex: 8 M) ou apenas número para 'Nenhuma Opção'.")

    imprimir(total, backend, frontend, mobile, dados, nenhum)


def percentual(parte, total):
    if total == 0:
        return 0.0
    return (parte / total) * 100


def imprimir(total, backend, frontend, mobile, dados, nenhum):
    print(f"\nTotal: {total} alunos")
    print(f"Total de Backend: {backend}")
    print(f"Total de Frontend: {frontend}")
    print(f"Total de Mobile: {mobile}")
    print(f"Total de Dados: {dados}")
    print(f"Total de Nenhuma Opção: {nenhum}")
    print(f"Percentual de Backend: {percentual(backend, total):.2f} %")
    print(f"Percentual de Frontend: {percentual(frontend, total):.2f} %")
    print(f"Percentual de Mobile: {percentual(mobile, total):.2f} %")
    print(f"Percentual de Dados: {percentual(dados, total):.2f} %")
    print(f"Percentual de Nenhuma Opção: {percentual(nenhum, total):.2f} %")


main()
# inicio: 25/05/2025  hora: 14:20
# final: 25/05/2025   hora: 15:15
