# Bibliotecas
import matplotlib.pyplot as plt
import numpy as np
import math, os

# Frecuencia base (centro geometrico)
f_b = 600               # frecuencia base en Hz
F_s = 4 * 16 * f_b      # frecuencia de muestreo
N = 128                  # vector size

#intervalo de tiempo de la gráfica
t = np.linspace(0.0, ((N-1) / F_s) , num = N)

# Frecuencias derivadas
f_1 = 2 * f_b
f_2 = 4 * f_b
f_3 = 6 * f_b

# Amplitudes menores a 1.0
A_1 = 0.5
A_2 = 0.3
A_3 = 0.2

# valor del parametro T_b , Tb
Tb = 1.0/300

# Expresion de x(t), funcion para generar vector de muestras.
def x(t):
    x_t =   A_1 * np.cos(2 * np.pi * f_1 * t)           \
            + A_2 * np.sin(2 * np.pi * f_2 * t)         \
            + A_3 * np.cos(2* np.pi * f_3 * t)
    return x_t

# Determina potencia promedio de x, Px
def Power(N):
    energ = Energy(N)
    Px = (1.0/N) * energ
    return Px

def Energy(N):
    counter = 0.0
    for k in range(0,N):
        counter += np.absolute ((x(k/F_s))**2)
    return counter

# Determina N_T
def N_b(T):
    N_T = T * F_s
    return N_T

def main():


    # Plotting del grafico
    plt.plot(t, x(t), 'b')
    plt.title('Señal x(t)')
    plt.ylabel("x(t)")
    plt.xlabel("t /[segundos]")

    # Guardar el grafico
    path = "../img"
    if not os.path.exists("../img"):
    	os.mkdir(path,0o777);
    plt.savefig("../img/1-SenPotencia.png")
    print ("<<<<<<<Gráfico guardado en ./img/1-SenPotencia.png>>>>>>> \n" +
            'Resultados:')

    plt.show()

    # Potencia
    print( '->Potencia promedio de x, P_x: ' + str(Power(N)) + ' W. ')
    # Energia
    print( '->Energía promedio de x, E_x: ' + str(Energy(N)) + ' J.')

    Nb = int (N_b(Tb))
    PowNb = Power(Nb)
    EnNb = Energy(Nb)

    print('->Tb = ' + str(Tb) + ' s.')
    #N_Tb
    print ('->Número de muestras para el intervalo [0,Tb]: '+ str( Nb ) )

    print('->Potencia promedio de x en el intervalo[0,Tb], PxTb = '
        + str(PowNb) + ' W. ')

    print('->Energía promedio de x en el intervalo[0,Tb], ExTb = '
        + str(EnNb) + ' J.')

    print('->Valor de  PxTb*NTb = '
        + str( PowNb *Nb) + ' J.')

    if np.around(PowNb*Nb, decimals = 2) == np.around(EnNb,decimals = 2) :
        print( '->Los resultados anteriores sí coinciden.')
    else:
        print('->Los resultados anteriores no coinciden.')

# Definicion de main
if __name__ == '__main__':
    main()
