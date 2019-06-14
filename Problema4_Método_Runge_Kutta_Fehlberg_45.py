
'''Algoritmo que implementa o Método Numérico de Runge-Kutta-Fehlberg 45 na equação diferencial que modela 
    um problema de velocidade de escape.
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

# Problema 4:
# VELOCIDADE DE ESCAPE

def metodo_runge_kutta_4_ordem(yk, k1, k3, k4, k5):
    return yk + (25/216)*k1 + (1408/2565)*k3 + (2197/4104)*k4 - (1/5)*k5

def metodo_runge_kutta_5_ordem(yk, k1, k3, k4, k5, k6):
    return yk + (16/135)*k1 + (6656/12825)*k3 + (28561/56430)*k4 - (9/50)*k5 + (2/55)*k6

def edo(V, x):
    return ((-9.8)*(6371000)**(2)) / (V*(6371000+x)**(2)) 

def abrir_arquivo():
    arquivo = open("../Dados/Problema4-Método-Runge-Kutta-Fehlberg-45.txt", "w")
    arquivo.write("{:<30} {:<30} {:<30} {:<30}\n".format("iteração", "Eixo x", "Eixo y", "Passo"))
    return arquivo

def plotar_grafico(coordenadas_x, coordenadas_y):
    plt.plot(coordenadas_x, coordenadas_y)
    plt.grid(True)
    plt.title('VELOCIDADE DE ESCAPE')
    plt.xlabel('Altitute')
    plt.ylabel('Velocidade')
    plt.savefig('../Gráficos/Problema-4-Runge-Kutta-Fehlberg-45.png', format='png', dpi=300)
    plt.show()

def main():

    #Condições Iniciais
    V = 11200
    x = 0
    h = h_init =  1
    coordenadas_x = []
    coordenadas_y = []
    count = 0

    epsilon = 10**(-5)
    ultimaIteracao = False

    coordenadas_x = []
    coordenadas_y = []

#Abrir arquivo
    arquivo = abrir_arquivo()

#Limite de execução definido para quando a edo se aproximar de 0
    while(x <= 500000):
        print(x)
        print(count)
        print(h)
        count += 1
        #pra não ultrapassar
        if 500000 - x > 0:
            h = min(h, 500000 - x)
        else:
            ultimaIteracao = True

#Escrever coordenadas no arquivo:
        arquivo.write("{: <30} {: <30} {: <30} {: <30} \n".format(str(count), str(x), str(V), str(h)))

#Salvar coordenadas em array
        coordenadas_x.append(x)
        coordenadas_y.append(V)

#Derivadas
        k1 = h * edo(V, x)
        k2 = h * edo(V + (k1/4), x)
        k3 = h * edo(V + (3/32)*k1 + (9/32)*k2, x)
        k4 = h * edo(V + (1932/2197)*k1 - (7200/2197)*k2 + (7296/2197)*k3, x)
        k5 = h * edo(V + (439/216)*k1 - (8)*k2 + (3680/513)*k3 - (845/4104)*k4, x)
        k6 = h * edo(V - (8/27)*k1 + (2)*k2 - (3544/2565)*k3 + (1859/4104)*k4 - (11/40)*k5, x)

        #Atualizações
        V_4_ordem = metodo_runge_kutta_4_ordem(V, k1, k3, k4, k5)
        V_5_ordem = metodo_runge_kutta_5_ordem(V, k1, k3, k4, k5, k6)

        #Erro obtido
        R = abs(V_5_ordem - V_4_ordem)/h

        if R == 0:
            delta = 1
        else:
            delta = 0.84*(epsilon/R)**(1/4)

        if R <= epsilon:
            x = x + h
            V = V_4_ordem
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
