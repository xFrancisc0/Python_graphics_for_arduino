import numpy as np
import matplotlib.pyplot as plt
import json

import pandas as pd


with open('input.json', 'r') as outfile:  
    var = json.load(outfile)
    
df = pd.DataFrame(var)
print(df)

fig, axarr = plt.subplots()
axarr = df.plot(x='Tiempo', y='Temperatura')
fig.savefig("Figura1.png")
plt.show()