"""
Este módulo contém funções para processamento de dados bidimensionais.

A função 'crescente' recebe duas listas x e y, e ordena os elementos de x em ordem crescente, mantendo a correspondência com os elementos de y.

A função 'limpar' recebe duas listas x e y, bem como limites inferior e superior (inv_min e inv_max, respectivamente), e retorna sublistas de x e y contendo apenas os valores de y que estão dentro do intervalo [inv_min, inv_max].
"""

def crescente(x, y):
    # Combina as listas x e y em tuplas e as ordena com base nos valores de x
    xy = zip(x, y)
    sorted_xy = sorted(xy, key=lambda t: t[0])
    
    # Separa os valores ordenados de x e y em listas separadas
    new_x = list(map(lambda t: t[0], sorted_xy))
    new_y = list(map(lambda t: t[1], sorted_xy))
    
    return new_x, new_y


def limpar(x, y, inv_min, inv_max):
    # Inicializa novas listas para armazenar os valores dentro do intervalo especificado
    new_x = []
    new_y = []
    
    # Itera sobre os valores de x e y simultaneamente
    for i, j in zip(x, y):
        # Verifica se o valor de y está dentro do intervalo especificado
        if inv_min <= j <= inv_max:
            # Adiciona os valores correspondentes de x e y às novas listas
            new_x.append(i)
            new_y.append(j)
        
    return new_x, new_y
