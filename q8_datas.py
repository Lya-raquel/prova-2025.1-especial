def main():
    while True:
        print('Primeira data:')
        dia1 = int(input('Dia: '))
        mes1 = int(input('Mês: '))
        ano1 = int(input('Ano: '))
        print('Segunda data:')
        dia2 = int(input('Dia: '))
        mes2 = int(input('Mês: '))
        ano2 = int(input('Ano: '))
        if dia1 == dia2 and mes1 == mes2 and ano1 == ano2:
            print('Você digitou datas iguais. Tente novamente!')
            continue
        else:
            break

    dias = total_dias(dia1, dia2)
    meses = total_meses(mes1, mes2)
    anos = total_anos(ano1, ano2, mes1, mes2, dia1, dia2)

    imprimir(dias, meses, anos)


def total_dias(dia1, dia2):
    return abs(dia1 - dia2)

    

def total_meses(mes1, mes2):
    return abs(mes1 - mes2)
    

def total_anos(ano1, ano2, mes1, mes2, dia1, dia2):
    anos = ano2 - ano1

    if mes2 < mes1 or (mes2 == mes1 and dia2 < dia1):
        anos -= 1

    return anos
    

def imprimir(dias, meses, anos):
    if dias == 0 and meses == 0:
        print(f'{anos} anos.')
    elif dias == 0 and anos == 0:
        print(f'{meses} meses.')
    elif anos == 0 and meses == 0:
        print(f'{dias} dias.')
    elif dias == 0:
        print(f'{anos} anos e {meses} meses.')
    elif anos == 0:
        print(f'{meses} meses e {dias} dias.')
    else:
        print(f'{anos} anos, {meses} meses e {dias} dias.')

     

main()
# inicio: 24/05/2025 hora: 13:20
# fim: 24/05/2025    hora: 14:40
