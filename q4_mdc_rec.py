def mdc(a, b):
    if b == 0:
        return a
    else:
        return mdc(b, a % b)
    
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
    
resultado = mdc(a, b)
    
print(f'MDC de {a} e {b}: {resultado}')

# inicio: 25/05/2025 hora: 12:46
# fim: 25/05/2025    hora: 13:14
