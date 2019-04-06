import numpy as np
import random, os, sys
sys.path.append('../utils')
import plot as plt
import wav

# h(t) parameters
b = 0.8
tau = 0.0005
# x(t) parameters
a1 = 0.5
a2 = 0.3
a3 = 0.2
fb = 600
f1 = 2 * fb
f2 = 4 * fb
f3 = 6 * fb
# z(t) parameters
A = 2.0
T = 1.0/ 1200           # T < 1/fb

def main():
	if not os.path.exists("../img"):
		os.mkdir( "../img", 0755 );
	fs = 44100 # in Hz
	length = 0.01 # in seconds
	t =  np.linspace(0, length, num=length*fs)
	h_function = lambda t : b*np.exp(-t/tau)
	h = h_function(t)
	plt.plot(h, t, fs, 3, "h(t)", "Signal h(t)")
	plt.savefig("../img/4.1-transfer_function.png")

	x_function = lambda t : a1*np.cos(2*np.pi*f1*t) + a2*np.sin(2*np.pi*f2*t) + a3*np.cos(2*np.pi*f3*t)
	x = x_function(t)
	plt.plot(x, t, fs, 10, "x(t)", "Signal x(t)")
	yx = np.convolve(h, x)
	plt.plot(np.array([x, yx[0:len(t)]]), t, fs, 10, "yx(t)", "Signal yx(t)")
	plt.savefig("../img/4.2-sines.png")

	z_function = lambda t : A * (abs((t - T/2)/T) < 1.0)
	z = z_function(t)
	yz = np.convolve(h, z)
	plt.plot(np.array([z, yz[0:len(t)]]), t, fs, 10, "yz(t)", "Signal yz(t)")
	plt.savefig("../img/4.3-rect.png")

	w, tw, rate, size, max = wav.readWav("../3-audio/af2.wav")
	h = h_function(tw) # new sample rate and time vector
	yw = np.convolve(h, w)
	plt.plot(np.array([w, yw[0:len(tw)]]), tw, rate, 10, "yw(t)", "Signal yw(t)")
	rel_max = np.amax(yw) if np.amax(yw) > abs(np.amin(yw)) else abs(np.amin(yw))
	yw = yw * (max/rel_max)
	wav.write("convoluted.wav", rate, yw.astype(np.dtype('i2')))
	plt.savefig("../img/4.4-audio.png")

if __name__ == '__main__':
    main()
