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
data_vd2 = pd.read_csv("k_vs_vx_vd2.txt",sep="\t")
k_vd2 = data_vd2["k"].tolist()
mean_vx_vd2 = data_vd2["mean vx"].tolist()
std_vx_vd2 = data_vd2["std vx"].tolist()

data_vd4 = pd.read_csv("k_vs_vx_vd4.txt",sep="\t")
k_vd4 = data_vd4["k"].tolist()
mean_vx_vd4 = data_vd4["mean vx"].tolist()
std_vx_vd4 = data_vd4["std vx"].tolist()

data_vd6 = pd.read_csv("k_vs_vx_vd6.txt",sep="\t")
k_vd6 = data_vd6["k"].tolist()
mean_vx_vd6 = data_vd6["mean vx"].tolist()
std_vx_vd6 = data_vd6["std vx"].tolist()

data_vd8 = pd.read_csv("k_vs_vx_vd8.txt",sep="\t")
k_vd8 = data_vd8["k"].tolist()
mean_vx_vd8 = data_vd8["mean vx"].tolist()
std_vx_vd8 = data_vd8["std vx"].tolist()

###  PLOT  ###
fig, ax1 = plt.subplots()

plt.plot(k_vd2,mean_vx_vd2,'-s',color='#1f77b4',mew=0.7,markeredgecolor='k',markersize=5,zorder=1,label='$v_d=2$~m s$^{-1}$') 
plt.plot(k_vd4,mean_vx_vd4,'-^',color = '#ff7f0e',mew=0.7,markeredgecolor='k',markersize=5,zorder=3,label='$v_d=4$~m s$^{-1}$') 
plt.plot(k_vd6,mean_vx_vd6,'-x',color = 'g',mew=0.7,markeredgecolor='k',markersize=5,zorder=1,label='$v_d=6$~m s$^{-1}$') 
#plt.plot(k_vd8,mean_vx_vd8,'-rv',mew=0.7,markeredgecolor='k',markersize=4,zorder=1,label='$v_d=8$~m s$^{-1}$') 
#plt.plot(vd_knE6,mean_comp_knE6,'-ko',mew=0.7,markeredgecolor='k',markersize=4,zorder=1,label='$k=1.2$ E6') 

pylab.grid(False)
pylab.xlabel('$k_n$')
pylab.ylabel('$\\langle v_x \\rangle $')
plt.xscale('symlog')
plt.title("Bottleneck")
lgd=plt.legend(numpoints=1,handlelength=0.8) 
pylab.legend(frameon=False,loc='best',labelspacing=0.2,borderpad=0.3,handletextpad=0.5,fontsize=7,numpoints=1) 
pylab.savefig('kn_vs_vx_bottleneck.png', format='png', dpi=300, bbox_inches='tight')
pylab.savefig('kn_vs_vx_bottleneck.eps', format='eps', dpi=300, bbox_inches='tight')

