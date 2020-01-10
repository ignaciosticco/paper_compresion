'''
Dados los archivos de velocity profile, calcula strain rate vs k
El strain rate esta definido como la secante entre un borde y el centro.

e = (v(centro)-v(borde))/(y(centro)-y(borde))
'''

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


     list_k = [0,12000,120000,1200000]
     y_borde = 0.5
     y_centro = 10.5
     plot_name = 'strain_rate_vs_kn'
     strain_rate = []
     error_strain_rate = []

     for k in list_k:
          file_name = 'vx_profile_kn{}.txt'.format(k)
          df = pd.read_csv('{}'.format(file_name),sep='\t')
          vx_borde = float(df.loc[df['bin y'] == y_borde, 'mean vx'])
          vx_centro = float(df.loc[df['bin y'] == y_centro, 'mean vx'])
          strain_rate += [(vx_centro-vx_borde)/float(y_centro-y_borde)] 
          error_strain_rate += [(float(df.loc[df['bin y'] == y_borde, 'std vx'])+float(df.loc[df['bin y'] == y_centro, 'std vx']))/float(y_centro-y_borde)]
     print(error_strain_rate)

     plot_strainrate_vs_k(plot_name,list_k,strain_rate,error_strain_rate)

def plot_strainrate_vs_k(plot_name,list_k,strain_rate,error_strain_rate):
     '''

     '''


     plt.errorbar(list_k,strain_rate,error_strain_rate, fmt='none')     
     plt.plot(list_k,strain_rate,'b-o',mec='k',mew=0.8,linewidth = '1',markersize=4)     
     pylab.grid(False)
     pylab.xlabel('$k_n$')
     pylab.ylabel('Strain rate~(1/s)')
     plt.xscale('symlog')
     #plt.title("Global density = 7")
     #plt.ylim(-0.25,6.2)
     #plt.xlim(4.5,9.1)
     #lgd=plt.legend(numpoints=1,handlelength=0.8) 
     #plt.legend(frameon=False,loc='best',labelspacing=-0.1,borderpad=0.3,handletextpad=0.5,fontsize=6,numpoints=1) 
     pylab.savefig('{}.png'.format(plot_name), format='png', dpi=300, bbox_inches='tight')
     pylab.savefig('{}.eps'.format(plot_name), format='eps', dpi=300, bbox_inches='tight')
     

if __name__=='__main__':
     main()