import numpy as np
import random, os, sys
sys.path.append('../utils')
import plot as plt
import wav

def main():
	w, tw, rate, size, max = wav.readWav("af2.wav")
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
	plt.plot(w, tw, rate, 10, "w(t)", "Signal w(t)", "Energy: " + str(round(Ew, 3)) + " W, Power: " + str(round(Pw, 3)) + " J")
	# Save the plot into an image file
	if not os.path.exists("img"):
		os.mkdir( "img", 0755 );
	plt.savefig("img/3-AudioSignal.png")
	plt.show()

if __name__ == '__main__':
    main()
