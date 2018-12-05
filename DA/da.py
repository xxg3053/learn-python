import pandas as pd
import numpy as np

# 1. Read Data
df = pd.read_csv("train.cvs")
label = df['TARGET']
df = df.drop(['ID', 'TARGET'], axis=1)
# Basic Analysis 计数类
#1. Missing Value
missSet = [np.nan, 9999999999, -999999 ]

#2. count distinct
len(df.iloc[:, 0].unique())

count_un = df.iloc[:, 0:3].apply(lambda x:len(x.unique()))

#3. Zero Values
np.sum(df.iloc[:, 0] == 0)
count_zero = df.iloc[:, 0:3].apply(lambda x:np.sum(x == 0))
