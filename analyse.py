#%%

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

a = []
with open("fil_STK.txt","r") as fil:
    for linje in fil:
        verdier = linje.split()
        a.append(int(verdier[1]))
        fil.readline()
    
a = np.asarray(a)
a = np.sort(a)
n = len(a)
median = a[int(n/2)]
print(f"Medianen er {median}, som tilvarer 0.5-prosentilen")

forventing = (np.sum(a))/n
print(f"Forventningen er {forventing:.2f} poeng for en student")
varians = np.asarray([(x-forventing)**2 for x in a])
print(f"Variansen er {(np.sum(varians)/n):.2f} for fordelingen av poeng")

plt.hist(a,color = "pink",edgecolor = "black")
plt.xlabel("Antall poeng")
plt.ylabel("Antall studenter")
plt.title("Nominell fordeling av antall poeng per student")
plt.show()

plt.hist(a,color = "skyblue",edgecolor = "black",density= True)
plt.xlabel("Antall poeng")
plt.ylabel("Sansynlighet for poengsummen")
plt.title("Sansynlighetsfordeling for poengsummene")
plt.show()

#q-q-plot

p_verdier = []
z_verdier = []
for i in range(1,len(a)+1):
    p = (i-0.5)/(len(a))
    p_verdier.append(p)
    z = norm.ppf(p)
    z_verdier.append(z)

plt.plot(a,z_verdier,".",color = "hotpink")
plt.xlabel("Reele verdier")
plt.ylabel("z-prosentiler")
plt.title("Q-Q-plot")
plt.grid()
plt.show()
