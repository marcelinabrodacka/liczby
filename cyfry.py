import pandas as pd
import numpy as np
import aseegg as ag
import scipy.stats as st
import matplotlib.pyplot as plt
dane = pd.read_csv(r"sub01trial03.csv", delimiter=',', engine='python')
nieprzefiltrowanysygnal=dane['sygnal']
przefiltrowanysygnal=ag.pasmowozaporowy(nieprzefiltrowanysygnal, 200, 49, 51)
sygnal=ag.pasmowoprzepustowy(przefiltrowanysygnal, 200, 1, 50)
cyfry=dane['cyfra']

for i in range (7602):
    if sygnal[i]>=0.05 and sygnal[i+1]<0.05:
        print(cyfry[i])
