"""
Módulo de Interface Gráfica para Operações Estatísticas e de Análise de Dados REV

Este módulo oferece uma interface gráfica para realizar diversas operações estatísticas e de análise de dados REV.
Ele inclui funcionalidades como geração de pastas, ordenação de valores, recolhimento de valores de um plano e
plotagem de regressões.

Última atualização: Julho de 2023
Desenvolvedor: Nathan Rangel Magalhães

O código a seguir contém uma série de funções que interagem com uma interface gráfica (GUI)
para permitir a execução de diversas operações estatísticas e análise de dados. 

"""
from tkinter import *
from gera_pasta import *  # Importa funções para gerar pastas
from ordena import *  # Importa funções para ordenação
from Recolher_valor_plan import *  # Importa funções para recuperar valores do plano
from plotar_regrecao import *  # Importa funções para plotar regressão
from tkinter.filedialog import askopenfilename  # Importa função para abrir diálogo de seleção de arquivo

# Função para plotar um novo gráfico com base nos intervalos fornecidos
def PlotarNovoGrafico(x, y, intervalo_inicial, intervalo_final, total):

    # Limpa os dados com base nos intervalos    
    new_x, new_y = limpar(x, y, intervalo_inicial, intervalo_final)
    new_x, new_y = crescente(new_x, new_y)
    plotResul(x, y, total, new_x, new_y, intervalo_inicial, intervalo_final, replot= 'y')

# Função para criar a interface gráfica para definir intervalos e plotar gráficos
def PlotarGraficoIntev(volume, phi, total):
                
    PlotarGraficoIntev = Tk()
    PlotarGraficoIntev.title("Entradas")
    PlotarGraficoIntev.geometry("240x100+1100+300")
    PlotarGraficoIntev.resizable(0, 0)

    PlotarGraficoIntev.columnconfigure(0, weight=1)
    PlotarGraficoIntev.columnconfigure(1, weight=3)
            
    # intervalo m�nimo
    label1 = Label(PlotarGraficoIntev, text='intervalo minimo:')
    label1.grid(column= 0, row= 0, sticky= E, padx= 5, pady= 5)
            
    inv_min = Entry(PlotarGraficoIntev)
    inv_min.grid(column= 1, row= 0, sticky= E, padx= 5, pady= 5)
            
    # intervalo m�ximo
    label2 = Label(PlotarGraficoIntev, text='intervalo maximo:')
    label2.grid(column= 0, row= 1, sticky= W, padx= 5, pady= 5)
            
    inv_max = Entry(PlotarGraficoIntev)
    inv_max.grid(column= 1, row= 1, sticky= E, padx= 5, pady= 5)
            
    # Bot�o de gerar
    btn = Button(PlotarGraficoIntev, text="Gerar", command= lambda: f'{PlotarNovoGrafico(volume, phi, int(inv_min.get()), int(inv_max.get()), total)} {PlotarGraficoIntev.mainloop()}')
    btn.grid(column= 1, row= 3, sticky= E, padx= 5, pady= 5)

    plotResul(volume, phi, total)

# Função para abrir um arquivo e plotar um gráfico com base nos dados
def PlotarGrafico():         

    filename = askopenfilename() # Isto te permite selecionar um arquivo

    phi = recolherValorPhi(filename)
    volume = recolherValorvolume(filename)
    volume, phi = crescente(volume, phi)
    total = valor_total(filename)
    
    PlotarGraficoIntev(volume, phi, total)

# Função para gerar subvolumes com base nos valores inseridos
def gerarSubvolume():
    gerarSubvolume = Tk()
    gerarSubvolume.title("Gerar Subvolume")
    gerarSubvolume.geometry("250x200+500+200")
    gerarSubvolume.resizable(0, 0)

    gerarSubvolume.columnconfigure(0, weight=0)
    gerarSubvolume.rowconfigure(2, weight=0)
        
    # Nome da amostra
    label1 = Label(gerarSubvolume, text='nome da amostra: ')
    label1.grid(column= 0, row= 0, sticky= W, padx= 5, pady= 5)
        
    nome = Entry(gerarSubvolume)
    nome.grid(column= 1, row= 0, sticky= E, padx= 5, pady= 5)
        
    #Valor eixo X
    label2 = Label(gerarSubvolume, text='valor do eixo X: ')
    label2.grid(column= 0, row= 1, sticky= W, padx= 5, pady= 5)
        
    eixoX = Entry(gerarSubvolume)
    eixoX.grid(column= 1, row= 1, sticky= E, padx= 5, pady= 5)
        
    # Valor eixo Y
    label3 = Label(gerarSubvolume, text='valor do eixo Y: ')
    label3.grid(column= 0, row= 2, sticky= W, padx= 5, pady= 5)
        
    eixoY = Entry(gerarSubvolume)
    eixoY.grid(column= 1, row= 2, sticky= E, padx= 5, pady= 5)
        
    #Valor eixo Z
    label4 = Label(gerarSubvolume, text='valor do eixo Z: ')
    label4.grid(column= 0, row= 3, sticky= W, padx= 5, pady= 5)
        
    eixoZ = Entry(gerarSubvolume)
    eixoZ.grid(column= 1, row= 3, sticky= E, padx= 5, pady= 5)
        
    # Bot�o gerar
    btn = Button(gerarSubvolume, text="Gerar SubVolumes", 
                    command= lambda: gerar_pastas(nome.get(), [int(eixoX.get()), int(eixoY.get()), int(eixoZ.get())]))
    btn.grid(column= 1, row= 4, sticky= W, padx= 5, pady= 5)
        
    # Bot�o Voltar
    btn = Button(gerarSubvolume, text="Voltar", 
                    command= lambda: [gerarSubvolume.destroy(), menuInicial()])
    btn.grid(column= 0, row= 4, sticky= W, padx= 5, pady= 5)
            
    gerarSubvolume.mainloop()

# Função para exibir o menu inicial com opções disponíveis
def menuInicial():
    
    menuInicial = Tk()
    menuInicial.title("REV")
    menuInicial.geometry("500x250+500+200")
    menuInicial.resizable(1, 1)
    menuInicial.minsize(500, 250)

    label1 = Label(menuInicial, text='Selecione a funcao desejada: ')
    btn = Button(menuInicial, text="Gerar SubVolumes", command= lambda: [menuInicial.destroy(), gerarSubvolume()])
    btn2 = Button(menuInicial, text="Plotar Grafico", command= lambda: [menuInicial.destroy(), PlotarGrafico()])

    label1.pack()
    btn.pack()
    btn2.pack()
    menuInicial.mainloop()
    
# Chama a função para exibir o menu inicial ao iniciar o programa
menuInicial()


