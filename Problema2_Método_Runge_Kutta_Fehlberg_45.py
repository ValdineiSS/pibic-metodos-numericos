
'''Algoritmo que implementa o Método Numérico de Runge-Kutta-Fehlberg 45 na equação diferencial que modela 
    um problema econômico de juros compostos com depositos/saques regulares.
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

# Problema 2:
# JUROS COMPOSTOS - Com depositos/saques regulares

def metodo_runge_kutta_4_ordem(yk, k1, k3, k4, k5):
    return yk + (25/216)*k1 + (1408/2565)*k3 + (2197/4104)*k4 - (1/5)*k5

def metodo_runge_kutta_5_ordem(yk, k1, k3, k4, k5, k6):
    return yk + (16/135)*k1 + (6656/12825)*k3 + (28561/56430)*k4 - (9/50)*k5 + (2/55)*k6

def edo(S):
    return 0.08*S + 1000

def abrir_arquivo():
    arquivo = open("../Dados/Problema2-Método-Runge-Kutta-Fehlberg-45.txt", "w")
    arquivo.write("{:<30} {:<30} {:<30} {:<30}\n".format("iteração", "Eixo x", "Eixo y", "Passo"))
    return arquivo

def plotar_grafico(coordenadas_x, coordenadas_y):
    plt.plot(coordenadas_x, coordenadas_y)
    plt.grid(True)
    plt.title('JUROS COMPOSTOS-DEPOSITOS/SAQUES REGULARES')
    plt.xlabel('Tempo')
    plt.ylabel('Rendimento')
    plt.savefig('../Gráficos/Problema-2-Runge-Kutta-Fehlberg-45.png', format='png', dpi=300)
    plt.show()

def main():
    #Condições Iniciais
    S = 1000
    x = 0
    h = 0.5
    coordenadas_x = []
    coordenadas_y = []
    count = 0
    ultimaIteracao = False
    epsilon = 10**(-1) #Verificação empírica



#Abrir arquivo
    arquivo = abrir_arquivo()

#Limite de execução definido para quando x <= 295
    while(x <= 100):
        count += 1
        #pra não ultrapassar
        if 100 - x > 0:
            h = min(h, 100 - x)
        else:
            ultimaIteracao = True
#Escrever coordenadas no arquivo:
        arquivo.write("{: <30} {: <30} {: <30} {: <30} \n".format(str(count), str(x), str(S), str(h)))

#Salvar coordenadas em array
        coordenadas_x.append(x)
        coordenadas_y.append(S)

#Derivadas
        k1 = h * edo(S)
        k2 = h * edo(S + (k1/4))
        k3 = h * edo(S + (3/32)*k1 + (9/32)*k2)
        k4 = h * edo(S + (1932/2197)*k1 - (7200/2197)*k2 + (7296/2197)*k3)
        k5 = h * edo(S + (439/216)*k1 - (8)*k2 + (3680/513)*k3 - (845/4104)*k4)
        k6 = h * edo(S - (8/27)*k1 + (2)*k2 - (3544/2565)*k3 + (1859/4104)*k4 - (11/40)*k5)

        #Atualizações
        S_4_ordem = metodo_runge_kutta_4_ordem(S, k1, k3, k4, k5)
        S_5_ordem = metodo_runge_kutta_5_ordem(S, k1, k3, k4, k5, k6)

        #Erro obtido
        R = abs(S_5_ordem - S_4_ordem)/h

        if R == 0:
            delta = 1
        else:
            delta = 0.84*(epsilon/R)**(1/4)

        if R <= epsilon:
            x = x + h
            S = S_4_ordem
            h = delta*h
        else:
            print('Erro Maior que o Tolerado!')
            h = delta*h

        if ultimaIteracao == True:
            break


    #Retornar as coordenadas 
    return [coordenadas_x, coordenadas_y]
    #Para plotar o gráfico, descomente a linha abaixo e comente a linha acima
    #plotar_grafico(coordenadas_x, coordenadas_y)

main()
