import pyvista as pv # 导入pyvista库，用于读取vtk文件
import vtk # 导入vtk库，用于读取vtk文件
import math # 导入math库，用于计算距离
import numpy as np # 导入numpy库，用于处理数组
import pygeodesic # MMP，计算几何的精确测地距离
import potpourri3d as p3d #HM，微分几何的测地距离计算

# r = vtk.vtkPolyDataReader() # 创建vtk文件读取器
mesh = pv.read(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\rb.vtk') # 读取vtk文件
#polydata
points = mesh.points # 纯Python数组
faces = mesh.faces.reshape(-1,4)[:,1:] # 从第 2 列开始，每个元素减去 1

# r = vtk.vtkPolyDataReader() # 创建vtk文件读取器
# r.SetFileName(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\rb.vtky') # 设置读取的vtk文件路径
# r.Update() # 更新读取器，读取文件内容
# pd = vtk.vtkPolyData() # 创建vtk多Data对象，用于存储读取的vtk文件内容
# pd.ShallowCopy(r.GetOutput()) # 深拷贝读取器的输出数据到多Data对象

sol = p3d.PointCloudHeatSolver(points) # 创建点云热Solver对象
v0 = 123 # 点v0的索引，从0开始计数
v1 = 234 # 点v1的索引，从0开始计数
v2 = 235 # 点v2的索引，从0开始计数
dist = sol.compute_distance_multisource([v0,v1,v2]) # 计算点v0,v1,v2到其他点的距离
