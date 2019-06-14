
'''Algoritmo que implementa o Método Numérico de Runge-Kutta-Gill na equação diferencial que modela 
    um problema econômico de juros compostos sem depositos/saques regulares.
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

# Problema 2-2:
# JUROS COMPOSTOS - SEM DEPOSITOS/SAQUES

#constantes de runge-kutta gill
a = (math.sqrt(2) - 1)/2
b = (2 - math.sqrt(2))/2
c = (-1*math.sqrt(2))/2
d = (math.sqrt(2) + 2)/2

def metodo_runge_kutta_gill(f_antes, h, edo_antes, edo_meio_1, edo_meio_2, edo_agora):
    return f_antes + (edo_antes + edo_agora)/6 + (b*edo_meio_1 + d*edo_meio_2)/3

def edo(S):
    return 0.08*S

def abrir_arquivo():
    arquivo = open("../Dados/Problema2-2-Método-Runge-Kutta-Gill.txt", "w")
    arquivo.write("iteração \t Eixo x \t Eixo y \n")
    return arquivo

def plotar_grafico(coordenadas_x, coordenadas_y):
    plt.plot(coordenadas_x, coordenadas_y)
    plt.grid(True)
    plt.title('JUROS COMPOSTOS-DEPOSITOS/SAQUES REGULARES')
    plt.xlabel('Tempo')
    plt.ylabel('Rendimento')
    plt.savefig('../Gráficos/Problema-2-2-Runge-Kutta-Gill.png', format='png', dpi=300)
    plt.show()

def main():
    #Condições Iniciais
    S = 1000
    x = 0
    h = 1
    coordenadas_x = []
    coordenadas_y = []
    count = 0

#Abrir arquivo
    arquivo = abrir_arquivo()

#Limite de execução definido para quando a edo se aproximar de 0
    while(x <= 100):
        count += 1

#Escrever coordenadas no arquivo:
        arquivo.write("%-8s \t %-8s \t %-8s \n" % (str(count), str(x), str(S)))

#Salvar coordenadas em array
        coordenadas_x.append(x)
        coordenadas_y.append(S)

#Derivadas
        k1 = h * edo(S)
        k2 = h * edo(S + (k1/2))
        k3 = h * edo(S + a*k1 + b*k2)
        k4 = h * edo(S + c*k2 + d*k3)

        #Atualizações
        S = metodo_runge_kutta_gill(S, h, k1, k2, k3, k4)
        x = x + h

    #Retornar as coordenadas 
    return [coordenadas_x, coordenadas_y]
    #Para plotar o gráfico, descomente a linha abaixo e comente a linha acima
    #plotar_grafico(coordenadas_x, coordenadas_y)

main()
