from tkinter import *
from gera_pasta import *
from ordena import *
from Recolher_valor_plan import *
from plotar_regrecao import *
from tkinter.filedialog import askopenfilename

def PlotarNovoGrafico(x, y, intervalo_inicial, intervalo_final, total):
        
    new_x, new_y = limpar(x, y, intervalo_inicial, intervalo_final)
    new_x, new_y = crescente(new_x, new_y)
    plotResul(x, y, total, new_x, new_y, intervalo_inicial, intervalo_final, replot= 'y')


def PlotarGraficoIntev(volume, phi, total):
                
    PlotarGraficoIntev = Tk()
    PlotarGraficoIntev.title("Entradas")
    PlotarGraficoIntev.geometry("240x100+1100+300")
    PlotarGraficoIntev.resizable(0, 0)

    PlotarGraficoIntev.columnconfigure(0, weight=1)
    PlotarGraficoIntev.columnconfigure(1, weight=3)
            
    # intervalo mínimo
    label1 = Label(PlotarGraficoIntev, text='intervalo minimo:')
    label1.grid(column= 0, row= 0, sticky= E, padx= 5, pady= 5)
            
    inv_min = Entry(PlotarGraficoIntev)
    inv_min.grid(column= 1, row= 0, sticky= E, padx= 5, pady= 5)
            
    # intervalo máximo
    label2 = Label(PlotarGraficoIntev, text='intervalo maximo:')
    label2.grid(column= 0, row= 1, sticky= W, padx= 5, pady= 5)
            
    inv_max = Entry(PlotarGraficoIntev)
    inv_max.grid(column= 1, row= 1, sticky= E, padx= 5, pady= 5)
            
    # Botão de gerar
    btn = Button(PlotarGraficoIntev, text="Gerar", command= lambda: f'{PlotarNovoGrafico(volume, phi, int(inv_min.get()), int(inv_max.get()), total)} {PlotarGraficoIntev.mainloop()}')
    btn.grid(column= 1, row= 3, sticky= E, padx= 5, pady= 5)

    plotResul(volume, phi, total)


def PlotarGrafico():         

    filename = askopenfilename() # Isto te permite selecionar um arquivo

    phi = recolherValorPhi(filename)
    volume = recolherValorvolume(filename)
    volume, phi = crescente(volume, phi)
    total = valor_total(filename)
    
    PlotarGraficoIntev(volume, phi, total)


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
        
    # Botão gerar
    btn = Button(gerarSubvolume, text="Gerar SubVolumes", 
                    command= lambda: gerar_pastas(nome.get(), [int(eixoX.get()), int(eixoY.get()), int(eixoZ.get())]))
    btn.grid(column= 1, row= 4, sticky= W, padx= 5, pady= 5)
        
    # Botão Voltar
    btn = Button(gerarSubvolume, text="Voltar", 
                    command= lambda: [gerarSubvolume.destroy(), menuInicial()])
    btn.grid(column= 0, row= 4, sticky= W, padx= 5, pady= 5)
            
    gerarSubvolume.mainloop()


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

menuInicial()


