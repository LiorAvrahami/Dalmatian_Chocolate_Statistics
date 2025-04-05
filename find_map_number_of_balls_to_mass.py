import numpy as np
import scipy.special


def get_expected_total_mass(Nw, Nb, Nk, b, Rw, Rb, Rk):
    N_vec = np.stack([Nw, Nb, Nk], axis=-1)
    R_vec = np.stack([Rw, Rb, Rk], axis=-1)
    return N_vec * ((b - np.dot(N_vec, R_vec))[..., np.newaxis])


def probability_of_mass_vector_under_N_vector(Ww, Wb, Wk, Nw, Nb, Nk, std=0.9165564292659392, a=1.16415, R=0.0107086875):
    Wp = get_expected_total_mass(Nw, Nb, Nk, a, R, R, R)
    print(Wp)
    W_vec = np.stack([Ww, Wb, Wk], axis=-1)
    d = (W_vec - Wp) / std
    return np.product(np.exp(-0.5 * d**2) / (np.sqrt(2 * np.pi) * std), axis=-1)


def get_pvalue_of_point(Ww, Wb, Wk, Nw, Nb, Nk, std=0.9165564292659392, a=1.16415, R=0.0107086875):
    Wp = get_expected_total_mass(Nw, Nb, Nk, a, R, R, R)
    W_vec = np.stack([Ww, Wb, Wk], axis=-1)
    d = (W_vec - Wp) / (std * (2**0.5))
    return (1 + scipy.special.erf(d)) / 2


def get_distribution_of_masses_around_N_vector(num_points, Nw, Nb, Nk, std=0.9165564292659392, a=1.16415, R=0.0107086875):
    ret = np.zeros((0, 3))
    while len(ret) < num_points:
        new_w_vector = np.random.uniform(0, 20, (10000, 3))
        p_arr = probability_of_mass_vector_under_N_vector(
            new_w_vector[:, 0], new_w_vector[:, 1], new_w_vector[:, 2], Nw, Nb, Nk, std, a, R)
        indexes = np.random.uniform(0, 1, p_arr.shape) < p_arr
        ret = np.concatenate([ret, new_w_vector[indexes, :]])
    return ret
