import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import linregress

def sample_independent_sum_of_distributions(arr_of_distributions,num_of_samples):
    arr_of_distributions = [not_nan(dist) for dist in arr_of_distributions]
    samples = np.zeros(num_of_samples)
    for dist in arr_of_distributions:
        samples += np.random.choice(dist,num_of_samples)
    return samples

def sample_independent_sum_of_dependant_multydistributions(num_of_samples,*set_of_arr_of_distributions):
    """
    for example if a,b,c,A,B,C are all distributions, and the input is (num_of_samples,[a,b,c],[A,B,C]) then randomly selects ri,qi,ti and returns the two sets:
    -   {a_ri + b_qi + c_ti | for i in range(num_of_samples)}
    -   {A_ri + b_qi + c_ti | for i in range(num_of_samples)}
    * also there are size constraints on the input: size(a) = size(A), size(B) = size(B), size(c) = size(C)
    :param num_of_samples: number of sample to randomly select
    :param set_of_arr_of_distributions: example set_of_arr_of_distributions = ([collection_of_],[])
    :return: a set of distributions. if set_of_arr_of_distributions is of shape (2,3,100), return value is of shape (2,num_of_samples)
    """
    # remove nan values from rows (only need to remove values where in the example )
    not_nan_idx = [None]*len(set_of_arr_of_distributions[0])
    for arr_index in range(len(set_of_arr_of_distributions[0])):
        not_nan_idx[arr_index] = indexes_not_nan(*[set_of_arr_of_distributions[i][arr_index] for i in range(len(set_of_arr_of_distributions))])

    set_of_arr_of_distributions = \
        [[set_of_arr_of_distributions[i][arr_index][not_nan_idx[arr_index]] for
          arr_index in range(len(set_of_arr_of_distributions[i]))] for
          i in range(len(set_of_arr_of_distributions))]

    samples = np.zeros((len(set_of_arr_of_distributions),num_of_samples))
    for arr_index in range(len(set_of_arr_of_distributions[0])):
        chosen_indexes = np.random.choice(np.arange(len(set_of_arr_of_distributions[0][arr_index])),num_of_samples)
        for set_index in range(len(set_of_arr_of_distributions)):
            samples[set_index] += set_of_arr_of_distributions[set_index][arr_index][chosen_indexes]
    return samples

def proportion_regretion(x_data,y_data):
    proportion = lambda x,a:a*x
    popt, pcov = curve_fit(proportion,x_data,y_data,p0=1)
    std = pcov[0,0]**0.5
    return [popt[0]+std/2,popt[0]-std/2]

def linier_regretion(x_data,y_data):
    return linregress(x_data,y_data)

def indexes_not_nan(*args):
    indexes = np.isfinite(args[0])
    for arg in args:
        indexes *= np.isfinite(arg)
    return indexes

def not_nan(*args):
    indexes = indexes_not_nan(*args)
    if len(args) == 1:
        return args[0][indexes]
    else:
        return [arg[indexes] for arg in args]

def std_of_graph(x,p):
    return np.sum(p*x**2)-np.sum(p*x)**2

if __name__=="__main__":
    from read import Nw ,Ww ,Nb ,Wb ,Nk ,Wk ,Wsum
    plt.scatter(Ww, Wsum, label="Wsum Vs Ww")
    plt.scatter(Wb, Wsum, label="Wsum Vs Wb")
    plt.scatter(Wk, Wsum, label="Wsum Vs Wk")
    plt.figure()
    plt.scatter(Ww, Wb + Wk, label="black+brown vs white")
    plt.scatter(Wb, Wb + Wk, label="black+brown vs brown")
    plt.scatter(Wk, Wb + Wk, label="black+brown vs black")
    plt.legend()
    plt.figure()
    plt.scatter(Wb, Wk, label="black vs brown")
    plt.legend()
    plt.figure()
    plt.scatter(Wb, Ww, label="white vs brown")
    plt.scatter(Wk, Ww, label="white vs black")
    a = np.corrcoef(*not_nan(Ww, Wsum))
    plt.legend()
    plt.show()







