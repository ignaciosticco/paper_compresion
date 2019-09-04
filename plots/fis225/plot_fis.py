# Sacado de https://scipy.github.io/old-wiki/pages/Cookbook/Matplotlib/LaTeX_Examples.html

'''
Grafica tiempo de evacuacion vs vd usando Pandas
'''

import pylab
import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd 

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



data_kcomp_E4 = pd.read_csv("tevsvd_N225_kcom_E4.txt", header=None,delimiter=' ') 
data_kcomp_E4.columns=['vd','iter','te','N_quedaron','nan']
vd_kcomp_E4 = list(data_kcomp_E4.vd.unique())
avg_te_kcomp_E4 = data_kcomp_E4.groupby(data_kcomp_E4['vd'])['te'].mean().values.tolist()
std_te_kcomp_E4 = data_kcomp_E4.groupby(data_kcomp_E4['vd'])['te'].std().values.tolist()

data_kcomp_E5 = pd.read_csv("tevsvd_N225_kcom_E5.txt", header=None,delimiter=' ') 
data_kcomp_E5.columns=['vd','iter','te','N_quedaron','nan']
vd_kcomp_E5 = list(data_kcomp_E5.vd.unique())
avg_te_kcomp_E5 = data_kcomp_E5.groupby(data_kcomp_E5['vd'])['te'].mean().values.tolist()
std_te_kcomp_E5 = data_kcomp_E5.groupby(data_kcomp_E5['vd'])['te'].std().values.tolist()


data = pd.read_csv("tevsvd_N225_sincomp.txt", header=None,delimiter=' ') 
data.columns=['vd','iter','te','N_quedaron','nan']
vd = list(data.vd.unique())
avg_te = data.groupby(data['vd'])['te'].mean().values.tolist()
std_te = data.groupby(data['vd'])['te'].std().values.tolist()


###  PLOT  ###

### No compression ###
plt.plot(vd,avg_te,'-.rs',mew=0.7,mec='k',markersize=4,label='$k_n = 0$ ') 
plt.errorbar(vd,avg_te,std_te,linestyle='none',fmt='none',color='none',ecolor='r') 

### With compression ###
plt.plot(vd_kcomp_E4,avg_te_kcomp_E4,'-y^',mew=0.7,mec='k',markersize=4,label='$k_n =$ 1.2 E4 ') 
plt.errorbar(vd_kcomp_E4,avg_te_kcomp_E4,std_te_kcomp_E4,linestyle='none',fmt='none',color='none',ecolor='y') 

plt.plot(vd_kcomp_E5,avg_te_kcomp_E5,'--bo',mew=0.7,mec='k',markersize=4,label='$k_n =$ 1.2 E5') 
plt.errorbar(vd_kcomp_E5,avg_te_kcomp_E5,std_te_kcomp_E5,linestyle='none',fmt='none',color='none',ecolor='b') 



pylab.grid(False)
pylab.xlabel('$v_d$~(m/s)')
pylab.ylabel('$t_e$~(s)')
pylab.title("N = 225 - Original Friction - Door = 0.92~m (2p)")
#pylab.ylim(40, 80)
lgd=plt.legend(numpoints=1,handlelength=0.8) 
plt.legend(frameon=False,loc='best',labelspacing=-0.1,borderpad=0.3,handletextpad=0.5,fontsize=6,numpoints=1) 

#pylab.savefig('vd_vs_te_N225_.png', format='png', dpi=300, bbox_inches='tight')
pylab.savefig('vd_vs_te_N225.eps', format='eps', dpi=300, bbox_inches='tight')
