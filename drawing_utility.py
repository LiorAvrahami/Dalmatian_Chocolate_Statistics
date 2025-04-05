import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Rectangle
import numpy as np
from find_map_number_of_balls_to_mass import get_distribution_of_masses_around_N_vector
import statistics_utility
import addcopyfighandler

whites_draw_color = np.array((0.85, 0.85, 0.85))
browns_draw_color = np.array((0.7, 0.5, 0.3))
blacks_draw_color = np.array((0.2, 0.4, 0.5))
sum_draw_color = np.array((1, 0.6, 0.8))
indipendent_sum_draw_color = np.array((1, 0.8, 0.2))

current_index = 0


def draw_scater_line_with_quatients(dat_to_plot, color, label, index=None, height=0.6, num_of_scater_to_plot=None):
    dat_to_plot_cleaned = dat_to_plot[np.isfinite(dat_to_plot)]
    global current_index
    if index == None:
        index = current_index
        current_index += 1
    else:
        current_index = index + 1
    if num_of_scater_to_plot == None:
        num_of_scater_to_plot = len(dat_to_plot_cleaned)
    low_partial = np.quantile(dat_to_plot_cleaned, 0.16)
    high_partial = np.quantile(dat_to_plot_cleaned, 0.84)
    avr = np.mean(dat_to_plot_cleaned)
    plt.gca().add_patch(Rectangle((low_partial, index - height / 2),
                                  high_partial - low_partial, height, color=color, zorder=1, label=label))
    plt.scatter(dat_to_plot_cleaned[:num_of_scater_to_plot], index +
                np.zeros(num_of_scater_to_plot), color=color * 0.8, zorder=2)
    plt.plot([avr], [index], 'x', color="black", zorder=3)


def get_cur_x_of_draw_scater_line():
    return current_index


def show_with_heatmap(x, y, z, res, size):
    fig = plt.figure()
    ax = fig.add_subplot()
    N_in_pixle = np.zeros((int(res * size), int(res * size)))
    image = np.ma.zeros((int(res * size), int(res * size)))
    for i in range(len(z)):
        if np.isnan(x[i]) or np.isnan(y[i]) or np.isnan(z[i]):
            continue
        curx = int(round(x[i] * res))
        cury = int(round(y[i] * res))
        image[cury, curx] = ((image[cury, curx] * N_in_pixle[cury, curx]) + z[i]) / (N_in_pixle[cury, curx] + 1)
        N_in_pixle[cury, curx] += 1

    image[image == 0] = np.ma.masked
    plot = ax.imshow(X=image, cmap="jet", interpolation='None',
                     vmin=np.nanmin(z), origin="lower", extent=(0, size, 0, size))
    fig.colorbar(plot, ax=ax)
    return ax


def show_3D_scatter_projection(x, y, z):
    fig = plt.figure()
    ax = fig.add_subplot()
    scatter = ax.scatter(x, y, c=z, cmap="jet")
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    plt.colorbar(scatter)
    return ax


def show_3D_scatter(x, y, z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z)
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    ax.set_xlim(0, np.nanmax(x))
    ax.set_ylim(np.nanmax(y), 0)
    ax.set_zlim(0, np.nanmax(z))
    return ax


def show_2D_scatter(x, y):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(x, y)
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    return ax


def draw_W_N_scater(N, W):
    ax = show_2D_scatter(N, W)
    ax.set_xlabel('Num of balls')
    ax.set_ylabel('Wight in gr')
    ax.set_xlim(0, np.nanmax(N))
    ax.set_ylim(0, np.nanmax(W))
    # not_nan_indexes = np.isfinite(N)*np.isfinite(W)
    # slope = statistics_utility.proportion_regretion(N[not_nan_indexes], W[not_nan_indexes])
    # x = np.array([0, np.nanmax(N)])
    # ax.plot(x, slope[0] * x)
    # ax.plot(x, slope[1] * x)
    # return slope


def draw_mapped_mass_from_N_vector(Nw, Nb, Nk, vmin=None, vmax=None, **kwargs):
    pW = get_distribution_of_masses_around_N_vector(1000, Nw, Nb, Nk)
    pW_mean = np.mean(pW[:, 0]), np.mean(pW[:, 1]), np.mean(pW[:, 2])
    pW_std = np.std(pW[:, 0]), np.std(pW[:, 1]), np.std(pW[:, 2])
    plt.gca().add_artist(Ellipse(pW_mean[:2], pW_std[0] * 2, pW_std[1] * 2, facecolor="none", edgecolor="k"))
    plt.gca().add_artist(Ellipse(pW_mean[:2], pW_std[0] * 4, pW_std[1] * 4, facecolor="none", edgecolor="k"))
    plt.scatter(pW_mean[0], pW_mean[1], c=pW_mean[2], vmin=vmin, vmax=vmax, marker="x", **kwargs)
    plt.xlim(pW_mean[0] - pW_std[0] * 3, pW_mean[0] + pW_std[0] * 3)
    plt.ylim(pW_mean[1] - pW_std[1] * 3, pW_mean[1] + pW_std[1] * 3)
