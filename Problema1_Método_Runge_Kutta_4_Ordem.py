
'''Algoritmo que implementa o Método Numérico de Runge-Kutta 4 na equação diferencial que modela 
	um problema químico de misturas.
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

def metodo_runge_kutta(f_antes, h, edo_antes, edo_meio_1, edo_meio_2, edo_agora):
	return f_antes + h * (edo_antes + (2*edo_meio_1) + (2*edo_meio_2) + edo_agora)/6

def edo(Q):
	return (3/4) - (3*Q)/100

def equacao_analitica(x):
	return 25 - 25*math.exp((-3/100)*x)

def abrir_arquivo():
	arquivo = open("Problema1-Método-Runge-Kutta-4-Ordem.txt", "w")
	arquivo.write("iteração \t Eixo x \t Eixo y \t Erro Global \n")
	return arquivo

def plotar_grafico(coordenadas_x, coordenadas_y):
	plt.plot(coordenadas_x, coordenadas_y)
	plt.grid(True)
	plt.title('Misturas')
	plt.xlabel('Tempo')
	plt.ylabel('Sal')
	plt.show()

def main():
	#Condições Iniciais
	Q = 0
	x = 0
	h = 1
	coordenadas_x = []
	coordenadas_y = []
	count = 0

	#Abrir arquivo
	arquivo = abrir_arquivo()

	#Limite de execução definido para quando a edo se aproximar de 0
	while(edo(Q)>0.0001):
		count += 1

		#Escrever coordenadas no arquivo:
		arquivo.write("%-8s \t %-8s \t %-8s \n" % (str(count), str(x), str(Q)))

		#Salvar coordenadas em array
		coordenadas_x.append(x)
		coordenadas_y.append(Q)

		#Derivadas
		k1 = edo(Q)
		k2 = edo(Q + (h/2)*k1)
		k3 = edo(Q + (h/2)*k2)
		k4 = edo(Q + h*k3)

		#Atualizações
		Q = metodo_runge_kutta(Q, h, k1, k2, k3, k4)
		x = x + h

	#Retornar as coordenadas 
	return [coordenadas_x, coordenadas_y]
	#Para plotar o gráfico, descomente a linha abaixo e comente a linha acima
	#plotar_grafico(coordenadas_x, coordenadas_y)

main()
		
