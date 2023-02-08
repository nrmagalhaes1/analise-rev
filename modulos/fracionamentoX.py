
# retorna um vetor com as medidas em X, Y e Z
def sub13(volumeTotal):

    divisao_em_partes = round(volumeTotal[0]/3, 2)
    y = volumeTotal[1]
    z = volumeTotal[2]
    
    interv1_x = [0, divisao_em_partes]
    interv2_x = [divisao_em_partes, divisao_em_partes*2]
    interv3_x = [divisao_em_partes*2, divisao_em_partes*3]
    
    sub13 = [[interv1_x, y, z],
            [interv2_x, y, z],
            [interv3_x, y, z]]
    
    return sub13


# retorna um vetor com as medidas em X, Y e Z
def sub23(volumeTotal):

    particao = round(volumeTotal[0]/3, 2)
    y = volumeTotal[1]
    z = volumeTotal[2]
    
    interv1_x = [0, particao*2]
    interv2_x = [particao, particao*3]
    
    sub23 = [[interv1_x, y, z],
            [interv2_x, y, z]]
    
    return sub23


# retorna um vetor com as medidas em X, Y e Z
def sub25(volumeTotal):

    particao = round(volumeTotal[0]/5, 2)
    y = volumeTotal[1]
    z = volumeTotal[2]
    
    interv1_x = [0, particao*2]
    interv2_x = [particao, particao*3]
    interv3_x = [particao*2, particao*4]
    interv4_x = [particao*3, particao*5]
    
    sub25 = [[interv1_x, y, z],
               [interv2_x, y, z],
               [interv3_x, y, z],
               [interv4_x, y, z]]
    
    return sub25


# retorna um vetor com as medidas em X, Y e Z
def sub35(volumeTotal):

    particao = round(volumeTotal[0]/5, 2)
    y = volumeTotal[1]
    z = volumeTotal[2]
    
    interv1_x = [0, particao*3]
    interv2_x = [particao, particao*4]
    interv3_x = [particao*2, particao*5]
    
    sub35 = [[interv1_x, y, z],
               [interv2_x, y, z],
               [interv3_x, y, z]]
    
    return sub35


# retorna um vetor com as medidas em X, Y e Z
def sub34(volumeTotal):

    particao = round(volumeTotal[0]/4, 2)
    y = volumeTotal[1]
    z = volumeTotal[2]
    
    interv1_x = [0, particao*3]
    interv2_x = [particao, particao*4]
    
    sub34 = [[interv1_x, y, z],
               [interv2_x, y, z]]
    
    return sub34


def executar(volume):
    sub_13 = sub13(volume)
    sub_23 = sub23(volume)
    sub_25 = sub25(volume)
    sub_35 = sub35(volume)
    sub_34 = sub34(volume)
    metodo2 = sub_13 + sub_23 + sub_25 + sub_35 + sub_34
    return metodo2