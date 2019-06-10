
'''Algoritmo que implementa o Método Numérico de Euler Modificado na equação diferencial que modela 
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

# Problema 2:
# JUROS COMPOSTOS - Com depositos/saques regulares

def metodo_euler_modificado(f_antes, h, k2):
	return f_antes + h * k2

def metodo_euler(f_antes, h, edo):
	return f_antes + h * edo

def edo(S):
	return 0.08*S + 1000

def abrir_arquivo():
	arquivo = open("../Dados/Problema2-Método-Euler-Modificado.txt", "w")
	arquivo.write("iteração \t Eixo x \t Eixo y \n")
	return arquivo

def plotar_grafico(coordenadas_x, coordenadas_y):
	plt.plot(coordenadas_x, coordenadas_y)
	plt.grid(True)
	plt.title('JUROS COMPOSTOS-DEPOSITOS/SAQUES REGULARES')
	plt.xlabel('Tempo')
	plt.ylabel('Rendimento')
	plt.savefig('../Gráficos/Problema-2-Euler-Modificado.png', format='png', dpi=300)
	plt.show()


def main():
	#Condições Iniciais
	S = 1000
	x = 0
	h = 5
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
		k1 = edo(S)
		k2 = edo(metodo_euler(S, h, (1/2)*edo(S)))

		#Atualizações
		S = metodo_euler_modificado(S, h, k2)
		x = x + h

	#Retornar as coordenadas 
	return [coordenadas_x, coordenadas_y]
	#Para plotar o gráfico, descomente a linha abaixo e comente a linha acima
	#plotar_grafico(coordenadas_x, coordenadas_y)

main()
