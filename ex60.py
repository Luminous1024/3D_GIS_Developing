import vtk # 导入vtk库，用于处理点云数据
import numpy as np # 导入numpy库，用于处理数组数据
import pyvista as pv # 导入pyvista库，用于处理点云数据

fl = open(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\cactus.3337.pts') # 打开点云数据文件
lines = fl.readlines() # 读取点云数据文件的所有行
print(len(lines)) # 打印点云数据文件的行数
# pts = vtk.vtkPoints() # 创建点云数据的点对象
# pts.SetDataTypeToDouble() # 设置点云数据的点对象的类型为双精度浮点数

X = [] # 点云数据的x坐标
Y = [] # 点云数据的y坐标
Z = [] # 点云数据的z坐标
for l in lines: # 遍历点云数据文件的所有行
    ln = l.split(' ') # 将行按空格分割
    if ln[0] != 'p':continue # 如果行不是点云数据的行，跳过
    x,y,z = float(ln[1]),float(ln[2]),float(ln[3]) # 将行中的x坐标、y坐标、z坐标转换为浮点数
    X.append(x) # 将x坐标添加到点云数据的x坐标列表中
    Y.append(y) # 将y坐标添加到点云数据的y坐标列表中
    Z.append(z) # 将z坐标添加到点云数据的z坐标列表中
pts = np.vstack([X,Y,Z]).T # 将点云数据的x坐标、y坐标、z坐标列表转换为numpy数组
#     pts.InsertNextPoint(x,y,z) # 将点云数据的点对象添加到点云数据的点对象中
# ca = vtk.vtkCellArray() # 创建点云数据的单元对象
# for i in range(pts.GetNumberOfPoints()): # 遍历点云数据的点对象
#     v = vtk.vtkVertex() # 创建点云数据的顶点对象
#     v.GetPointIds().SetId(0,i) # 设置点云数据的顶点对象的点对象的索引为i
#     ca.InsertNextCell(v) # 将点云数据的顶点对象添加到点云数据的单元对象中
# pd = vtk.vtkPolyData() # 创建点云数据的多边形数据对象
# pd.SetPoints(pts) # 设置点云数据的多边形数据对象的点对象为点云数据的点对象
# pd.SetVerts(ca) # 设置点云数据的多边形数据对象的单元对象为点云数据的单元对象

# pdd = pv.PolyData(pd) # 创建点云数据的多边形数据对象
# pdd.plot(color = 'green') # 绘制点云数据的多边形数据对象

pdd = pv.PolyData(pts) # 创建点云数据的多边形数据对象
pd = pdd.reconstruct_surface() # 重构点云数据的表面

pd.plot(color = 'green') # 绘制点云数据的表面

# pdd.plot(color = 'green') # 绘制点云数据的多边形数据对象
