
'''Algoritmo que implementa o Método Numérico de Euler Melhorado na equação diferencial que modela 
	a doença Encefalopatia Espongiforme Bovina (doença da Vaca Louca)
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

# Problema 0:
# EEB

def metodo_euler_melhorado(f_antes, h, edo_antes, edo_agora):
	return f_antes + h * (edo_antes + edo_agora)/2

def metodo_euler(f_antes, h, edo):
	return f_antes + h * edo

def edo(b):
	return 0.01*(1-b)*b 

def equacao_analitica(x):
	return 25 - 25*math.exp((-3/100)*x)

def abrir_arquivo():
	arquivo = open("Problema0-Método-Euler-Melhorado.txt", "w")
	arquivo.write("iteração \t Eixo x \t Eixo y\n")
	return arquivo	

def plotar_grafico(coordenadas_x, coordenadas_y):
	plt.plot(coordenadas_x, coordenadas_y)
	plt.grid(True)
	plt.title('Encefalopatia Espongiforme Bovina')
	plt.xlabel('Tempo')
	plt.ylabel('Contaminação')
	plt.show()

def main():
	#Condições Iniciais
	b = 10**(-14)
	x = 0
	h = 1
	coordenadas_x = []
	coordenadas_y = []
	erro_global_trunc = 0
	count = 0

	#Abrir arquivo
	arquivo = abrir_arquivo()

	#Limite de execução definido para quando a edo se aproximar de 0
	while(x <= 4000):
		count += 1


		#Escrever coordenadas no arquivo:
		arquivo.write("%-8s \t %-8s \t %-8s \n" % (str(count), str(x), str(b)))

		#Salvar coordenadas em array
		coordenadas_x.append(x)
		coordenadas_y.append(b)

		#Derivadas
		k1 = edo(b)
		k2 = edo(metodo_euler(b, h, edo(b)))

		#Atualizações
		b = metodo_euler_melhorado(b, h, k1, k2)
		x = x + h

	#Retornar coordenadas
	return [coordenadas_x, coordenadas_y]
	#Para plotar o gráfico, descomente a linha abaixo e comente a linha acima
	#plotar_grafico(coordenadas_x, coordenadas_y)

main()
		
