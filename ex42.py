import vtk # 导入 vtk 库，用于读取 vtk 文件
import numpy as np # 导入 numpy 库，用于处理数组
import math

r = vtk.vtkPolyDataReader() # 创建 vtk 多数据读取器
r.SetFileName(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\c15_mid_pd.vtk') # 设置读取的 vtk 文件路径
r.Update() # 更新读取器，读取 vtk 文件
pd = vtk.vtkPolyData() # 创建 vtk 多数据对象，用于存储读取的 vtk 文件内容
pd.ShallowCopy(r.GetOutput()) # 将读取的 vtk 文件内容浅拷贝到 vtk 多数据对象中

cid = 770828 # 选择的单元格索引
pis = vtk.vtkIdList() # 创建 vtk 索引列表对象，用于存储单元格点的索引
pd.GetCellPoints(cid,pis) # 获取单元格点的索引
v0 = pis.GetId(0) # 第一个点的索引
v1 = pis.GetId(1) # 第二个点的索引
v2 = pis.GetId(2) # 第三个点的索引
p0 = np.zeros(3,dtype = np.float64) # 创建一个 3 维的数组，用于存储第一个点的坐标
pd.GetPoint(v0,p0) # 获取第一个点的坐标
p1 = np.zeros(3,dtype = np.float64) # 创建一个 3 维的数组，用于存储第二个点的坐标
pd.GetPoint(v1,p1) # 获取第二个点的坐标
p2 = np.zeros(3,dtype = np.float64) # 创建一个 3 维的数组，用于存储第三个点的坐标
pd.GetPoint(v2,p2) # 获取第三个点的坐标
cent = (p0 + p1 + p2) / 3 # 计算单元格的中心坐标
z0 = cent.copy() # 创建一个 3 维的数组，用于存储第一个点的坐标
z1 = cent.copy() # 创建一个 3 维的数组，用于存储第二个点的坐标
z0[2] += 10 # 第一个点的 z 坐标增加 1，模拟高度
z1[2] -= 10 # 第二个点的 z 坐标减少 1，模拟高度

cloc = vtk.vtkCellLocator() # 创建 vtk 单元格定位器对象，用于定位单元格
cloc.SetDataSet(pd) # 设置定位器的输入数据为 vtk 多数据对象
cloc.BuildLocator() # 构建定位器，

tx = np.zeros(3,dtype = np.float64) # 创建一个 3 维的数组，用于存储第一个点的坐标
cellid = vtk.reference(0) # 创建一个 vtk 叕用计数器对象，用于存储单元格的索引
subid = vtk.reference(0) # 创建一个 vtk 叕用计数器对象，用于存储子单元格的索引
dist2 = vtk.reference(0.0) # 创建一个 vtk 叕用计数器对象，用于存储第一个点到最近单元格的距离

t = vtk.reference(0.0) # 创建交点参数对象
pcoords = np.zeros(3,dtype = np.float64) # 创建参数化坐标数组
cloc.IntersectWithLine(z0,z1,0.001,t,tx,pcoords,subid,cellid) # 检测线段与网格的交点
print("交点坐标:", tx[0], tx[1], tx[2]) # 打印交点坐标
print("交点参数 t:", float(t)) # 打印交点参数
print("交点所在单元ID:", int(cellid)) # 打印交点所在单元ID

cloc.FindClosestPoint(z0,tx,cellid,subid,dist2) # 查找第一个点最近的单元格，将结果存储在 cellid、subid、dist2 中
print(cent[0],cent[1],cent[2]) # 打印单元格的中心坐标
print(tx[0],tx[1],tx[2]) # 打印第一个点的坐标
print(math.dist(z0,tx),np.sqrt(float(dist2))) # 打印第一个点到最近单元格的距离
