
'''Algoritmo que implementa o Método Numérico de Euler Modificado na equação diferencial que modela 
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

def metodo_euler_modificado(f_antes, h, k2):
	return f_antes + h * k2

def metodo_euler(f_antes, h, edo):
	return f_antes + h * edo

def edo(V, x):
	return ((-9.8)*(6371000)**(2)) / (V*(6371000+x)**(2)) 

def abrir_arquivo():
	arquivo = open("../Dados/Problema4-Método-Euler-Modificado.txt", "w")
	arquivo.write("iteração \t Eixo x \t Eixo y \n")
	return arquivo	

def plotar_grafico(coordenadas_x, coordenadas_y):
	plt.plot(coordenadas_x, coordenadas_y)
	plt.grid(True)
	plt.title('PRODUTOS QUḾICOS')
	plt.xlabel('Tempo')
	plt.ylabel('P. Químicos')
	plt.savefig('../Gráficos/Problema-4-Euler-Modificado.png',format='png',dpi=300)
	plt.show()

def main():
	print('modificado')
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
		k1 = edo(Q, t)
		k2 = edo(metodo_euler(Q, h, (1/2)*edo(Q, t)), t)

		#Atualizações
		Q = metodo_euler_modificado(Q, h, k2)
		t = t + h

	#Retornar as coordenadas 
	return [coordenadas_x, coordenadas_y]
	#Para plotar o gráfico, descomente a linha abaixo e comente a linha acima
	#plotar_grafico(coordenadas_x, coordenadas_y)

main()
