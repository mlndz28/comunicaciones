import scipy.io.wavfile as spwav
import numpy as np

def readWav(path):
	rate, w = spwav.read(path)	# returns the audio's sampling rate and its data
	max = np.amax(w) if np.amax(w) > abs(np.amin(w)) else abs(np.amin(w))
	w = w/float(max) # normalized vector
	size = len(w)
	tw = np.linspace(0., 1.*size/rate, 1.*size)
	return w, tw, rate, size, max

write = spwav.write
