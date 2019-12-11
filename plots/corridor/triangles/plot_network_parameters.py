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


     df = pd.read_csv('network_data_kn1.2E6_t30s.txt',delimiter = '\t') 
     global_density = df['0.density'].tolist()
     f_in_giant = df['2.fraction nodes in giant'].tolist()
     shortest_path = df['5.average shortest path length'].tolist()
     diameter = df['6.diameter'].tolist()
     mean_degree = df['7.mean degree'].tolist()
     std_degree = df['8.std degree'].tolist()
     triangles = df['9.triangles per node'].tolist()
     simbol ='-o'
     color = 'k'
     label = "$k_n=1.2$~E6"
     #plot_degree(global_density,mean_degree,std_degree,color,simbol,label)
     #plot_fraction_in_giant(global_density,f_in_giant,color,simbol,label)
     #plot_shortest_path(global_density,shortest_path,color,simbol,label)
     #plot_diameter(global_density,diameter,color,simbol,label)
     plot_triangles(global_density,triangles,color,simbol,label)



     df = pd.read_csv('network_data_knE5_t30s.txt',delimiter = '\t') 
     global_density = df['0.density'].tolist()
     f_in_giant = df['2.fraction nodes in giant'].tolist()
     shortest_path = df['5.average shortest path length'].tolist()
     diameter = df['6.diameter'].tolist()
     mean_degree = df['7.mean degree'].tolist()
     std_degree = df['8.std degree'].tolist()
     triangles = df['9.triangles per node'].tolist()
     simbol ='-x'
     color = 'b'
     label = "$k_n=1.2$~E5"
     #plot_degree(global_density,mean_degree,std_degree,color,simbol,label)
     #plot_fraction_in_giant(global_density,f_in_giant,color,simbol,label)
     #plot_shortest_path(global_density,shortest_path,color,simbol,label)
     #plot_diameter(global_density,diameter,color,simbol,label)
     plot_triangles(global_density,triangles,color,simbol,label)

     df = pd.read_csv('network_data_knE4_t30s.txt',delimiter = '\t') 
     global_density = df['0.density'].tolist()
     f_in_giant = df['2.fraction nodes in giant'].tolist()
     shortest_path = df['5.average shortest path length'].tolist()
     diameter = df['6.diameter'].tolist()
     mean_degree = df['7.mean degree'].tolist()
     std_degree = df['8.std degree'].tolist()
     triangles = df['9.triangles per node'].tolist()
     simbol ='-^'
     color = 'y'
     label = "$k_n=1.2$~E4"

     #plot_degree(global_density,mean_degree,std_degree,color,simbol,label)
     #plot_fraction_in_giant(global_density,f_in_giant,color,simbol,label)
     #plot_shortest_path(global_density,shortest_path,color,simbol,label)
     #plot_diameter(global_density,diameter,color,simbol,label)
     plot_triangles(global_density,triangles,color,simbol,label)



     df = pd.read_csv('network_data_kn0_t30s.txt',delimiter = '\t') 
     global_density = df['0.density'].tolist()
     f_in_giant = df['2.fraction nodes in giant'].tolist()
     shortest_path = df['5.average shortest path length'].tolist()
     diameter = df['6.diameter'].tolist()
     mean_degree = df['7.mean degree'].tolist()
     std_degree = df['8.std degree'].tolist()
     triangles = df['9.triangles per node'].tolist()
     simbol ='-s'
     color = 'c'
     label = "$k_n=$0"

     #plot_degree(global_density,mean_degree,std_degree,color,simbol,label)
     #plot_fraction_in_giant(global_density,f_in_giant,color,simbol,label)
     #plot_shortest_path(global_density,shortest_path,color,simbol,label)
     #plot_diameter(global_density,diameter,color,simbol,label)
     plot_triangles(global_density,triangles,color,simbol,label)





def plot_degree(global_density,degree,std_degree,color,simbol,label):

     plt.errorbar(global_density,degree,std_degree,color=color,mec='k',label=label)   
     plt.plot(global_density,degree,simbol,color=color,mec='k',mew=0.8,linewidth = '0.8',markersize=4)   
     pylab.grid(False)
     pylab.xlabel('Density~(p m$^{-2}$)')
     pylab.ylabel('Degree in giant cluster')
     lgd=plt.legend(numpoints=1,handlelength=0.8) 
     plt.legend(frameon=False,loc='best',labelspacing=-0.1,borderpad=0.3,handletextpad=0.5,fontsize=6,numpoints=1) 
     pylab.savefig('density_degree.png', format='png', dpi=300, bbox_inches='tight')

def plot_fraction_in_giant(global_density,f_in_giant,color,simbol,label):


     plt.plot(global_density,f_in_giant,simbol,color=color,mec='k',mew=0.8,linewidth = '1',markersize=4,label=label)   
     pylab.grid(False)
     pylab.xlabel('Density~(p m$^{-2}$)')
     pylab.ylabel('Fraction of indiv. in Giant')
     plt.xlim(4.74,6)
     lgd=plt.legend(numpoints=1,handlelength=0.8) 
     plt.legend(frameon=False,loc='best',labelspacing=-0.1,borderpad=0.3,handletextpad=0.5,fontsize=6,numpoints=1) 

     pylab.savefig('fraction_in_giant.png', format='png', dpi=300, bbox_inches='tight')


def plot_triangles(global_density,triangles,color,simbol,label):

     plt.plot(global_density,triangles,simbol,color=color,mec='k',mew=0.8,linewidth = '1',markersize=4,label=label)   
     pylab.grid(False)
     pylab.xlabel('Density~(p m$^{-2}$)')
     pylab.ylabel('Triangles per node')
     plt.ylim(-0.25,6.1)
     plt.xlim(4.5,9.1)
     lgd=plt.legend(numpoints=1,handlelength=0.8) 
     plt.legend(frameon=False,loc='best',labelspacing=-0.1,borderpad=0.3,handletextpad=0.5,fontsize=6,numpoints=1) 

     pylab.savefig('triangles.png', format='png', dpi=300, bbox_inches='tight')
     pylab.savefig('triangles.eps', format='eps', dpi=300, bbox_inches='tight')


def plot_shortest_path(global_density,shortest_path,color,simbol,label):

     plt.plot(global_density,shortest_path,simbol,color=color,mec='k',mew=0.8,linewidth = '1',markersize=4,label=label)   
     pylab.grid(False)
     pylab.xlabel('Density~(p m$^{-2}$)')
     pylab.ylabel('Average shortest path length')
     #plt.xlim(4,6)
     lgd=plt.legend(numpoints=1,handlelength=0.8) 
     plt.legend(frameon=False,loc='best',labelspacing=-0.1,borderpad=0.3,handletextpad=0.5,fontsize=6,numpoints=1) 

     pylab.savefig('shortest_path.png', format='png', dpi=300, bbox_inches='tight')


def plot_diameter(global_density,diameter,color,simbol,label):

     plt.plot(global_density,diameter,simbol,color=color,mec='k',mew=0.8,linewidth = '1',markersize=4,label=label)   
     pylab.grid(False)
     pylab.xlabel('Density~(p m$^{-2}$)')
     pylab.ylabel('Diameter')
     #plt.xlim(4,6)
     lgd=plt.legend(numpoints=1,handlelength=0.8) 
     plt.legend(frameon=False,loc='best',labelspacing=-0.1,borderpad=0.3,handletextpad=0.5,fontsize=6,numpoints=1) 

     pylab.savefig('diameter.png', format='png', dpi=300, bbox_inches='tight')
     pylab.savefig('diameter.eps', format='eps', dpi=300, bbox_inches='tight')




if __name__=='__main__':
     main()