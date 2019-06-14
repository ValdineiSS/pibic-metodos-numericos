
'''Algoritmo que implementa o Método Numérico de Euler na equação diferencial que modela 
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

def metodo_euler(f_antes, h, edo):
	return f_antes + h * edo

def edo(Q, t):
	return (10 + 5*math.sin(2*t)) - (Q/2)

def abrir_arquivo():
	arquivo = open("../Dados/Problema3-Método-Euler.txt", "w")
	arquivo.write("iteração \t Eixo x \t Eixo y \n")
	return arquivo	

def plotar_grafico(coordenadas_x, coordenadas_y):
	plt.plot(coordenadas_x, coordenadas_y)
	plt.grid(True)
	plt.title('PRODUTOS QUḾICOS')
	plt.xlabel('Tempo')
	plt.ylabel('P. Químicos')
	plt.savefig('../Gráficos/Problema-3-Euler.png',format='png',dpi=300)
	plt.show()

def main():
	#Condições Iniciais
	Q = 0
	t = 0
	h = 0.1 
	coordenadas_x = []
	coordenadas_y = []
	count = 0

	#Abrir arquivo
	arquivo = abrir_arquivo()

	#Repetição enquanto o tempo for menor que 20 unidades
	while(t <= 20):
		count += 1

		#Escrever coordenadas no arquivo:
		arquivo.write("%-8s \t %-8s \t %-8s \n" % (str(count), str(t), str(Q)))

		#Salvar coordenadas em array
		coordenadas_x.append(t)
		coordenadas_y.append(Q)

		#Atualizações
		Q = metodo_euler(Q, h, edo(Q, t))
		t = t + h

	#Retornar as coordenadas 
	return [coordenadas_x, coordenadas_y]
	#Para plotar o gráfico, descomente a linha abaixo e comente a linha acima
	#plotar_grafico(coordenadas_x, coordenadas_y)

main()
