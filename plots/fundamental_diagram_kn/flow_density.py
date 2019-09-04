# Sacado de https://scipy.github.io/old-wiki/pages/Cookbook/Matplotlib/LaTeX_Examples.html

'''

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

### DATA ###
data_kn0 = np.genfromtxt("flow-density_vd1_pasillo22m_kn0.txt",delimiter = ' ') 
density_kn0 = data_kn0[:,0]
flow_kn0 = data_kn0[:,1]

data_knE4 = np.genfromtxt("flow-density_vd1_pasillo22m_knE4.txt",delimiter = ' ') 
density_knE4 = data_knE4[:,0]
flow_knE4 = data_knE4[:,1]

data_knE5 = np.genfromtxt("flow-density_vd1_pasillo22m_knE5.txt",delimiter = ' ') 
density_knE5 = data_knE5[:,0]
flow_knE5 = data_knE5[:,1]


###  PLOT  ###

fig, ax1 = plt.subplots()

#plt.plot(density_kn0,flow_kn0,'k--+',mew=0.7,markersize=4,label='width = 2m') 
plt.plot(density_kn0,flow_kn0,'b--x',mew=0.7,markersize=4,label='$k_n = 0$') 
plt.plot(density_knE4,flow_knE4,'g:^',mew=0.7,markerfacecolor='g',markersize=4,markeredgecolor='k',label='$k_n = 1.2$ E4') 
plt.plot(density_knE5,flow_knE5,'y-.o',mew=0.7,markerfacecolor='y',markeredgecolor='k',markersize=4,zorder=3,label='$k_n = 1.2$ E5') 
#plt.plot(density_22m[:len(density_22m)-1],flow_22m[:len(density_22m)-1],'-rs',mew=0.7,markerfacecolor='r',markeredgecolor='k',markersize=4,label='width = 22m') 



pylab.grid(False)
#pylab.xlabel('time~$(s)$')
pylab.xlabel('Density~(p~m$^{-2}$)')
pylab.ylabel('Flow~(p~m$^{-1}$s$^{-1}$)')
#pylab.legend()
#pylab.ylim(0.0, 3.6)
#pylab.yticks(np.arange(3,11,2))
#pylab.ylim(0, 9.5)
#pylab.xticks(np.arange(0,1100,200))
#pylab.xlim(1.0, 10)
pylab.title("Fundamental diagram - Original friction ")
lgd=plt.legend(numpoints=1,handlelength=0.8) 
plt.legend(frameon=False,loc='best',labelspacing=-0.1,borderpad=0.3,handletextpad=0.5,fontsize=6,numpoints=1) 
#pylab.savefig('flow-density_vd1_multiple_widths.eps', format='eps', dpi=300, bbox_inches='tight')

pylab.savefig('flow-density_vd1_multi_kn.png', format='png', dpi=300, bbox_inches='tight')
pylab.savefig('flow-density_vd1_multi_kn.eps', format='eps', dpi=300, bbox_inches='tight')