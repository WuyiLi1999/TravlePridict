# 皮尔逊相关系数极端
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_context(font_scale=1.5)
df=pd.read_excel("../data/Internet.xlsx")
df=df.dropna()
# 计算皮尔逊相关系数
corr_matrix = df.corr()
dp_keys=list(df.keys())
# 绘制热力图
plt.figure(figsize=(10, 8))  # 设置图形大小
ax=sns.heatmap(corr_matrix, annot=True, cmap='RdBu', vmin=-1, vmax=1)

# 设置标题
# plt.title('Pearson Correlation Heatmap')
# 设置x轴和y轴标签
ax.set_xticklabels(dp_keys, rotation=90, fontproperties="SimHei")
ax.set_yticklabels(dp_keys, rotation=0, fontproperties="SimHei")
# 显示图形
plt.show()