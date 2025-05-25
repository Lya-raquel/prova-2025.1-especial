def main():
    soma = 0
    valores_validos = []
    anterior = None

    while True:
        casos = input("Digite um valor inteiro ou 'fim' para encerrar: ")

        if casos.lower() == 'fim':
            break

        try:
            numero = int(casos)

            if numero < 0:
                print('Valor não computado.')
                continue

            soma += numero  
            valores_validos.append(numero)

            if anterior == None:
                print('Primeiro valor recebido.')
            else:
                if anterior == 0:
                    print('Em Alta (dia anterior foi 0)')
                else:
                    variacao = ((numero - anterior) / anterior) * 100

                    if variacao > 15:
                        print("Em Alta")
                    elif variacao < - 15:
                        print("Em Queda")
                    else:
                        print("Em Estabilidade")

            anterior = numero

        except ValueError:
            print("Valor não computado.")

    print('\n--- Conceito do dia ---')
    if valores_validos:
        media = soma / len(valores_validos)
        print(f'Total de casos: {soma}')
        print(f"Média de casos por dia: {media:.2f}")
    else:
        print("Nenhum valor válido foi computado.")


main()
# inicio: 25/05/2025 hora: 12:00
# fim: 25/05/2025    hora: 12:45
