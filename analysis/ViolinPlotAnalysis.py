# 小提琴图
# 小提琴图结合了箱线图和核密度估计图，以更全面地展示数据的分布情况。
# 在小提琴图中，你可以使用flag作为x轴，totalTime作为y轴，绘制两个小提琴图，分别表示flag为0和1的情况。
# 小提琴图的宽度表示数据密度，所以你可以直观地比较两种情况下totalTime的分布形状和密度。
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 假设你有一个名为data的数据框，其中包含flag和totalTime两列数据

sns.set_context(font_scale=1.5)
df=pd.read_excel("../data/Communication.xlsx")

print(df.keys())
data1 = df[['total','flag']]
data1['total']=data1['total'].astype(float).fillna(0.0,inplace=True)
# data1['flag']=data1['flag'].astype(int).fillna(1,inplace=True)
data1 = df.dropna()

# 绘制小提琴图
sns.violinplot(x='flag', y='total', data=data1,cmap='RdBu')

# 设置图形标题和轴标签
# plt.title('Distribution of totalTime by flag')
plt.xlabel('是否出行标识', fontsize=16, fontproperties="SimHei")
plt.ylabel('当月总通话次数', fontsize=16, fontproperties="SimHei")

# 显示图形
plt.show()