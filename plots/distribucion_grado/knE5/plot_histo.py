# Sacado de https://scipy.github.io/old-wiki/pages/Cookbook/Matplotlib/LaTeX_Examples.html
'''
Grafica histogramas 
'''

import pylab
import numpy as np
import matplotlib.pyplot as plt
import math
#import numarray

# a dos columnas: 3+3/8 (ancho, in)
# a una columna : 6.5   (ancho  in)

golden_mean = (math.sqrt(5)-1.0)/2.0        # Aesthetic ratio
fig_width = 3+3/8 			    # width  in inches
fig_height = fig_width*golden_mean          # height in inches
fig_size =  [fig_width,fig_height]

params = {'backend': 'ps',
          'axes.titlesize': 8,
          'axes.labelsize': 9,
          'axes.linewidth': 0.5, 
          'axes.grid': True,
          'axes.labelweight': 'normal',  
          'font.family': 'serif',
          'font.size': 8.0,
          'font.weight': 'normal',
          'text.color': 'black',
          'xtick.labelsize': 8,
          'ytick.labelsize': 8,
          'text.usetex': True,
          'legend.fontsize': 8,
          'figure.dpi': 300,
          'figure.figsize': fig_size,
          'savefig.dpi': 300,
         }

pylab.rcParams.update(params)

########################  MAIN  ########################
def main():

	##### PARAMETERS ##### 
	density = 9
	kn = "E5"
	clase = "density{}_width22_kn{}".format(density,kn)
	distribucion = np.genfromtxt("distrib_grado_{}".format(clase),delimiter = ' ')    
	title_plot= "Corridor $w=$22~m - $k_n$={} - Density={}".format(kn,density)
	out_name = "histo_grado_{}".format(clase)
	binwidth = 0.007
	min_comp = 0.0
	max_comp = 0.17

	min_grado = 0
	max_grado = 7
	plot_histo_norm_discreta(distribucion,title_plot,out_name,min_grado,max_grado)
	#plot_histo_normalized(distribucion,title_plot,out_name,binwidth,min_comp,max_comp)




def plot_histo_ocurrence(distribucion,titulo,out_name):
     plt.figure()
     plt.hist(distribucion) # para cuando son solo cero
     pylab.grid(False)
     pylab.xlabel('compression~(m)',fontsize=10)
     pylab.ylabel('Ocurrence',fontsize=10)
     pylab.title('{}'.format(titulo),fontsize=10)
     #pylab.xlim(0, 25)
     #pylab.ylim(0, 1)
     pylab.savefig('{}.png'.format(out_name), format='png', dpi=300, bbox_inches='tight')


def plot_histo_normalized(distribucion,titulo,out_name,binwidth,min_comp,max_comp):
	plt.figure()

	weights = np.ones_like(distribucion)/float(len(distribucion))
	plt.hist(distribucion, bins=np.arange(min_comp, max_comp+binwidth, binwidth),weights=weights)
	pylab.grid(False)
	pylab.xlabel('compresion~(m)',fontsize=10)
	pylab.ylabel('Frecuency',fontsize=10)
	pylab.title('{}'.format(titulo),fontsize=10)
	#pylab.xticks(np.linspace(0,80,5))
	#pylab.xticks(np.linspace(0,3000,4))
	#pylab.xlim(-0.01, 0.155)
	#pylab.ylim(0, 0.25)
	#plt.yscale('log')
	#pylab.ylim(10**(-4), 10**(0))
	#plt.tick_params(labelsize=15)
	pylab.savefig('{}.png'.format(out_name), format='png', dpi=300, bbox_inches='tight')


def plot_histo_norm_discreta(distribucion,titulo,out_name,min_grado,max_grado):
     plt.figure()
     hist,bins = np.histogram(distribucion,np.arange(min_grado,max_grado+2,1))
     dist_normed = np.divide(hist,float(np.sum(hist)))
     plt.bar(bins[:-1], dist_normed, width=0.5,color='orange')
     pylab.grid(False)
     pylab.xlabel('Degree',fontsize=10)
     pylab.ylabel('Ocurrence',fontsize=10)
     pylab.title('{}'.format(titulo),fontsize=10)
     #pylab.xlim(0, 25)
     pylab.ylim(0, 0.75)
     pylab.xticks(np.arange(min_grado,max_grado+2,1))
     pylab.savefig('{}.png'.format(out_name), format='png', dpi=300, bbox_inches='tight')
     pylab.savefig('{}.eps'.format(out_name), format='eps', dpi=300, bbox_inches='tight')




if __name__=='__main__':
     main()
