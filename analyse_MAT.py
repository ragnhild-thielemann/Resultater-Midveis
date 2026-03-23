#%%

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

a = []
with open("fil_MAT.txt","r") as fil:
    for linje in fil:
        verdier = linje.split(",")
        for k in verdier:
            a.append(int(k))


a = np.asarray(a)
a = np.sort(a)
n = len(a)
median = a[int(n/2)]
print(f"Medianen er {(median/15):.2f}, som tilvarer 0.5-prosentilen")

forventing = (np.sum(a))/n
print(f"Forventningen er {(forventing/15):.2f} poeng for en student")
varians = np.asarray([(x-forventing)**2 for x in a])
print(f"Variansen er {(np.sum(varians)/n):.2f} for fordelingen av poeng")

plt.hist(a,color = "hotpink", edgecolor = "black")
plt.show()