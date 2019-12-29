import sys
import os
import pandas as pd
import pylab
import numpy as np
import matplotlib.pyplot as plt
import math

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



def main():

     file_name = 'network_data_corridor_avgt_kn0.txt'
     simbol ='-s'
     color = 'c'
     label = "$k_n=$~0"
     plot_triangles(file_name,simbol,color,label)

     file_name= 'network_data_corridor_avgt_kn1.2E4.txt' 
     simbol ='-^'
     color = 'y'
     label = "$k_n=1.2$~E4"
     plot_triangles(file_name,simbol,color,label)

     file_name = 'network_data_corridor_avgt_kn1.2E5.txt' 
     simbol ='-x'
     color = 'b'
     label = "$k_n=1.2$~E5"
     plot_triangles(file_name,simbol,color,label)

     file_name = 'network_data_corridor_avgt_kn1.2E6.txt'
     simbol ='-o'
     color = 'k'
     label = "$k_n=1.2$~E6"
     plot_triangles(file_name,simbol,color,label)



def plot_triangles(file_name,simbol,color,label):
     '''
     Importa un archivo con las caracteristicas de la red 
     y grafica triangulos vs densidad
     '''
     df = pd.read_csv('{}'.format(file_name),delimiter = '\t') 
     global_density = df['0.Global dens'].tolist()
     f_in_giant = df['1.fraction nodes in giant'].tolist()
     diameter = df['3.diameter'].tolist()
     mean_degree = df['4.mean degree'].tolist()
     std_degree = df['5.std degree'].tolist()
     triangles = df['6.triangles per node'].tolist()
     triangles_std = df['7.std triangles per node'].tolist()
     plt.plot(global_density,triangles,simbol,color=color,mec='k',mew=0.8,linewidth = '1',markersize=4,label=label)     
     pylab.grid(False)
     pylab.xlabel('Density~(p m$^{-2}$)')
     pylab.ylabel('Triangles per node')
     plt.ylim(-0.25,6.2)
     plt.xlim(4.5,9.1)
     lgd=plt.legend(numpoints=1,handlelength=0.8) 
     plt.legend(frameon=False,loc='best',labelspacing=-0.1,borderpad=0.3,handletextpad=0.5,fontsize=6,numpoints=1) 
     pylab.savefig('triangles.eps', format='eps', dpi=300, bbox_inches='tight')
     pylab.savefig('triangles.png', format='png', dpi=300, bbox_inches='tight')


if __name__=='__main__':
     main()