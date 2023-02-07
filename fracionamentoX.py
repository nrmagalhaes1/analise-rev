
# retorna um vetor com as medidas em X, Y e Z
def sub13(volumeTotal):

    particao = volumeTotal[0]/3
    y = volumeTotal[1]
    z = volumeTotal[2]
    
    interv1_x = [0, round(particao, 2)]
    interv2_x = [round(particao, 2), round(particao*2, 2)]
    interv3_x = [round(particao*2, 2), round(particao*3, 2)]
    
    sub13 = [[interv1_x, y, z],
            [interv2_x, y, z],
            [interv3_x, y, z]]
    
    return sub13


# ------------------------------------------------------------------------------------------------------------------------
# retorna um vetor com as medidas em X, Y e Z
def sub23(volumeTotal):

    particao = volumeTotal[0]/3
    y = volumeTotal[1]
    z = volumeTotal[2]
    
    interv1_x = [0, round(particao*2, 2)]
    interv2_x = [round(particao, 2), round(particao*3, 2)]
    
    sub23 = [[interv1_x, y, z],
            [interv2_x, y, z]]
    
    return sub23


# ------------------------------------------------------------------------------------------------------------------------
# retorna um vetor com as medidas em X, Y e Z
def sub25(volumeTotal):

    particao = volumeTotal[0]/5
    y = volumeTotal[1]
    z = volumeTotal[2]
    
    interv1_x = [0, round(particao*2, 2)]
    interv2_x = [round(particao, 2), round(particao*3, 2)]
    interv3_x = [round(particao*2, 2), round(particao*4, 2)]
    interv4_x = [round(particao*3, 2), round(particao*5, 2)]
    
    sub25 = [[interv1_x, y, z],
               [interv2_x, y, z],
               [interv3_x, y, z],
               [interv4_x, y, z]]
    
    return sub25


# ------------------------------------------------------------------------------------------------------------------------
# retorna um vetor com as medidas em X, Y e Z
def sub35(volumeTotal):

    particao = volumeTotal[0]/5
    y = volumeTotal[1]
    z = volumeTotal[2]
    
    interv1_x = [0, round(particao*3, 2)]
    interv2_x = [round(particao, 2), round(particao*4, 2)]
    interv3_x = [round(particao*2, 2), round(particao*5, 2)]
    
    sub35 = [[interv1_x, y, z],
               [interv2_x, y, z],
               [interv3_x, y, z]]
    
    return sub35


# ------------------------------------------------------------------------------------------------------------------------
# retorna um vetor com as medidas em X, Y e Z
def sub34(volumeTotal):

    particao = volumeTotal[0]/4
    y = volumeTotal[1]
    z = volumeTotal[2]
    
    interv1_x = [0, round(particao*3, 2)]
    interv2_x = [round(particao, 2), round(particao*4, 2)]
    
    sub34 = [[interv1_x, y, z],
               [interv2_x, y, z]]
    
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