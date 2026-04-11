import vtk # 导入 vtk 库，用于读取 vtk 文件
import numpy as np # 导入 numpy 库，用于处理数组

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
print(v0,v1,v2) # 打印单元格点的索引

nis = vtk.vtkIdList() # 创建 vtk 索引列表对象，用于存储单元格边的索引
pd.GetCellEdgeNeighbors(cid,v1,v2,nis) # 获取单元格边的索引
print(nis.GetNumberOfIds(),nis.GetId(0)) # 打印单元格边的索引数量和第一个边的索引
