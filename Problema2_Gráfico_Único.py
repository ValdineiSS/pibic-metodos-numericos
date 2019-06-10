
'''Algoritmo de plotagem de gráficos com a utilização de métodos numéricos que discretizam EDO's
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

#Importar demais códigos
import Problema2_Método_Euler as euler
import Problema2_Método_Euler_Modificado as emo
import Problema2_Método_Euler_Melhorado as eme
import Problema2_Método_Runge_Kutta_3_Ordem as rk3
import Problema2_Método_Runge_Kutta_Gill as rkg
import Problema2_Método_Runge_Kutta_4_Ordem as rk4
import Problema2_Método_Runge_Kutta_Fehlberg_45 as rkf45
import Problema2_Método_Runge_Kutta_Fehlberg_54 as rkf54

# Problema 2:
# JUROS COMPOSTOS - Com depositos/saques regulares


def main():

	#Pegando as coordenadas
	euler_x,euler_y = euler.main()
	emo_x,emo_y = emo.main()
	eme_x,eme_y = eme.main()
	rk3_x,rk3_y = rk3.main()
	rkg_x,rkg_y = rkg.main()
	rk4_x,rk4_y = rk4.main()
	rkf45_x,rkf45_y = rkf45.main()
	rkf54_x,rkf54_y = rkf54.main()

	#Plotando coordenadas
	plt.plot(euler_x, euler_y, 'k:', linewidth=1)
	plt.plot(emo_x, emo_y, linewidth=1)
	plt.plot(eme_x, eme_y, linewidth=1)
	plt.plot(rk3_x, rk3_y, linewidth=1)
	plt.plot(rkg_x, rkg_y, 'k--', linewidth=1)
	plt.plot(rk4_x, rk4_y,linewidth=1)
	plt.plot(rkf45_x, rkf45_y)
	plt.plot(rkf54_x, rkf54_y)


	#Legenda
	plt.legend(['Euler', 'Euler Modificado', 'Euler Melhorado', 'RK3', 'RKG', 'RK4','RKF45','RKF54'])

	#Detalhes
	plt.grid(True)
	plt.title('Juros Compostos - Com Saques/Depositos Regulares')
	plt.xlabel('Tempo')
	plt.ylabel('Rendimento')
	plt.savefig('../Gráficos/Problema1_Gráfico_Único_Métodos_Passo_Fixo_5',format='png',dpi=600)
	plt.show()


main()
		
