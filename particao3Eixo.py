
# retorna um vetor com as medidas em X, Y e Z
def particaoEixoZ(volumeTotal):
    volume = []
    
    x = volumeTotal[0]
    y = volumeTotal[1]
    particao = volumeTotal[2]/2
    
    interv1_z = [0, particao]
    interv2_z = [particao, particao*2]
    
    subVol1 = [[x,y,interv1_z],
                [x,y, interv2_z]]
    
    return subVol1


# ------------------------------------------------------------------------------------------------------------------------
# retorna um vetor com as medidas em X, Y e Z
def particaoEixoX(particaoEixoZ):

    particao = particaoEixoZ[0][0]/2
    y = particaoEixoZ[0][1]
    
    interv1_z = particaoEixoZ[0][2]
    interv2_z = particaoEixoZ[1][2]
    interv1_x = [0, particao]
    interv2_x = [particao, particao*2]
    
    subVol2 = [[interv1_x, y, interv1_z],
                [interv2_x, y, interv1_z],
                [interv1_x, y, interv2_z],
                [interv2_x, y, interv2_z]]
    
    return subVol2
 
 
 # ------------------------------------------------------------------------------------------------------------------------
 # retorna um vetor com as medidas em X, Y e Z   
def particaoEixoY(particaoEixoY):

    particao = particaoEixoY[0][1]/2
    
    interv1_z = particaoEixoY[0][2]
    interv2_z = particaoEixoY[2][2]
    interv1_x = particaoEixoY[0][0]
    interv2_x = particaoEixoY[1][0]
    interv1_y = [0, particao]
    interv2_y = [particao, particao*2]
    
    subVol3 = [[interv1_x,interv1_y,interv1_z],
               [interv2_x,interv1_y,interv1_z],
               [interv1_x,interv1_y,interv2_z],
               [interv2_x,interv1_y,interv2_z],
               [interv1_x,interv2_y,interv1_z],
               [interv2_x,interv2_y,interv1_z],
               [interv1_x,interv2_y,interv2_z],
               [interv2_x,interv2_y,interv2_z]]
    
    return subVol3
    
def executar(volume):
    EixoZ = particaoEixoZ(volume)
    EixoX = particaoEixoX(EixoZ)
    EixoY = particaoEixoY(EixoX)
    metodo1 = [volume] + EixoZ + EixoX + EixoY
    return metodo1

    
    
    