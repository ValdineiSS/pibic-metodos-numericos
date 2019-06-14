import matplotlib.pyplot as plt
import math

# Problema 4:
# VELOCIDADE DE ESCAPE

#constantes de runge-kutta gill
a = (math.sqrt(2) - 1)/2
b = (2 - math.sqrt(2))/2
c = (-1*math.sqrt(2))/2
d = (math.sqrt(2) + 2)/2

def metodo_runge_kutta_gill(f_antes, h, edo_antes, edo_meio_1, edo_meio_2, edo_agora):
    return f_antes + (edo_antes + edo_agora)/6 + (b*edo_meio_1 + d*edo_meio_2)/3

def edo(V, x):
    return ((-9.8)*(6371000)**(2)) / (V*(6371000+x)**(2))

def abrir_arquivo():
    arquivo = open("../Dados/Problema3-Método-Runge-Kutta-Gill.txt", "w")
    arquivo.write("iteração \t Eixo x \t Eixo y \n")
    return arquivo  

def plotar_grafico(coordenadas_x, coordenadas_y):
    plt.plot(coordenadas_x, coordenadas_y)
    plt.grid(True)
    plt.title('PRODUTOS QUḾICOS')
    plt.xlabel('Tempo')
    plt.ylabel('P. Químicos')
    plt.savefig('../Gráficos/Problema-3-Runge-Kutta-Gill.png',format='png',dpi=300)
    plt.show()

def main():
    print('gill')
    #Condições Iniciais
    Q = 11200
    t = 0
    h = 5 #Verificação empírica
    coordenadas_x = []
    coordenadas_y = []
    count = 0

#Abrir arquivo
    arquivo = abrir_arquivo()

#Limite de execução definido para quando a edo se aproximar de 0
    while(t < 500000):
        count += 1

#Escrever coordenadas no arquivo:
        arquivo.write("%-8s \t %-8s \t %-8s \n" % (str(count), str(t), str(Q)))

#Salvar coordenadas em array
        coordenadas_x.append(t)
        coordenadas_y.append(Q)

#Derivadas
        k1 = h * edo(Q, t)
        k2 = h * edo(Q + (k1/2), t)
        k3 = h * edo(Q + a*k1 + b*k2, t)
        k4 = h * edo(Q + c*k2 + d*k3, t)

        #Atualizações
        Q = metodo_runge_kutta_gill(Q, h, k1, k2, k3, k4)
        t = t + h

#Mostrar gráfico
    return (coordenadas_x, coordenadas_y)
