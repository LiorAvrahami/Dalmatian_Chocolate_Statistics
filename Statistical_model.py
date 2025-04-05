import numpy as np
import scipy.special


def get_normal(normal_w, normal_b):
    # assert 1-normal_w**2-normal_b**2 >= 0
    return (normal_w, normal_b, (1 - normal_w**2 - normal_b**2)**0.5)


def statistical_model(normal_w=0.69115, normal_b=0.49616, mean=16.05390, std=1.20868):
    prob_w = 0.21896850868981296
    prob_b = 0.40271531669606014
    prob_k = 0.37831617461412687
    pi = np.array([prob_w, prob_b, prob_k])

    normal = get_normal(normal_w, normal_b)

    def get_p_at_x(Ww, Wb, Wk):
        Ww_Wb_Wk = np.stack([Ww, Wb, Wk], axis=-1)
        Ww_Wb_Wk = Ww_Wb_Wk[np.any(np.isfinite(Ww_Wb_Wk), axis=-1)]
        d = np.dot(Ww_Wb_Wk, normal)
        d = (d - mean) / std
        p = np.exp(-0.5 * d**2) / (np.sqrt(2 * np.pi) * std)

        B = (scipy.special.gamma(1 + np.sum(Ww_Wb_Wk, axis=-1)) /
             np.product(scipy.special.gamma(1 + Ww_Wb_Wk), axis=-1)) *         \
            np.product(pi[np.newaxis, :] ** Ww_Wb_Wk, axis=-1)

        p *= B
        return p
    return get_p_at_x


W_vector_distribution = None
w_prob_densities = None


def get_p_value_of_mass_vector(Ww, Wb, Wk, normal_w=0.69115, normal_b=0.49616, mean=16.05390, std=1.20868):
    get_p_at_W_vec = statistical_model(normal_w, normal_b, mean, std)

    global W_vector_distribution, w_prob_densities
    if W_vector_distribution is None:
        W_vector_distribution = np.zeros((0, 3))
        w_prob_densities = np.zeros((0))
        while w_prob_densities is None or len(w_prob_densities) < 10000:
            W_matrix = np.random.uniform(0, 25, (1000000, 3))
            prob_densities = get_p_at_W_vec(W_matrix[:, 0], W_matrix[:, 1], W_matrix[:, 2])
            indexes = prob_densities > np.random.uniform(0, 1, prob_densities.shape)
            w_prob_densities = np.concatenate([w_prob_densities, prob_densities[indexes]])
            W_vector_distribution = np.concatenate([W_vector_distribution, W_matrix[indexes,:]])

    prob_density_0 = get_p_at_W_vec(Ww, Wb, Wk)
    p_value = np.mean(prob_density_0 > w_prob_densities)
    return p_value
