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

data_kn0_kt = pd.read_csv("fd_kt_kn0.txt",sep="\t")
global_density_kn0_kt = data_kn0_kt["mean_global_dens"].tolist()
density_kn0_kt = data_kn0_kt["mean_local_dens"].tolist()
flow_kn0_kt = data_kn0_kt["mean_local_flowx"].tolist()
std_flow_kn0_kt = data_kn0_kt["std_local_flowx"].tolist()
speed_kn0_kt = np.divide(flow_kn0_kt,density_kn0_kt)

'''
data_kn0_ktx3 = pd.read_csv("flow_density_kn0_ktx3.txt",sep=" ")
density_kn0_ktx3 = data_kn0_ktx3["density"].tolist()
flow_kn0_ktx3 = data_kn0_ktx3["flow"].tolist()
speed_kn0_ktx3=np.divide(flow_kn0_ktx3,density_kn0_ktx3)

data_kn0_ktx7 = pd.read_csv("flow_density_kn0_ktx7.txt",sep=" ")
density_kn0_ktx7 = data_kn0_ktx7["density"].tolist()
flow_kn0_ktx7 = data_kn0_ktx7["flow"].tolist()
speed_kn0_ktx7=np.divide(flow_kn0_ktx7,density_kn0_ktx7)

data_kn0_ktx9 = pd.read_csv("flow_density_kn0_ktx9.txt",sep=" ")
density_kn0_ktx9 = data_kn0_ktx9["density"].tolist()
flow_kn0_ktx9 = data_kn0_ktx9["flow"].tolist()
speed_kn0_ktx9=np.divide(flow_kn0_ktx9,density_kn0_ktx9)
'''

data_ktx5_kn0 = pd.read_csv("fd_ktx5_kn0.txt",sep="\t")
global_density_ktx5_kn0 = data_ktx5_kn0["mean_global_dens"].tolist()
density_ktx5_kn0 = data_ktx5_kn0["mean_local_dens"].tolist()
flow_ktx5_kn0 = data_ktx5_kn0["mean_local_flowx"].tolist()
std_flow_ktx5_kn0 = data_ktx5_kn0["std_local_flowx"].tolist()
speed_ktx5_kn0 = np.divide(flow_ktx5_kn0,density_ktx5_kn0)

data_ktx10_kn0 = pd.read_csv("fd_ktx10_kn0.txt",sep="\t")
global_density_ktx10_kn0 = data_ktx10_kn0["mean_global_dens"].tolist()
density_ktx10_kn0 = data_ktx10_kn0["mean_local_dens"].tolist()
flow_ktx10_kn0 = data_ktx10_kn0["mean_local_flowx"].tolist()
std_flow_ktx10_kn0 = data_ktx10_kn0["std_local_flowx"].tolist()
speed_ktx10_kn0 = np.divide(flow_ktx10_kn0,density_ktx10_kn0)

###  PLOT  ###


fig, ax1 = plt.subplots()

plt.plot(global_density_kn0_kt,flow_kn0_kt,'-o',mew=0.7,markeredgecolor='k',markersize=4,zorder=3,label='$\\kappa = 1 \\times \\kappa_o$') 
plt.errorbar(global_density_kn0_kt,flow_kn0_kt, yerr=std_flow_kn0_kt,color='b')

plt.plot(global_density_ktx5_kn0,flow_ktx5_kn0,'-+',mew=0.7,markeredgecolor='k',markersize=4,zorder=3,label='$\\kappa = 5 \\times \\kappa_o$') 
plt.errorbar(global_density_ktx5_kn0,flow_ktx5_kn0, yerr=std_flow_ktx5_kn0,color='orange')

plt.plot(global_density_ktx10_kn0,flow_ktx10_kn0,'-^',mew=0.7,markeredgecolor='k',markersize=4,zorder=3,label='$\\kappa = 10 \\times \\kappa_o$') 
plt.errorbar(global_density_ktx10_kn0,flow_ktx10_kn0, yerr=std_flow_ktx10_kn0,color='g')


pylab.grid(False)
pylab.xlabel('Density~(p~m$^{-2}$)')
pylab.ylabel('Flow~(p~m$^{-1}$s$^{-1}$)')

#pylab.ylabel('Speed~(m s$^{-1}$)')
#pylab.legend()
pylab.ylim(0.0,6)
#pylab.xlim(1.0, 10)
#pylab.yticks(np.arange(3,11,2))
#pylab.xticks(np.arange(0,1100,200))
pylab.title("$\\mathcal{K}_c=$ 0")
#lgd=plt.legend(numpoints=1,handlelength=0.8) 
#plt.legend(frameon=False,loc='upper left',labelspacing=0.2,borderpad=0.3,handletextpad=0.5,fontsize=7,numpoints=1) 


############ Insert plot ############



data_johansson = np.genfromtxt('Flujo_vs_densidad_Helbing_2007.dat', delimiter = '')
density_johansson = data_johansson[:,0] 
flow_johansson = data_johansson[:,1] 

############  PLOT  ############


left, bottom, width, height = [0.15, 0.60, 0.28, 0.28]
ax2 = fig.add_axes([left, bottom, width, height])

ax2.plot(density_johansson,flow_johansson,'*',color='orange',markeredgecolor='orange',markersize=2) 
fig.patch.set_facecolor('black')
#pylab.yticks(np.arange(0,1.1,1),size='4.5')
#pylab.xticks(np.arange(0,1.1,1),size='0.0')
pylab.xlabel('Density ',size='4.5',labelpad=1)
pylab.ylabel('Flow  ',size='3.5',labelpad=-6,zorder=1)
#pylab.ylim(0.3, 1.1)
#pylab.xlim(0, 1.02)
#ax2.tick_params(axis='y', pad=-4)
ax2.set_yticklabels([])
plt.tick_params(axis='x',which='both',bottom=False,top=False,labelbottom=False) 
plt.tick_params(axis='y',which='both',bottom=False,top=False,labelbottom=False) 

ax2.xaxis.set_ticks_position('none') 
ax2.yaxis.set_ticks_position('none') 
ax2.grid(False)
plt.text(1.05, -0.1, "0", size=4.5)
#plt.text(9, -0.1, "10", size=4.5)
plt.text(0.25, 1.7, "2", size=4.5)


pylab.savefig('flow-density_multifric_nobodyforce.png', format='png', dpi=300, bbox_inches='tight')
pylab.savefig('flow-density_multifric_nobodyforce.eps', format='eps', dpi=300, bbox_inches='tight')
