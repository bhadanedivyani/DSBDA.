import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x=np.array([95,85,80,70,60]) 
y=np.array([85,95,70,65,70]) 

model=np.polyfit(x,y,1)
model

predict=np.poly1d(model)
predict(65)

y_pred=predict(x)
y_pred

