
'''Algoritmo que implementa o Método Numérico de Euler na equação diferencial que modela 
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

# Problema 4:
# VELOCIDADE DE ESCAPE

def metodo_euler(f_antes, h, edo):
	return f_antes + h * edo

def edo(V, x):
	return ((-9.8)*(6371000)**(2)) / (V*(6371000+x)**(2)) 

def abrir_arquivo():
	arquivo = open("Problema4-Método-Euler-Velocidade-Menor.txt", "w")
	arquivo.write("iteração \t Eixo x \t Eixo y \n")
	return arquivo	

def plotar_grafico(coordenadas_x, coordenadas_y):
	plt.plot(coordenadas_x, coordenadas_y)
	plt.grid(True)
	plt.title('VELOCIDADE DE ESCAPE')
	plt.xlabel('Altitute')
	plt.ylabel('Velocidade')
	plt.show()

def main():
	print('euler')
	#Condições Iniciais
	V = 11200 #Velocidade de escape
	x = 0
	h = 5
	coordenadas_x = []
	coordenadas_y = []
	count = 0

	#Abrir arquivo
	arquivo = abrir_arquivo()

	#Limite de execução definido para quando a altitude 500000
	while(x < 500000):
		count += 1
		#Escrever coordenadas no arquivo:
		arquivo.write("%-8s \t %-8s \t %-8s \n" % (str(count), str(x), str(V)))

		#Salvar coordenadas em array
		coordenadas_x.append(x)
		coordenadas_y.append(V)

		#Atualizações
		V = metodo_euler(V, h, edo(V, x))
		x = x + h

	#Retornar as coordenadas 
	return [coordenadas_x, coordenadas_y]
	#Para plotar o gráfico, descomente a linha abaixo e comente a linha acima
	#plotar_grafico(coordenadas_x, coordenadas_y)

main()
