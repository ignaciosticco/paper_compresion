import pylab as plt
from matplotlib_venn import venn3, venn3_circles
import math
import pylab

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

v = venn3(subsets=(1,1,1,1,1,1,1),set_labels = ('$\mathcal{A}$', '$\mathcal{K}$', '$\mathcal{K}_c$'))
v.get_label_by_id('100').set_text(' $\\frac{A \\tau}{m v_d}$')
v.get_label_by_id('010').set_text('$\\frac{\\kappa B \\tau}{m}$')
v.get_label_by_id('001').set_text('$\\frac{k B \\tau}{m v_d}$')
v.get_label_by_id('111').set_text('$m/\\tau$')
v.get_label_by_id('101').set_text('$\\frac{\\tau}{m v_d}$')
v.get_label_by_id('110').set_text('')
v.get_label_by_id('011').set_text('$\\frac{B\\tau}{m}$')


pylab.savefig('venn_parameters.png', format='png', dpi=300, bbox_inches='tight')
pylab.savefig('venn_parameters.eps', format='eps', dpi=300, bbox_inches='tight')