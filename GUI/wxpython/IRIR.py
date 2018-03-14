

import pandas as pd
import seaborn as sns
from sklearn import datasets
import matplotlib.pyplot as plt
sns.set(style="white",color_codes=True)

iris=pd.read_csv("D:/iris.csv")
iris.head()
# iris = datasets.load_iris()






sns.FacetGrid(iris,hue="Species",size=4).map(plt.scatter,"SepalLengthCm","SepalWidthCm").add_legend()
# plt.show() 
sns.FacetGrid(iris,hue="Species",size=4).map(plt.scatter,"PetalLengthCm","PetalWidthCm").add_legend()
# plt.show() 
sns.FacetGrid(iris,hue="Species",size=4).map(plt.scatter,"SepalLengthCm","PetalLengthCm").add_legend()
# plt.show() 
sns.FacetGrid(iris,hue="Species",size=4).map(plt.scatter,"SepalWidthCm","PetalWidthCm").add_legend()
plt.show() 
print "result"