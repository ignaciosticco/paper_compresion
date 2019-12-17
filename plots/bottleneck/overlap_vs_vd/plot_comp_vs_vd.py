'''
Grafica compresion vs vd para muchos kn diferentes
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

data_kn0 = pd.read_csv("overlap_vs_vd_kn0.txt",sep="\t")
vd_kn0 = data_kn0["vd"].tolist()
mean_comp_kn0 = data_kn0["list_mean_overlap"].tolist()
std_comp_kn0 = data_kn0["list_std_overlap"].tolist()

data_knE4 = pd.read_csv("overlap_vs_vd_kn1.2E4.txt",sep="\t")
vd_knE4 = data_knE4["vd"].tolist()
mean_comp_knE4 = data_knE4["list_mean_overlap"].tolist()
std_comp_knE4 = data_knE4["list_std_overlap"].tolist()

data_knx5 = pd.read_csv("overlap_vs_vd_kn6E4.txt",sep="\t")
vd_knx5 = data_knx5["vd"].tolist()
mean_comp_knx5 = data_knx5["list_mean_overlap"].tolist()
std_comp_knx5 = data_knx5["list_std_overlap"].tolist()

data_knE5 = pd.read_csv("overlap_vs_vd_kn1.2E5.txt",sep="\t")
vd_knE5 = data_knE5["vd"].tolist()
mean_comp_knE5 = data_knE5["list_mean_overlap"].tolist()
std_comp_knE5 = data_knE5["list_std_overlap"].tolist()

data_knE6 = pd.read_csv("overlap_vs_vd_kn1.2E6.txt",sep="\t")
vd_knE6 = data_knE6["vd"].tolist()
mean_comp_knE6 = data_knE6["list_mean_overlap"].tolist()
std_comp_knE6 = data_knE6["list_std_overlap"].tolist()


###  PLOT  ###


fig, ax1 = plt.subplots()

plt.plot(vd_kn0,mean_comp_kn0,'-cs',mew=0.7,markeredgecolor='k',markersize=4,zorder=3,label='$k=0$') 
#plt.errorbar(density_kn_kt,flow_kn_kt, yerr=std_flow_kn_kt,color='y')

plt.plot(vd_knE4,mean_comp_knE4,'-y^',mew=0.7,markeredgecolor='k',markersize=4,zorder=3,label='$k=1.2$~E4') 
#plt.errorbar(density_kn_kt,flow_kn_kt, yerr=std_flow_kn_kt,color='y')

plt.plot(vd_knx5,mean_comp_knx5,'-rv',mew=0.7,markeredgecolor='k',markersize=4,zorder=3,label='$k=6$~E4') 
#plt.errorbar(density_kn_kt,flow_kn_kt, yerr=std_flow_kn_kt,color='y')

plt.plot(vd_knE5,mean_comp_knE5,'-bx',mew=0.7,markeredgecolor='k',markersize=4,zorder=3,label='$k=1.2$~E5') 
#plt.errorbar(density_kn_kt,flow_kn_kt, yerr=std_flow_kn_kt,color='y')

plt.plot(vd_knE6,mean_comp_knE6,'-ko',mew=0.7,markeredgecolor='k',markersize=4,zorder=3,label='$k=1.2$~E6') 
#plt.errorbar(density_kn_kt,flow_kn_kt, yerr=std_flow_kn_kt,color='y')


pylab.grid(False)
pylab.xlabel('$v_d$~(m~s$^{-1})$')
pylab.ylabel('Mean Overlap~(m)')
#pylab.legend()
#plt.ylim(-0.001,0.1)
#pylab.xlim(1.0, 10)
#pylab.yticks(np.arange(3,11,2))
#pylab.xticks(np.arange(0,1100,200))
#pylab.title("With Body Force")
lgd=plt.legend(numpoints=1,handlelength=0.8) 
plt.legend(frameon=False,loc='best',labelspacing=0.2,borderpad=0.3,handletextpad=0.5,fontsize=7,numpoints=1) 
pylab.savefig('overlap_vs_vd_multi_kn.png', format='png', dpi=300, bbox_inches='tight')
pylab.savefig('overlap_vs_vd_multi_kn.eps', format='eps', dpi=300, bbox_inches='tight')
