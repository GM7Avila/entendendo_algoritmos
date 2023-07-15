# supondo que a > b
def mdc_iterativo(a, b):
    if a < b:
        # troca de posição
        a, b = b, a
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b

print(mdc_iterativo(10,15))

def mdc_recursivo(a, b):
    if a < b:
        return mdc_recursivo(b, a)
    if b == 0: 
        return a 
    r = a % b
    return mdc_recursivo(b,r)

print(mdc_recursivo(100,150))
