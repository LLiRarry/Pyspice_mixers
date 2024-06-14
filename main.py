import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import json
with open('minxer_data.json', 'r') as f:
    data = json.load(f)

Rf=data['RF']
Rf=np.array(Rf).flatten().tolist()
print(len(Rf))