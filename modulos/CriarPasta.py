import os
users = str(os.getlogin())
unidadeDeDisco = str(os.path.abspath(os.sep))

def CriarSubamostras(diretorioSalve, amostra):
    directoryPach = Rf'{diretorioSalve}\Amostra {amostra}'
    os.mkdir(directoryPach)
    
    directoryPach = Rf'{diretorioSalve}\Amostra {amostra}\Subvolumes'
    os.mkdir(directoryPach)


    for i in range(0,43):
        if i == 0:    
            directoryPach = Rf'{diretorioSalve}\Amostra {amostra}\Subvolumes\ {i}- Amostra {amostra}_volumeTotal'
            os.mkdir(directoryPach)
            
        else:
            if i<=14:    
                directoryPach = Rf'{diretorioSalve}\Amostra {amostra}\Subvolumes\ {i}- Amostra {amostra}_particao{i-1}'
                os.mkdir(directoryPach)
                
            else:
                if i <= 28:
                    directoryPach = Rf'{diretorioSalve}\Amostra {amostra}\Subvolumes\ {i}- Amostra {amostra}_FracX{i-15}'
                    os.mkdir(directoryPach)
                
                else:
                    directoryPach = Rf'{diretorioSalve}\Amostra {amostra}\Subvolumes\ {i}- Amostra {amostra}_FracZ{i-29}'
                    os.mkdir(directoryPach)
    return