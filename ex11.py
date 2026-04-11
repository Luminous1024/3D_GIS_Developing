# import pandas as pan
# import vtk
# import numpy as np
#
# df = pan.read_csv(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\monthly_summary_202001_fit.csv')
# x = df['x']
# y = df['y']
# z = df['z']
# #print(x,len(x))
#
# pts = vtk.vtkPoints() # 构建点集
# for i in range(len(x)): # 对len(x)进行遍历
#     pts.InsertNextPoint(x[i],y[i],z[i])
#     #pts.InsertNextPoint(i,np.array([x[i],y[i],z[i]]))
# print(pts.GetNumberOfPoints()) # 输出点集的点数
#
# vtx = vtk.vtkCellArray() # 构建顶点集
# #for i in range(len(x)): #存在风险：i可能会超出范围
# for i in range(pts.GetNumberOfPoints()): # 使用点集的点数更安全
#     v = vtk.vtkVertex() # 构建一个顶点
#     v.GetPointIds().SetId(0,i) # 为顶点v添加一个点索引i
#     vtx.InsertNextCell(v) # 为顶点集vtx添加一个顶点v
#
# pd = vtk.vtkPolyData() # 构建一个多边形数据集
# pd.SetPoints(pts) # 为多边形数据集pd添加点集pts
# pd.SetVerts(vtx) # 为多边形数据集pd添加顶点集vtx
#
# w = vtk.vtkPolyDataWriter() # 构建一个多边形数据集写入器
# w.SetFileName(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\monthly_summary_202001_fit.vtk') # 设置写入文件名
# w.SetInputData(pd) # 为写入器w添加多边形数据集pd
# w.Write() # 写入文件

# import pandas as pan
# import pyvista as pv
# import numpy as np
#
# df = pan.read_csv(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\monthly_summary_202001_fit.csv') # 读取CSV文件
# x = df['x'] # 从DataFrame中提取x列
# y = df['y'] # 从DataFrame中提取y列
# z = df['z'] # 从DataFrame中提取z列
# cords = np.array([x,y,z]).T # 将x、y、z列转换为点坐标数组
# # 使用pyvista与使用vtk时的区别：
# # 1. pyvista直接使用点坐标构建网格，而vtk需要先构建点集和顶点集
# # 2. pyvista的plot()方法可以直接显示网格，而vtk需要通过渲染器、渲染窗口和交互器来显示
# # 3. 数据类型上，pyvista使用numpy数组，而vtk使用vtkPoints对象
# points = pv.PolyData(cords) # 从点坐标数组构建PolyData对象
# points.plot() # 显示网格

#--------------------#

# import pandas as pan # 导入pandas库，用于读取CSV文件
# import vtk # 导入vtk库，用于构建点集、顶点集和多边形数据集
# import numpy as np # 导入numpy库，用于数组操作
#
# df = pan.read_csv(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\monthly_summary_202001_fit.csv') # 读取CSV文件
# x = df['x'] # 从DataFrame中提取x列
# y = df['y'] # 从DataFrame中提取y列
# z = df['z'] # 从DataFrame中提取z列
# #print(x,len(x)) # 输出x列和其长度
#
# pts = vtk.vtkPoints() # 构建点集
# for i in range(len(x)): # 对len(x)进行遍历
#     pts.InsertNextPoint(x[i],y[i],z[i])
#     #pts.InsertNextPoint(i,np.array([x[i],y[i],z[i]]))
# print(pts.GetNumberOfPoints()) # 输出点集的点数
#
# vtx = vtk.vtkCellArray() # 构建顶点集
# #for i in range(len(x)): #存在风险：i可能会超出范围
# for i in range(pts.GetNumberOfPoints()): # 使用点集的点数更安全
#     v = vtk.vtkVertex() # 构建一个顶点
#     v.GetPointIds().SetId(0,i) # 为顶点v添加一个点索引i
#     vtx.InsertNextCell(v) # 为顶点集vtx添加一个顶点v
#
# pd = vtk.vtkPolyData() # 构建一个多边形数据集
# pd.SetPoints(pts) # 为多边形数据集pd添加点集pts
# pd.SetVerts(vtx) # 为多边形数据集pd添加顶点集vtx
#
# w = vtk.vtkPolyDataWriter() # 构建一个多边形数据集写入器
# w.SetFileName(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\monthly_summary_202001_fit.vtk') # 设置写入文件名
# w.SetInputData(pd) # 为写入器w添加多边形数据集pd
# w.Write() # 写入文件

#--------------------#

# import pandas as pan # 导入pandas库，用于读取CSV文件
# import pyvista as pv # 导入pyvista库，用于可视化网格
# import numpy as np # 导入numpy库，用于数组操作
#
# df = pan.read_csv(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\monthly_summary_202001_fit.csv') # 读取CSV文件
# x = df['x'] # 从DataFrame中提取x列
# y = df['y'] # 从DataFrame中提取y列
# z = df['z'] # 从DataFrame中提取z列
# cords = np.array([x,y,z]).T # 将x、y、z列转换为点坐标数组
#
# #使用pyvista与使用vtk时的区别：
# # 1. pyvista直接使用点坐标构建网格，而vtk需要先构建点集和顶点集
# # 2. pyvista的plot()方法可以直接显示网格，而vtk需要通过渲染器、渲染窗口和交互器来显示
# # 3. 数据类型上，pyvista使用numpy数组，而vtk使用vtkPoints对象
#
# points = pv.PolyData(cords) # 从点坐标数组构建PolyData对象
# points.plot() # 显示网格

#--------------------#