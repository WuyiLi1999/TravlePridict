import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("toUser_1_train.csv")


def age_flag(df):
    df_age=df[['age','flag']]
    # 去除age为NaN的数据
    df_age = df_age.dropna(subset=['age'])
    df_age['age'] = df_age['age'].astype(float)

    # 将age划分为每10岁一组，并统计flag为1和0的个数
    df_age['age_group'] = pd.cut(df_age['age'], bins=range(0, 100, 10), right=False)
    age_group_counts = df_age.groupby(['age_group', 'flag']).size().unstack().fillna(0)
    age_group_counts.to_csv('age.csv', index=False)
    return  age_group_counts

## 性别对出行的影响
def sex_flag(df):
    sex=df[['sex','flag']]
    # 去除age为NaN的数据
    sex = sex.dropna(subset=['sex'])
    sex['sex']=sex['sex'].astype(int)
    sex_group_counts = sex.groupby(['sex', 'flag']).size().unstack().fillna(0)
    sex_group_counts.to_csv('sex.csv', index=False)
    return  sex_group_counts
#已婚对出行的影响
def marr_flag(df):
    marr=df[['ismarr','flag']]
    # 去除age为NaN的数据
    marr = marr.dropna(subset=['ismarr'])
    marr['ismarr']=marr['ismarr'].astype(int)
    marr_group_counts = marr.groupby(['ismarr', 'flag']).size().unstack().fillna(0)
    marr_group_counts.to_csv('marr.csv', index=False)
    return  marr_group_counts

# 已育对出行的影响
def fertile_flag(df):
    marr=df[['fertile','flag']]
    # 去除age为NaN的数据
    marr = marr.dropna(subset=['fertile'])
    marr['fertile']=marr['fertile'].astype(int)
    marr_group_counts = marr.groupby(['fertile', 'flag']).size().unstack().fillna(0)
    marr_group_counts.to_csv('fertile.csv', index=False)
    return  marr_group_counts

def haveold_flag(df):
    marr=df[['haveold','flag']]
    # 去除age为NaN的数据
    marr = marr.dropna(subset=['haveold'])
    marr['haveold']=marr['haveold'].astype(int)
    marr_group_counts = marr.groupby(['haveold', 'flag']).size().unstack().fillna(0)
    marr_group_counts.to_csv('haveold.csv', index=False)
    return  marr_group_counts

def car_flag(df):
    marr=df[['has_car','flag']]
    # 去除age为NaN的数据
    marr = marr.dropna(subset=['has_car'])
    marr['has_car']=marr['has_car'].astype(int)
    marr_group_counts = marr.groupby(['has_car', 'flag']).size().unstack().fillna(0)
    marr_group_counts.to_csv('car.csv', index=False)
    return  marr_group_counts

def income_flag(df):
    marr=df[['income_level_id','flag']]
    # 去除age为NaN的数据
    marr = marr.dropna(subset=['income_level_id'])
    marr['income_level_id']=marr['income_level_id'].astype(int)
    marr_group_counts = marr.groupby(['income_level_id', 'flag']).size().unstack().fillna(0)
    marr_group_counts.to_csv('income.csv', index=False)
    return  marr_group_counts

def country_flag(df):
    data = [
        {'编号': '5712', '区县': '下沙经济技术开发区'},
        {'编号': '5716', '区县': '余杭区'},
        {'编号': '5711', '区县': '建德市'},
        {'编号': '571D', '区县': '下沙经济技术开发区'},
        {'编号': '5714', '区县': '富阳区'},
        {'编号': '571C', '区县': '临安区'},
        {'编号': '571B', '区县': '淳安县'},
        {'编号': '5713', '区县': '桐庐县'},
        {'编号': '5718', '区县': '萧山区'},
        {'编号': '5719', '区县': '西湖区'},
        {'编号': '571A', '区县': '上城区'},
        {'编号': '5715', '区县': '滨江区'},
        {'编号': '5792', '区县': '下沙经济技术开发区'},
        {'编号': '5733', '区县': '下城区'},
        {'编号': '5701', '区县': '滨江区'},
        {'编号': '5749', '区县': '下沙经济技术开发区'},
        {'编号': '5779', '区县': '淳安县'},
        {'编号': '5735', '区县': '余杭区'},
        {'编号': '5788', '区县': '临安区'},
        {'编号': '5803', '区县': '桐庐县'},
        {'编号': '5766', '区县': '富阳区'},
        {'编号': '5795', '区县': '萧山区'},
        {'编号': '5731', '区县': '西湖区'},
        {'编号': '5723', '区县': '江干区'},
        {'编号': '5804', '区县': '下沙经济技术开发区'},
        {'编号': '5794', '区县': '淳安县'},
        {'编号': '5706', '区县': '拱墅区'},
        {'编号': '571E', '区县': '下沙经济技术开发区'},
    ]
    countryData = pd.DataFrame(data)
    countryData.to_csv('country.csv', index=False)
    marr=df[['county_name','flag']]
    # 去除age为NaN的数据
    country = marr.dropna(subset=['county_name'])
    country['county_name']=country['county_name'].map(countryData.set_index('编号')['区县'])
    marr_group_counts = country.groupby(['county_name', 'flag']).size().unstack().fillna(0)
    marr_group_counts.to_csv('countryTable.csv', index=False)
    return  marr_group_counts


# 绘制堆叠图
result = age_flag(df)
# sex_flag(df)
# country_flag(df)
# marr_flag(df)
# fertile_flag(df)
# haveold_flag(df)
# car_flag(df)
# income_flag(df)

# 设置中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

ax = result.plot(kind='bar', stacked=True, edgecolor='black')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')  # 设置X轴标签旋转角度和对齐方式

# 显示每一部分的数据值和分割线
for container in ax.containers:
    for child in container:
        height = child.get_height()
        if height > 0:
            ax.annotate(f"{height:.0f}", xy=(child.get_x() + child.get_width() / 2, height),
                        xytext=(0, 2), textcoords="offset points", ha='center', va='bottom', fontsize='small')
        else:
            ax.annotate("", xy=(child.get_x() + child.get_width() / 2, height),
                        xytext=(0, 2), textcoords="offset points", ha='center', va='bottom', fontsize='small')


# 设置中文字体，确保字体文件存在于您的系统中
plt.rcParams['font.family'] = 'SimSun'
plt.rcParams['font.size'] = 5

# 设置图表标题和坐标轴标签
plt.title('')
plt.xlabel('')
plt.ylabel('')

# 显示图表
plt.show()