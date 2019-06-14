
'''Algoritmo que implementa o Método Numérico de Runge-Kutta-Fehberg 54 na equação diferencial que modela 
    um problema de produtos químicos em um açude.
    Copyright (C) 2019  Valdinei da Silva Santos

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation version 3 of the License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

import matplotlib.pyplot as plt
import math

# Problema 3:
# PRODUTOS QUÍMICOS

def metodo_runge_kutta_4_ordem(yk, k1, k3, k4, k5):
    return yk + (25/216)*k1 + (1408/2565)*k3 + (2197/4104)*k4 - (1/5)*k5

def metodo_runge_kutta_5_ordem(yk, k1, k3, k4, k5, k6):
    return yk + (16/135)*k1 + (6656/12825)*k3 + (28561/56430)*k4 - (9/50)*k5 + (2/55)*k6

def edo(Q, t):
    return (10 + 5*math.sin(2*t)) - (Q/2)

def abrir_arquivo():
    arquivo = open("../Dados/Problema3-Método-Runge-Kutta-Fehlberg-54.txt", "w")
    arquivo.write("{:<30} {:<30} {:<30} {:<30}\n".format("iteração", "Eixo x", "Eixo y", "Passo"))
    return arquivo

def plotar_grafico(coordenadas_x, coordenadas_y):
    plt.plot(coordenadas_x, coordenadas_y)
    plt.grid(True)
    plt.title('PRODUTOS QUḾICOS')
    plt.xlabel('Tempo')
    plt.ylabel('P. Químicos')
    plt.savefig('../Gráficos/Problema-3-Runge-Kutta-Fehlberg-54.png',format='png',dpi=300)
    plt.show()

def main():
    #Condições Iniciais
    Q = 0
    t = 0
    h = 0.1 #Verificação empírica
    coordenadas_x = []
    coordenadas_y = []
    count = 0
    epsilon = 10**(-8) #Verificação empírica
    ultimaIteracao = False

#Abrir arquivo
    arquivo = abrir_arquivo()

#Limite de execução definido para quando x <= 295
    while(t <= 20):
        count += 1
        #pra não ultrapassar
        if 20 - t > 0:
            h = min(h, 20 - t)
        else:
            ultimaIteracao = True
#Escrever coordenadas no arquivo:
        arquivo.write("{: <30} {: <30} {: <30} {: <30} \n".format(str(count), str(t), str(Q), str(h)))

#Salvar coordenadas em array
        coordenadas_x.append(t)
        coordenadas_y.append(Q)

#Derivadas
        k1 = h * edo(Q, t)
        k2 = h * edo(Q + (k1/4), t)
        k3 = h * edo(Q + (3/32)*k1 + (9/32)*k2, t)
        k4 = h * edo(Q + (1932/2197)*k1 - (7200/2197)*k2 + (7296/2197)*k3, t)
        k5 = h * edo(Q + (439/216)*k1 - (8)*k2 + (3680/513)*k3 - (845/4104)*k4, t)
        k6 = h * edo(Q - (8/27)*k1 + (2)*k2 - (3544/2565)*k3 + (1859/4104)*k4 - (11/40)*k5, t)

        #Atualizações
        Q_4_ordem = metodo_runge_kutta_4_ordem(Q, k1, k3, k4, k5)
        Q_5_ordem = metodo_runge_kutta_5_ordem(Q, k1, k3, k4, k5, k6)

        #Erro obtido
        R = abs(Q_5_ordem - Q_4_ordem)/h

        if R == 0:
            delta = 1
        else:
            delta = 0.84*(epsilon/R)**(1/4)

        if R <= epsilon:
            t = t + h
            Q = Q_5_ordem
            h = delta*h
        else:
            h = delta*h

        if ultimaIteracao == True:
            break


    #Retornar as coordenadas 
    return [coordenadas_x, coordenadas_y]
    #Para plotar o gráfico, descomente a linha abaixo e comente a linha acima
    #plotar_grafico(coordenadas_x, coordenadas_y)

main()
