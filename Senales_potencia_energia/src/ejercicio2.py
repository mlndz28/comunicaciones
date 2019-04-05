# Bibliotecas
import matplotlib.pyplot as plt
import numpy as np
import math, os

# Frecuencia base (centro geometrico)
f_b = 600               # frecuencia base en Hz
F_s = 4 * 16 * f_b      # frecuencia de muestreo
N = 128                 # vector size

# Valores definidos para A y T
A = 2.0
T = 1.0/ 1200           # T < 1/fb

# Intervalo de tiempo de la gráfica
t = np.linspace(-0.00001, ((N-1) / F_s) , num = N)

# Funcion Rect: Pendiente definir como comparar
def rect(t):
    # ternario
    return np.where(abs(t) < 0.5, 1, \
             (np.where(abs(t) > 0.5, 0, 0.5)))

#Funcion z(t)
def z(t):
    z_t = A * rect( (t - T/2)/T )
    return z_t

def main():

    # Plotting del grafico
    plt.plot(t, z(t), 'b')
    plt.title('Señal z(t)')
    plt.ylabel("z(t)")
    plt.xlabel("t /[segundos]")

    # Guardar el grafico
    path = "../img"
    if not os.path.exists("../img"):
    	os.mkdir(path,0o777);
    plt.savefig("../img/1-SenEnergia.png")
    print ("<<<<<<<Gráfico guardado en ./img/1-SenEnergia.png>>>>>>>")

    plt.show()

# Definicion de main
if __name__ == '__main__':
    main()
