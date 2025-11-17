import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.show()
import warnings

warnings.filterwarnings('ignore')

data = 'C:/datasets/car.data'
df = pd.read_csv(data, header=None)

df.shape