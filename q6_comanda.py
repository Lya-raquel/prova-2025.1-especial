def main():
    inserir_produtos()
    total = 0
    contador = 0
    total_cervejas = 0

    while True:
        produto = input('Adicionar produto: ').strip().upper()
        if produto == '0':
            break

        qtd, tipo = num_letra(produto)

        if tipo == 'C':
            total += qtd * 9
            total_cervejas += qtd 
        elif tipo == 'T':
            total += qtd * 39
        elif tipo == 'A':
            total += qtd * 5
        else:
            print("Entrada inválida.")
            continue

        contador += 1

    if total > 0:
        try:
            num_pessoas = int(input('Quantas pessoas vão pagar? '))
            if num_pessoas <= 0:
                print('Número inválido, assumindo 1 pessoa.')
                num_pessoas = 1
        except ValueError:
            print('Entrada inválida, assumindo 1 pessoa.')
            num_pessoas = 1

        imprimir_conta(total, num_pessoas, total_cervejas)
    else:
        print("Nenhum produto foi adicionado.")

    if contador > 0:
        imprimir_conta(total, contador, total_cervejas)
    else:
        print("Nenhum produto foi adicionado.")


def imprimir_conta(total, num_pessoas, total_cervejas):
    if total_cervejas > 10 or total > 200:
        taxa = 0
    else:
        taxa = total * 0.10

    total_com_taxa = total + taxa

    if num_pessoas > 0:
        valor_por_pessoa = total_com_taxa / num_pessoas
    else:
        valor_por_pessoa = 0

    tela = f'''
    Valor da conta: R${total:.2f}
    Valor por pessoa: R${valor_por_pessoa:.2f}
    Valor da taxa de serviço: R${taxa:.2f}
    Valor total com taxa de serviço: R${total_com_taxa:.2f}
'''
    print(tela)


def num_letra(produto):
    if len(produto) == 2 and produto[0].isdigit():
        qtd = int(produto[0])
        tipo = produto[1].upper()
        return qtd, tipo
    else:
        return 0, ''
   

def inserir_produtos():
    tela = '''
    RS Bar
    Produtos:         Código:      Preço:
    - Cerveja.          C          R$ 9,00
    - Tira-gosto.       T          R$ 39,00
    - Água.             A          R$ 5,00
'''
    print(tela)

main()
# inicio: 24/05/2025 hora: 12:00
# fim: 24/05/2025    hora: 13:20
