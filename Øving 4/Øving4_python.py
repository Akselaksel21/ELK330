# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 21:31:08 2026

@author: Aksel
"""
#Felles for alle oppgaver
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv( "load_data.csv",parse_dates=[0], index_col=0, dayfirst=True);
df.index=pd.to_datetime(df.index, utc=True);


#Oppgave 4
print(df.head())


#Oppgave 5

print (df.index[0])



#Oppgave 6
day = df.loc["2026-01-01"];

#Jeg lager 2 forskjellige plott siden jeg har en y-akse med verdier som overlapper
plt.plot(day.index, day["Consumption"], label="Consumption")
plt.title("Consumption Lastprofil 01.01.2026")
plt.xlabel("Tid")
plt.ylabel("MW")
plt.grid()
plt.legend()
plt.show()

plt.plot(day.index, day["Production"], label="Production")
plt.title("Production Lastprofil 01.01.2026")
plt.xlabel("Tid")
plt.ylabel("MW")
plt.grid()
plt.legend()
plt.show()



#Oppgave 7

df["Production"] = pd.to_numeric(df["Production"].astype(str).str.replace(",", "."))
df["Consumption"] = pd.to_numeric(df["Consumption"].astype(str).str.replace(",", "."))
df["Netto"] = df["Production"]-df["Consumption"]

print(df["Netto"])

#Oppgave 8

Pro_max=df["Production"].max()
Pro_min=df["Production"].min()
Pro_mean=df["Production"].mean()

print(Pro_max)
print(Pro_mean)
print(Pro_min)


#Oppgave 9


Nett_max=df["Netto"].max()
Nett_min=df["Netto"].min()
print(Nett_max)
print(Nett_min)


#Oppgave 10
Sum = df["Production"].sum()
print(Sum)


#Oppgave 11

df.plot(y=["Production", "Consumption"],figsize=(10,5))

plt.title("Produksjon og forbruk som funksjon av tid")
plt.xlabel("Tid")
plt.ylabel("MW")
plt.grid(True)
plt.legend()
plt.show()

#Oppgave 12
df.plot(y=["Production", "Consumption", "Netto"],figsize=(10,5))

plt.title("Produksjon, forbruk og nettoeffekt som funksjon av tid")
plt.xlabel("Tid")
plt.ylabel("MW")
plt.grid(True)
plt.legend()
plt.show()

#Oppgave 13


#Oppgave 14
Max_Pro_index= df["Production"].idxmax()
Max_Con_index= df["Consumption"].idxmax()
print(Max_Pro_index)
print(Max_Con_index)




