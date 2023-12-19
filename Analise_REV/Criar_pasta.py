"""
Este módulo contém funcionalidades para criar amostras e subamostras em um sistema de arquivos. 
Ele utiliza o módulo 'os' para operações relacionadas ao sistema. O propósito principal é organizar 
e criar diretórios representando amostras e suas subdivisões para análises posteriores.

- 'os': Módulo que fornece funcionalidades para interagir com o sistema operacional, como criar diretórios.
- 'CriarSubamostras': Função para criar uma estrutura de diretórios para amostras e subamostras.
"""

import os
users = str(os.getlogin())
unidadeDeDisco = str(os.path.abspath(os.sep))


def CriarSubamostras(local_de_salvamento, nome_amostra):
    
    # Diretório para criação da pasta de amostra e subamostra 
    local_pasta_amostra = Rf'{local_de_salvamento}\Amostra {nome_amostra}'
    local_pasta_subvolume = Rf'{local_de_salvamento}\Amostra {nome_amostra}\Subvolumes'
    
    # Função geradora das pastas
    os.mkdir(local_pasta_amostra)  # Cria a pasta da amostra
    os.mkdir(local_pasta_subvolume)  # Cria a pasta de subvolumes

    for i in range(0,61):
        if i == 0:
            os.mkdir(local_pasta_subvolume + f'\{i}- Amostra {nome_amostra}_volumeTotal' )  # Cria pasta para o volume total
        
        elif i > 0 and i <= 14:
            os.mkdir(local_pasta_subvolume + f'\{i}- Amostra {nome_amostra}_particao{i-1}')  # Cria pastas para partições
                
        elif i > 14 and i <= 37:
            os.mkdir(local_pasta_subvolume + f'\{i}- Amostra {nome_amostra}_FracX{i-15}')  # Cria pastas para FracX
                
        else:
            os.mkdir(local_pasta_subvolume + f'\{i}- Amostra {nome_amostra}_FracZ{i-38}')  # Cria pastas para FracZ
