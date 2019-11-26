import pylab
import numpy as np
import math
import matplotlib.pyplot as plt
import pandas as pd
from   scipy.spatial import Voronoi, voronoi_plot_2d
from   scipy.spatial import ConvexHull
import matplotlib.patches as patches
import matplotlib as mpl
import matplotlib.cm as cm

golden_mean = (math.sqrt(5)-1.0)/2.0        # Aesthetic ratio
fig_width = 3+3/8                            # width  in inches
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
          'savefig.dpi': 600,
         }

pylab.rcParams.update(params)


################## PRAMETERS ######################### 
selected_time = 30
global_density = 7
output_name = "tesselation_d{}_time{}_color_relative_kn0".format(global_density,selected_time)
data_config = "config_density{}_width22_kn0".format(global_density)
xmin = 1.0
xmax = 27.0
ymin = 1
ymax = 21.0


######################## Functions ##################### 

def extract_config(data,t):
     '''
     t is the selected time
     this function extracts the configuration for the time t
     only one timestep is extracted
     '''
     ESCALA_TIME = 10000

     str_selected_timestep='{}\n'.format(int(t*ESCALA_TIME))
     f=open(data, 'r')
     lines=f.readlines()
     x=[]
     y=[]
     i=0
     flag=True
     while i<len(lines) and flag:
          line = lines[i].rstrip('\n')
          if(line=='ITEM: TIMESTEP'):
               iter_time=lines[i+1]
               if(iter_time==str_selected_timestep):
                    number_pedestrians=int(lines[i+3])
                    first_line_table=i+9
                    for j in range(first_line_table, first_line_table+number_pedestrians):
                         row=lines[j].split(' ')
                         x+=[float(row[1])]
                         y+=[float(row[2])]
                    flag=False
          i+=1
     f.close()
     if i==len(lines):
          print("\nERROR: Selected time  not found. Try a different selected time\n")
          exit()
     return x,y


def crea_array_points(x,y):
     '''
     Crea el array de puntos necesario para el programa que calcula
     las areas de voronoi
     '''

     list_points =[]
     i=0
     while i<len(x):
          list_points+=[[x[i],y[i]]]
          i+=1
     points = np.array(list_points)
     return points

def voronoi_volumes(points):
     '''
     Calcula los volumenes de voronoi dados los puntos
     '''
     v = Voronoi(points)
     vol = np.zeros(v.npoints)
     for i, reg_num in enumerate(v.point_region):
        indices = v.regions[reg_num]
        if -1 in indices: # some regions can be opened
            vol[i] = np.inf
        else:
            vol[i] = ConvexHull(v.vertices[indices]).volume
     return vol

def halla_max_min_sin_bordes(x,y,list_vol_tmp,xmin,xmax,ymin,ymax):
     '''
     Encuentra el valor maximo y el minimo de todo el recinto 
     sin tener en cuenta a los bordes
     Crea una nueva lista con los volumenes asociados a las particulas
     tales que xmin<x<xmax (idem con y)
     '''
     i=0
     new_list_vol_tmp = []
     while i<len(x):
          if x[i]>xmin and x[i]<xmax and y[i]>ymin and y[i]<ymax:
               new_list_vol_tmp+=[list_vol_tmp[i]]
          i+=1
     return min(new_list_vol_tmp),max(new_list_vol_tmp)



########################  MAIN  ########################
def main():

     x,y=extract_config(data_config,selected_time)
     points = crea_array_points(x,y)
     vor = Voronoi(points)
     list_vol = list(voronoi_volumes(points))

     # find min/max values for normalization
     minima,maxima = halla_max_min_sin_bordes(x,y,list_vol,xmin,xmax,ymin,ymax)
     print(minima,maxima)
     minima = 0.122
     maxima = 0.167
     levels=np.linspace(minima,maxima,10,endpoint=True)
     # normalize chosen colormap
     norm = mpl.colors.Normalize(vmin=minima, vmax=maxima, clip=True)
     mapper = cm.ScalarMappable(norm=norm, cmap=cm.jet_r)

     # plot Voronoi diagram, and fill finite regions with color mapped from speed value
     voronoi_plot_2d(vor, show_points=True, show_vertices=False,color='k', line_width=0.2, point_size=0.25)
     for r in range(len(vor.point_region)):
         region = vor.regions[vor.point_region[r]]
         if not -1 in region:
             polygon = [vor.vertices[i] for i in region]
             plt.fill(*zip(*polygon), color=mapper.to_rgba(list_vol[r]))
     plt.xlim(1,27)  
     plt.ylim(1,21)                               
     plt.grid(False)
     pylab.savefig('{}.png'.format(output_name), format='png', dpi=300, bbox_inches='tight')
     pylab.savefig('{}.eps'.format(output_name), format='eps', dpi=300, bbox_inches='tight')
     

if __name__=='__main__':
     main()
