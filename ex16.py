# import pyvista as pv # 导入pyvista库，用于可视化vtk数据
# from scipy.interpolate import Rbf # 导入scipy库中的Rbf函数，用于径向基函数插值
# import numpy as np # 导入numpy库，用于数值计算
#
# pcl = pv.read(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\lidar0.ply') # 读取lidar0.ply文件，将其存储在PolyData对象pcl中
# # pcl.plot() # 可视化pcl对象，显示点云数据
#
# points = pcl.points # 从PolyData对象pcl中提取点数据，将其存储在numpy数组points中
# # face = pcl.faces.reshape(-1,4)[:,1:] # 从PolyData对象pcl中提取面数据，将其存储在numpy数组face中
# x = points[:,0] # 从numpy数组points中提取第0列数据，将其存储在numpy数组x中
# y = points[:,1] # 从numpy数组points中提取第1列数据，将其存储在numpy数组y中
# z = points[:,2] # 从numpy数组points中提取第2列数据，将其存储在numpy数组z中
# f = Rbf(x,y,z) # 创建Rbf对象f，用于径向基函数插值，输入参数为x、y、z
# xx = np.linspace(min(x),max(x),100) # 创建numpy数组xx，用于存储x的等间距样本点，范围为x的最小值到最大值，共100个样本点
# yy = np.linspace(min(y),max(y),100) # 创建numpy数组yy，用于存储y的等间距样本点，范围为y的最小值到最大值，共100个样本点
# pts = [] # 创建空列表pts，用于存储插值后的点数据
# for i in xx:
#     for j in yy:
#         pts.append([i,j,f(i,j)])
# pts = np.array(pts) # 将列表pts转换为numpy数组pts，用于存储插值后的点数据
# pd = pv.PolyData(pts) # 创建PolyData对象pd，用于可视化插值后的点数据
# pd = pd.delaunay_2d() # 对PolyData对象pd进行2D Delaunay三角剖分，将其存储在PolyData对象pd中
#
# pd.plot(color = 'green') # 可视化PolyData对象pd，将其颜色设置为绿色

import numpy as np # 导入numpy库，用于数值计算
import matplotlib.pyplot as plt # 导入matplotlib.pyplot库，用于绘制图表
import matplotlib # 导入matplotlib库，用于绘制图表

# 设置中文字体
matplotlib.rcParams['font.sans-serif'] = ['SimHei'] # 设置中文字体为SimHei
matplotlib.rcParams['axes.unicode_minus'] = False # 解决负号显示问题

# 样本点
x_i = np.array([-2, -1, 0, 1, 2]) # 创建numpy数组x_i，用于存储样本点的x坐标，范围为-2到2，共5个样本点
w_i = np.array([1, -0.8, 1.2, -1, 0.9]) # 创建numpy数组w_i，用于存储样本点的权重，范围为-0.8到1.2，共5个权重

# 径向基函数
def phi(r): # 定义径向基函数phi，输入参数为r，返回值为e^(-r^2)
    return np.exp(-r**2) # 返回值为e^(-r^2)，即径向基函数的输出值

# 拟合函数
def f_hat(x): # 定义拟合函数f_hat，输入参数为x，返回值为拟合函数的输出值
    return sum(w * phi(x - xi) for w, xi in zip(w_i, x_i)) # 返回值为样本点权重与径向基函数输出值的加权和，即拟合函数的输出值

x = np.linspace(-3, 3, 400) # 创建numpy数组x，用于存储x的等间距样本点，范围为-3到3，共400个样本点
y = f_hat(x) # 调用拟合函数f_hat，输入参数为x，将其输出存储在numpy数组y中

plt.figure(figsize=(9,6)) # 创建新的图表，设置图表大小为9x6英寸

# 绘制各个径向基函数
for idx, (w, xi) in enumerate(zip(w_i, x_i)): # 遍历样本点权重与x坐标，idx为样本点索引，w为权重，xi为x坐标
    plt.plot(x, w*phi(x - xi), '--', alpha=0.7, label=fr"$w_{idx}\varphi(x-x_{idx})$") # 绘制径向基函数曲线，设置为虚线，透明度为0.7，标签为$w_i\varphi(x-x_i)$
    plt.scatter(xi, 0, color='red') # 在(xi,0)位置绘制红色散点，用于表示样本点

# 绘制拟合曲线
plt.plot(x, y, 'k', linewidth=2, label=r"$\hat{f}(x)$")

# 添加径向基函数公式文本框
plt.text(2.05, 0.985,
         r"$\hat{f}(x) = \sum_{i=1}^N w_i \varphi(\|x-x_i\|)$" "\n" r"$\varphi(r)=e^{-r^2}$",
         fontsize=12, bbox=dict(facecolor='white', alpha=0.7)) # 在(2.05,0.985)位置添加径向基函数公式文本框，设置字体大小为12，背景为白色，透明度为0.7

# 红色箭头批注
plt.annotate("中心点 $x_i$", xy=(x_i[2],0), xytext=(0.2,-0.5), # 在(x_i[2],0)位置添加注释文字"中心点 $x_i$"，文字位置为(0.2,-0.5)
             arrowprops=dict(arrowstyle="->", color="red"), fontsize=12, color="red") # 在(x_i[2],0)位置添加红色箭头，指向(0.2,-0.5)，箭头样式为"->"，字体大小为12，颜色为红色

# 黑色箭头批注（仿照红色箭头写法，避免超出画框）
plt.annotate(r"拟合曲线 $\hat{f}(x)$", # 在(0.5,f_hat(0.5))位置添加注释文字"拟合曲线 $\hat{f}(x)$"，文字位置为(1.0,1.2)
             xy=(0.5, f_hat(0.5)),       # 箭头指向拟合曲线上的点
             xytext=(1.0, 1.2),         # 注释文字放在图像内部
             arrowprops=dict(arrowstyle="->", color="black"), # 在(0.5,f_hat(0.5))位置添加黑色箭头，指向(1.0,1.2)，箭头样式为"->"，字体大小为12，颜色为黑色
             fontsize=12, color="black") # 在(0.5,f_hat(0.5))位置添加注释文字"拟合曲线 $\hat{f}(x)$"，文字位置为(1.0,1.2)，字体大小为12，颜色为黑色

plt.title("径向基函数拟合曲线") # 在图表顶部添加标题"径向基函数拟合曲线"
plt.xlabel("x") # 在图表底部添加x轴标签"x"
plt.ylabel(r"$\hat{f}(x)$") # 在图表左侧添加y轴标签"$\hat{f}(x)$"
plt.legend(loc="lower left", fontsize=9) # 在图表左下角添加图例，设置字体大小为9
plt.grid(True) # 显示网格线
plt.show() # 显示图表
