def main():
    n = int(input('Inicial: '))
    m = int(input('Final: '))

    primos = []

    i = n
    while i <= m:
        if eh_primo(i):
            primos.append(str(i))
        i += 1

    print(f'Números primos entre {n} e {m}: ')
    print(','.join(primos) + '.')


def eh_primo(i):
    if i < 2:
        return False

    divisor = 2
    while divisor * divisor <= i:
        if i % divisor == 0:
            return False
        divisor += 1

    return True

main()