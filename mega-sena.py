from random import sample

def sorteia_numeros(limite, quantidade):
    """sorteia uma quantidade especificada de números únicos 
    de 1 até o limite estipulado.

    Args:
        limite (int): o número limite a ser sorteado
        quantidade (int): quantidade de números a ser sorteados

    Returns:
        list: Retorna uma lista com os números sorteados
    """    
    numeros = sample(range(1, limite+1), quantidade)
    numeros.sort()
    return numeros

# list comprehension para quantidade desejada de sorteios
senas = [sorteia_numeros(60, 6) for x in range(1)]

print('\n'.join(str(row) for row in senas))