# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 10:06:26 2026

@author: Aksel
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Oppgave 1

t = np.linspace(0, 24, 500)
A = 800
mu = 13
sigma = 2

Gauss = A * np.exp(-(t - mu)**2 / (2 * sigma**2))

plt.plot(t, Gauss)
plt.xlabel("Tid [timer]")
plt.ylabel("Innstråling [W/m²]")
plt.grid()
plt.show()


#Oppgave 5
#Jeg leser inn dataen skipper første 8 radene   
df = pd.read_csv("Data_tid.csv", skiprows=8)


#Jeg henter ut 1 dag fra dataen. 
August = df[df["time"].astype(str).str.startswith("20230815")]

#Gb har object som type så gjør det om til float
August["Gb(i)"] = pd.to_numeric(August["Gb(i)"]) 

#Jeg regner ut total solinnstråling med disse 3 variablene 
Gb=August["Gb(i)"] #direkte solinnstråling
Gd=August["Gd(i)"] #diffus solinnstråling
Gr=August["Gr(i)"] #reflektert solinnstråling
Tid=np.linspace(0,24,24) #Lager tid for data

G = Gb + Gd + Gr

plt.plot(Tid,G)
plt.xlabel("Tid")
plt.ylabel("Global solinnstråling")
plt.show()


#Oppgave 6/7
#Jeg legger det til igjen her slik at jeg fortsatt får første bilde 
#når jeg skal endre på a,mu og sigma
t = np.linspace(0, 24, 500)
A = 890
mu = 13
sigma = 1.1

Gauss = A * np.exp(-(t - mu)**2 / (2 * sigma**2))


plt.plot(Tid, G, label="Data")
plt.plot(t, Gauss, label="Gauss")
plt.xlabel("Tid")
plt.ylabel("Solinnstråling")
plt.grid()
plt.legend()
plt.show()


