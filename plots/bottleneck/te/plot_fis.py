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


data_kcomp_E4 = pd.read_csv("tevsvd_N225_k26200.txt", header=None,delimiter=' ') 
data_kcomp_E4.columns=['vd','iter','te','N_quedaron','nan']
vd_kcomp_E4 = list(data_kcomp_E4.vd.unique())
avg_te_kcomp_E4 = data_kcomp_E4.groupby(data_kcomp_E4['vd'])['te'].mean().values.tolist()
std_te_kcomp_E4 = data_kcomp_E4.groupby(data_kcomp_E4['vd'])['te'].std().values.tolist()

data_kcomp_E5 = pd.read_csv("tevsvd_N225_k120000.txt", header=None,delimiter=' ') 
data_kcomp_E5.columns=['vd','iter','te','N_quedaron','nan']
vd_kcomp_E5 = list(data_kcomp_E5.vd.unique())
avg_te_kcomp_E5 = data_kcomp_E5.groupby(data_kcomp_E5['vd'])['te'].mean().values.tolist()
std_te_kcomp_E5 = data_kcomp_E5.groupby(data_kcomp_E5['vd'])['te'].std().values.tolist()

data_kE6 = pd.read_csv("tevsvd_N225_k1200000.txt", header=None,delimiter=' ') 
data_kE6.columns=['vd','iter','te','N_quedaron','nan']
vd_kE6 = list(data_kE6.vd.unique())
avg_te_kE6 = data_kE6.groupby(data_kE6['vd'])['te'].mean().values.tolist()
std_te_kE6 = data_kE6.groupby(data_kE6['vd'])['te'].std().values.tolist()

data_6E4 = pd.read_csv("tevsvd_N225_k60000.txt", header=None,delimiter=' ') 
data_6E4.columns=['vd','iter','te','N_quedaron','nan']
vd_6E4 = list(data_6E4.vd.unique())
avg_te_6E4 = data_6E4.groupby(data_6E4['vd'])['te'].mean().values.tolist()
std_te_6E4 = data_6E4.groupby(data_6E4['vd'])['te'].std().values.tolist()

data = pd.read_csv("tevsvd_N225_k0.txt", header=None,delimiter=' ') 
data.columns=['vd','iter','te','N_quedaron','nan']
vd = list(data.vd.unique())
avg_te = data.groupby(data['vd'])['te'].mean().values.tolist()
std_te = data.groupby(data['vd'])['te'].std().values.tolist()


###  PLOT  ###

### No compression ###
plt.plot(vd,avg_te,'-s',mew=0.7,mec='k',markersize=4,label='$k_n =$ 0 ') 
plt.errorbar(vd,avg_te,std_te,linestyle='none',fmt='none',color='b',ecolor='#1f77b4') 

### With compression ###
plt.plot(vd_kcomp_E4,avg_te_kcomp_E4,'-^',mew=0.7,mec='k',markersize=4,label='$k_n =$ 2.62 E4 ') 
plt.errorbar(vd_kcomp_E4,avg_te_kcomp_E4,std_te_kcomp_E4,linestyle='none',fmt='none',color='orange',ecolor='#ff7f0e') 

plt.plot(vd_6E4,avg_te_6E4,'-v',color='firebrick',mew=0.7,mec='k',markersize=4,label='$k_n =$ 6 E4') 
plt.errorbar(vd_6E4,avg_te_6E4,std_te_6E4,linestyle='none',fmt='none',color='firebrick',ecolor='firebrick') 

plt.plot(vd_kcomp_E5,avg_te_kcomp_E5,'-x',mew=0.7,mec='k',markersize=4,label='$k_n =$ 1.2 E5') 
plt.errorbar(vd_kcomp_E5,avg_te_kcomp_E5,std_te_kcomp_E5,linestyle='none',fmt='none',color='none',ecolor='g') 

plt.plot(vd_kE6,avg_te_kE6,'-ko',mew=0.7,mec='k',markersize=4,label='$k_n =$ 1.2 E6') 
plt.errorbar(vd_kE6,avg_te_kE6,std_te_kE6,linestyle='none',fmt='none',color='none',ecolor='k') 


pylab.grid(False)
pylab.xlabel('$v_d$~(ms$^{-1}$)')
pylab.ylabel('$t_e$~(s)')
#pylab.title("N = 225 - Original Friction - Door = 0.92~m (2p)")
#pylab.ylim(40, 80)
lgd=plt.legend(numpoints=1,handlelength=0.8) 
plt.legend(frameon=False,loc='best',labelspacing=-0.1,borderpad=0.3,handletextpad=0.5,fontsize=6,numpoints=1) 

pylab.savefig('vd_vs_te_N225.eps', format='eps', dpi=300, bbox_inches='tight')
pylab.savefig('vd_vs_te_N225.png', format='png', dpi=300, bbox_inches='tight')
