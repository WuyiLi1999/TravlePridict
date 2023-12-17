# 用户上网信息分析
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("../data/toUser_1_train.csv")
df=df.iloc[:,31:53]

print(df.head(10))