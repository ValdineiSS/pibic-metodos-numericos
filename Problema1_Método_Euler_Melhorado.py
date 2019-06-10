
'''Algoritmo que implementa o Método Numérico de Euler Melhorado na equação diferencial que modela 
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

def metodo_euler_melhorado(f_antes, h, edo_antes, edo_agora):
	return f_antes + h * (edo_antes + edo_agora)/2

def metodo_euler(f_antes, h, edo):
	return f_antes + h * edo

def edo(Q):
	return (3/4) - (3*Q)/100 

def equacao_analitica(x):
	return 25 - 25*math.exp((-3/100)*x)

def abrir_arquivo():
	arquivo = open("Problema1-Método-Euler-Melhorado.txt", "w")
	arquivo.write("iteração \t Eixo x \t Eixo y \t Erro Global\n")
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
	erro_global_trunc = 0
	count = 0

	#Abrir arquivo
	arquivo = abrir_arquivo()

	#Limite de execução definido para quando a edo se aproximar de 0
	while(edo(Q)>0.0001):
		count += 1

		#salvando valor analítico e o erro local de truncation
		y_analitico = equacao_analitica(x)
		erro_global_trunc += (y_analitico - Q)

		#Escrever coordenadas no arquivo:
		arquivo.write("%-8s \t %-8s \t %-8s \t %-8s \n" % (str(count), str(x), str(Q), str(erro_global_trunc)))

		#Salvar coordenadas em array
		coordenadas_x.append(x)
		coordenadas_y.append(Q)

		#Derivadas
		k1 = edo(Q)
		k2 = edo(metodo_euler(Q, h, edo(Q)))

		#Atualizações
		Q = metodo_euler_melhorado(Q, h, k1, k2)
		x = x + h

	#Retornar as coordenadas 
	return [coordenadas_x, coordenadas_y]
	#Para plotar o gráfico, descomente a linha abaixo e comente a linha acima
	#plotar_grafico(coordenadas_x, coordenadas_y)

main()
		
