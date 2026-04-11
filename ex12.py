# import geopandas as gpd # 导入geopandas库，用于读取SHP文件
# import vtk # 导入vtk库，用于构建点集、顶点集和多边形数据集
# import numpy as numpy # 导入numpy库，用于数组操作
# import pyvista as pv # 导入pyvista库，用于可视化

# df = gpd.read_file(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\REG.shp',encoding = 'gbk') # 读取REG.shp文件
# print(df.columns) # 打印列名
# print(df.geometry[2].exterior.coords) # 打印第3个几何对象的外部坐标
# l = len(df.geometry[2].exterior.coords) # 提取第3个几何对象的外部坐标的长度

# x = [df.geometry[2].exterior.coords[i][0] for i in range(l)] # 提取x坐标
# x = [] # 提取x坐标
# y = [] # 提取y坐标
# z = [] # 提取z坐标
# for i in range(l): # 遍历所有点
#     x.append(df.geometry[2].exterior.coords[i][0]) # 提取x坐标
#     y.append(df.geometry[2].exterior.coords[i][1]) # 提取y坐标
#     z.append(0) # 提取z坐标

# pts = vtk.vtkPoints() # 创建点对象
# pts.SetDataTypeToDouble() # 设置数据类型为双精度浮点数
# for i in range(l): # 遍历所有点
#     pts.InsertNextPoint(df.geometry[2].exterior.coords[i][0], df.geometry[2].exterior.coords[i][1], 0) # 插入点
# ca = vtk.vtkCellArray() # 创建单元数组对象

# 提取所有点的索引
# for i in range(pts.GetNumberOfPoints()): # 遍历所有点
#     v = vtk.vtkVertex() # 创建顶点对象
#     v.GetPointIds().SetId(0,i) # 设置顶点的点索引
#     ca.InsertNextCell(v) # 插入单元
# pd = vtk.vtkPolyData() # 创建多边形数据对象
# pd.SetPoints(pts) # 设置点对象
# pd.SetVerts(ca) # 设置单元数组对象
#
# pp = pv.PolyData(pd) # 创建PyVista多边形数据对象
# pp.plot(color = 'green') # 绘制多边形数据对象

# 提取所有线的索引
# for i in range(pts.GetNumberOfPoints() - 1): # 遍历所有点
#     ln = vtk.vtkLine() # 创建线对象
#     ln.GetPointIds().SetId(0,i) # 设置线的点索引
#     ln.GetPointIds().SetId(1,(i+1)) # 设置线的点索引
#     ca.InsertNextCell(ln) # 插入单元
# ln = vtk.vtkLine() # 创建线对象
# ln.GetPointIds().SetId(0,(pts.GetNumberOfPoints() - 1)) # 设置线的点索引
# ln.GetPointIds().SetId(1,0) # 设置线的点索引
# ca.InsertNextCell(ln) # 插入单元
#
# pd = vtk.vtkPolyData() # 创建多边形数据对象
# pd.SetPoints(pts) # 设置点对象
# pd.SetLines(ca) # 设置单元数组对象
#
# pp = pv.PolyData(pd) # 创建PyVista多边形数据对象
# pp.plot(color = 'green') # 绘制多边形数据对象

# 提取所有线的索引
# pln = vtk.vtkPolyLineSource() # 创建折线源对象
# pln.SetPoints(pts) # 设置折线源对象的点对象
# pln.Update() # 更新折线源对象
#
# pp = pv.PolyData(pln.GetOutput()) # 创建PyVista折线数据对象
# pp.plot(color = 'red') # 绘制折线数据对象

# 提取所有线的索引
# plg = vtk.vtkPolygon() # 创建多边形对象
# plg.GetPointIds().SetNumberOfIds(pts.GetNumberOfPoints()) # 设置折线点对象的点索引数量
# for i in range(pts.GetNumberOfPoints()): # 遍历所有点
#     plg.GetPointIds().SetId(i, i) # 设置折线点对象的点索引
# ca.InsertNextCell(plg) # 插入单元
#
# pd = vtk.vtkPolyData() # 创建多边形数据对象
# pd.SetPoints(pts) # 设置点对象
# pd.SetPolys(ca) # 设置单元数组对象 # 来自人的先验知识，而不是vtk的自动三角化

# 进行Delaunay2D三角化
# d2d = vtk.vtkDelaunay2D() # 创建Delaunay2D对象
# d2d.SetInputData(pd) # 设置Delaunay2D对象的输入数据
# d2d.Update() # 更新Delaunay2D对象

# 提取所有三角形的索引
# tri = vtk.vtkTriangleFilter() # 创建三角形过滤器对象
# tri.SetInputData(pd) # 设置三角形过滤器对象的输入数据
# tri.Update() # 更新三角形过滤器对象

# pp = pv.PolyData(pd) # 创建PyVista多边形数据对象
# pp = pp.triangulate() # 三角化多边形数据对象
# pp.plot(color = 'green') # 绘制三角化多边形数据对象

# 单纯形simplex:
# 一个单纯形是一个n维空间中的一个n-1维的子空间，它由n个点组成，这些点在n维空间中是线性独立的。
# 例如，在二维空间中，一个三角形就是一个单纯形，它由三个点组成，这些点在二维空间中是线性独立的。
# 在三维空间中，一个四面体就是一个单纯形，它由四个点组成，这些点在三维空间中是线性独立的。

#pyvsita渲染折线源和多边形数据对象的区别:
# 折线源对象是一个vtk对象，它可以直接渲染出来。
# 多边形数据对象是一个vtk对象，它可以直接渲染出来。
# 但是，折线源对象和多边形数据对象的渲染结果是不同的。
# 折线源对象的渲染结果是一条折线，它由多个点组成，这些点之间是连续的。
# 多边形数据对象的渲染结果是一个多边形，它由多个点组成，这些点之间是不连续的。

#solid和wireframe:
# solid: 渲染出一个实心的多边形，它由多个点组成，这些点之间是不连续的。
# wireframe: 渲染出一个空心的多边形，它由多个点组成，这些点之间是不连续的。

#共线与Delaunay三角化：
# 共线：如果在一个n维空间中，n个点是共线的，那么这n个点就构成了一个n-1维的子空间，这个子空间就是一个单纯形。
# Delaunay三角化：Delaunay三角化是一种三角化算法，它可以将一个平面上的点集三角化，使得每个三角形的外接圆都不包含其他点。

#凸多边形和Delaunay三角化：
# 凸多边形：如果一个多边形的所有内角都小于180度，那么这个多边形就是一个凸多边形。
# Delaunay三角化：Delaunay三角化是一种三角化算法，它可以将一个平面上的点集三角化，使得每个三角形的外接圆都不包含其他点。

#显卡能接受的多边形都是三角形，所以不能渲染出非三角形的多边形。只有通过三角化才能渲染出非三角形的多边形。

#--------------------#

# 1.读取 Shapefile 并打印基本信息
# import geopandas as gpd # 导入geopandas库，用于读取Shapefile文件
#
# # 读取数据（请根据实际路径修改）
# df = gpd.read_file(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\REG.shp', encoding='gbk') # 读取Shapefile文件
# print("列名：", df.columns) # 打印列名
# print("第三个几何对象的外环坐标：", df.geometry[2].exterior.coords[:]) # 打印第三个几何对象的外环坐标
# print("点数：", len(df.geometry[2].exterior.coords)) # 打印第三个几何对象的外环坐标点数

#--------------------#

# 2.提取坐标点并构建 VTK 点集（供后续使用）
# import geopandas as gpd # 导入geopandas库，用于读取Shapefile文件
# import vtk # 导入vtk库，用于构建点集、顶点集和多边形数据集
#
# df = gpd.read_file(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\REG.shp', encoding='gbk') # 读取Shapefile文件
# coords = df.geometry[2].exterior.coords # 提取第三个几何对象的外环坐标点
# l = len(coords) # 提取第三个几何对象的外环坐标点数
#
# pts = vtk.vtkPoints() # 构建一个点集对象
# pts.SetDataTypeToDouble() # 设置点集对象的数据类型为双精度浮点数
# for i in range(l): # 遍历所有点
#     pts.InsertNextPoint(coords[i][0], coords[i][1], 0) # 插入点到点集对象中
#
# print("点集中共有 {} 个点".format(pts.GetNumberOfPoints())) # 打印点集中的点数

#--------------------#

# 3.绘制点云（绿色）
# import geopandas as gpd # 导入geopandas库，用于读取Shapefile文件
# import vtk # 导入vtk库，用于构建点集、顶点集和多边形数据集
# import pyvista as pv # 导入pyvista库，用于渲染点云
#
# df = gpd.read_file(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\REG.shp', encoding='gbk') # 读取Shapefile文件
# coords = df.geometry[2].exterior.coords # 提取第三个几何对象的外环坐标点
# l = len(coords) # 提取第三个几何对象的外环坐标点数
#
# pts = vtk.vtkPoints() # 构建一个点集对象
# pts.SetDataTypeToDouble() # 设置点集对象的数据类型为双精度浮点数
# for i in range(l): # 遍历所有点
#     pts.InsertNextPoint(coords[i][0], coords[i][1], 0) # 插入点到点集对象中
#
# print("点集中共有 {} 个点".format(pts.GetNumberOfPoints())) # 打印点集中的点数
#
# ca = vtk.vtkCellArray() # 构建一个顶点集对象
# for i in range(pts.GetNumberOfPoints()): # 遍历所有点
#     v = vtk.vtkVertex() # 构建一个顶点对象
#     v.GetPointIds().SetId(0, i) # 设置顶点对象的点索引为i
#     ca.InsertNextCell(v) # 插入顶点到顶点集对象中
#
# pd = vtk.vtkPolyData() # 构建一个多边形数据集对象
# pd.SetPoints(pts) # 设置多边形数据集对象的点集为pts
# pd.SetVerts(ca) # 设置多边形数据集对象的顶点集为ca
#
# pp = pv.PolyData(pd) # 从多边形数据集对象pd构建一个PolyData对象
# plotter = pv.Plotter() # 构建一个渲染器对象
# plotter.add_mesh(pp, color='green', point_size=10, render_points_as_spheres=True) # 添加PolyData对象pp到渲染器对象plotter中，设置颜色为绿色，点大小为10，渲染为球体
# plotter.show(title='点云 (绿色)') # 显示渲染器对象plotter中的内容，标题为'点云 (绿色)'

#--------------------#

# 4.手动构建闭合折线（绿色线）
# import geopandas as gpd
# import vtk
# import pyvista as pv
#
# df = gpd.read_file(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\REG.shp', encoding='gbk')
# coords = df.geometry[2].exterior.coords
# l = len(coords)
#
# pts = vtk.vtkPoints()
# pts.SetDataTypeToDouble()
# for i in range(l):
#     pts.InsertNextPoint(coords[i][0], coords[i][1], 0)
#
# ca = vtk.vtkCellArray()
# n = pts.GetNumberOfPoints()
# for i in range(n - 1):
#     line = vtk.vtkLine()
#     line.GetPointIds().SetId(0, i)
#     line.GetPointIds().SetId(1, i+1)
#     ca.InsertNextCell(line)
# line = vtk.vtkLine()
# line.GetPointIds().SetId(0, n-1)
# line.GetPointIds().SetId(1, 0)
# ca.InsertNextCell(line)
#
# pd = vtk.vtkPolyData()
# pd.SetPoints(pts)
# pd.SetLines(ca)
#
# pp = pv.PolyData(pd)
# plotter = pv.Plotter()
# plotter.add_mesh(pp, color='green', line_width=3)
# plotter.show(title='手动构建闭合折线 (绿色)')

#--------------------#

# 5.使用 vtkPolyLineSource 绘制闭合折线（红色线）
# import geopandas as gpd
# import vtk
# import pyvista as pv
#
# df = gpd.read_file(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\REG.shp', encoding='gbk')
# coords = df.geometry[2].exterior.coords
# l = len(coords)
#
# pts = vtk.vtkPoints()
# pts.SetDataTypeToDouble()
# for i in range(l):
#     pts.InsertNextPoint(coords[i][0], coords[i][1], 0)
#
# pline_source = vtk.vtkPolyLineSource()
# pline_source.SetPoints(pts)
# pline_source.Update()
#
# pp = pv.PolyData(pline_source.GetOutput())
# plotter = pv.Plotter()
# plotter.add_mesh(pp, color='red', line_width=3)
# plotter.show(title='vtkPolyLineSource 折线 (红色)')

#--------------------#

# 6.构建多边形并三角化渲染（绿色填充）
# import geopandas as gpd
# import vtk
# import pyvista as pv
#
# df = gpd.read_file(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\REG.shp', encoding='gbk')
# coords = df.geometry[2].exterior.coords
# l = len(coords)
#
# pts = vtk.vtkPoints()
# pts.SetDataTypeToDouble()
# for i in range(l):
#     pts.InsertNextPoint(coords[i][0], coords[i][1], 0)
#
# polygon = vtk.vtkPolygon()
# polygon.GetPointIds().SetNumberOfIds(pts.GetNumberOfPoints())
# for i in range(pts.GetNumberOfPoints()):
#     polygon.GetPointIds().SetId(i, i)
#
# ca = vtk.vtkCellArray()
# ca.InsertNextCell(polygon)
#
# pd = vtk.vtkPolyData()
# pd.SetPoints(pts)
# pd.SetPolys(ca)
#
# pp = pv.PolyData(pd)
# pp = pp.triangulate()
# plotter = pv.Plotter()
# plotter.add_mesh(pp, color='green', show_edges=True)
# plotter.show(title='多边形三角化 (绿色填充+边)')

#--------------------#

import pandas as pd # 导入pandas库，用于读取CSV文件
import vtk # 导入vtk库，用于构建点集、顶点集和多边形数据集
import pyvista as pv # 导入pyvista库，用于可视化渲染

# ==================== 配置 ====================
csv_path = r"C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\polyline.csv" # 请修改为实际文件路径
line_output = r"C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\line.vtk"  # 输出的线文件
polygon_output = r"C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\polygon.vtk"  # 输出的多边形文件
show_visualization = True  # 是否显示可视化窗口

# ==================== 读取数据 ====================
# 假设 CSV 包含 x, y, z 三列（若无 z 列则自动填充 0）
df = pd.read_csv(csv_path)
x = df['x'].values
y = df['y'].values
z = df['z'].values if 'z' in df.columns else [0.0] * len(x)

# 创建 VTK 点集
points = vtk.vtkPoints()
points.SetDataTypeToDouble()
for xi, yi, zi in zip(x, y, z):
    points.InsertNextPoint(xi, yi, zi)

print(f"共读取 {points.GetNumberOfPoints()} 个点")

# ==================== 构建线（折线） ====================
line_source = vtk.vtkPolyLineSource()
line_source.SetPoints(points)
line_source.Update()  # 生成折线数据
line_polydata = line_source.GetOutput()

# 写入线 VTK 文件
writer = vtk.vtkPolyDataWriter()
writer.SetFileName(line_output)
writer.SetInputData(line_polydata)
writer.Write()
print(f"线数据已保存至: {line_output}")

# ==================== 构建多边形 ====================
# 创建多边形单元（假设点顺序已闭合，若不闭合需在末尾添加第一个点）
polygon = vtk.vtkPolygon()
polygon.GetPointIds().SetNumberOfIds(points.GetNumberOfPoints())
for i in range(points.GetNumberOfPoints()):
    polygon.GetPointIds().SetId(i, i)

# 将多边形加入单元数组
cells = vtk.vtkCellArray()
cells.InsertNextCell(polygon)

# 创建多边形数据集
poly_polydata = vtk.vtkPolyData()
poly_polydata.SetPoints(points)
poly_polydata.SetPolys(cells)

# 三角化（显卡只能渲染三角形，故将多边形转为三角形网格）
tri_filter = vtk.vtkTriangleFilter()
tri_filter.SetInputData(poly_polydata)
tri_filter.Update()
tri_polydata = tri_filter.GetOutput()

# 写入多边形 VTK 文件
writer.SetFileName(polygon_output)
writer.SetInputData(tri_polydata)
writer.Write()
print(f"多边形数据已保存至: {polygon_output}")

# ==================== 可选：可视化 ====================
if show_visualization:
    plotter = pv.Plotter(shape=(1, 2), window_size=(1200, 500))

    # 子图1：显示线
    plotter.subplot(0, 0)
    line_mesh = pv.wrap(line_polydata)
    plotter.add_mesh(line_mesh, color='red', line_width=3)
    plotter.add_text("Line (折线)", position='upper_left', font_size=12)

    # 子图2：显示多边形（三角化后）
    plotter.subplot(0, 1)
    poly_mesh = pv.wrap(tri_polydata)
    plotter.add_mesh(poly_mesh, color='green', show_edges=True)
    plotter.add_text("Polygon (三角化多边形)", position='upper_left', font_size=12)

    plotter.show()