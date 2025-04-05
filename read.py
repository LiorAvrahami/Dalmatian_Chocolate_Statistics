import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import drawing_utility


# class array_with_description(np.ndarray):
#     description = None
#     def __init__(self):

def parse(str):
    try:
        return float(str)
    except ValueError:
        return np.nan


weight_plastic = 3.03

file = open("Dalmati_data_v3.csv", "r")
Lines = file.readlines()
data = []
for Line in Lines:
    Line = Line.replace(", ", " ").replace(" ,", " ").replace(",", " ").replace("  ", " ").split(" ")
    data.append(np.array([parse(Line_word) for Line_word in Line]))

Nw = []
Ww = []
Nb = []
Wb = []
Nk = []
Wk = []
for point in data:
    Nw.append(point[0])
    Ww.append(point[1] - weight_plastic)
    Nb.append(point[2])
    Wb.append(point[3] - weight_plastic)
    Nk.append(point[4])
    Wk.append(point[5] - weight_plastic)

Nw = np.array(Nw)
Ww = np.array(Ww)
Nb = np.array(Nb)
Wb = np.array(Wb)
Nk = np.array(Nk)
Wk = np.array(Wk)
Wsum = Ww + Wb + Wk

packege_Nw = 15
packege_Nb = 24
packege_Nk = 14

Nw_avr = np.nanmean(Nw)
Nk_avr = np.nanmean(Nk)
Nb_avr = np.nanmean(Nb)

if __name__ == "__main__":
    pass

    # Wk.flags
    ax = drawing_utility.show_with_heatmap(Wk, Wb, Ww, 1.5, 20)
    plt.xlabel("weight black gr")
    plt.ylabel("weight brown gr")
    plt.title("weight white gr vs weight black,brown")
    plt.grid()
    # drawing_utility.show_with_heatmap(Wk, Wb, Wsum, 3, 20)
    # ax = drawing_utility.show_with_heatmap(Nw, Nb, Nk, 1, 40)
    # drawing_utility.show_with_heatmap([packege_Nw], [packege_Nb], [packege_Nk], 1, 40)
    plt.show()
