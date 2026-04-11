import vtk # 导入vtk库，用于读取vtk文件
import math # 导入math库，用于计算距离
import numpy as np # 导入numpy库，用于处理数组
import time # 导入time库，用于计算时间差

r = vtk.vtkPolyDataReader() # 创建vtk文件读取器
r.SetFileName(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\c15_mid_pd.vtk') # 设置读取的vtk文件路径
r.Update() # 更新读取器，读取文件内容
pd = vtk.vtkPolyData() # 创建vtk多Data对象，用于存储读取的vtk文件内容
pd.ShallowCopy(r.GetOutput()) # 深拷贝读取器的输出数据到多Data对象
print(pd.GetNumberOfPoints()) # 获取多Data对象中的点的数量

v0 = 1234 # 选择一个点作为参考点
p0 = [0,0,0] # 存储参考点的坐标
pd.GetPoint(v0,p0) # 获取参考点的坐标
dth = 8000 # 定义距离阈值
t0 = time.perf_counter() # 记录开始时间
pis = [] # 存储距离小于阈值的点的索引
for i in range(pd.GetNumberOfPoints()): # 遍历多Data对象中的点
    p1 = [0,0,0] # 存储当前点的坐标
    pd.GetPoint(i,p1) # 获取当前点的坐标
    if math.dist(p0,p1) < dth: # 如果当前点与参考点的距离小于阈值
        pis.append(i) # 将当前点的索引添加到距离小于阈值的点的索引列表中
print(len(pis)) # 输出距离小于阈值的点的数量
t1 = time.perf_counter() # 记录结束时间
print(t1-t0) # 输出距离小于阈值的点的索引列表的构建时间

loc = vtk.vtkPointLocator() # 创建vtk点定位器对象
loc.SetDataSet(pd) # 设置点定位器对象的输入数据为多Data对象
loc.BuildLocator() # 构建点定位器对象

t0 = time.perf_counter() # 记录开始时间
ids = vtk.vtkIdList() # 创建vtkIdList对象，用于存储最近的点的索引
loc.FindClosestNPoints(598,p0,ids) # 查找最近的598个点的索引
print(ids.GetNumberOfIds()) # 输出最近的598个点的索引的数量
t1 = time.perf_counter() # 记录结束时间
print(t1-t0) # 输出最近的598个点的索引的查找时间
