import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
import pandas as pd

sns.set_context(font_scale=1.5)
df=pd.read_excel("../data/UserInformation.xlsx")
my_pca=PCA(n_components=7)
my_pca.fit_transform(df.drop(labels=["user_id","sex","ismarr","fertile","haveold","has_car","income_level_id","flag"],axis=1))
print(my_pca.explained_variance_ratio_)