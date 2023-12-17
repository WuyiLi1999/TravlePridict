# 通信信息分析
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
import pandas as pd

sns.set_context(font_scale=1.5)
df=pd.read_excel("../data/Communication.xlsx")
df=df.dropna()
# 绘制箱线图
# sns.boxplot(data=df['当月总通话次数'])
# plt.xlabel('当月总通话次数', fontproperties="SimHei", fontsize=16)
# # 显示图形
# plt.show()
# print(df['当月总通话次数'])
dp_keys=list(df.keys())
my_pca=PCA(n_components=18)
lower_mat=my_pca.fit_transform(df)
print(my_pca.explained_variance_ratio_)
ax=sns.heatmap(pd.DataFrame(lower_mat).corr(), annot=True, vmin=-1, vmax=1,cmap=sns.color_palette("Reds",n_colors=256)) # 指定颜色 cmap=sns.color_palette("RdBu",n_colors=128)
# 设置x轴和y轴标签
ax.set_xticklabels(dp_keys, rotation=90, fontproperties="SimHei")
ax.set_yticklabels(dp_keys, rotation=0, fontproperties="SimHei")
plt.show()