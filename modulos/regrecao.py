import numpy as np
import matplotlib.pyplot as plt
from   sklearn.linear_model import LinearRegression
from   sklearn.preprocessing import PolynomialFeatures
from   sklearn.metrics import r2_score



def linear(x, y):
    
    x = np.asarray(x)
    y = np.asarray(y)
    X = x.reshape(-1,1)
    Y = y.reshape(-1,1)   
    
    reg = LinearRegression()
    reg.fit(X, Y)
    
    f_previsaoes = reg.predict(X)


    plt.plot(
        x,
        f_previsaoes,
        c='g',
        linewidth=1,
        linestyle=':')
    return f'Linear R²: {round(r2_score(Y, f_previsaoes, force_finite=False),4)}'


def grau(x, y, g, c= 'red', l= 'grau'):

    x = np.asarray(x)
    y = np.asarray(y)
        
    if g == 4:
        ...
        log_x = np.log(x)
        log_y = np.log(y)
        coefficients = np.polyfit(x, log_y, 1)
        ys = np.exp(coefficients[1]) * np.exp(coefficients[0]*x)
        plt.plot(x, ys, color= c, linestyle=':')
        
    else:
        z = np.polyfit(x, y, g)
        p = np.poly1d(z)

        xs = np.linspace(x[0], x[len(x)-1], 1000)
        plt.plot(xs,p(xs), color= c, linestyle=':')

    caracteristicas_2 = PolynomialFeatures(degree=g, include_bias=False)
    x = x.reshape(-1,1)
    x_polinomio_2 = caracteristicas_2.fit_transform(x)
    
    modelo2 = LinearRegression()
    modelo2.fit(x_polinomio_2, y)
    y_polinomio_2 = modelo2.predict(x_polinomio_2)
    return l+f' R²: {round(r2_score(y, y_polinomio_2, force_finite=False), 4)}'
