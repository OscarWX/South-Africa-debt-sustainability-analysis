import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
pd.set_option('display.max_columns',None)
shuju=pd.read_excel("D:\FTP\Python\spearman correlation data.xlsx")
corr_mat=shuju.corr()
f,ax=plt.subplots(figsize=(25,30))
mask = np.zeros_like(corr_mat)
cmap = sns.diverging_palette(600,10,as_cmap=True)
for i in range(1,len(mask)):
    for j in range(0,i):
        mask[j][i]=True
sns.heatmap(shuju.corr(),mask=mask,cmap=cmap,square=True,annot=True,fmt="0.2f")
plt.xticks(fontsize=7)
plt.yticks(fontsize=7)
plt.show()


"""
cmap = sns.diverging_palette(600,10,as_cmap=True)
plt.figure(figsize=(25,20))
sns.heatmap(shuju.corr(method='spearman'),cmap=cmap,annot=True)
plt.xticks(fontsize=9)
plt.yticks(fontsize=9)
plt.show()
"""


'''import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
shuju=pd.read_excel("D:\FTP\Python\graph 1.xlsx")
cmap = sns.diverging_palette(600,10,as_cmap=True)
plt.figure(figsize=(25,20))
sns.heatmap(shuju.corr(method='spearman'),cmap=cmap,square=True,annot=True)
plt.xticks(fontsize=9)
plt.yticks(fontsize=9)
plt.show()
'''
