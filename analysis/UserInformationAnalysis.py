#用户基础信息分析

import pandas as pd
import numpy as np
import scipy.stats as ss
import seaborn as sns
import matplotlib.pyplot as plt

# df=df.iloc[:,:13]
df=pd.read_csv("../data/toUser_1_train.csv")

## 交叉分析：采用热力图的形式进行分析可视化
# 年龄段进行交叉分析
def Age_CrossOverAnalysis(df):
    df_age = df[['age', 'flag']]
    df_cleaned = df_age.dropna()
    df_cleaned['age'] = df_cleaned['age'].astype(float)
    df_cleaned['age'] = (df_cleaned['age'] // 10).astype(int)
    dp_indices = df_cleaned.groupby('age').indices
    dp_keys = list(dp_indices.keys())
    level3 = df_age["flag"].iloc[dp_indices[3]].values
    level4 = df_age["flag"].iloc[dp_indices[5]].values
    # P值统计量
    print(ss.ttest_ind(level3, level4))
    dp_t_mat = np.zeros([len(dp_keys), len(dp_keys)])
    for i in range(len(dp_keys)):
        for j in range(len(dp_keys)):
            p_value = ss.ttest_ind(df_age["flag"].iloc[dp_indices[dp_keys[i]]].values,
                                   df_age["flag"].iloc[dp_indices[dp_keys[j]]].values)[1]
            if p_value < 0.05:
                dp_t_mat[i][j] = -1
            else:
                dp_t_mat[i][j] = p_value
    # 使用热力图进行可视化展示
    sns.heatmap(dp_t_mat, annot=True, xticklabels=dp_keys, yticklabels=dp_keys)
    plt.show()

def income_CrossOverAnalysis(df):
    df_age = df[['income_level_id', 'flag']]
    df_cleaned = df_age.dropna()
    df_cleaned['income_level_id'] = df_cleaned['income_level_id'].astype(int)
    dp_indices = df_cleaned.groupby('income_level_id').indices
    dp_keys = list(dp_indices.keys())
    level3 = df_age["flag"].iloc[dp_indices[3]].values
    level4 = df_age["flag"].iloc[dp_indices[5]].values
    # P值统计量
    print(ss.ttest_ind(level3, level4))
    dp_t_mat = np.zeros([len(dp_keys), len(dp_keys)])
    for i in range(len(dp_keys)):
        for j in range(len(dp_keys)):
            p_value = ss.ttest_ind(df_age["flag"].iloc[dp_indices[dp_keys[i]]].values,
                                   df_age["flag"].iloc[dp_indices[dp_keys[j]]].values)[1]
            if p_value < 0.05:
                dp_t_mat[i][j] = -1
            else:
                dp_t_mat[i][j] = p_value
    # 使用热力图进行可视化展示
    sns.heatmap(dp_t_mat, annot=True, xticklabels=dp_keys, yticklabels=dp_keys)
    plt.show()

## 性别、是否已婚、是否已育、是否有老人、是否有车这些指标与是否出行的相关性分析
def CrossOverAnalysis(df):
    df1 = df[["sex", "ismarr", "fertile", "haveold", "has_car", "flag"]]
    df1.loc[:, 'sex'] = df1['sex'].fillna('0').astype(int)
    df1.loc[:, 'ismarr'] = df1['ismarr'].fillna('0').astype(int)
    df1.loc[:, 'fertile'] = df1['fertile'].fillna('0').astype(int)
    df1.loc[:, 'haveold'] = df1['haveold'].fillna('0').astype(int)
    df1.loc[:, 'has_car'] = df1['has_car'].fillna('0').astype(int)
    df1.loc[:, 'flag'] = df1['flag'].astype(int)
    # print(df1['sex'].isna().any())
    # print(df1['ismarr'].isna().any())
    # print(df1['fertile'].isna().any())
    # print(df1['haveold'].isna().any())
    # print(df1['has_car'].isna().any())
    # print(np.isinf(df1['sex']).any())
    # print(np.isinf(df1['ismarr']).any())
    # print(np.isinf(df1['fertile']).any())
    # print(np.isinf(df1['haveold']).any())
    # print(np.isinf(df1['has_car']).any())
    # 透视表：出行与工作是否已婚、是否已育、是否有老人、是否有车  作为索引；性别  作为列的关系
    piv_tb = pd.pivot_table(df1, values="flag", index=["ismarr", "fertile", "haveold", "has_car"], columns=["sex"],
                            aggfunc=np.mean)
    print(piv_tb)
    sns.heatmap(piv_tb, annot=True, vmin=0, vmax=1, cmap=sns.color_palette("Reds", n_colors=256), annot_kws={'size': 16})
    # 设置横坐标轴的刻度字体大小为12
    plt.xticks(fontsize=16)
    # 设置纵坐标轴的刻度字体大小为12
    plt.yticks(fontsize=16)
    # 设置x轴标签的字体大小
    plt.xlabel('性别', fontsize=16, fontproperties="SimHei")
    # 设置y轴标签的字体大小
    plt.ylabel('是否已婚-是否已育-是否有老人-是否有车', fontsize=16, fontproperties="SimHei")
    plt.show()


# #年龄段与是否出行指标的相关性分析
# Age_CrossOverAnalysis(df)
# #性别、是否已婚、是否已育、是否有老人、是否有车这些指标与是否出行的相关性分析
# CrossOverAnalysis(df)

income_CrossOverAnalysis(df)

## 分组分析

def GroupAnalysis(df):
    df1=df[['income_level_id','county_name','flag']]
    sns.set_context(font_scale=1)
    sns.barplot(x="income_level_id", y="flag", hue="county_name", data=df1)  # 通过地区向下钻取
    plt.xticks(fontsize=16)
    # 设置纵坐标轴的刻度字体大小为12
    plt.yticks(fontsize=16)
    # 设置x轴标签的字体大小
    plt.xlabel('收入水平', fontsize=16, fontproperties="SimHei")
    # 设置y轴标签的字体大小
    plt.ylabel('出行所占概率', fontsize=16, fontproperties="SimHei")
    plt.show()

    # # 连续值分组分析
    # sl_s = df1["income_level_id"]
    # sns.barplot(list(range(len(sl_s))), sl_s.sort_values())
    # plt.show()


GroupAnalysis(df)
