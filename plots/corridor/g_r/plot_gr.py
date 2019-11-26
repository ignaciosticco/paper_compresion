'''
Calcula la funcion de correlacion radial g(r)
'''
import pylab
import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd

golden_mean = (math.sqrt(5)-1.0)/2.0        # Aesthetic ratio
fig_width = 3+3/8                            # width  in inches
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
          'savefig.dpi': 600,
         }

pylab.rcParams.update(params)

density = "7"
output_name_histo = "g(r)_d{}_knE5".format(density)
titulo = "Global density ={}".format(density)+" p.m$^{-2}$"

data_kn0_d7 = pd.read_csv("r_g_density{}_width22_kn0_r28x22".format(density),sep="\t")
r_kn0_d7 =  data_kn0_d7["bins"].tolist()
g_kn0_d7 =  data_kn0_d7["g"].tolist()

data_knE5_d7 = pd.read_csv("r_g_density{}_width22_knE5_r28x22".format(density),sep="\t")
r_knE5_d7 =  data_knE5_d7["bins"].tolist()
g_knE5_d7 =  data_knE5_d7["g"].tolist()


#plt.plot(r_kn0_d7, g_kn0_d7, '-r',lw=1,label="$k_n=$0")
plt.plot(r_knE5_d7, g_knE5_d7, '-b',lw=1,label="$k_n=$1.2 E5")

pylab.grid(False)
pylab.xlabel('$r$(m)',fontsize=10)
pylab.ylabel('$g~(r)$',fontsize=10)
pylab.title('{}'.format(titulo),fontsize=10)
pylab.xlim(0.0, 2)
pylab.ylim(-0.1, 12)
lgd=plt.legend(numpoints=1,handlelength=0.8) 
plt.legend(frameon=False,loc='best',labelspacing=-0.1,borderpad=0.3,handletextpad=0.5,fontsize=6,numpoints=1) 
pylab.savefig('{}.png'.format(output_name_histo), format='png', dpi=300, bbox_inches='tight')
pylab.savefig('{}.eps'.format(output_name_histo), format='eps', dpi=300, bbox_inches='tight')