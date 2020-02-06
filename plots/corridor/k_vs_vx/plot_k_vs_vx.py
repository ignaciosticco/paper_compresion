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

data_d5_5 = pd.read_csv("k_vs_vx_d5.5.txt",sep="\t")
k_d5_5 = data_d5_5["k"].tolist()
mean_vx_d5_5 = data_d5_5["mean vx"].tolist()
std_vx_d5_5 = data_d5_5["std vx"].tolist()

data_d6 = pd.read_csv("k_vs_vx_d6.txt",sep="\t")
k_d6 = data_d6["k"].tolist()
mean_vx_d6 = data_d6["mean vx"].tolist()
std_vx_d6 = data_d6["std vx"].tolist()
'''
data_d7 = pd.read_csv("k_vs_vx_d7.txt",sep="\t")
k_d7 = data_d7["k"].tolist()
mean_vx_d7 = data_d7["mean vx"].tolist()
std_vx_d7 = data_d7["std vx"].tolist()
'''
data_d8 = pd.read_csv("k_vs_vx_d8.txt",sep="\t")
k_d8 = data_d8["k"].tolist()
mean_vx_d8 = data_d8["mean vx"].tolist()
std_vx_d8 = data_d8["std vx"].tolist()

###  PLOT  ###
fig, ax1 = plt.subplots()

plt.plot(k_d5_5,mean_vx_d5_5,'-s',color='#1f77b4',mew=0.7,markeredgecolor='k',markersize=5,zorder=1,label='$\\rho=5.5$')
plt.plot(k_d6,mean_vx_d6,'-^',color = '#ff7f0e',mew=0.7,markeredgecolor='k',markersize=5,zorder=1,label='$\\rho=6$') 
#plt.plot(k_d7,mean_vx_d7,'-cs',mew=0.7,markeredgecolor='k',markersize=4,zorder=3,label='$d=7$') 
plt.plot(k_d8,mean_vx_d8,'-x',color = 'g',mew=0.7,markeredgecolor='k',markersize=5,zorder=1,label='$\\rho=8$') 
#plt.plot(vd_knE6,mean_comp_knE6,'-ko',mew=0.7,markeredgecolor='k',markersize=4,zorder=1,label='$k=1.2$ E6') 

pylab.grid(False)
pylab.xlabel('$k_n$')
pylab.ylabel('$\\langle v_x \\rangle $')
plt.xscale('symlog')
plt.title("Corridor")
lgd=plt.legend(numpoints=1,handlelength=0.8) 
pylab.legend(frameon=False,loc='best',labelspacing=0.2,borderpad=0.3,handletextpad=0.5,fontsize=7,numpoints=1) 
pylab.savefig('kn_vs_vx_corridor.png', format='png', dpi=300, bbox_inches='tight')
pylab.savefig('kn_vs_vx_corridor.eps', format='eps', dpi=300, bbox_inches='tight')

