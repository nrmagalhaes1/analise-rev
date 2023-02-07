
# retorna um vetor com as medidas em X, Y e Z
def sub13(volumeTotal):

    x = volumeTotal[0]
    y = volumeTotal[1]
    particao = volumeTotal[2]/3
    
    interv1_z = [0, round(particao, 2)]
    interv2_z = [round(particao, 2), round(particao*2, 2)]
    interv3_z = [round(particao*2, 2), round(particao*3, 2)]
    
    sub13 = [[x, y, interv1_z],
            [x, y, interv2_z],
            [x, y, interv3_z]]
    
    return sub13


# ------------------------------------------------------------------------------------------------------------------------
# retorna um vetor com as medidas em X, Y e Z
def sub23(volumeTotal):

    x = volumeTotal[0]
    y = volumeTotal[1]
    particao = volumeTotal[2]/3
    
    interv1_z = [0, round(particao*2, 2)]
    interv2_z = [round(particao, 2), round(particao*3, 2)]
    
    sub23 = [[x, y, interv1_z],
            [x, y, interv2_z]]
    
    return sub23


# ------------------------------------------------------------------------------------------------------------------------
# retorna um vetor com as medidas em X, Y e Z
def sub25(volumeTotal):

    x = volumeTotal[0]
    y = volumeTotal[1]
    particao = volumeTotal[2]/5
    
    interv1_z = [0, round(particao*2, 2)]
    interv2_z = [round(particao, 2), round(particao*3, 2)]
    interv3_z = [round(particao*2, 2), round(particao*4, 2)]
    interv4_z = [round(particao*3, 2), round(particao*5, 2)]
    
    sub25 = [[x, y, interv1_z],
               [x, y, interv2_z],
               [x, y, interv3_z],
               [x, y, interv4_z]]
    
    return sub25


# ------------------------------------------------------------------------------------------------------------------------
# retorna um vetor com as medidas em X, Y e Z
def sub35(volumeTotal):

    x = volumeTotal[0]
    y = volumeTotal[1]
    particao = volumeTotal[2]/5
    
    interv1_z = [0, round(particao*3, 2)]
    interv2_z = [round(particao, 2), round(particao*4, 2)]
    interv3_z = [round(particao*2, 2), round(particao*5, 2)]
    
    sub35 = [[x, y, interv1_z],
               [x, y, interv2_z],
               [x, y, interv3_z]]
    
    return sub35


# ------------------------------------------------------------------------------------------------------------------------
# retorna um vetor com as medidas em X, Y e Z
def sub34(volumeTotal):

    x = volumeTotal[0]
    y = volumeTotal[1]
    particao = volumeTotal[2]/4
    
    interv1_z = [0, round(particao*3, 2)]
    interv2_z = [round(particao, 2), round(particao*4, 2)]
    
    sub34 = [[x, y, interv1_z],
               [x, y, interv2_z]]
    
    return sub34


# ------------------------------------------------------------------------------------------------------------------------
def executar(volume):
    sub_13 = sub13(volume)
    sub_23 = sub23(volume)
    sub_25 = sub25(volume)
    sub_35 = sub35(volume)
    sub_34 = sub34(volume)
    metodo2 = sub_13 + sub_23 + sub_25 + sub_35 + sub_34
    return metodo2