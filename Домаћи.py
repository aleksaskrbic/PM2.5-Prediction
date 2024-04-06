#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 20:23:55 2021

@author: vladimir
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("/home/vladimir/Desktop/Домаћи 1/ShenyangPM20100101_20151231.csv")
df_niki = pd.read_csv("/home/vladimir/Downloads/NIkolina/ChengduPM20100101_20151231.csv")


# %% 

print(df.shape)
print(df.dtypes)

df.isna().sum() / len(df) #Suma NaN vrednosti

df.PM_Taiyuanjie.isna().sum()
df.PM_Xiaoheyan.isna().sum()

# Menjamo ime koloni da bismo joj proverili nedostajuce vrednosti
df.columns = ["No","year","month","day","hour","season","PM_Taiyuanjie", "PM_US Post",
      "PM_Xiaoheyan","DEWP","HUMI","PRES","TEMP","cbwd","lws","precipitation",
           "lprec"]      





# %% Izbacivanje obelezja tj kolona PM_Taiyuanjie, PM_Xiaoheyan (koje imaju preko 50% NaN vrednosti)

df.drop(columns = ['PM_Taiyuanjie', 'PM_Xiaoheyan'], inplace = True)

df.dropna(axis = 0, subset = ['PM_US Post'], inplace = True)
# Provera da li su svi podaci iz Kolone PM_US_Post nedostajuci

print(df.isna().sum() / len(df))



#population = population.sort_values(by = ["abbreviation","ages","year"])
#population = population.fillna(method="bfill")






        






#%%
