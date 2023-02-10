
def subvolume_13(volume_total):

    divisao_em_partes = round(volume_total[0]/3, 2)
    y = volume_total[1]
    z = volume_total[2]
    
    primeiro_intervalo_x = [0, divisao_em_partes]
    segundo_intervalo_x = [divisao_em_partes, divisao_em_partes*2]
    terceiro_intervalo_x = [divisao_em_partes*2, divisao_em_partes*3]
    
    subvolume_13 = [[primeiro_intervalo_x, y, z],
            [segundo_intervalo_x, y, z],
            [terceiro_intervalo_x, y, z]]
    
    return subvolume_13


def subvolume_23(volume_total):

    divisao_em_partes = round(volume_total[0]/3, 2)
    eixo_y = volume_total[1]
    eixo_z = volume_total[2]
    
    primeiro_intervalo_x = [0, divisao_em_partes*2]
    segundo_intervalo_x = [divisao_em_partes, divisao_em_partes*3]
    
    subvolume_23 = [[primeiro_intervalo_x, eixo_y, eixo_z],
            [segundo_intervalo_x, eixo_y, eixo_z]]
    
    return subvolume_23


def subvolume_25(volume_total):

    divisao_em_partes = round(volume_total[0]/5, 2)
    eixo_y = volume_total[1]
    eixo_z = volume_total[2]
    
    primeiro_intervalo_x = [0, divisao_em_partes*2]
    segundo_intervalo_x = [divisao_em_partes, divisao_em_partes*3]
    terceiro_intervalo_x = [divisao_em_partes*2, divisao_em_partes*4]
    quarto_intervalo_x = [divisao_em_partes*3, divisao_em_partes*5]
    
    subvolume_25 = [[primeiro_intervalo_x, eixo_y, eixo_z],
            [segundo_intervalo_x, eixo_y, eixo_z],
            [terceiro_intervalo_x, eixo_y, eixo_z],
            [quarto_intervalo_x, eixo_y, eixo_z]]
    
    return subvolume_25


def subvolume_35(volume_total):

    divisao_em_partes = round(volume_total[0]/5, 2)
    eixo_y = volume_total[1]
    eixo_z = volume_total[2]
    
    primeiro_intervalo_x = [0, divisao_em_partes*3]
    segundo_intervalo_x = [divisao_em_partes, divisao_em_partes*4]
    terceiro_intervalo_x = [divisao_em_partes*2, divisao_em_partes*5]
    
    subvolume_35 = [[primeiro_intervalo_x, eixo_y, eixo_z],
            [segundo_intervalo_x, eixo_y, eixo_z],
            [terceiro_intervalo_x, eixo_y, eixo_z]]
    
    return subvolume_35


def subvolume_34(volume_total):

    divisao_em_partes = round(volume_total[0]/4, 2)
    eixo_y = volume_total[1]
    eixo_z = volume_total[2]
    
    primeiro_intervalo_x = [0, divisao_em_partes*3]
    segundo_intervalo_x = [divisao_em_partes, divisao_em_partes*4]
    
    subvolume_34 = [[primeiro_intervalo_x, eixo_y, eixo_z],
            [segundo_intervalo_x, eixo_y, eixo_z]]
    
    return subvolume_34


def fracionamento_em_x(volume_total):

    return subvolume_13(volume_total) \
        + subvolume_23(volume_total)\
        + subvolume_25(volume_total)\
        + subvolume_35(volume_total)\
        + subvolume_34(volume_total)