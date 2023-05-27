import os
users = str(os.getlogin())
unidadeDeDisco = str(os.path.abspath(os.sep))


def CriarSubamostras(local_de_salvamento, nome_amostra):
    
    # Diretório para criação da pasta de amostra e subamostra 
    local_pasta_amostra = Rf'{local_de_salvamento}\Amostra {nome_amostra}'
    local_pasta_subvolume = Rf'{local_de_salvamento}\Amostra {nome_amostra}\Subvolumes'
    
    # Função geradora das pastas
    os.mkdir(local_pasta_amostra)
    os.mkdir(local_pasta_subvolume)

    for i in range(0,61):
        if i == 0:
            os.mkdir(local_pasta_subvolume + f'\{i}- Amostra {nome_amostra}_volumeTotal' )
        
        elif i > 0 and i<=14:
            os.mkdir(local_pasta_subvolume + f'\{i}- Amostra {nome_amostra}_particao{i-1}')
                
        elif i > 14 and  i <= 37:
            os.mkdir(local_pasta_subvolume + f'\{i}- Amostra {nome_amostra}_FracX{i-15}')
                
        else:
            os.mkdir(local_pasta_subvolume + f'\{i}- Amostra {nome_amostra}_FracZ{i-38}')