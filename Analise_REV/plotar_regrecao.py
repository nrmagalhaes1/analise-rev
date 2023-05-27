import matplotlib.pyplot as plt
from regrecao import *
from Recolher_valor_plan import *

    
def plotResul(x, y, total, novo_x=0, novo_y=0,
            intervalo_inicial=0, intervalo_final=0,
            replot='n'):
    
    vetorx = []
    vetory = []

    supx= [3.010775628194522, 5.351820072580289, 6.25222178195943, 7.422744004152315, 10.439089730572437, 24.980577337045574]
    supy= [10.576523782876327, 9.555388919977615, 9.385199776161162, 9.151189703413541, 8.85335870173475, 8.257696698377167]

    midx= [0.30957050005709785, 0.3996106709950116, 1.0298918675604103, 1.5701328931878953, 1.66017306412581, 2.9207354572566073, 3.1008157991324357, 3.1908559700703503, 3.145835884601393, 3.280896141008264, 5.261779901642375, 6.25222178195943, 25.02559742251453]
    midy= [8.283630094085126, 7.5272799818001594, 7.598187804826875, 7.5272799818001594, 7.8581831559248325, 8.236358212067316, 8.047270683996073, 7.8581831559248325, 7.57455186381797, 7.385464335746729, 8.425445740138557, 7.952726919960453, 8.141814448031694]

    infx= [3.111554313492997, 6.134785499611827, 7.387266991003915, 10.540065227956411, 12.569949024350482, 25.0515749213268]
    infy= [6.087785114717402, 6.640899832120872, 7.38547733631785, 7.470571908226075, 7.747129266927811, 8.215149412423054]

    
    x.append(total[1])
    y.append(total[0])

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

    part14X_x = x[29:33]
    part14X_y = y[29:33]

    part15X_x = x[33:38]
    part15X_y = y[33:38]    

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

    ax.scatter(part14X_x, part14X_y, s=60, c='#20B2AA', alpha=0.7, edgecolors="w");
    ax.scatter(part15X_x, part15X_y, s=60, c='#BDB76B', alpha=0.7, edgecolors="w");

    
    for i in np.arange(intervalo_inicial, intervalo_final, 0.1):
        plt.axhline(y = i, color = '#D3D3D3', linestyle = '-', alpha= 0.2)
    
    if replot == 'n':
        sup = grau(supx,supy, 2,'red', 'Grau 2')
        mid = grau(midx,midy, 2,'red', 'Grau 2')
        inf = grau(infx,infy, 2,'red', 'Grau 2') 
    else:
        R2_2 = grau(novo_x, novo_y, 2,'red', f'Grau 2')

    
    plt.title('Subvolumes', size = 20)
    plt.xlabel('Volume (cm_3)')
    plt.ylabel('Phi (%)')
    ax.grid(True)
    ax.legend(['Total', 'PartZ', 'PartX', 'PartY',
            '1/3', '2/3', '2/5',
            '3/5', '3/4', '1/4',
            '1/5',sup, mid, inf],
              bbox_to_anchor = (1.05, 1), loc='upper left')   
    plt.tight_layout()

    while True:
        try:
            # Aguarda um clique do mouse
            click = plt.ginput(1, timeout=0)
            # Se um clique foi detectado, exibe as coordenadas
            if click:
                vetorx.append(click[0][0])
                vetory.append(click[0][1])
                
                print('Voce clicou em x =', vetorx, 'e y =', vetory)
        except KeyboardInterrupt:
            # Se o usuário pressionar Ctrl+C, encerra o loop
            break

    # Fecha o gráfico ao final
    plt.close(fig)
    plt.show()


    