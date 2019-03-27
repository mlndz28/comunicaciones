import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as wav
import random, os

def main():
	w, tw, rate, size, max = readWav("af2.wav")
	Ew = np.sum(np.square(w))/rate
	Pw = np.sum(np.square(w))/size
	# Get 10 random intervals and measure the power of the signal
	for i in range(10):
		interval = [random.randint(0, size)]
		interval.append(random.randint(0, size))
		interval.sort()
		Pwi = np.sum(np.square(w[interval[0]:interval[1]+1]))/(interval[1]-interval[0])
		print("Power for " + str(round(interval[0]/float(rate), 5)) + "s - " + str(round(interval[1]/float(rate),5)) + "s = " +str(round(Pwi, 5)) + "W")
	# Plot the audio signal
	plot(w, tw, Ew, Pw, rate)
	# Save the plot into an image file
	if not os.path.exists("img"):
		os.mkdir( "img", 0755 );
	plt.savefig("img/3-AudioSignal.png")
	plt.show()


def readWav(path):
	rate, w = wav.read(path)	# returns the audio's sampling rate and its data
	max = np.amax(w) if np.amax(w) > abs(np.amin(w)) else abs(np.amin(w))
	w = w/float(max) # normalized vector
	size = len(w)
	tw = np.linspace(0., 1.*size/rate, 1.*size)
	return w, tw, rate, size, max

def addSubplot(figure, x ,y ,position):
	figure.add_subplot(2, 1, position)
	plt.plot(x, y)
	plt.ylabel("w(t)")
	plt.xlabel("t/s")

def plot(w, tw, Ew, Pw, rate):
	fig = plt.figure()
	fig.subplots_adjust(hspace=0.4, wspace=0.4)
	addSubplot(fig, tw, w, 1)
	plt.suptitle("Signal w(t)")
	plt.title("Energy: " + str(round(Ew, 3)) + " W, Power: " + str(round(Pw, 3)) + " J")
	index = [np.where(abs(w) == 1.0)[0][0]]
	window = 0.05 # seconds
	index.append(index[0]+int(window*rate))
	addSubplot(fig, tw[index[0]:index[1]], w[index[0]:index[1]], 2)

if __name__ == '__main__':
    main()
