import pylab
import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd
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

###  DATA  ###
data_kn0 = pd.read_csv("degree_vs_vd_kn0.txt",sep="\t")
vd_kn0 = data_kn0["vd"].tolist()
mean_comp_kn0 = data_kn0["list_mean_degree"].tolist()
std_comp_kn0 = data_kn0["list_std_degree"].tolist()

data_kn = pd.read_csv("degree_vs_vd_kn120000.txt",sep="\t")
vd_kn = data_kn["vd"].tolist()
mean_comp_kn = data_kn["list_mean_degree"].tolist()
std_comp_kn = data_kn["list_std_degree"].tolist()

###  PLOT  ###
fig, ax1 = plt.subplots()

plt.plot(vd_kn0,mean_comp_kn0,'-cs',mew=0.7,markeredgecolor='k',markersize=4,zorder=3,label='$k=0$') 
plt.plot(vd_kn,mean_comp_kn,'-bx',mew=0.7,markeredgecolor='k',markersize=4,zorder=3,label='$k=1.2$ E5') 


pylab.grid(False)
pylab.xlabel('$v_d$~(m~s$^{-1})$')
pylab.ylabel('Mean degree')
#plt.ylim(-0.1,6.1)
lgd=plt.legend(numpoints=1,handlelength=0.8) 
plt.legend(frameon=False,loc='best',labelspacing=0.2,borderpad=0.3,handletextpad=0.5,fontsize=7,numpoints=1) 
pylab.savefig('degree_vs_vd_multi_kn.png', format='png', dpi=300, bbox_inches='tight')
pylab.savefig('degree_vs_vd_multi_kn.eps', format='eps', dpi=300, bbox_inches='tight')

