from tkinter import *
from modulos.gerarPasta import *
from modulos.ordena import *
from modulos.RecolherValorPlan import *
from modulos.PlotarRegrecao import *
from tkinter.filedialog import askopenfilename


def menuInicial():
    
    def PlotarGrafico():
        def PlotarGraficoIntev(volume, phi):
            def PlotarNovoGrafico(x, y, a, b):
        
                new_x, new_y = limpar(x, y, a, b)
                new_x, new_y = crescente(new_x, new_y)
                plotResul2(x, y, new_x, new_y, a, b, total)
                
            PlotarGraficoIntev = Tk()
            PlotarGraficoIntev.title("Entradas")
            PlotarGraficoIntev.geometry("240x100+1100+300")
            PlotarGraficoIntev.resizable(0, 0)

            PlotarGraficoIntev.columnconfigure(0, weight=1)
            PlotarGraficoIntev.columnconfigure(1, weight=3)
            
            # intervalo mínimo
            label1 = Label(PlotarGraficoIntev, text='intervalo mínimo:')
            label1.grid(column= 0, row= 0, sticky= E, padx= 5, pady= 5)
            
            inv_min = Entry(PlotarGraficoIntev)
            inv_min.grid(column= 1, row= 0, sticky= E, padx= 5, pady= 5)
            
            # intervalo máximo
            label2 = Label(PlotarGraficoIntev, text='intervalo máximo:')
            label2.grid(column= 0, row= 1, sticky= W, padx= 5, pady= 5)
            
            inv_max = Entry(PlotarGraficoIntev)
            inv_max.grid(column= 1, row= 1, sticky= E, padx= 5, pady= 5)
            
            # Botão de gerar
            btn = Button(PlotarGraficoIntev, text="Gerar", command= lambda: f'{PlotarNovoGrafico(volume, phi, int(inv_min.get()), int(inv_max.get()))} {PlotarGraficoIntev.mainloop()}')
            btn.grid(column= 1, row= 3, sticky= E, padx= 5, pady= 5)
            

        menuInicial.destroy()
        filename = askopenfilename() # Isto te permite selecionar um arquivo

        phi = recolherValorPhi(filename)
        volume = recolherValorvolume(filename)
        volume, phi = crescente(volume, phi)
        total = valor_total(filename)
        
        PlotarGraficoIntev(volume, phi)
        plotResul(volume, phi, total)

    def gerarSubvolume():
        menuInicial.destroy()
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
                    command= lambda: ...)
        btn.grid(column= 0, row= 4, sticky= W, padx= 5, pady= 5)
            
        gerarSubvolume.mainloop()
    
    menuInicial = Tk()
    menuInicial.title("REV")
    menuInicial.geometry("500x250+500+200")
    menuInicial.resizable(1, 1)
    menuInicial.minsize(500, 250)

    label1 = Label(menuInicial, text='Selecione a função desejada: ')
    btn = Button(menuInicial, text="Gerar SubVolumes", command= lambda: gerarSubvolume())
    btn2 = Button(menuInicial, text="Plotar Gráfico", command= lambda: PlotarGrafico())

    label1.pack()
    btn.pack()
    btn2.pack()
    menuInicial.mainloop()

menuInicial()


