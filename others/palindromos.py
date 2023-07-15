# PALINDROMOS: osso, radar, socorram-me subi no ônibus em marrocos, etc...

# Para definirmos a função isPalindromo, que verifica se uma palavra é um palindromo, devemos levar em consideração palavras com número par de letras, e palavras com números ímpares de letras.

palavra1 = "Osso"
palavra2 = "Guilherme"

def isPalindromo(palavra):
    palavra = palavra.lower() 

    inicio = 0
    fim = len(palavra)-1

    for i in range(len(palavra)//2):        
        if palavra[inicio] != palavra[fim]:
            return False
        inicio += 1
        fim -= 1
    
    return True

if(isPalindromo(palavra1) == True):
    print(palavra1, "-> True")
else: 
    print(palavra1, "-> False")

if(isPalindromo(palavra2) == True):
    print(palavra2, "-> True")
else: 
    print(palavra2, "-> False")