
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
import pandas as pd

sns.set_context(font_scale=1.5)
df=pd.read_excel("../data/Communication.xlsx")
df=df.dropna()
dp_keys=list(df.keys())
my_pca=PCA(n_components=18)
lower_mat=my_pca.fit_transform(df)
print(my_pca.explained_variance_ratio_)
ax=sns.heatmap(pd.DataFrame(lower_mat).corr(), annot=True, vmin=-1, vmax=1,cmap=sns.color_palette("Reds",n_colors=256)) # 指定颜色 cmap=sns.color_palette("RdBu",n_colors=128)
# 设置x轴和y轴标签
ax.set_xticklabels(dp_keys, rotation=90, fontproperties="SimHei")
ax.set_yticklabels(dp_keys, rotation=0, fontproperties="SimHei")
plt.tight_layout(rect=[0.945, 0.2, 0.115, 1])
plt.show()