# Função para particionar o volume ao longo do eixo z
def particao_eixo_z(volumeTotal):
    # Obtém as dimensões do volume
    eixo_x = volumeTotal[0]
    eixo_y = volumeTotal[1]
    # Calcula a divisão ao longo do eixo z
    divisao_em_partes = volumeTotal[2] / 2
    
    # Define os intervalos ao longo do eixo z
    primeiro_intervalo_z = [0, divisao_em_partes]
    segundo_intervalo_z = [divisao_em_partes, divisao_em_partes * 2]
    
    # Cria a partição ao longo do eixo z
    particao_eixo_z = [[eixo_x, eixo_y, primeiro_intervalo_z],
                       [eixo_x, eixo_y, segundo_intervalo_z]]
    
    return particao_eixo_z


# Função para particionar o volume ao longo do eixo x
def particao_eixo_x(particao_eixo_z):
    # Obtém a informação de partição ao longo do eixo z
    divisao_em_partes = particao_eixo_z[0][0] / 2
    eixo_y = particao_eixo_z[0][1]
    
    primeiro_intervalo_z = particao_eixo_z[0][2]
    segundo_intervalo_z = particao_eixo_z[1][2]
    
    # Define os intervalos ao longo do eixo x
    primeiro_intervalo_x = [0, divisao_em_partes]
    segundo_intervalo_x = [divisao_em_partes, divisao_em_partes * 2]
    
    # Cria a partição ao longo do eixo x usando informações do eixo z
    particao_eixo_x = [[primeiro_intervalo_x, eixo_y, primeiro_intervalo_z],
                       [segundo_intervalo_x, eixo_y, primeiro_intervalo_z],
                       [primeiro_intervalo_x, eixo_y, segundo_intervalo_z],
                       [segundo_intervalo_x, eixo_y, segundo_intervalo_z]]
    
    return particao_eixo_x


# Função para particionar o volume ao longo do eixo y
def particao_eixo_y(particao_eixo_y):
    # Obtém a informação de partição ao longo do eixo x
    divisao_em_partes = particao_eixo_y[0][1] / 2
    
    primeiro_intervalo_z = particao_eixo_y[0][2]
    segundo_intervalo_z = particao_eixo_y[2][2]
    primeiro_intervalo_x = particao_eixo_y[0][0]
    segundo_intervalo_x = particao_eixo_y[1][0]
    
    # Define os intervalos ao longo do eixo y
    primeiro_intervalo_y = [0, divisao_em_partes]
    segundo_intervalo_y = [divisao_em_partes, divisao_em_partes * 2]
    
    # Cria a partição ao longo do eixo y usando informações do eixo x
    particao_eixo_y = [[primeiro_intervalo_x, primeiro_intervalo_y, primeiro_intervalo_z],
                       [segundo_intervalo_x, primeiro_intervalo_y, primeiro_intervalo_z],
                       [primeiro_intervalo_x, primeiro_intervalo_y, segundo_intervalo_z],
                       [segundo_intervalo_x, primeiro_intervalo_y, segundo_intervalo_z],
                       [primeiro_intervalo_x, segundo_intervalo_y, primeiro_intervalo_z],
                       [segundo_intervalo_x, segundo_intervalo_y, primeiro_intervalo_z],
                       [primeiro_intervalo_x, segundo_intervalo_y, segundo_intervalo_z],
                       [segundo_intervalo_x, segundo_intervalo_y, segundo_intervalo_z]]
    
    return particao_eixo_y


# Função principal para particionar o volume nos três eixos
def particao_em_3eixos(volume_total):
    # Divide o volume nos eixos z, x e y
    eixo_z = particao_eixo_z(volume_total)
    eixo_x = particao_eixo_x(eixo_z)
    eixo_y = particao_eixo_y(eixo_x)
    
    # Retorna a partição nos três eixos
    return [volume_total] + eixo_z + eixo_x + eixo_y
