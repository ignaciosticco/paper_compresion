'''
Grafica multiples densidades vs flujo
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

data_kn_kt = pd.read_csv("fd_kt_kn.txt",sep="\t")
global_density_kn_kt = data_kn_kt["mean_global_dens"].tolist()
density_kn_kt = data_kn_kt["mean_local_dens"].tolist()
flow_kn_kt = data_kn_kt["mean_local_flowx"].tolist()
std_flow_kn_kt = data_kn_kt["std_local_flowx"].tolist()
speed_kn_kt = np.divide(flow_kn_kt,density_kn_kt)

'''
data_kn_ktx3 = pd.read_csv("flow_density_kn_ktx3.txt",sep=" ")
density_kn_ktx3 = data_kn_ktx3["density"].tolist()
flow_kn_ktx3 = data_kn_ktx3["flow"].tolist()
speed_kn_ktx3=np.divide(flow_kn_ktx3,density_kn_ktx3)

data_kn_ktx5 = pd.read_csv("flow_density_kn_ktx5.txt",sep=" ")
density_kn_ktx5 = data_kn_ktx5["density"].tolist()
flow_kn_ktx5 = data_kn_ktx5["flow"].tolist()
speed_kn_ktx5=np.divide(flow_kn_ktx5,density_kn_ktx5)

data_kn_ktx7 = pd.read_csv("flow_density_kn_ktx7.txt",sep=" ")
density_kn_ktx7 = data_kn_ktx7["density"].tolist()
flow_kn_ktx7 = data_kn_ktx7["flow"].tolist()
speed_kn_ktx7=np.divide(flow_kn_ktx7,density_kn_ktx7)

data_kn_ktx9 = pd.read_csv("flow_density_kn_ktx9.txt",sep=" ")
density_kn_ktx9 = data_kn_ktx9["density"].tolist()
flow_kn_ktx9 = data_kn_ktx9["flow"].tolist()
speed_kn_ktx9=np.divide(flow_kn_ktx9,density_kn_ktx9)
'''
data_ktx5_kn = pd.read_csv("fd_ktx5_kn.txt",sep="\t")
global_density_ktx5_kn = data_ktx5_kn["mean_global_dens"].tolist()
density_ktx5_kn = data_ktx5_kn["mean_local_dens"].tolist()
flow_ktx5_kn = data_ktx5_kn["mean_local_flowx"].tolist()
std_flow_ktx5_kn = data_ktx5_kn["std_local_flowx"].tolist()
speed_ktx5_kn = np.divide(flow_ktx5_kn,density_ktx5_kn)


data_ktx10_kn = pd.read_csv("fd_ktx10_kn.txt",sep="\t")
global_density_ktx10_kn = data_ktx10_kn["mean_global_dens"].tolist()
density_ktx10_kn = data_ktx10_kn["mean_local_dens"].tolist()
flow_ktx10_kn = data_ktx10_kn["mean_local_flowx"].tolist()
std_flow_ktx10_kn = data_ktx10_kn["std_local_flowx"].tolist()
speed_ktx10_kn = np.divide(flow_ktx10_kn,density_ktx10_kn)

###  PLOT  ###


fig, ax1 = plt.subplots()

plt.plot(global_density_kn_kt,flow_kn_kt,'y-o',mew=0.7,markerfacecolor='y',markeredgecolor='k',markersize=4,zorder=3,label='$\\kappa = 1 \\times \\kappa_o$') 
plt.errorbar(global_density_kn_kt,flow_kn_kt, yerr=std_flow_kn_kt,color='y')

plt.plot(global_density_ktx5_kn,flow_ktx5_kn,'k-+',mew=0.7,markerfacecolor='g',markeredgecolor='k',markersize=4,zorder=3,label='$\\kappa = 5 \\times \\kappa_o$') 
plt.errorbar(global_density_ktx5_kn,flow_ktx5_kn, yerr=std_flow_ktx5_kn,color='k')

plt.plot(global_density_ktx10_kn,flow_ktx10_kn,'g-^',mew=0.7,markerfacecolor='g',markeredgecolor='k',markersize=4,zorder=3,label='$\\kappa = 10 \\times \\kappa_o$') 
plt.errorbar(global_density_ktx10_kn,flow_ktx10_kn, yerr=std_flow_ktx10_kn,color='g')

#plt.plot(density_kn_ktx3,flow_kn_ktx3,'-ro',mew=0.7,markerfacecolor='r',markeredgecolor='k',markersize=4,label='$\\kappa = 3 \\times \\kappa_o$') 
#plt.plot(density_kn_ktx5,flow_kn_ktx5,'k-+',mew=0.7,markersize=4,label='$\\kappa = 5 \\times \\kappa_o$') 
#plt.plot(density_kn_ktx7,flow_kn_ktx7,'b-x',mew=0.7,markersize=4,label='$\\kappa = 7 \\times \\kappa_o$') 
#plt.plot(density_kn_ktx9,flow_kn_ktx9,'c-s',mew=0.7,markerfacecolor='c',markersize=4,markeredgecolor='k',label='$\\kappa = 9 \\times \\kappa_o$ ') 
#plt.plot(density_kn_ktx10,flow_kn_ktx10,'g-^',mew=0.7,markerfacecolor='g',markersize=4,markeredgecolor='k',label='$\\kappa = 10 \\times \\kappa_o$') 
'''

plt.plot(density_kn_kt,speed_kn_kt,'y-o',mew=0.7,markerfacecolor='y',markeredgecolor='k',markersize=4,zorder=3,label='$\\kappa = 1 \\times \\kappa_o$') 
plt.plot(density_kn_ktx3,speed_kn_ktx3,'-ro',mew=0.7,markerfacecolor='r',markeredgecolor='k',markersize=4,label='$\\kappa = 3 \\times \\kappa_o$') 
plt.plot(density_kn_ktx5,speed_kn_ktx5,'k-+',mew=0.7,markersize=4,label='$\\kappa = 5 \\times \\kappa_o$') 
plt.plot(density_kn_ktx7,speed_kn_ktx7,'b-x',mew=0.7,markersize=4,label='$\\kappa = 7 \\times \\kappa_o$') 
plt.plot(density_kn_ktx9,speed_kn_ktx9,'c-s',mew=0.7,markerfacecolor='c',markersize=4,markeredgecolor='k',label='$\\kappa = 9 \\times \\kappa_o$ ') 
plt.plot(density_kn_ktx10,speed_kn_ktx10,'g-^',mew=0.7,markerfacecolor='g',markersize=4,markeredgecolor='k',label='$\\kappa = 10 \\times \\kappa_o$') 
'''
pylab.grid(False)
pylab.xlabel('Density~(p~m$^{-2}$)')
pylab.ylabel('Flow~(p~m$^{-1}$s$^{-1}$)')
#pylab.ylabel('Speed~(m s$^{-1}$)')
#pylab.legend()
pylab.ylim(0.0,6)
#pylab.xlim(1.0, 10)
#pylab.yticks(np.arange(3,11,2))
#pylab.xticks(np.arange(0,1100,200))
#pylab.title("$k_n=$0")
lgd=plt.legend(numpoints=1,handlelength=0.8) 
plt.legend(frameon=False,loc='upper left',labelspacing=0.2,borderpad=0.3,handletextpad=0.5,fontsize=7,numpoints=1) 
pylab.savefig('flow-density_multifric_comp.png', format='png', dpi=300, bbox_inches='tight')
pylab.savefig('flow-density_multifric_bodyforce.eps', format='eps', dpi=300, bbox_inches='tight')
