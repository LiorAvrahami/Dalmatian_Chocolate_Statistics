import matplotlib.pyplot as plt
import numpy as np
import drawing_utility
from drawing_utility import draw_W_N_scater,\
    whites_draw_color,browns_draw_color,blacks_draw_color,sum_draw_color,indipendent_sum_draw_color
import scipy.stats
from read import Nw ,Ww ,Nb ,Wb ,Nk ,Wk ,Wsum
import statistics_utility
from statistics_utility import indexes_not_nan

def get_ball_mass(W,N):
    not_nan_indexes = np.isfinite(N) * np.isfinite(W)
    ball_mass_avr =  np.sum(W[not_nan_indexes])/np.sum(N[not_nan_indexes])
    ball_mass_std_guess = np.sqrt(np.var(W[not_nan_indexes])/np.mean(N[not_nan_indexes]))
    return ball_mass_avr,ball_mass_std_guess


ball_mass_avr_w, ball_mass_std_guess_w = get_ball_mass(Ww,Nw)
ball_mass_avr_b, ball_mass_std_guess_b = get_ball_mass(Wb,Nb)
ball_mass_avr_k, ball_mass_std_guess_k = get_ball_mass(Wk,Nk)
ball_mass_avr_n, ball_mass_std_guess_n = get_ball_mass(np.concatenate([Ww,Wb,Wk]),np.concatenate([Nw,Nb,Nk]))

idx = indexes_not_nan(Nw,Ww)
fit_res_w = np.polyfit(Nw[idx],Ww[idx],1,cov=True)
idx = indexes_not_nan(Nb,Wb)
fit_res_b = np.polyfit(Nb[idx],Wb[idx],1,cov=True)
idx = indexes_not_nan(Nk,Wk)
fit_res_k = np.polyfit(Nk[idx],Wk[idx],1,cov=True)

# chocolate_density

if __name__=="__main__":
    plt.figure()
    plt.plot(Nw, Ww, "o", color=whites_draw_color*0.85,alpha=1,
             label="whites in each pack")
    plt.plot(Nb, Wb, "o", color=browns_draw_color*0.85,alpha=0.5,
             label="browns in each pack")
    plt.plot(Nk, Wk, "o", color=blacks_draw_color*0.85,alpha=0.5,
             label="blacks in each pack")

    plt.plot(Nb + Nk + Nw, Ww + Wb + Wk, "o", color=sum_draw_color*0.7,alpha=0.7,
             label="total of each packs",zorder=3)

    plt.plot(*statistics_utility.sample_independent_sum_of_dependant_multydistributions(200,[Nb, Nk, Nw],[Wb, Wk, Ww]),
             "o", color=indipendent_sum_draw_color * 0.85, alpha=0.5,
             label="total of colors mixed from three different packs")

    avr_mass_lim = 60
    plt.plot([0, avr_mass_lim], [0, ball_mass_avr_n * avr_mass_lim + ball_mass_avr_n], color="m",alpha=0.5,
             label="group mass = (average ball mass) * (nubmer of balls)")

    plt.xlabel("number of balls in group")
    plt.ylabel("mass of ball group [gr]")
    plt.title("group mass vs group size distributions for different groups of balls")

    plt.grid(ls="--")
    plt.legend()
    plt.show()
