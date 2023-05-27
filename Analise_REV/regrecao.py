import numpy as np
import matplotlib.pyplot as plt
from   sklearn.metrics import r2_score


def grau(x, y, g, c= 'red', l= 'grau'):

    x = np.asarray(x)
    y = np.asarray(y)
        
    if g == 4:
        
        log_y = np.log(y)
        coefficients = np.polyfit(x, log_y, 1)
        ys = np.exp(coefficients[1]) * np.exp(coefficients[0]*x)
        plt.plot(x, ys, color= c, linestyle=':')
        return l+f' R_2: {round(r2_score(y, ys, force_finite=False), 4)}'
        
    else:
        
        z = np.polyfit(x, y, g)
        p = np.poly1d(z)

        xs = np.linspace(x[0], x[len(x)-1], 1000)
        plt.plot(xs,p(xs), color= c, linestyle=':')
        
        return l+f' R_2: {round(r2_score(y, p(x), force_finite=False), 4)}'
