'''
Genera un grafico con nodos y links a partir de una configuracion
Las posiciones de los nodos corresponden a las posiciones de los
individuos en el recinto. 
'''
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import pylab
import math

# a dos columnas: 3+3/8 (ancho, in)
# a una columna : 6.5   (ancho  in)

golden_mean = (math.sqrt(5)-1.0)/2.0        # Aesthetic ratio
fig_width = 3+3/8                           # width  in inches
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
     index = []
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
                         index+=[int(row[0])]
                         x+=[float(row[1])]
                         y+=[float(row[2])]
                    flag=False
          i+=1
     f.close()
     if i==len(lines):
     	print("\nERROR: Selected time  not found. Try a different selected time\n")
     	exit()
     return index,x,y


def calcula_matriz_adyacencia(index,x,y,sum_rads):
     '''
     crea la matriz de adyacencia a partir de una config.
     hay un link cuando se estan tocando. 
     '''
     extra = 100 # nodos extra por las dudas
     sum_rads2 = sum_rads*sum_rads 
     i = 0
     matriz_adyacencia = np.zeros((len(x)+extra, len(x)+extra))
     while i<len(x):
          j=0
          while j<len(x):
               dist2 = (x[i]-x[j])*(x[i]-x[j])+(y[i]-y[j])*(y[i]-y[j])
               if dist2<=sum_rads2 and i!=j:
                         index_i = int(index[i])
                         index_j = int(index[j])
                         matriz_adyacencia[index_i][index_j]=1
                         matriz_adyacencia[index_j][index_i]=1
               j+=1
          i+=1
     return matriz_adyacencia    

def elimina_nodos_inexistentes(index,G):
     '''
     Elimina nodos que no corresponden a individuos del recinto
     Devuelve el grafo con los nodos que si forman parte del recinto
     '''

     for i in range(0,len(G)):
          if i not in index:
               G.remove_node(i)
     return G

def crea_dict_pos(index,x,y):
     
     pos = dict()
     for i in range(0,len(index)):
          indice = index[i]
          xy = (x[i],y[i])
          pos.update( {'{}'.format(indice) : xy} )
     return pos

def plot_network(G,output_filename):
     '''
     Grafica nodos y links ubicados en la posicion correspondiente
     del recinto. El color de cada nodo esta en funcion del grado. 
     '''

     degrees = G.degree() 
     nodes = G.nodes()
     n_color = np.asarray([degrees[n] for n in nodes])
     fig, ax = plt.subplots()
     pos=nx.get_node_attributes(G,'pos')
     sc = nx.draw(G,pos,width=0.5,node_color=n_color,cmap='viridis',node_size=5,with_labels=False,edge_color='black')
     plt.axis([13,20,4,16])
     plt.axis('on')
     plt.grid('false')
     #plt.text(15.5, 5.5, "16", fontsize=10)
     #plt.text(8, 5.5, "8", fontsize=10)
     #plt.text(7.5, 6, "6", fontsize=10)
     #plt.text(7.5, 13.5, "14", fontsize=10)
     ax.set_xlabel('$x$-position',fontsize=8)
     ax.set_ylabel('$y$-position',fontsize=8)
     cmap=plt.cm.viridis
     sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin = min(n_color), vmax=max(n_color)))
     sm._A = []
     plt.colorbar(sm)
     #sm.set_clim(0, 100)
     pylab.savefig('{}.png'.format(output_filename), format='png', dpi=300, bbox_inches='tight')
     pylab.savefig('{}.eps'.format(output_filename), format='eps', dpi=300, bbox_inches='tight')



########################  MAIN  ########################
def main():

     ############# PARAMETERS #############
     input_filename = 'config_bottleneck_vd10_k120000'
     output_filename = 'network_vd10_kn120000'
     time = 100
     sum_rads = 0.46
     ######################################
     index,x,y = extract_config(input_filename,time)
     pos = crea_dict_pos(index,x,y)
     matriz_adyacencia = calcula_matriz_adyacencia(index,x,y,sum_rads)
     G = nx.from_numpy_matrix(np.array(matriz_adyacencia))
     G = elimina_nodos_inexistentes(index,G)
     # Asigna atributo de posicion xy a cada nodo
     for i in index:
          G.nodes[i]['pos'] = pos['{}'.format(i)]

     plot_network(G,output_filename)


if __name__=='__main__':
     main()