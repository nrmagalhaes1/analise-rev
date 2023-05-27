def subvolume_13(volume_total):

    divisao_em_partes_x = round(volume_total[0]/3, 2)
    divisao_em_partes_y = round(volume_total[1]/3, 2)
    divisao_em_partes_z = round(volume_total[2]/3, 2)
    y = volume_total[1]
    z = volume_total[2]
    
    primeiro_intervalo_x = [0, divisao_em_partes_x]
    segundo_intervalo_x = [divisao_em_partes_x, divisao_em_partes_x*2]
    terceiro_intervalo_x = [divisao_em_partes_x*2, divisao_em_partes_x*3]

    primeiro_intervalo_y = [0, divisao_em_partes_y]
    segundo_intervalo_y = [divisao_em_partes_y, divisao_em_partes_y*2]
    terceiro_intervalo_y = [divisao_em_partes_y*2, divisao_em_partes_y*3]

    primeiro_intervalo_z = [0, divisao_em_partes_z]
    segundo_intervalo_z = [divisao_em_partes_z, divisao_em_partes_z*2]
    terceiro_intervalo_z = [divisao_em_partes_z*2, divisao_em_partes_z*3]
    
    subvolume_13 = [[primeiro_intervalo_x, primeiro_intervalo_y, primeiro_intervalo_z],
            [segundo_intervalo_x, segundo_intervalo_y, segundo_intervalo_z],
            [terceiro_intervalo_x, terceiro_intervalo_y, terceiro_intervalo_z]]
    
    return subvolume_13


def subvolume_23(volume_total):

    divisao_em_partes_x = round(volume_total[0]/3, 2)
    divisao_em_partes_y = round(volume_total[1]/3, 2)
    divisao_em_partes_z = round(volume_total[2]/3, 2)
    
    primeiro_intervalo_x = [0, divisao_em_partes_x*2]
    segundo_intervalo_x = [divisao_em_partes_x, divisao_em_partes_x*3]

    primeiro_intervalo_y = [0, divisao_em_partes_y*2]
    segundo_intervalo_y = [divisao_em_partes_y, divisao_em_partes_y*3]

    primeiro_intervalo_z = [0, divisao_em_partes_z*2]
    segundo_intervalo_z = [divisao_em_partes_z, divisao_em_partes_z*3]
    
    subvolume_23 = [[primeiro_intervalo_x, primeiro_intervalo_y, primeiro_intervalo_z],
            [segundo_intervalo_x, segundo_intervalo_y, segundo_intervalo_z]]
    
    return subvolume_23


def subvolume_25(volume_total):

    divisao_em_partes_x = round(volume_total[0]/5, 2)
    divisao_em_partes_y = round(volume_total[1]/5, 2)
    divisao_em_partes_z = round(volume_total[2]/5, 2)
    
    primeiro_intervalo_x = [0, divisao_em_partes_x*2]
    segundo_intervalo_x = [divisao_em_partes_x, divisao_em_partes_x*3]
    terceiro_intervalo_x = [divisao_em_partes_x*2, divisao_em_partes_x*4]
    quarto_intervalo_x = [divisao_em_partes_x*3, divisao_em_partes_x*5]
    
    primeiro_intervalo_y = [0, divisao_em_partes_y*2]
    segundo_intervalo_y = [divisao_em_partes_y, divisao_em_partes_y*3]
    terceiro_intervalo_y = [divisao_em_partes_y*2, divisao_em_partes_y*4]
    quarto_intervalo_y = [divisao_em_partes_y*3, divisao_em_partes_y*5]

    primeiro_intervalo_z = [0, divisao_em_partes_z*2]
    segundo_intervalo_z = [divisao_em_partes_z, divisao_em_partes_z*3]
    terceiro_intervalo_z = [divisao_em_partes_z*2, divisao_em_partes_z*4]
    quarto_intervalo_z = [divisao_em_partes_z*3, divisao_em_partes_z*5]
    
    subvolume_25 = [[primeiro_intervalo_x, primeiro_intervalo_y, primeiro_intervalo_z],
            [segundo_intervalo_x, segundo_intervalo_y, segundo_intervalo_z],
            [terceiro_intervalo_x, terceiro_intervalo_y, terceiro_intervalo_z],
            [quarto_intervalo_x, quarto_intervalo_y, quarto_intervalo_z]]
    
    return subvolume_25


def subvolume_35(volume_total):

    divisao_em_partes_x = round(volume_total[0]/5, 2)
    divisao_em_partes_y = round(volume_total[1]/5, 2)
    divisao_em_partes_z = round(volume_total[2]/5, 2)

    
    primeiro_intervalo_x = [0, divisao_em_partes_x*3]
    segundo_intervalo_x = [divisao_em_partes_x, divisao_em_partes_x*4]
    terceiro_intervalo_x = [divisao_em_partes_x*2, divisao_em_partes_x*5]

    primeiro_intervalo_y = [0, divisao_em_partes_y*3]
    segundo_intervalo_y = [divisao_em_partes_y, divisao_em_partes_y*4]
    terceiro_intervalo_y = [divisao_em_partes_y*2, divisao_em_partes_y*5]

    primeiro_intervalo_z = [0, divisao_em_partes_z*3]
    segundo_intervalo_z = [divisao_em_partes_z, divisao_em_partes_z*4]
    terceiro_intervalo_z = [divisao_em_partes_z*2, divisao_em_partes_z*5]
    
    subvolume_35 = [[primeiro_intervalo_x, primeiro_intervalo_y, primeiro_intervalo_z],
            [segundo_intervalo_x, segundo_intervalo_y, segundo_intervalo_z],
            [terceiro_intervalo_x, terceiro_intervalo_y, terceiro_intervalo_z]]
    
    return subvolume_35


def subvolume_34(volume_total):

    divisao_em_partes_x = round(volume_total[0]/4, 2)
    divisao_em_partes_y = round(volume_total[1]/4, 2)
    divisao_em_partes_z = round(volume_total[2]/4, 2)

    primeiro_intervalo_x = [0, divisao_em_partes_x*3]
    segundo_intervalo_x = [divisao_em_partes_x, divisao_em_partes_x*4]

    primeiro_intervalo_y = [0, divisao_em_partes_y*3]
    segundo_intervalo_y = [divisao_em_partes_y, divisao_em_partes_y*4]

    primeiro_intervalo_z = [0, divisao_em_partes_z*3]
    segundo_intervalo_z = [divisao_em_partes_z, divisao_em_partes_z*4]
    
    subvolume_34 = [[primeiro_intervalo_x, primeiro_intervalo_y, primeiro_intervalo_z],
            [segundo_intervalo_x, segundo_intervalo_y, segundo_intervalo_z]]
    
    return subvolume_34

def subvolume_14(volume_total):

    divisao_em_partes_x = round(volume_total[0]/4, 2)
    divisao_em_partes_y = round(volume_total[1]/4, 2)
    divisao_em_partes_z = round(volume_total[2]/4, 2)
    
    primeiro_intervalo_x = [0, divisao_em_partes_x]
    segundo_intervalo_x = [divisao_em_partes_x, divisao_em_partes_x*2]
    terceiro_intervalo_x = [divisao_em_partes_x*2, divisao_em_partes_x*3]
    quarto_intervalo_x = [divisao_em_partes_x*3, divisao_em_partes_x*4]

    primeiro_intervalo_y = [0, divisao_em_partes_y]
    segundo_intervalo_y = [divisao_em_partes_y, divisao_em_partes_y*2]
    terceiro_intervalo_y = [divisao_em_partes_y*2, divisao_em_partes_y*3]
    quarto_intervalo_y = [divisao_em_partes_y*3, divisao_em_partes_y*4]

    primeiro_intervalo_z = [0, divisao_em_partes_z]
    segundo_intervalo_z = [divisao_em_partes_z, divisao_em_partes_z*2]
    terceiro_intervalo_z = [divisao_em_partes_z*2, divisao_em_partes_z*3]
    quarto_intervalo_z = [divisao_em_partes_z*3, divisao_em_partes_z*4]
    
    subvolume_14 = [[primeiro_intervalo_x, primeiro_intervalo_y, primeiro_intervalo_z],
            [segundo_intervalo_x, segundo_intervalo_y, segundo_intervalo_z],
            [terceiro_intervalo_x, terceiro_intervalo_y, terceiro_intervalo_z],
            [quarto_intervalo_x, quarto_intervalo_y, quarto_intervalo_z]]
    
    return subvolume_14

def subvolume_15(volume_total):

    divisao_em_partes_x = round(volume_total[0]/5, 2)
    divisao_em_partes_y = round(volume_total[1]/5, 2)
    divisao_em_partes_z = round(volume_total[2]/5, 2)
    
    primeiro_intervalo_x = [0, divisao_em_partes_x]
    segundo_intervalo_x = [divisao_em_partes_x, divisao_em_partes_x*2]
    terceiro_intervalo_x = [divisao_em_partes_x*2, divisao_em_partes_x*3]
    quarto_intervalo_x = [divisao_em_partes_x*3, divisao_em_partes_x*4]
    quinto_intervalo_x = [divisao_em_partes_x*4, divisao_em_partes_x*5]

    primeiro_intervalo_y = [0, divisao_em_partes_y]
    segundo_intervalo_y = [divisao_em_partes_y, divisao_em_partes_y*2]
    terceiro_intervalo_y = [divisao_em_partes_y*2, divisao_em_partes_y*3]
    quarto_intervalo_y = [divisao_em_partes_y*3, divisao_em_partes_y*4]
    quinto_intervalo_y = [divisao_em_partes_y*4, divisao_em_partes_y*5]

    primeiro_intervalo_z = [0, divisao_em_partes_z]
    segundo_intervalo_z = [divisao_em_partes_z, divisao_em_partes_z*2]
    terceiro_intervalo_z = [divisao_em_partes_z*2, divisao_em_partes_z*3]
    quarto_intervalo_z = [divisao_em_partes_z*3, divisao_em_partes_z*4]
    quinto_intervalo_z = [divisao_em_partes_z*4, divisao_em_partes_z*5]

    subvolume_15 = [[primeiro_intervalo_x, primeiro_intervalo_y, primeiro_intervalo_z],
            [segundo_intervalo_x, segundo_intervalo_y, segundo_intervalo_z],
            [terceiro_intervalo_x, terceiro_intervalo_y, terceiro_intervalo_z],
            [quarto_intervalo_x, quarto_intervalo_y, quarto_intervalo_z],
            [quinto_intervalo_x, quinto_intervalo_y, quinto_intervalo_z]]
    
    return subvolume_15


def fracionamento(volume_total):

    return subvolume_13(volume_total) \
        + subvolume_23(volume_total)\
        + subvolume_25(volume_total)\
        + subvolume_35(volume_total)\
        + subvolume_34(volume_total)\
        + subvolume_14(volume_total)\
        + subvolume_15(volume_total)