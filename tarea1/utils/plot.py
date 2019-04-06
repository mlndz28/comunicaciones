import matplotlib.pyplot as plt
import numpy as np

def plot(y_arr, x, rate, h_zoom, y_label, title, subtitle=''):
	''' Draws a signal (or several on top of each other) on a grid that
	 	also shows a window with the zoomed signal.
		Args:
			y_arr: an array with signals, it can also be a single signal.
			x: vector on which y is plotted against
			rate: sampling rate
			h_zoom: amount of magnification for the second view
			y_label: name to display on the vertical axis
			title: text displayed on the title of the plot
			subtitle: text displayed below the title
	'''

	if(y_arr.ndim == 1): # if multiple signals are not used
		y_arr = [y_arr]
	fig = plt.figure()
	fig.subplots_adjust(hspace=0.4, wspace=0.4)
	addSubplot(fig, x, y_arr, 1, y_label)
	plt.title(subtitle)
	plt.suptitle(title)
	zoomed = []
	index = [np.where(y_arr[0] == np.max(y_arr[0]))[0][0]]
	window = int(len(x)/h_zoom) # number of samples
	for y in y_arr:
		index.append(index[0]+window)
		zoomed.append(y[index[0]:index[1]])
	addSubplot(fig, x[index[0]:index[1]], zoomed, 2, y_label)

def addSubplot(figure, x ,y_arr ,position, y_label):
	''' Draws each of the charts on the main frame.
	 	Module for the main function "plot"
	'''
	figure.add_subplot(2, 1, position)
	for y in y_arr:
		plt.plot(x, y)
	plt.ylabel(y_label)
	plt.xlabel("t/s")

show = plt.show
savefig = plt.savefig
title = plt.title
