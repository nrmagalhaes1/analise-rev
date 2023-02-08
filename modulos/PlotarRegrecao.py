import matplotlib.pyplot as plt
from modulos.regrecao import *
from modulos.RecolherValorPlan import *

def plotResul(x, y, total):
    
    
    partZ_x = x[1:3]
    partZ_y = y[1:3]

    partX_x = x[3:7]
    partX_y = y[3:7]

    partY_x = x[7:15]
    partY_y = y[7:15]

    part13X_x = x[15:18]
    part13X_y = y[15:18]

    part23X_x = x[18:20]
    part23X_y = y[18:20]

    part25X_x = x[20:24]
    part25X_y = y[20:24]

    part35X_x = x[24:27]
    part35X_y = y[24:27]

    part34X_x = x[27:29]
    part34X_y = y[27:29]

    part13Z_x = x[29:32]
    part13Z_y = y[29:32]

    part23Z_x = x[32:34]
    part23Z_y = y[32:34]

    part25Z_x = x[34:38]
    part25Z_y = y[34:38]

    part35Z_x = x[38:41]
    part35Z_y = y[38:41]

    part34Z_x = x[41:43]
    part34Z_y = y[41:43]

    fig, ax = plt.subplots(figsize = (9, 6))

    ax.scatter(total[1], total[0], s = 60, marker = "D");
    
    ax.scatter(partZ_x, partZ_y, s=60, c='#000000', alpha=0.7, edgecolors="w");
    ax.scatter(partX_x, partX_y, s=60, c='#FF4500', alpha=0.7, edgecolors="w");
    ax.scatter(partY_x, partY_y, s=60, c='#B03060', alpha=0.7, edgecolors="w");

    ax.scatter(part13X_x, part13X_y, s=60, c='#708090', alpha=0.7, edgecolors="w");
    ax.scatter(part23X_x, part23X_y, s=60, c='#191970', alpha=0.7, edgecolors="w");
    ax.scatter(part25X_x, part25X_y, s=60, c='#6495ED', alpha=0.7, edgecolors="w");
    ax.scatter(part35X_x, part35X_y, s=60, c='#00BFFF', alpha=0.7, edgecolors="w");
    ax.scatter(part34X_x, part34X_y, s=60, c='#006400', alpha=0.7, edgecolors="w");

    ax.scatter(part13Z_x, part13Z_y, s=60, c='#20B2AA', alpha=0.7, edgecolors="w");
    ax.scatter(part23Z_x, part23Z_y, s=60, c='#BDB76B', alpha=0.7, edgecolors="w");
    ax.scatter(part25Z_x, part25Z_y, s=60, c='#FFD700', alpha=0.7, edgecolors="w");
    ax.scatter(part35Z_x, part35Z_y, s=60, c='#CD853F', alpha=0.7, edgecolors="w");
    ax.scatter(part34Z_x, part34Z_y, s=60, c='#B22222', alpha=0.7, edgecolors="w");
    
    R2_1 = linear(x,y)
    R2_2 = grau(x,y, 2,'red', 'Grau 2')
    R2_3 = grau(x,y, 3, 'blue', 'Grau 3')
    R2_4 = grau(x,y, 4, 'black', 'Grau 4')
    
    plt.title('Subvolumes', size = 20)
    plt.xlabel('Volume (mm²)')
    plt.ylabel('Phi (%)')
    ax.grid(True)
    ax.legend(['Total', 'PartZ', 'PartX', 'PartY',
               '1/3 X', '2/3 X', '2/5 X',
               '3/5 X', '3/4 X', '1/3 Z',
               '2/3 Z', '2/5 Z', '3/5 Z',
               '3/4 Z', R2_1, R2_2, R2_3, R2_4], bbox_to_anchor = (1.05, 1), loc='upper left')   
    plt.tight_layout()
    plt.show()
    

def plotResul2(x, y, a, b, inicial, final, total):
    
    partZ_x = x[1:3]
    partZ_y = y[1:3]

    partX_x = x[3:7]
    partX_y = y[3:7]

    partY_x = x[7:15]
    partY_y = y[7:15]

    part13X_x = x[15:18]
    part13X_y = y[15:18]

    part23X_x = x[18:20]
    part23X_y = y[18:20]

    part25X_x = x[20:24]
    part25X_y = y[20:24]

    part35X_x = x[24:27]
    part35X_y = y[24:27]

    part34X_x = x[27:29]
    part34X_y = y[27:29]

    part13Z_x = x[29:32]
    part13Z_y = y[29:32]

    part23Z_x = x[32:34]
    part23Z_y = y[32:34]

    part25Z_x = x[34:38]
    part25Z_y = y[34:38]

    part35Z_x = x[38:41]
    part35Z_y = y[38:41]

    part34Z_x = x[41:43]
    part34Z_y = y[41:43]

    fig, ax = plt.subplots(figsize = (9, 6))
    
    ax.scatter(total[1], total[0], s = 60, marker = "D");
    
    ax.scatter(partZ_x, partZ_y, s=60, c='#000000', alpha=0.7, edgecolors="w");
    ax.scatter(partX_x, partX_y, s=60, c='#FF4500', alpha=0.7, edgecolors="w");
    ax.scatter(partY_x, partY_y, s=60, c='#B03060', alpha=0.7, edgecolors="w");

    ax.scatter(part13X_x, part13X_y, s=60, c='#708090', alpha=0.7, edgecolors="w");
    ax.scatter(part23X_x, part23X_y, s=60, c='#191970', alpha=0.7, edgecolors="w");
    ax.scatter(part25X_x, part25X_y, s=60, c='#6495ED', alpha=0.7, edgecolors="w");
    ax.scatter(part35X_x, part35X_y, s=60, c='#00BFFF', alpha=0.7, edgecolors="w");
    ax.scatter(part34X_x, part34X_y, s=60, c='#006400', alpha=0.7, edgecolors="w");

    ax.scatter(part13Z_x, part13Z_y, s=60, c='#20B2AA', alpha=0.7, edgecolors="w");
    ax.scatter(part23Z_x, part23Z_y, s=60, c='#BDB76B', alpha=0.7, edgecolors="w");
    ax.scatter(part25Z_x, part25Z_y, s=60, c='#FFD700', alpha=0.7, edgecolors="w");
    ax.scatter(part35Z_x, part35Z_y, s=60, c='#CD853F', alpha=0.7, edgecolors="w");
    ax.scatter(part34Z_x, part34Z_y, s=60, c='#B22222', alpha=0.7, edgecolors="w");
    
    for i in np.arange(inicial, final, 0.1):
        plt.axhline(y = i, color = '#D3D3D3', linestyle = '-', alpha= 0.2)
    
    R2_1 = linear(a,b)
    R2_2 = grau(a,b, 2,'#FF4500', f'Grau 2')
    R2_4 = grau(a,b, 4, '#000000', f'Grau 4')
    
    plt.title('Subvolumes', size = 20)
    plt.xlabel('Volume (mm²)')
    plt.ylabel('Phi (%)')
    ax.grid(True)
    ax.legend(['PartZ', 'PartX', 'PartY',
               '1/3 X', '2/3 X', '2/5 X',
               '3/5 X', '3/4 X', '1/3 Z',
               '2/3 Z', '2/5 Z', '3/5 Z',
               '3/4 Z', R2_1, R2_2, R2_4], bbox_to_anchor = (1.05, 1), loc='upper left')   
    plt.tight_layout()
    plt.show() 
    