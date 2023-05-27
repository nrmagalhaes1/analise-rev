import shutil, os, webbrowser
from Particao_3_eixos import *
from fracionamento_3_eixos import *
from Criar_pasta import *
import posicao_tabela as pt
from tkinter.filedialog import  askdirectory
from openpyxl import load_workbook
from tkinter import Tk

Tk().withdraw() 

unidadeDeDisco = str(os.path.abspath(os.sep))
usuario_atual_win = str(os.getlogin())


# ------------------------------------------------------------------------------------------------------------------------
# Recolhendo os valores das coordenadas X, Y e Z

def gerar_pastas(nome_da_amostra, volume_total):
    
    local_salvamento = askdirectory()

    metodo1 = particao_em_3eixos(volume_total)
    metodo2 = fracionamento(volume_total)

    CriarSubamostras(local_salvamento, nome_da_amostra)
    webbrowser.open(os.path.realpath(f'{local_salvamento}\Amostra {nome_da_amostra}'))

    lista=particao_em_3eixos(volume_total)+fracionamento(volume_total)
    q=[]
    w=[]
    e=[]
    r=[]
    t=[]
    y=[]

    for vetor in lista:
        if isinstance(vetor[0], list):
            q.append(int(vetor[0][0]))
            r.append(int(vetor[0][1]))
        else:
            q.append(int(1))
            r.append(int(vetor[0]))

        if isinstance(vetor[1], list):
            w.append(int(vetor[1][0]))
            t.append(int(vetor[1][1]))
        else:
            w.append(1)
            t.append(int(vetor[1]))

        if isinstance(vetor[2], list):
            e.append(int(vetor[2][0]))
            y.append(int(vetor[2][1]))
        else:
            e.append(1)
            y.append(int(vetor[2]))

    q = [1 if x == 0 else x for x in q]
    w = [1 if x == 0 else x for x in w]
    e = [1 if x == 0 else x for x in e]
    r = [1 if x == 0 else x for x in r]
    t = [1 if x == 0 else x for x in t]
    y = [1 if x == 0 else x for x in y]
    
    print(lista)
    print("\n")
    print(q)
    print("\n")
    print(w)
    print("\n")
    print(e)
    print("\n")
    print(r)
    print("\n")
    print(t)
    print("\n")
    print(y)
# ------------------------------------------------------------------------------------------------------------------------
# importando os dados para a planilha método 01

    wb = load_workbook(fr'{os.getcwd()}\modulos\Modelo.xlsx')
    ws = wb['Plan1']

    Tabela01 = pt.celulasTabela01()
    c=0
    for d in range (0,15):
        for k in range (0, 3):
            ws[Tabela01[c]] = str(metodo1[d][k])
            c += 1

    wb.save(f'{os.getcwd()}\Subvolume da amostra X.xlsx')

# ------------------------------------------------------------------------------------------------------------------------
# importando os dados para a planilha método 02 em X

    wb = load_workbook(f'{os.getcwd()}\Subvolume da amostra X.xlsx')
    ws = wb['Plan1']

    Tabela02 = pt.celulasTabela02()
    c=0
    for d in range (0,23):
        for k in range (0, 3):
            ws[Tabela02[c]] = str(metodo2[d][k])
            c += 1
            
    wb.save(f'{os.getcwd()}\Subvolume da amostra X.xlsx')


# ------------------------------------------------------------------------------------------------------------------------
# Copiando o arqivo para área de trabalho
    wb.save(f'{os.getcwd()}\Subvolume da amostra X.xlsx')
    source = rf'{os.getcwd()}\Subvolume da amostra X.xlsx'
    destination = rf'{local_salvamento}\Amostra {nome_da_amostra}'
    shutil.copy(source, destination)
    os.rename(rf'{local_salvamento}\Amostra {nome_da_amostra}\Subvolume da amostra X.xlsx', rf'{local_salvamento}\Amostra {nome_da_amostra}\Subvolume da amostra {nome_da_amostra}.xlsx')

# ------------------------------------------------------------------------------------------------------------------------


