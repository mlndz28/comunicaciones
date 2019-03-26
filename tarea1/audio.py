import matplotlib.pyplot as plt
import numpy as np
import scipy.io.wavfile as wav
import random, os
rate, w = wav.read("af2.wav")	# returns the audio's sampling rate and its data
max = np.amax(w) if np.amax(w) > abs(np.amin(w)) else abs(np.amin(w))
w = w/float(max) # normalized vector
size = len(w)
tw = np.linspace(0., 1.*size/rate, 1.*size)
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
plt.title("Energy: " + str(round(Ew, 3)) + " W, Power: " + str(round(Pw, 3)) + " J")
plt.plot(tw, w)	#plot time against amplitude
plt.ylabel("w(t)")
plt.xlabel("t/s")
plt.suptitle("Signal w(t)")
if not os.path.exists("img"):
	os.mkdir( "img", 0755 );
plt.savefig("img/3-AudioSignal.png")
plt.show()
