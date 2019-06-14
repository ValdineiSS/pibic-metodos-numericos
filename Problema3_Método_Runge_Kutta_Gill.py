
'''Algoritmo que implementa o Método Numérico de Runge-Kutta-Gill na equação diferencial que modela 
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

# Problema 1:
# MISTURAS

#constantes de runge-kutta gill
a = (math.sqrt(2) - 1)/2
b = (2 - math.sqrt(2))/2
c = (-1*math.sqrt(2))/2
d = (math.sqrt(2) + 2)/2

def metodo_runge_kutta_gill(f_antes, h, edo_antes, edo_meio_1, edo_meio_2, edo_agora):
    return f_antes + (edo_antes + edo_agora)/6 + (b*edo_meio_1 + d*edo_meio_2)/3

def edo(Q, t):
    return (10 + 5*math.sin(2*t)) - (Q/2)

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
    #Condições Iniciais
    Q = 0
    t = 0
    h = 0.1 #Verificação empírica
    coordenadas_x = []
    coordenadas_y = []
    count = 0

#Abrir arquivo
    arquivo = abrir_arquivo()

#Limite de execução definido para quando a edo se aproximar de 0
    while(t <= 20):
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

    #Retornar as coordenadas 
    return [coordenadas_x, coordenadas_y]
    #Para plotar o gráfico, descomente a linha abaixo e comente a linha acima
    #plotar_grafico(coordenadas_x, coordenadas_y)

main()
