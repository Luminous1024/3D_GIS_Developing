import laspy as las # 导入laspy库，用于处理点云数据
import numpy as np # 导入numpy库，用于处理数组数据
import pyvista as pv # 导入pyvista库，用于处理点云数据
import vtk # 导入vtk库，用于处理点云数据

lidar = las.read(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\MT_Helena_2012_000283.las') # 读取点云数据
print(lidar) # 打印点云数据
print(lidar.header.offsets[0],lidar.header.offsets[1],lidar.header.offsets[2]) # 打印点云数据的偏移量
print(lidar.header.scales[0],lidar.header.scales[1],lidar.header.scales[2]) # 打印点云数据的缩放因子
print(list(lidar.header.point_format.dimension_names)) # 打印点云数据的维度名称列表

x = np.array(lidar['X'], dtype=np.float64)
y = np.array(lidar['Y'], dtype=np.float64)
z = np.array(lidar['Z'], dtype=np.float64)
cls = np.array(lidar['classification'], dtype=np.int32)

pts = np.vstack((x, y, z)).T

pdd = pv.PolyData(pts) # 创建点云数据的多边形数据对象
pdd['Classification'] = cls
pdd.set_active_scalars('Classification') # 设置点云数据的多边形数据对象的标量为点云数据的分类
pdd.plot() # 绘制点云数据的多边形数据对象

# 点云的特征：
# uneven density: 不均匀密度
# voids: 大面积空白
# strip: 条带状
