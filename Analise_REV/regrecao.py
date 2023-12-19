# Módulo para ajuste de polinômios de diferentes graus aos dados e cálculo do R^2

import numpy as np  # Biblioteca para operações numéricas eficientes
import matplotlib.pyplot as plt  # Biblioteca para plotagem
from sklearn.metrics import r2_score  # Métrica para avaliação do modelo

def grau(x, y, g, c='red', l='grau'):
    """
    Ajusta polinômios aos dados e plota o resultado.

    Args:
    x (array): Valores do eixo x.
    y (array): Valores do eixo y.
    g (int): Grau do polinômio a ser ajustado.
    c (str): Cor da linha no gráfico.
    l (str): Rótulo para a legenda do gráfico.

    Returns:
    str: Rótulo do grau e o valor do R^2.
    """

    x = np.asarray(x)
    y = np.asarray(y)
        
    if g == 4:
        # Ajuste de um polinômio logarítmico
        log_y = np.log(y)
        coefficients = np.polyfit(x, log_y, 1)
        ys = np.exp(coefficients[1]) * np.exp(coefficients[0]*x)
        plt.plot(x, ys, color=c, linestyle=':')
        return l + f' R_2: {round(r2_score(y, ys, force_finite=False), 4)}'
        
    else:
        # Ajuste de um polinômio de grau g
        z = np.polyfit(x, y, g)
        p = np.poly1d(z)

        xs = np.linspace(x[0], x[-1], 1000)
        plt.plot(xs, p(xs), color=c, linestyle=':')
        
        return l + f' R_2: {round(r2_score(y, p(x), force_finite=False), 4)}'
