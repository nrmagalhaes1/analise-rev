# Este módulo contém funções para gerar listas de referências para células em diferentes tabelas.

# Função para células da Tabela 01
def celulasTabela01():
    celulasTabela01 = []

    # Loop para gerar referências para células de D7 a F21
    for i in range(7, 22):
        x = 'D'+f'{i}'
        y = 'E'+f'{i}'
        z = 'F'+f'{i}'
        celulasTabela01.append(x)
        celulasTabela01.append(y)
        celulasTabela01.append(z)
    
    return celulasTabela01


# Função para células da Tabela 02
def celulasTabela02():
    celulasTabela02 = []

    # Loop para gerar referências para células de D25 a F47
    for i in range(25, 48):
        x = 'D'+f'{i}'
        y = 'E'+f'{i}'
        z = 'F'+f'{i}'
        celulasTabela02.append(x)
        celulasTabela02.append(y)
        celulasTabela02.append(z)
    
    return celulasTabela02


# Lista de células da Tabela 03
celulasTabela03 = ['G7', 'G8', 'G9', 'G10', 'G11',
                'G12', 'G13', 'G14', 'G15' ,'G16',
                'G17', 'G18', 'G19', 'G20' ,'G21',
                'G25', 'G26', 'G27', 'G28' ,'G29',
                'G30', 'G31', 'G32', 'G33' ,'G34',
                'G35', 'G36', 'G37', 'G38']


# Função para células da Tabela 04
def celulasTabela04():
    celulasTabela04 = []

    # Loop para gerar referências para células de D51 a F73
    for i in range(51, 74):
        x = 'D'+f'{i}'
        y = 'E'+f'{i}'
        z = 'F'+f'{i}'
        celulasTabela04.append(x)
        celulasTabela04.append(y)
        celulasTabela04.append(z)
    
    return celulasTabela04
