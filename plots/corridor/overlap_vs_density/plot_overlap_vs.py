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
data_kn0 = pd.read_csv("overlap_vs_dens_kn0.txt",sep="\t")
dens_kn0 = data_kn0["dens"].tolist()
mean_overlap_kn0 = data_kn0["list_mean_overlap"].tolist()
std_overlap_kn0 = data_kn0["list_std_overlap"].tolist()

data_knE4 = pd.read_csv("overlap_vs_dens_kn26200.txt",sep="\t")
dens_knE4 = data_knE4["dens"].tolist()
mean_overlap_knE4 = data_knE4["list_mean_overlap"].tolist()
std_overlap_knE4 = data_knE4["list_std_overlap"].tolist()

data_kn = pd.read_csv("overlap_vs_dens_knE5.txt",sep="\t")
dens_kn = data_kn["dens"].tolist()
mean_overlap_kn = data_kn["list_mean_overlap"].tolist()
std_overlap_kn = data_kn["list_std_overlap"].tolist()

data_knE6 = pd.read_csv("overlap_vs_dens_knE6.txt",sep="\t")
dens_knE6 = data_knE6["dens"].tolist()
mean_overlap_knE6 = data_knE6["list_mean_overlap"].tolist()
std_overlap_knE6 = data_knE6["list_std_overlap"].tolist()

###  PLOT  ###
fig, ax1 = plt.subplots()

plt.plot(dens_kn0,mean_overlap_kn0,'-s',color='#1f77b4',mew=0.7,markeredgecolor='k',markersize=4,zorder=3,label='$k_n=0$') 
plt.plot(dens_knE4,mean_overlap_knE4,'-^',color = '#ff7f0e',mew=0.7,markeredgecolor='k',markersize=4,zorder=3,label='$k_n=2.6$ E4') 
plt.plot(dens_kn,mean_overlap_kn,'-x',color = 'g',mew=0.7,markeredgecolor='k',markersize=4,zorder=3,label='$k_n=1.2$ E5') 
plt.plot(dens_knE6,mean_overlap_knE6,'-ko',mew=0.7,markeredgecolor='k',markersize=3,zorder=3,label='$k_n=1.2$ E6') 


pylab.grid(False)
pylab.xlabel('density~(p m$^{-2})$')
pylab.ylabel('Mean overlap~(m)')
#plt.ylim(0.0,0.1)
lgd=plt.legend(numpoints=1,handlelength=0.8) 
plt.legend(frameon=False,loc='best',labelspacing=0.2,borderpad=0.3,handletextpad=0.5,fontsize=7,numpoints=1) 
pylab.savefig('overlap_vs_dens_multi_kn.png', format='png', dpi=300, bbox_inches='tight')
pylab.savefig('overlap_vs_dens_multi_kn.eps', format='eps', dpi=300, bbox_inches='tight')

