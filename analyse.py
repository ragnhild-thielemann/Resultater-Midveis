#%%

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
MAT1105 = ([17]*7 +[16]*17 +[15]*21 +[14,13,12]*11 +[11]*8 +[10]*12 +[9]*6 +[8]*10 +[7,6,4]*4 +[5]
)

s = np.asarray(MAT1105)
s = np.sort(s)
n = len(s)
median = s[int(n/2)]
print(f"Medianen for MAT1105 {(median/17):.2f}")
plt.grid()
forventing = (np.sum(s))/n
print(f"Forventningen for MAT1105 {(forventing/17):.2f} poeng for en student")
plt.xlabel("Antall poeng")
plt.ylabel("Antall studenter")
varians = np.asarray([(x/17-forventing/17)**2 for x in MAT1105])
print(np.sum(varians)/n)

plt.hist(s,color = "pink", edgecolor = "black")
plt.title("Poengfordeling for MAT1105")
plt.show()

plt.show()
a_mat = []
with open("fil_MAT.txt","r") as fil:
    for linje in fil:
        verdier = linje.split(",")
        for k in verdier:
            a_mat.append(int(k))


a = np.asarray(a_mat)
a_mat = np.sort(a_mat)
n = len(a_mat)
median = a_mat[int(n/2)]
print(f"Medianen for MAT1100 {(median/15):.2f}")

forventing = (np.sum(a))/n
print(f"Forventningen for MAT1100 {(forventing/15):.2f} poeng for en student")
varians = np.asarray([(x/15-forventing/15)**2 for x in a])
print(f"Variansen er {(np.sum(varians)/n):.2f} for fordelingen av poeng")
print("Vi kan dermed si at matten er positivt skjev")
plt.hist(a,color = "hotpink", edgecolor = "black")
plt.title("Poengfordeling for MAT1100")
plt.xlabel("Antall poeng")
plt.ylabel("Antall studenter")
plt.show()


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
print(f"Medianen for STK1100 er {median/20}")

forventing = (np.sum(a))/n
print(f"Forventningen for STK1100 {(forventing/20):.2f} poeng for en student")
varians = np.asarray([((x/20)-(forventing/20))**2 for x in a])
print(f"Variansen er {(np.sum(varians)/n):.2f} for fordelingen av poeng")
print("Statestikken er derfor negativt skjev")
plt.hist(a,color = "skyblue",edgecolor = "black")
plt.xlabel("Antall poeng")
plt.ylabel("Antall studenter")
plt.title("Poengfordeling for STK1100")
plt.show()




# --- NORMALISER TIL PROSENT AV MAKS ---
mat1105_norm = s / 17
mat1100_norm = a_mat / 15
stk1100_norm = a / 20

# --- LAG FELLES PERCENTILER ---
p = np.linspace(0, 100, 100)

q_mat1105 = np.percentile(mat1105_norm, p)
q_mat1100 = np.percentile(mat1100_norm, p)
q_stk1100 = np.percentile(stk1100_norm, p)

# --- PLOT ---
plt.plot(p, q_mat1105, label="MAT1105",color = "purple")
#plt.plot(p, q_mat1100, label="MAT1100")
plt.plot(p, q_stk1100, label="STK1100",color = "hotpink")

plt.xlabel("Percentil")
plt.ylabel("Andel av maks poeng")
plt.title("Sammenligning av fag (percentiler)")
plt.legend()
plt.grid()
plt.show()

