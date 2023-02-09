
def subvolume_13(volume_total):

    eixo_x = volume_total[0]
    eixo_y = volume_total[1]
    divisao_em_partes = round(volume_total[2]/3, 2)
    
    primeiro_intervalo_z = [0, divisao_em_partes]
    segundo_intervalo_z = [divisao_em_partes, divisao_em_partes*2]
    terceiro_intervalo_z = [divisao_em_partes*2, divisao_em_partes*3]
    
    sub13 = [[eixo_x, eixo_y, primeiro_intervalo_z],
            [eixo_x, eixo_y, segundo_intervalo_z],
            [eixo_x, eixo_y, terceiro_intervalo_z]]
    
    return sub13


def subvolume_23(volume_total):

    eixo_x = volume_total[0]
    eixo_y = volume_total[1]
    divisao_em_partes = round(volume_total[2]/3, 2)
    
    primeiro_intervalo_z = [0, divisao_em_partes*2]
    segundo_intervalo_z = [divisao_em_partes, divisao_em_partes*3]
    
    sub23 = [[eixo_x, eixo_y, primeiro_intervalo_z],
            [eixo_x, eixo_y, segundo_intervalo_z]]
    
    return sub23


def subvolume_25(volume_total):

    eixo_x = volume_total[0]
    eixo_y = volume_total[1]
    divisao_em_partes = round(volume_total[2]/5, 2)
    
    primeiro_intervalo_z = [0, divisao_em_partes*2]
    segundo_intervalo_z = [divisao_em_partes, divisao_em_partes*3]
    terceiro_intervalo_z = [divisao_em_partes*2, divisao_em_partes*4]
    quarto_intervalo_z = [divisao_em_partes*3, divisao_em_partes*5]
    
    sub25 = [[eixo_x, eixo_y, primeiro_intervalo_z],
               [eixo_x, eixo_y, segundo_intervalo_z],
               [eixo_x, eixo_y, terceiro_intervalo_z],
               [eixo_x, eixo_y, quarto_intervalo_z]]
    
    return sub25


def subvolume_35(volume_total):

    eixo_x = volume_total[0]
    eixo_y = volume_total[1]
    divisao_em_partes = round(volume_total[2]/5, 2)
    
    primeiro_intervalo_z = [0, divisao_em_partes*3]
    segundo_intervalo_z = [divisao_em_partes, divisao_em_partes*4]
    terceiro_intervalo_z = [divisao_em_partes*2, divisao_em_partes*5]
    
    sub35 = [[eixo_x, eixo_y, primeiro_intervalo_z],
               [eixo_x, eixo_y, segundo_intervalo_z],
               [eixo_x, eixo_y, terceiro_intervalo_z]]
    
    return sub35


def subvolume_34(volume_total):

    eixo_x = volume_total[0]
    eixo_y = volume_total[1]
    divisao_em_partes = round(volume_total[2]/4, 2)
    
    primeiro_intervalo_z = [0, divisao_em_partes*3]
    segundo_intervalo_z = [divisao_em_partes, divisao_em_partes*4]
    
    sub34 = [[eixo_x, eixo_y, primeiro_intervalo_z],
               [eixo_x, eixo_y, segundo_intervalo_z]]
    
    return sub34


def fracionamento_em_z(volume_total):

    return subvolume_13(volume_total) \
        + subvolume_23(volume_total)\
        + subvolume_25(volume_total)\
        + subvolume_35(volume_total)\
        + subvolume_34(volume_total)