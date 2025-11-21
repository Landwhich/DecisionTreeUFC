import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# plt.show()
import warnings

warnings.filterwarnings('ignore')

data = './datasets/car.data'
df = pd.read_csv(data, header=None)

col_names = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'class']
df.columns = col_names

### view metadata of dataset
# print(df.shape)
# print(df.head())
# print(df.info())

# for col in col_names:
#     print(df[col].value_counts())

print(df['class'].value_counts())


