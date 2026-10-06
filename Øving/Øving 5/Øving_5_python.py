# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 10:17:16 2026

@author: Aksel
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#Oppgave 1

Tid=np.linspace(0, 24, 1000)
#Verdier for figur 1
Lo1=1; #Grunnlasten
Ai1=100; #Ampliituden til komponeneten i;høy
mu1=4; #Tidspunktet for topp kl4
sigma1=1; #Bredden på komponenten; small topp

#Verdier for figur 2
Lo2=1; #Grunnlasten
Ai2=20; #Ampliituden til komponeneten i;lav
mu2=18; #Tidspunktet for topp kl18
sigma2=5; #Bredden på komponenten bred topp

L1=Lo1+Ai1*np.exp(-(Tid-mu1)**2/(2*sigma1**2));
L2=Lo2+Ai2*np.exp(-(Tid-mu2)**2/(2*sigma2**2));

plt.plot(Tid, L1)
plt.xlabel("TID")
plt.ylabel("Belastning")
plt.title("Belastning over tid")
plt.grid()
plt.show()


plt.plot(Tid, L2)
plt.xlabel("TID")
plt.ylabel("Belastning")
plt.title("Belastning over tid 2")
plt.grid()
plt.show()



#Oppgave 3
#linje 4-99 (100 blir 2015.01.02)
#Jeg har valg å bruke DE_load_actual som jeg tror er faktisk last for Tyskland. 
#Jeg velger å se på dataen for den første dagen som er 2015.01.01.
df = pd.read_csv( "time_series_15min_singleindex.csv",parse_dates=[0], index_col=0, dayfirst=True);
Tid2 = df.index[4:100]
Tyskland_load = df["DE_load_actual_entsoe_transparency"] ;
Tyskland_load_dag =Tyskland_load[4:100]
t = np.linspace(0,24,96);

#Kode som er med Generell modelering som vi brukt i oppgave 1
L0 = 41000 #Jeg ser hvor dataen starter

#parameter for natt
A1 = -2500 #Jeg ser at den er -2500 en L0 ca kl 4
mu1 = 4 #dette skjer ca kl:4
sigma1 = 2 

#Parameter for dag
A2 = 7000 #Jeg ser at den er ca 7000 større en L0
mu2 = 11 #Dette skjer ca kl:11 
sigma2 = 2 

#Parameter for kveld
A3= 13000; #Jeg ser at den er ca 14000 større en L0
mu3 = 17 # Dette skjer ca kl:17
sigma3 = 2 
L = (L0 + A1*np.exp(-(t-mu1)**2/(2*sigma1**2))+ A2*np.exp(-(t-mu2)**2/(2*sigma2**2))+A3*np.exp(-(t-mu3)**2/(2*sigma3**2)))


plt.plot(Tid2.hour, Tyskland_load_dag)
plt.xlabel("TID")
plt.ylabel("Last")
plt.title("Last i tyskland")
plt.grid()
plt.show()

plt.plot(t, L)
plt.xlabel("TID")
plt.ylabel("Last")
plt.title("Last i tyskland modellert kurve")
plt.grid()
plt.show()

plt.plot(t, L, label="Formel")
plt.plot(t, Tyskland_load_dag, label="Data")
plt.xlabel("TID")
plt.ylabel("Last")
plt.title("Last i tyskland begge")
plt.grid()
plt.legend()
plt.show()

