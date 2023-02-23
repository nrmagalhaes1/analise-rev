![Capa](https://user-images.githubusercontent.com/102970648/217289588-89ab5431-3e6d-43e4-a222-3701ce606f91.png)

# Descrição

> **Status do projeto:** Em andamento :construction:

**Sobre o projeto:** Esse código tem o intuito de automatizar o processo que analisa o volume elementar representativo (REV) de amostras reconstruidas digitalmente através de imagens obtidas por microtomografias de raios X. Tal processo soluciona a dificuldade de estabelecer o volume que seja capaz de representar as propriedades petrofísicas em uma escala maior. Baseando-se na porosidade como a propriedade petrofísica para o estudo, a determinação do REV das amostras tem como objetivo obter um volume que seja estatisticamente representativo o bastante para fins de simulação numérica em escala de poros.
> **Saiba mais sobre o estudo aqui:** [PEREIRA_F_P_2018_REV.pdf](https://github.com/nrmagalhaes1/analise-rev/files/10676954/PEREIRA_F_P_2018_REV.pdf) ; [Resumo_expandido_AM.pdf](https://github.com/nrmagalhaes1/analise-rev/files/10676967/Resumo_expandido_AM.pdf)

# 🛠️ Funcionalidades

- `Funcionalidade 1`: subdivisão da amostra
- `Funcionalidade 1a`: aplicar método das três partições em cada eixo ortogonal
- `Funcionalidade 1b`: aplicar método do fracionamento em X e Z.
- `Funcionalidade 2`: Análise Estatística dos Dados entre PHIxVolume
- `Funcionalidade 2a`: Regressão linear e polinomial a partir do gráfico plotado

# 🛠️ Abrir e rodar o projeto

**Para rodar esse projeto em sua máquina é nescessário que você esteja ultilizando o SO windows, Python e tenha instalado as seguintes bibliotecas:**

```
python -m pip install webbrowser
python -m pip install tkinter
python -m pip install openpyxl
python -m pip install shutil
python -m pip install matplotlib
python -m pip install numpy
python -m pip install scikit-learn
```

**Rode o arquivo interface.py, nele você precisará gerar as repartições das amostras (Gerar Subvolumes > Inserir valores dos eixos > Gerar)**

![interface](https://user-images.githubusercontent.com/102970648/217296265-847d255e-6244-4d9d-bdcd-f87f7df99a01.png) ![gerar](https://user-images.githubusercontent.com/102970648/217296141-520a57d0-126c-4361-bc95-ed1c32ae00ec.png)

**Volte a interface e plote o gráfico, selecionando o arquivo Excel preenchido com os valores de PHi e Volume :**
![2](https://user-images.githubusercontent.com/102970648/217297392-00c8a78a-9893-4681-a328-8220d5fb7136.png)

![pastas](https://user-images.githubusercontent.com/102970648/220923190-cb81acf4-7f75-45ea-b22f-e5f5e8d71fa0.png)


## ✔️ Técnicas e tecnologias utilizadas

- ``Python 3``

## 📁 Acesso ao projeto
Você pode acessar os arquivos do projeto clicando [aqui](https://github.com/nrmagalhaes1/analise-rev).
