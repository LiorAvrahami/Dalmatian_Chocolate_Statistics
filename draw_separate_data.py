import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
from read import Nw ,Ww ,Nb ,Wb ,Nk ,Wk ,Wsum
from drawing_utility import draw_scater_line_with_quatients, get_cur_x_of_draw_scater_line,\
    whites_draw_color,browns_draw_color,blacks_draw_color,sum_draw_color,indipendent_sum_draw_color
import statistics_utility
from statistics_of_single_ball import ball_mass_avr_b,ball_mass_avr_k,ball_mass_avr_w

# weight white
draw_scater_line_with_quatients(Ww,np.array(whites_draw_color),"white balls")
# weight brown
draw_scater_line_with_quatients(Wb,np.array(browns_draw_color),"brown balls")
# weight black
draw_scater_line_with_quatients(Wk,np.array(blacks_draw_color),"black balls")
# weight balck + brown
# draw_scater_line_with_quatients(Wb+Wk,np.array((0.4,0.8,1)),"black+brown")
# weight sum
draw_scater_line_with_quatients(Wsum, np.array(sum_draw_color), "black+brown+white")
# calculate independent sum
Sum_independent = statistics_utility.sample_independent_sum_of_distributions([Ww,Wb,Wk],20000)
draw_scater_line_with_quatients(Sum_independent,np.array(indipendent_sum_draw_color),"black+brown+white if they were independent",num_of_scater_to_plot=200)
plt.title("Weight of balls of a certain color in pack")
plt.xlabel("weight in gr")
plt.xlim(0,plt.xlim()[1])
plt.ylim(plt.ylim()[0],plt.ylim()[1]*1.5)
plt.yticks([])
plt.locator_params(nbins=25)
plt.grid(ls="--")
plt.legend()
plt.gcf().set_size_inches([9.87, 4.48])

plt.figure()

# weight white
draw_scater_line_with_quatients(Nw,np.array(whites_draw_color),"white balls",index=0)
# weight brown
draw_scater_line_with_quatients(Nb,np.array(browns_draw_color),"brown balls")
# weight black
draw_scater_line_with_quatients(Nk,np.array(blacks_draw_color),"black balls")
# # weight balck + brown
# draw_scater_line_with_quatients(Nb+Nk,np.array((0.4,0.8,1)),"black+brown")
# weight sum
draw_scater_line_with_quatients(Nb+Nk+Nw,np.array(sum_draw_color),"black+brown+white")
# calculate independent sum
Sum_independent = statistics_utility.sample_independent_sum_of_distributions([Nw,Nb,Nk],20000)
draw_scater_line_with_quatients(Sum_independent,np.array(indipendent_sum_draw_color),"black+brown+white if they were independent",num_of_scater_to_plot=200)
plt.title("Number of balls of a certain color in pack")
plt.xlabel("number of balls")
plt.xlim(0,plt.xlim()[1])
plt.ylim(plt.ylim()[0],plt.ylim()[1]*1.5)
plt.yticks([])
plt.locator_params(nbins=25)
plt.grid(ls="--")
plt.legend()
plt.gcf().set_size_inches([9.87, 4.48])


plt.show()