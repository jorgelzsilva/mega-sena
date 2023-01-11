from random import sample
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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
senas = [sorteia_numeros(60, 6) for x in range(10)]

#print('\n'.join(str(row) for row in senas))

#juntando os números em uma única lista
senas = np.array(senas)
senas = np.sort(senas.flatten())

#Mostrando a incidência de números

g = sns.countplot(x=senas)
g.set_title('Incidência de números')
g.set(xlabel='Números sorteados',
ylabel='Quantidade de sorteios')

plt.show()