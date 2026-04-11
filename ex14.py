import pandas as pd # 导入pandas库，用于读取csv文件
from scipy.interpolate import Rbf # 导入Rbf函数，用于插值
import matplotlib.pyplot as plt # 导入matplotlib.pyplot库，用于绘制图表
import numpy as np

df = pd.read_csv(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\china_gdp.csv') # 读取csv文件，将其存储在DataFrame对象df中
x = df['Year'] # 从df中提取Year列，将其存储在Series对象x中
y = df['Value'] # 从df中提取Value列，将其存储在Series对象y中

f = Rbf(x, y) # 创建Rbf对象f，用于插值
xx = np.linspace(min(x), max(x), 1000) # 创建一个包含1000个元素的数组xx，用于插值
yy = f(xx) # 使用Rbf对象f对xx进行插值，将结果存储在数组yy中
plt.plot(xx, yy)

plt.scatter(x,y) # 绘制原始数据的散点图
plt.show() # 显示图表