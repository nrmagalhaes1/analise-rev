
def crescente(x,y):
    xy = zip(x,y)
    sorted_xy = sorted(xy, key = lambda t: t[0])
    
    new_x = list(map(lambda t: t[0], sorted_xy))
    new_y = list(map(lambda t: t[1], sorted_xy))
    
    return new_x, new_y


def limpar(x, y, inv_min, inv_max):
    
    new_x = []
    new_y = []
    
    for i, j in zip(x, y):
        if j >= inv_min and j <= inv_max:
            new_x.append(i)
            new_y.append(j)
        
    return new_x, new_y