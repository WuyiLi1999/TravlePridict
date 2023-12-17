import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set_context(font_scale=1.5)
df=pd.read_excel("../data/Internet.xlsx")
# df=pd.read_csv("../data/toUser_1_train.csv")
result=df['map_app_visit_cnt']
# 绘制箱线图
sns.boxplot(data=result,color='red')
plt.xlabel('当月地图类App访问次数', fontproperties="SimHei", fontsize=16)
# 显示图形
plt.show()