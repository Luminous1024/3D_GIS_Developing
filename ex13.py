'''
一、实验目的
1.掌握Python读取与处理文本的方法；
2.掌握散点矢量数据的组织方式和方法；
3.掌握在Paraview中可视化矢量数据的主要用法；
二、实验内容
1. 读取与处理文本
2. 组织散点矢量格式
3. 在Paraview中展示散点数据并调整视觉变量
'''

#----------使用 VTK 生成散点矢量文件----------#

# import pandas as pd          # 导入pandas库，用于读取CSV文件
# import vtk                    # 导入VTK库，用于构建和保存矢量数据
# import numpy as np            # 导入numpy（虽未直接使用，但常用于数据处理，保留备用）
#
# # 1. 读取CSV文件，已知列名分别为'x','y','z','v'
# df = pd.read_csv(r'C:\Users\吕梓源\Desktop\课程\大三下学期\三维GIS开发\第一次实验\monthly_summary_202001_fit.csv')
#
# # 2. 分别提取x, y, z坐标以及气温变量v
# x = df['x']                   # 经度或X坐标
# y = df['y']                   # 纬度或Y坐标
# z = df['z']                   # 高度或Z坐标
# v = df['v']                   # 气温值
#
# # 3. 构建点集（顶点表）
# pts = vtk.vtkPoints()         # 创建vtkPoints对象，用于存储所有点的坐标
# for i in range(len(x)):       # 遍历每个站点
#     pts.InsertNextPoint(x[i], y[i], z[i])   # 插入一个点的三维坐标
#
# print("点数：", pts.GetNumberOfPoints())    # 输出点集数量，用于验证
#
# # 4. 为散点建立拓扑元（vtkVertex）及拓扑元数组（vtkCellArray）
# vtx = vtk.vtkCellArray()      # 创建vtkCellArray对象，用于存储所有顶点的单元信息
# for i in range(pts.GetNumberOfPoints()):   # 遍历每个点（使用点集点数确保一致）
#     vertex = vtk.vtkVertex()                 # 创建一个顶点对象（代表一个独立的点）
#     vertex.GetPointIds().SetId(0, i)         # 设置该顶点所引用的点的索引为i
#     vtx.InsertNextCell(vertex)                # 将该顶点添加到单元数组中
#
# # 5. 构建多边形数据集（vtkPolyData），并设置几何和拓扑
# pd = vtk.vtkPolyData()        # 创建vtkPolyData对象，用于存储几何、拓扑和属性数据
# pd.SetPoints(pts)             # 将点集设置到数据集中
# pd.SetVerts(vtx)              # 将顶点单元（散点）设置到数据集中
#
# # 6. 将气温属性数组插入到点属性数据（PointData）中
# temperature = vtk.vtkDoubleArray()   # 创建双精度浮点型数组，用于存储气温值
# temperature.SetName("temperature")   # 设置数组名称，便于在ParaView中识别
# for val in v:                        # 遍历每个点的气温值
#     temperature.InsertNextValue(val) # 将气温值插入数组
# pd.GetPointData().AddArray(temperature)   # 将气温数组添加到数据集的点属性数据中
#
# # 7. 保存为VTK矢量文件
# writer = vtk.vtkPolyDataWriter()          # 创建多边形数据写入器
# writer.SetFileName(r'C:\Users\吕梓源\Desktop\课程\大三下学期\三维GIS开发\第一次实验\monthly_summary_202001_fit.vtk')  # 设置输出文件路径
# writer.SetInputData(pd)                    # 设置要写入的数据集
# writer.Write()                              # 执行写入操作
#
# print("VTK文件已生成，包含点坐标及气温属性。")

#----------使用 PyVista 实现同样的视觉效果（仿 ParaView 样式）----------#

# import pyvista as pv # 导入PyVista库，用于可视化点云
# import pandas as pd # 导入pandas库，用于读取CSV文件
#
# # 1. 读取原始数据（或直接读取 VTK 文件）
# df = pd.read_csv(r'C:\Users\吕梓源\Desktop\课程\大三下学期\三维GIS开发\第一次实验\monthly_summary_202001_fit.csv') # 读取CSV文件
# points = df[['x', 'y', 'z']].values # 提取点坐标
# temperature = df['v'].values # 提取气温属性
#
# # 2. 创建 PyVista 点云对象
# point_cloud = pv.PolyData(points) # 创建点云对象
# point_cloud.point_data['temperature'] = temperature  # 添加气温属性
#
# # 3. 创建绘图对象
# plotter = pv.Plotter() # 创建绘图对象
# plotter.add_mesh(point_cloud, # 添加点云对象
#                  render_points_as_spheres=True,  # 对应 Marker Style = Circle
#                  point_size=10,                   # 对应 Point size
#                  scalars='temperature',           # 对应 Coloring
#                  cmap='coolwarm',                  # 颜色映射
#                  show_scalar_bar=True)             # 显示颜色条
# # 4. 在左下角添加三维坐标系
# plotter.add_axes(line_width=2)   # 可调整线条粗细，默认位置左下角
#
# # 5. 显示可视化窗口
# plotter.show() # 显示可视化窗口

#--------------------#

# import geopandas as gpd
# import vtk
# import pyvista as pv
# import numpy as np
#
# # ========== 1. 读取 Shapefile，提取第二个多边形 ==========
# gdf = gpd.read_file(r'C:\Users\吕梓源\Desktop\课程\大三下学期\三维GIS开发\第一次实验\REG.shp')
# polygon = gdf.geometry.iloc[1]   # 索引1对应第二个多边形
# print("多边形类型:", polygon.geom_type)
#
# # 处理 MultiPolygon 或 Polygon
# if polygon.geom_type == 'Polygon':
#     poly = polygon
# elif polygon.geom_type == 'MultiPolygon':
#     poly = polygon[0]   # 简化：取第一个子多边形
# else:
#     raise ValueError("不支持的几何类型")
#
# # 获取外环和内环坐标，并确保闭合但不含重复点
# def get_closed_ring(ring_coords):
#     """返回闭合但不包含最后一个重复点的坐标列表"""
#     coords = np.array(ring_coords)
#     if not np.allclose(coords[0], coords[-1]):
#         coords = np.vstack([coords, coords[0]])
#     return coords[:-1]   # 去掉最后一个重复点
#
# exterior_pts = get_closed_ring(poly.exterior.coords)
# interior_pts_list = [get_closed_ring(ring.coords) for ring in poly.interiors]
#
# # ========== 2. 方向检查函数 ==========
# def is_clockwise(pts):
#     """通过有向面积判断方向，正面积为逆时针，负面积为顺时针"""
#     area = 0.0
#     n = len(pts)
#     for i in range(n - 1):
#         area += (pts[i][0] * pts[i+1][1] - pts[i+1][0] * pts[i][1])
#     area += (pts[-1][0] * pts[0][1] - pts[0][0] * pts[-1][1])
#     return area < 0
#
# # 调整外环方向（应为逆时针）
# if is_clockwise(exterior_pts):
#     exterior_pts = exterior_pts[::-1]
#     print("外环方向已调整为逆时针")
#
# # 调整内环方向（应为顺时针）
# for i, ring in enumerate(interior_pts_list):
#     if not is_clockwise(ring):
#         interior_pts_list[i] = ring[::-1]
#         print(f"内环 {i} 方向已调整为顺时针")
#
# # ========== 3. 构建单一多边形单元（包含外环和内环所有点） ==========
# points = vtk.vtkPoints()
# # 按顺序插入所有点：先外环，后内环
# all_pts = []  # 用于记录点顺序（可选）
# for x, y in exterior_pts:
#     points.InsertNextPoint(x, y, 0.0)
#     all_pts.append((x, y))
# for ring in interior_pts_list:
#     for x, y in ring:
#         points.InsertNextPoint(x, y, 0.0)
#         all_pts.append((x, y))
#
# total_pts = points.GetNumberOfPoints()
# print(f"总点数: {total_pts}")
#
# # 创建一个多边形单元，包含所有点
# polygon_cell = vtk.vtkPolygon()
# polygon_cell.GetPointIds().SetNumberOfIds(total_pts)
# for i in range(total_pts):
#     polygon_cell.GetPointIds().SetId(i, i)
#
# # 构建 CellArray，只包含这一个单元
# cells = vtk.vtkCellArray()
# cells.InsertNextCell(polygon_cell)
#
# # 创建 Polydata
# polydata = vtk.vtkPolyData()
# polydata.SetPoints(points)
# polydata.SetPolys(cells)
#
# # ========== 4. 三角化处理 ==========
# # 4.1 vtkTriangleFilter（将单一多边形三角化，但可能填充洞）
# tri_filter = vtk.vtkTriangleFilter()
# tri_filter.SetInputData(polydata)
# tri_filter.Update()
# tri_polydata = tri_filter.GetOutput()
#
# # 4.2 vtkContourTriangulator（处理带洞多边形，正确保留洞）
# contour_tri = vtk.vtkContourTriangulator()
# contour_tri.SetInputData(polydata)
# contour_tri.Update()
# contour_output = contour_tri.GetOutput()
#
# print(f"vtkTriangleFilter 生成 {tri_polydata.GetNumberOfCells()} 个三角形")
# print(f"vtkContourTriangulator 生成 {contour_output.GetNumberOfCells()} 个三角形")
#
# # ========== 5. 分别显示三个结果（独立窗口） ==========
# original_pv = pv.wrap(polydata)
# tri_pv = pv.wrap(tri_polydata)
# contour_pv = pv.wrap(contour_output)
#
# # 窗口1：原始多边形（线框）
# plotter1 = pv.Plotter()
# plotter1.add_mesh(original_pv, color='black', line_width=2, style='wireframe', label='Original Polygon')
# plotter1.add_legend()
# plotter1.show(title="Original Polygon with Holes")
#
# # 窗口2：vtkTriangleFilter 结果（绿色半透明面）
# plotter2 = pv.Plotter()
# plotter2.add_mesh(tri_pv, color='green', opacity=0.5, label='vtkTriangleFilter', show_edges=True)
# plotter2.add_legend()
# plotter2.show(title="vtkTriangleFilter")
#
# # 窗口3：vtkContourTriangulator 结果（蓝色半透明面）
# plotter3 = pv.Plotter()
# plotter3.add_mesh(contour_pv, color='blue', opacity=0.3, label='vtkContourTriangulator', show_edges=True)
# plotter3.add_legend()
# plotter3.show(title="vtkContourTriangulator")
#
# # ========== 6. 叠加显示三个结果（同一窗口） ==========
# plotter4 = pv.Plotter()
# plotter4.add_mesh(original_pv, color='black', line_width=2, style='wireframe', label='Original Polygon')
# plotter4.add_mesh(tri_pv, color='green', opacity=0.4, label='vtkTriangleFilter', show_edges=True)
# plotter4.add_mesh(contour_pv, color='blue', opacity=0.3, label='vtkContourTriangulator', show_edges=True)
# plotter4.add_legend()
# plotter4.show(title="Overlay: Original + TriangleFilter + ContourTriangulator")

#--------------------#

'''
（二）多边形及三角化
一、实验目的
1.理解多边形的构成与构造方法
2.理解三角化与Delaunay三角化，以及为什么图形学工业里需要三角化
二、实验内容
1.以pyshp/geopandas读入reg.shp多边形数据
2.读取第2个多边形，并为之生成polygon
3.使用vtkTriangleFilter对前述多边形三角化，并叠加显示前后多边形，比较其异同
4.使用vtkDelaunay2D对前述多边形三角化，并叠加显示，比较其异同
'''

# 引入必要的库
# import shapefile # 导入shapefile库，用于读取shapefile文件
# import vtk # 导入vtk库，用于处理点云数据
# import numpy as np # 导入numpy库，用于数组操作
# import pyvista as pv # 导入pyvista库，用于可视化

# # 读取shapefile文件
# shp = shapefile.Reader(r'C:\Users\吕梓源\Desktop\课程\大三下学期\三维GIS开发\第一次实验\REG.shp', encodingErrors='ignore') # 读取shapefile文件
# print(f"Shapefile中包含 {len(shp.shapes())} 个多边形")

# # 读取第40个多边形（索引为39）
# plg1 = shp.shape(39) # 读取第40个多边形
# points = plg1.points  # 获取多边形的点坐标
# print(f"第40个多边形包含 {len(points)} 个顶点")

# # 创建VTK点集
# pts = vtk.vtkPoints()
# for point in points:
#     pts.InsertNextPoint(point[0], point[1], 0.0)  # 将2D点转换为3D点（z=0）

# # 创建多边形单元
# polygon = vtk.vtkPolygon()
# polygon.GetPointIds().SetNumberOfIds(len(points))
# for i in range(len(points)):
#     polygon.GetPointIds().SetId(i, i)

# # 创建单元数组
# cells = vtk.vtkCellArray()
# cells.InsertNextCell(polygon)

# # 创建多边形数据对象
# pd = vtk.vtkPolyData()
# pd.SetPoints(pts)
# pd.SetPolys(cells)

# print("原始多边形数据对象创建完成")

# # 写成矢量文件
# writer = vtk.vtkPolyDataWriter()
# writer.SetFileName(r'C:\Users\吕梓源\Desktop\课程\大三下学期\三维GIS开发\第一次实验\original_polygon.vtk')
# writer.SetInputData(pd)
# writer.Write()
# print("原始多边形已保存为VTK文件")

# # 三角化后再写出，生成多边形2
# tri = vtk.vtkTriangleFilter() # 创建三角化对象
# tri.SetInputData(pd) # 设置输入数据
# tri.Update() # 更新三角化对象

# # 保存三角化结果
# tri_writer = vtk.vtkPolyDataWriter()
# tri_writer.SetFileName(r'C:\Users\吕梓源\Desktop\课程\大三下学期\三维GIS开发\第一次实验\triangulated_polygon.vtk')
# tri_writer.SetInputData(tri.GetOutput())
# tri_writer.Write()
# print(f"三角化完成，生成 {tri.GetOutput().GetNumberOfCells()} 个三角形")

# # Delaunay三角化后再写出，生成多边形3
# d2d = vtk.vtkDelaunay2D() # 创建Delaunay三角化对象
# d2d.SetInputData(pd) # 设置输入数据
# d2d.Update() # 更新Delaunay三角化对象

# # 保存Delaunay三角化结果
# d2d_writer = vtk.vtkPolyDataWriter()
# d2d_writer.SetFileName(r'C:\Users\吕梓源\Desktop\课程\大三下学期\三维GIS开发\第一次实验\delaunay_polygon.vtk')
# d2d_writer.SetInputData(d2d.GetOutput())
# d2d_writer.Write()
# print(f"Delaunay三角化完成，生成 {d2d.GetOutput().GetNumberOfCells()} 个三角形")

# # 可视化比较
# print("\n开始可视化比较...")

# # 创建PyVista数据对象
# original_pv = pv.wrap(pd)
# tri_pv = pv.wrap(tri.GetOutput())
# delaunay_pv = pv.wrap(d2d.GetOutput())

# # 创建绘图窗口
# plotter = pv.Plotter(shape=(2, 2), window_size=(1200, 1000))

# # 子图1：原始多边形
# plotter.subplot(0, 0)
# plotter.add_mesh(original_pv, color='red', line_width=3, style='wireframe', 
#                 label=f'原始多边形 ({original_pv.n_cells} 个单元)')
# plotter.add_title("原始多边形")
# plotter.add_legend()

# # 子图2：三角化结果
# plotter.subplot(0, 1)
# plotter.add_mesh(tri_pv, color='green', opacity=0.7, show_edges=True,
#                 label=f'三角化 ({tri_pv.n_cells} 个三角形)')
# plotter.add_title("vtkTriangleFilter三角化")
# plotter.add_legend()

# # 子图3：Delaunay三角化结果
# plotter.subplot(1, 0)
# plotter.add_mesh(delaunay_pv, color='blue', opacity=0.7, show_edges=True,
#                 label=f'Delaunay三角化 ({delaunay_pv.n_cells} 个三角形)')
# plotter.add_title("vtkDelaunay2D三角化")
# plotter.add_legend()

# # 子图4：叠加显示比较
# plotter.subplot(1, 1)
# plotter.add_mesh(original_pv, color='red', line_width=3, style='wireframe', 
#                 label='原始多边形')
# plotter.add_mesh(tri_pv, color='green', opacity=0.5, show_edges=True,
#                 label='三角化')
# plotter.add_mesh(delaunay_pv, color='blue', opacity=0.3, show_edges=True,
#                 label='Delaunay三角化')
# plotter.add_title("叠加比较")
# plotter.add_legend()

# # 显示结果
# plotter.show()

# print("实验完成！请观察可视化结果比较三种方法的异同:")
# print("1. 原始多边形：显示为红色线框")
# print("2. 三角化结果：显示为绿色面，边缘可见")
# print("3. Delaunay三角化：显示为蓝色面，边缘可见")
# print("4. 叠加显示：可同时比较三种方法的效果")

#-------------------#

'''
一、实验目的
1.理解测绘对距离的关注
2.理解欧氏距离与表面距离
3.理解三维表面距离的计算方法
4.理解三维距离与欧氏距离比值的地理学含义
二、实验内容
1.读入sh10.vtk地形格网
2.计算高程范围
3.计算欧氏距离的距离矩阵，求其平均值
4.计算表面距离（Dijkstra距离）的距离矩阵，求其平均值
'''

# # 引入必要的库
# import vtk
# import numpy as np
# import pyvista as pv

# # 读入TIN格网
# r = vtk.vtkPLYReader() # 
# pd =  vtk.vtkPolyData() # 

# # 读出四至范围
# bs = [0,0,0,0,0,0] # 
# pd.GetBounds(bs) # 

# # 计算搞成范围zs
# N = pd.GetNumberOfPoints() # 

# # 计算欧氏距离矩阵
# dist = [] # 
# for i in range(N - 1): # 
#     for j in range(i + 1,N): # 
#         dist.append(d) # 
# print(np.min(dist),np.max(dist),np.mean(dist)) # 

# # 计算表面距离矩阵
# pd = pv.Polydata(pd) # 
# N = pd.GetNumberOfPoints() # 
# dist = [] # 
# for i in range(N - 1):
#     for j in range(i + 1,N):
#         dist.append(pd.geodesic(i,j))
# print(np.min(dist),np.max(dist),mp.mean(dist))

#----------Dijkstra算法----------#

# # 引入必要的库
# import vtk
# import numpy as np
# import pyvista as pv
# import time

# print("=== 三维表面距离计算实验 ===")

# # 读入TIN格网（sh10.vtk文件）
# print("1. 读取TIN格网数据...")
# reader = vtk.vtkPolyDataReader()  # 创建VTK polydata读取器
# reader.SetFileName(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\sh10.vtk')  # 设置文件路径
# reader.Update()  # 读取数据

# # 获取读取的多边形数据
# pd = reader.GetOutput()  # 获取输出的polydata
# print(f"成功读取TIN格网，包含 {pd.GetNumberOfPoints()} 个顶点和 {pd.GetNumberOfCells()} 个单元")

# # 读出四至范围（边界范围）
# print("\n2. 计算地形范围信息...")
# bounds = [0, 0, 0, 0, 0, 0]  # 初始化边界数组[xmin, xmax, ymin, ymax, zmin, zmax]
# pd.GetBounds(bounds)  # 获取数据边界
# print(f"地形范围:")
# print(f"  X方向: {bounds[0]:.2f} 到 {bounds[1]:.2f} (范围: {bounds[1]-bounds[0]:.2f})")
# print(f"  Y方向: {bounds[2]:.2f} 到 {bounds[3]:.2f} (范围: {bounds[3]-bounds[2]:.2f})")
# print(f"  Z方向: {bounds[4]:.2f} 到 {bounds[5]:.2f} (高程范围: {bounds[5]-bounds[4]:.2f})")

# # 计算高程统计信息
# print(f"\n高程统计信息:")
# print(f"  最低高程: {bounds[4]:.2f}")
# print(f"  最高高程: {bounds[5]:.2f}")
# print(f"  高程差: {bounds[5]-bounds[4]:.2f}")

# # 获取点数
# N = pd.GetNumberOfPoints()
# print(f"\n3. 计算欧氏距离矩阵...")
# print(f"总点数: {N}，需要计算 {N*(N-1)//2} 对距离")

# # 计算欧氏距离矩阵（三维欧氏距离）
# euclidean_distances = []  # 存储所有欧氏距离
# points_array = []  # 存储点坐标用于后续计算

# # 首先获取所有点坐标
# for i in range(N):
#     point = pd.GetPoint(i)  # 获取第i个点的坐标
#     points_array.append([point[0], point[1], point[2]])  # 存储为numpy数组格式

# points_array = np.array(points_array)  # 转换为numpy数组以提高计算效率

# # 计算所有点对的欧氏距离
# print("正在计算欧氏距离矩阵...")
# start_time = time.time()
# for i in range(N - 1):
#     for j in range(i + 1, N):
#         # 计算三维欧氏距离
#         point1 = points_array[i]
#         point2 = points_array[j]
#         distance = np.sqrt(np.sum((point1 - point2)**2))  # 三维欧氏距离公式
#         euclidean_distances.append(distance)

# euclidean_time = time.time() - start_time
# print(f"欧氏距离计算完成，耗时: {euclidean_time:.2f}秒")

# # 统计欧氏距离信息
# print(f"\n欧氏距离统计:")
# print(f"  最小距离: {np.min(euclidean_distances):.4f}")
# print(f"  最大距离: {np.max(euclidean_distances):.4f}")
# print(f"  平均距离: {np.mean(euclidean_distances):.4f}")
# print(f"  标准差: {np.std(euclidean_distances):.4f}")

# # 计算表面距离矩阵（Dijkstra距离）
# print(f"\n4. 计算表面距离矩阵...")
# print("注意：表面距离计算可能较慢，请耐心等待...")

# # 将VTK数据转换为PyVista格式以使用geodesic计算
# pv_mesh = pv.wrap(pd)  # 转换为PyVista网格对象
# surface_distances = []  # 存储所有表面距离

# start_time = time.time()
# calculated_pairs = 0  # 已计算的点对数
# total_pairs = N * (N - 1) // 2  # 总点对数

# for i in range(N - 1):
#     for j in range(i + 1, N):
#         try:
#             # 计算表面距离（测地线距离）
#             geodesic_path = pv_mesh.geodesic(i, j)  # 计算两点间的最短表面路径
#             surface_distance = geodesic_path['GeodesicLength'][0]  # 获取表面距离
#             surface_distances.append(surface_distance)
#         except Exception as e:
#             # 如果计算失败，使用欧氏距离作为备选
#             print(f"警告：点 {i} 到点 {j} 的表面距离计算失败，使用欧氏距离替代")
#             point1 = points_array[i]
#             point2 = points_array[j]
#             fallback_distance = np.sqrt(np.sum((point1 - point2)**2))
#             surface_distances.append(fallback_distance)
        
#         calculated_pairs += 1
#         if calculated_pairs % 100 == 0:  # 每100对显示进度
#             print(f"进度: {calculated_pairs}/{total_pairs} ({calculated_pairs/total_pairs*100:.1f}%)")

# surface_time = time.time() - start_time
# print(f"表面距离计算完成，耗时: {surface_time:.2f}秒")

# # 统计表面距离信息
# print(f"\n表面距离统计:")
# print(f"  最小距离: {np.min(surface_distances):.4f}")
# print(f"  最大距离: {np.max(surface_distances):.4f}")
# print(f"  平均距离: {np.mean(surface_distances):.4f}")
# print(f"  标准差: {np.std(surface_distances):.4f}")

# # 计算距离比值分析
# print(f"\n5. 距离比值分析...")
# ratio = np.array(surface_distances) / np.array(euclidean_distances)
# print(f"表面距离/欧氏距离比值统计:")
# print(f"  最小比值: {np.min(ratio):.4f}")
# print(f"  最大比值: {np.max(ratio):.4f}")
# print(f"  平均比值: {np.mean(ratio):.4f}")
# print(f"  标准差: {np.std(ratio):.4f}")

# # 地理学含义解释
# print(f"\n6. 地理学含义分析:")
# print(f"  平均比值 {np.mean(ratio):.4f} 表示地形对距离的放大效应")
# print(f"  比值 > 1：表面距离大于欧氏距离，存在地形起伏")
# print(f"  比值 ≈ 1：表面距离接近欧氏距离，地形相对平坦")
# print(f"  比值越大：地形越复杂，起伏越剧烈")

# # 可视化结果
# print(f"\n7. 生成可视化结果...")

# # 创建绘图窗口
# plotter = pv.Plotter(shape=(2, 2), window_size=(1200, 1000))

# # 子图1：原始地形网格
# plotter.subplot(0, 0)
# plotter.add_mesh(pv_mesh, color='tan', show_edges=True, 
#                 label=f'地形网格 ({N} 个点)')
# plotter.add_title("原始地形TIN网格")
# plotter.show_axes()

# # 子图2：高程分布
# plotter.subplot(0, 1)
# elevation = pv_mesh.points[:, 2]  # 获取高程值
# plotter.add_mesh(pv_mesh, scalars=elevation, cmap='terrain', 
#                 show_edges=False, label='高程分布')
# plotter.add_scalar_bar("高程 (m)")
# plotter.add_title("高程分布图")

# # 子图3：距离分布直方图
# plotter.subplot(1, 0)
# import matplotlib.pyplot as plt
# fig, ax = plt.subplots(figsize=(6, 4))
# ax.hist(euclidean_distances, bins=50, alpha=0.7, label='欧氏距离', color='blue')
# ax.hist(surface_distances, bins=50, alpha=0.7, label='表面距离', color='red')
# ax.set_xlabel('距离')
# ax.set_ylabel('频数')
# ax.set_title('距离分布直方图')
# ax.legend()
# ax.grid(True, alpha=0.3)
# plotter.add_figure(fig, position=[0, 0], scale=0.8)
# plotter.add_title("距离分布对比")

# # 子图4：比值分布
# plotter.subplot(1, 1)
# fig2, ax2 = plt.subplots(figsize=(6, 4))
# ax2.hist(ratio, bins=50, alpha=0.7, color='green', edgecolor='black')
# ax2.set_xlabel('表面距离/欧氏距离比值')
# ax2.set_ylabel('频数')
# ax2.set_title('距离比值分布')
# ax2.axvline(np.mean(ratio), color='red', linestyle='--', 
#            label=f'平均值: {np.mean(ratio):.3f}')
# ax2.legend()
# ax2.grid(True, alpha=0.3)
# plotter.add_figure(fig2, position=[0, 0], scale=0.8)
# plotter.add_title("距离比值分布")

# # 显示结果
# plotter.show()

# print(f"\n=== 实验总结 ===")
# print(f"1. 地形高程范围: {bounds[4]:.2f}m - {bounds[5]:.2f}m")
# print(f"2. 欧氏距离平均: {np.mean(euclidean_distances):.4f}")
# print(f"3. 表面距离平均: {np.mean(surface_distances):.4f}")
# print(f"4. 地形放大效应: {np.mean(ratio):.4f} 倍")
# print(f"5. 计算效率: 欧氏距离 {euclidean_time:.2f}s, 表面距离 {surface_time:.2f}s")
# print(f"\n实验完成！通过比较欧氏距离和表面距离，可以量化地形的复杂程度。")

#----------HM算法----------#

# # 引入必要的库
# import vtk # 引入vtk库，用于读取vtk文件
# import numpy as np # 引入numpy库，用于数组操作
# import pyvista as pv # 引入pyvista库，用于可视化结果
# import time # 引入time库，用于计算计算时间
# import matplotlib.pyplot as plt # 引入matplotlib用于绘图
# import potpourri3d as pp3d # 导入potpourri3d库用于HM方法计算

# print("=== 三维表面距离计算实验 ===")

# # 读入TIN格网（注意：应该是VTK格式，不是PLY格式）
# print("1. 读取TIN格网数据...")

# # 读取VTK格式的文件
# reader = vtk.vtkPolyDataReader()
# reader.SetFileName(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\sh10.vtk')
# reader.Update()
# pd = reader.GetOutput()

# print(f"成功读取TIN格网，包含 {pd.GetNumberOfPoints()} 个顶点和 {pd.GetNumberOfCells()} 个单元")

# # 读出四至范围（边界范围）
# print("\n2. 计算地形范围信息...")
# bounds = [0, 0, 0, 0, 0, 0]  # 初始化边界数组[xmin, xmax, ymin, ymax, zmin, zmax]
# pd.GetBounds(bounds)  # 获取数据边界
# print(f"地形范围:")
# print(f"  X方向: {bounds[0]:.2f} 到 {bounds[1]:.2f} (范围: {bounds[1]-bounds[0]:.2f})")
# print(f"  Y方向: {bounds[2]:.2f} 到 {bounds[3]:.2f} (范围: {bounds[3]-bounds[2]:.2f})")
# print(f"  Z方向: {bounds[4]:.2f} 到 {bounds[5]:.2f} (高程范围: {bounds[5]-bounds[4]:.2f})")

# # 计算高程统计信息
# print(f"\n高程统计信息:")
# print(f"  最低高程: {bounds[4]:.2f}")
# print(f"  最高高程: {bounds[5]:.2f}")
# print(f"  高程差: {bounds[5]-bounds[4]:.2f}")

# # 获取点数
# N = pd.GetNumberOfPoints()
# if N == 0:
#     print("错误：没有读取到任何点数据！")
#     exit(1)
    
# print(f"\n3. 计算欧氏距离矩阵...")
# print(f"总点数: {N}，需要计算 {N*(N-1)//2} 对距离")

# # 计算欧氏距离矩阵
# euclidean_distances = [] # 存储欧氏距离的列表
# print("正在计算欧氏距离矩阵...")
# start_time = time.time()

# for i in range(N - 1): # 遍历所有点对
#     for j in range(i + 1, N): # 避免重复计算
#         # 获取两个点的坐标
#         point1 = pd.GetPoint(i)
#         point2 = pd.GetPoint(j)
#         # 计算三维欧氏距离
#         d = np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2 + (point1[2] - point2[2])**2)
#         euclidean_distances.append(d) # 将距离添加到列表

# euclidean_time = time.time() - start_time
# print(f"欧氏距离计算完成，耗时: {euclidean_time:.2f}秒")
# print(f"计算了 {len(euclidean_distances)} 对距离")
# print(f"欧氏距离统计 - 最小值: {np.min(euclidean_distances):.4f}, 最大值: {np.max(euclidean_distances):.4f}, 平均值: {np.mean(euclidean_distances):.4f}")

# # 计算表面距离矩阵 - 使用HM（Heat Method）方法
# print("使用HM（Heat Method）方法计算表面距离，比Dijkstra算法更快更精确...")

# # 将VTK数据转换为PyVista格式
# pv_mesh = pv.wrap(pd)

# # 获取顶点和面片数据
# vertices = pv_mesh.points  # 获取所有顶点坐标
# faces = pv_mesh.faces  # 获取面片连接关系

# # 处理面片数据格式（PyVista格式转换为HM方法需要的格式）
# # PyVista的faces格式：[n0, p0_0, p0_1, ..., p0_n0-1, n1, p1_0, p1_1, ..., p1_n1-1, ...]
# # HM方法需要格式：[[p0_0, p0_1, p0_2], [p1_0, p1_1, p1_2], ...]
# faces_array = faces.reshape(-1, 4)[:, 1:]  # 假设是三角形网格，每4个元素为一组，去掉第一个元素（顶点数）

# print(f"顶点数: {vertices.shape[0]}, 面片数: {faces_array.shape[0]}")

# # 创建HM距离求解器
# print("正在初始化HM距离求解器...")
# solver = pp3d.MeshHeatMethodDistanceSolver(vertices, faces_array)
# print("HM求解器初始化完成")

# # 计算表面距离矩阵
# surface_distances = []  # 存储表面距离的列表
# N = vertices.shape[0]  # 获取顶点总数

# print(f"开始计算表面距离矩阵，共 {N*(N-1)//2} 对距离...")
# start_time = time.time()

# for i in range(N - 1):
#     # 为每个顶点计算到所有其他顶点的距离
#     distances = solver.compute_distance(i)  # 计算从点i到所有点的距离
    
#     for j in range(i + 1, N):
#         surface_distance = distances[j]  # 获取点i到点j的距离
#         surface_distances.append(surface_distance)
    
#     # 显示进度
#     if (i + 1) % 10 == 0:  # 每10个源点显示一次进度
#         progress = (i + 1) / N * 100
#         elapsed_time = time.time() - start_time
#         estimated_total_time = elapsed_time / (i + 1) * N
#         remaining_time = estimated_total_time - elapsed_time
#         print(f"进度: {progress:.1f}% ({i+1}/{N}), 已用时间: {elapsed_time:.1f}s, 预计剩余: {remaining_time:.1f}s")

# surface_time = time.time() - start_time
# print(f"表面距离计算完成，耗时: {surface_time:.2f}秒")

# # 统计表面距离信息
# print(f"\n表面距离统计:")
# print(f"  最小距离: {np.min(surface_distances):.4f}")
# print(f"  最大距离: {np.max(surface_distances):.4f}")
# print(f"  平均距离: {np.mean(surface_distances):.4f}")
# print(f"  标准差: {np.std(surface_distances):.4f}")

# # 计算距离比值分析
# print(f"\n距离比值分析 (表面距离/欧氏距离):")
# ratio = np.array(surface_distances) / np.array(euclidean_distances)
# print(f"  最小比值: {np.min(ratio):.4f}")
# print(f"  最大比值: {np.max(ratio):.4f}")
# print(f"  平均比值: {np.mean(ratio):.4f}")
# print(f"  标准差: {np.std(ratio):.4f}")

# # 地理学含义解释
# print(f"\n地理学含义分析:")
# print(f"  平均比值 {np.mean(ratio):.4f} 表示地形对距离的放大效应")
# print(f"  比值 > 1：表面距离大于欧氏距离，存在地形起伏")
# print(f"  比值 ≈ 1：表面距离接近欧氏距离，地形相对平坦")
# print(f"  比值越大：地形越复杂，起伏越剧烈")

# # 性能对比和变量验证
# print(f"\n性能对比:")
# print(f"  HM方法计算时间: {surface_time:.2f}秒")
# print(f"  相比Dijkstra方法，HM方法通常快10-100倍")
# print(f"  且HM方法提供更精确的测地距离计算")

# # 可视化结果
# print(f"\n7. 生成可视化结果...")

# # 创建绘图窗口
# plotter = pv.Plotter(shape=(2, 2), window_size=(1200, 1000))

# # 子图1：原始地形网格
# plotter.subplot(0, 0)
# plotter.add_mesh(pv_mesh, color='tan', show_edges=True, 
#                 label=f'地形网格 ({N} 个点)')
# plotter.add_title("原始地形TIN网格")
# plotter.show_axes()

# # 子图2：高程分布
# plotter.subplot(0, 1)
# elevation = pv_mesh.points[:, 2]  # 获取高程值
# plotter.add_mesh(pv_mesh, scalars=elevation, cmap='terrain', 
#                 show_edges=False, label='高程分布')
# plotter.add_scalar_bar("高程 (m)")
# plotter.add_title("高程分布图")

# # 子图3：距离分布分析（使用PyVista原生方法）
# plotter.subplot(1, 0)
# # 创建距离数据用于可视化分析
# distance_data = np.zeros(len(euclidean_distances))
# for i, (euc_dist, surf_dist) in enumerate(zip(euclidean_distances, surface_distances)):
#     distance_data[i] = surf_dist - euc_dist  # 差异值

# # 创建简单的条形图显示统计信息
# stats_text = f"""距离统计对比:
# 欧氏距离:
#   最小值: {np.min(euclidean_distances):.3f}
#   最大值: {np.max(euclidean_distances):.3f}
#   平均值: {np.mean(euclidean_distances):.3f}

# 表面距离:
#   最小值: {np.min(surface_distances):.3f}
#   最大值: {np.max(surface_distances):.3f}
#   平均值: {np.mean(surface_distances):.3f}

# 差异分析:
#   平均差异: {np.mean(distance_data):.3f}
#   最大差异: {np.max(distance_data):.3f}"""

# plotter.add_text(stats_text, position='upper_left', font_size=10)
# plotter.add_title("HM方法距离分析")

# # 子图4：HM方法特点展示
# plotter.subplot(1, 1)
# # 创建比值颜色映射
# ratio_colors = np.array(ratio)
# ratio_mesh = pv_mesh.copy()
# ratio_mesh.point_data['距离比值'] = np.zeros(N)

# # 将比值数据映射到网格顶点（用于可视化）
# idx = 0
# for i in range(N - 1):
#     for j in range(i + 1, N):
#         # 简单映射：将比值赋给两个顶点
#         ratio_mesh.point_data['距离比值'][i] = max(ratio_mesh.point_data['距离比值'][i], ratio_colors[idx])
#         ratio_mesh.point_data['距离比值'][j] = max(ratio_mesh.point_data['距离比值'][j], ratio_colors[idx])
#         idx += 1

# plotter.add_mesh(ratio_mesh, scalars='距离比值', cmap='coolwarm', 
#                 show_edges=False, clim=[1.0, np.max(ratio_colors)])
# plotter.add_scalar_bar("表面距离/欧氏距离比值")
# plotter.add_title("地形复杂度可视化")

# # 显示结果
# plotter.show()

# # 生成独立的统计图表（可选）
# print("\n生成详细统计图表...")
# import matplotlib.pyplot as plt
# fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))

# # 距离分布直方图
# ax1.hist(euclidean_distances, bins=50, alpha=0.7, label='欧氏距离', color='blue', density=True)
# ax1.hist(surface_distances, bins=50, alpha=0.7, label='表面距离', color='red', density=True)
# ax1.set_xlabel('距离')
# ax1.set_ylabel('密度')
# ax1.set_title('距离分布对比（HM方法）')
# ax1.legend()
# ax1.grid(True, alpha=0.3)

# # 比值分布
# ax2.hist(ratio, bins=50, alpha=0.7, color='green', edgecolor='black', density=True)
# ax2.axvline(np.mean(ratio), color='red', linestyle='--', 
#            label=f'平均值: {np.mean(ratio):.3f}')
# ax2.set_xlabel('表面距离/欧氏距离比值')
# ax2.set_ylabel('密度')
# ax2.set_title('距离比值分布')
# ax2.legend()
# ax2.grid(True, alpha=0.3)

# # 差异散点图
# ax3.scatter(euclidean_distances, surface_distances, alpha=0.5, s=1)
# ax3.plot([0, max(euclidean_distances)], [0, max(euclidean_distances)], 'r--', label='1:1线')
# ax3.set_xlabel('欧氏距离')
# ax3.set_ylabel('表面距离')
# ax3.set_title('欧氏距离 vs 表面距离（HM方法）')
# ax3.legend()
# ax3.grid(True, alpha=0.3)

# # 性能对比
# methods = ['欧氏距离', 'HM表面距离']
# times = [euclidean_time, surface_time]
# colors = ['blue', 'red']
# bars = ax4.bar(methods, times, color=colors, alpha=0.7)
# ax4.set_ylabel('计算时间 (秒)')
# ax4.set_title('计算性能对比')
# ax4.grid(True, alpha=0.3)

# # 在柱状图上添加数值标签
# for bar, time_val in zip(bars, times):
#     height = bar.get_height()
#     ax4.text(bar.get_x() + bar.get_width()/2., height + 0.01,
#              f'{time_val:.2f}s', ha='center', va='bottom')

# plt.tight_layout()
# plt.savefig('hm_method_analysis.png', dpi=300, bbox_inches='tight')
# print("统计图表已保存为 'hm_method_analysis.png'")

# print(f"\n=== 实验总结 ===")
# print(f"1. 地形高程范围: {bounds[4]:.2f}m - {bounds[5]:.2f}m")
# print(f"2. 欧氏距离平均: {np.mean(euclidean_distances):.4f}")
# print(f"3. 表面距离平均: {np.mean(surface_distances):.4f}")
# print(f"4. 地形放大效应: {np.mean(ratio):.4f} 倍")
# if euclidean_time > 0 and surface_time > 0:
#     print(f"5. 计算效率: 欧氏距离 {euclidean_time:.2f}s, 表面距离 {surface_time:.2f}s")
#     print(f"   表面距离计算时间比欧氏距离长 {surface_time/euclidean_time:.1f} 倍")
# print(f"\n实验完成！通过比较欧氏距离和表面距离，可以量化地形的复杂程度。")

# ---------- HM算法（中文优先版，修复双色带，自定义保存路径）----------

import vtk
import numpy as np
import pyvista as pv
import time
import matplotlib.pyplot as plt
import potpourri3d as pp3d
from scipy.spatial.distance import pdist
import random
import os
from matplotlib.font_manager import FontProperties

# ------------------ 解决matplotlib中文显示 ------------------
def get_chinese_font():
    font_paths = [
        'C:/Windows/Fonts/simhei.ttf',
        'C:/Windows/Fonts/msyh.ttc',
        'C:/Windows/Fonts/simsun.ttc',
    ]
    for path in font_paths:
        if os.path.exists(path):
            return FontProperties(fname=path, size=12)
    return None

chinese_font = get_chinese_font()
if chinese_font:
    print("已加载中文字体，综合图表将显示中文。")
    plt.rcParams['font.sans-serif'] = [chinese_font.get_name()]
    plt.rcParams['axes.unicode_minus'] = False
else:
    print("警告：未找到中文字体文件，综合图表将使用英文。")

print("=== 三维表面距离计算实验（中文优先版）===")

# 1. 读取TIN格网
print("1. 读取TIN格网数据...")
reader = vtk.vtkPolyDataReader()
reader.SetFileName(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\sh10.vtk')
reader.Update()
pd = reader.GetOutput()
print(f"成功读取TIN格网，包含 {pd.GetNumberOfPoints()} 个顶点和 {pd.GetNumberOfCells()} 个单元")

# 2. 地形范围信息
print("\n2. 计算地形范围信息...")
bounds = [0, 0, 0, 0, 0, 0]
pd.GetBounds(bounds)
print(f"地形范围:")
print(f"  X方向: {bounds[0]:.2f} 到 {bounds[1]:.2f} (范围: {bounds[1]-bounds[0]:.2f})")
print(f"  Y方向: {bounds[2]:.2f} 到 {bounds[3]:.2f} (范围: {bounds[3]-bounds[2]:.2f})")
print(f"  Z方向: {bounds[4]:.2f} 到 {bounds[5]:.2f} (高程范围: {bounds[5]-bounds[4]:.2f})")

points = np.array([pd.GetPoint(i) for i in range(pd.GetNumberOfPoints())])
N = points.shape[0]
print(f"\n总点数: {N}")

# 3. 欧氏距离
print("\n3. 计算欧氏距离矩阵...")
start_time = time.time()
euclidean_distances = pdist(points, metric='euclidean')
euclidean_time = time.time() - start_time
print(f"欧氏距离计算完成，耗时: {euclidean_time:.2f}秒")
print(f"欧氏距离统计 - 最小值: {np.min(euclidean_distances):.4f}, 最大值: {np.max(euclidean_distances):.4f}, 平均值: {np.mean(euclidean_distances):.4f}")

# 4. 准备HM方法数据
print("\n4. 准备HM方法数据...")
pv_mesh = pv.wrap(pd)
vertices = pv_mesh.points
faces = pv_mesh.faces
faces_array = faces.reshape(-1, 4)[:, 1:]
print(f"顶点数: {vertices.shape[0]}, 面片数: {faces_array.shape[0]}")

# 5. 初始化HM求解器
print("\n5. 初始化HM距离求解器...")
solver = pp3d.MeshHeatMethodDistanceSolver(vertices, faces_array)
print("HM求解器初始化完成")

# 6. 计算表面距离矩阵
print(f"\n6. 计算表面距离矩阵，共 {N*(N-1)//2} 对距离...")
surface_distances = []
start_time = time.time()

for i in range(N - 1):
    distances = solver.compute_distance(i)
    for j in range(i + 1, N):
        surface_distances.append(distances[j])
    if (i + 1) % 10 == 0:
        progress = (i + 1) / N * 100
        elapsed = time.time() - start_time
        estimated = elapsed / (i + 1) * N
        print(f"进度: {progress:.1f}% ({i+1}/{N}), 已用: {elapsed:.1f}秒, 剩余: {estimated - elapsed:.1f}秒")

surface_time = time.time() - start_time
surface_distances = np.array(surface_distances)
print(f"表面距离计算完成，耗时: {surface_time:.2f}秒")
print(f"表面距离统计 - 最小值: {np.min(surface_distances):.4f}, 最大值: {np.max(surface_distances):.4f}, 平均值: {np.mean(surface_distances):.4f}")

# 7. 距离比值
ratio = surface_distances / euclidean_distances
print(f"\n距离比值分析 (表面距离/欧氏距离):")
print(f"  最小比值: {np.min(ratio):.4f}, 最大比值: {np.max(ratio):.4f}, 平均比值: {np.mean(ratio):.4f}")
print(f"地理学含义: 平均比值 {np.mean(ratio):.4f} 表示地形对距离的放大效应，比值越大地形越复杂。")

# ========== 独立可视化部分 ==========
print("\n7. 生成独立可视化图形...")
print("注意：PyVista窗口因不支持中文，标题/标签使用英文。")

# 图1：原始地形网格
print("  显示图1：原始地形网格...")
plotter1 = pv.Plotter(window_size=[800, 600])
plotter1.add_mesh(pv_mesh, color='tan', show_edges=True, label=f'TIN Mesh ({N} points)')
plotter1.add_title("Original TIN Mesh")
plotter1.show_axes()
plotter1.show()

# 图2：高程分布图（修复双色带）
print("  显示图2：高程分布图...")
plotter2 = pv.Plotter(window_size=[800, 600])
elevation = pv_mesh.points[:, 2]
plotter2.add_mesh(pv_mesh, scalars=elevation, cmap='terrain', show_edges=False, show_scalar_bar=False)
plotter2.add_scalar_bar("Elevation (m)", title_font_size=10, label_font_size=10)
plotter2.add_title("Elevation Distribution")
plotter2.show_axes()
plotter2.show()

# 图3：统计结果打印到控制台
print("\n  图3：距离统计结果（打印到控制台）:")
diff = surface_distances - euclidean_distances
print("-" * 50)
print("欧氏距离统计:")
print(f"  最小值: {np.min(euclidean_distances):10.3f}")
print(f"  最大值: {np.max(euclidean_distances):10.3f}")
print(f"  平均值: {np.mean(euclidean_distances):10.3f}")
print("\n表面距离统计 (HM方法):")
print(f"  最小值: {np.min(surface_distances):10.3f}")
print(f"  最大值: {np.max(surface_distances):10.3f}")
print(f"  平均值: {np.mean(surface_distances):10.3f}")
print("\n差异分析:")
print(f"  平均差异: {np.mean(diff):10.3f}")
print(f"  最大差异: {np.max(diff):10.3f}")
print("-" * 50)

# 图4：地形复杂度可视化
print("  显示图4：地形复杂度可视化...")
vertex_ratio = np.zeros(N)
n_samples = min(5000, len(ratio))
sample_indices = random.sample(range(len(ratio)), n_samples)

def get_pair_from_index(idx, N):
    i = 0
    total = N - 1
    while idx >= total:
        idx -= total
        total -= 1
        i += 1
    j = i + 1 + idx
    return i, j

for idx in sample_indices:
    i, j = get_pair_from_index(idx, N)
    r = ratio[idx]
    if r > vertex_ratio[i]:
        vertex_ratio[i] = r
    if r > vertex_ratio[j]:
        vertex_ratio[j] = r

ratio_mesh = pv_mesh.copy()
ratio_mesh.point_data['Distance Ratio'] = vertex_ratio
plotter4 = pv.Plotter(window_size=[800, 600])
plotter4.add_mesh(ratio_mesh, scalars='Distance Ratio', cmap='coolwarm', show_edges=False,
                  clim=[1.0, np.max(vertex_ratio)])
plotter4.add_scalar_bar("Surface/Euclidean Ratio")
plotter4.add_title("Terrain Complexity (Sampled Ratio)")
plotter4.show_axes()
plotter4.show()

# ========== 生成详细统计图表（保存到指定路径） ==========
print("\n生成详细统计图表...")
# 设置保存路径
save_dir = r'C:\Users\吕梓源\Desktop\课程\大三下学期\三维GIS开发\第一次实验'
os.makedirs(save_dir, exist_ok=True)  # 自动创建文件夹（如果不存在）
save_path = os.path.join(save_dir, 'hm_method_analysis_final.png')

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))

ax1.hist(euclidean_distances, bins=50, alpha=0.7, label='欧氏距离', color='blue', density=True)
ax1.hist(surface_distances, bins=50, alpha=0.7, label='表面距离', color='red', density=True)
ax1.set_xlabel('距离')
ax1.set_ylabel('密度')
ax1.set_title('距离分布对比（HM方法）')
ax1.legend()
ax1.grid(True, alpha=0.3)

ax2.hist(ratio, bins=50, alpha=0.7, color='green', edgecolor='black', density=True)
ax2.axvline(np.mean(ratio), color='red', linestyle='--', label=f'平均值: {np.mean(ratio):.3f}')
ax2.set_xlabel('表面距离/欧氏距离比值')
ax2.set_ylabel('密度')
ax2.set_title('距离比值分布')
ax2.legend()
ax2.grid(True, alpha=0.3)

sample_step = max(1, len(euclidean_distances) // 5000)
sample_idx = np.arange(0, len(euclidean_distances), sample_step)
ax3.scatter(euclidean_distances[sample_idx], surface_distances[sample_idx], alpha=0.5, s=1)
ax3.plot([0, max(euclidean_distances)], [0, max(euclidean_distances)], 'r--', label='1:1线')
ax3.set_xlabel('欧氏距离')
ax3.set_ylabel('表面距离')
ax3.set_title('欧氏距离 vs 表面距离（采样显示）')
ax3.legend()
ax3.grid(True, alpha=0.3)

methods = ['欧氏距离 (pdist)', 'HM表面距离']
times = [euclidean_time, surface_time]
bars = ax4.bar(methods, times, color=['blue','red'], alpha=0.7)
ax4.set_ylabel('计算时间 (秒)')
ax4.set_title('计算性能对比')
ax4.grid(True, alpha=0.3)
for bar, t in zip(bars, times):
    ax4.text(bar.get_x() + bar.get_width()/2., t + 0.01, f'{t:.2f}s', ha='center', va='bottom')

if chinese_font:
    for ax_ in [ax1, ax2, ax3, ax4]:
        for item in ([ax_.title, ax_.xaxis.label, ax_.yaxis.label] +
                     ax_.get_xticklabels() + ax_.get_yticklabels()):
            item.set_fontproperties(chinese_font)
    for ax_ in [ax1, ax2, ax3]:
        leg = ax_.get_legend()
        if leg:
            for text in leg.get_texts():
                text.set_fontproperties(chinese_font)

plt.tight_layout()
plt.savefig(save_path, dpi=300, bbox_inches='tight')
print(f"综合统计图表已保存为: {save_path}")
plt.show()

print(f"\n=== 实验总结 ===")
print(f"1. 地形高程范围: {bounds[4]:.2f}m - {bounds[5]:.2f}m")
print(f"2. 欧氏距离平均: {np.mean(euclidean_distances):.4f}")
print(f"3. 表面距离平均: {np.mean(surface_distances):.4f}")
print(f"4. 地形放大效应: {np.mean(ratio):.4f} 倍")
print(f"5. 计算效率: 欧氏距离 {euclidean_time:.2f}秒, 表面距离 {surface_time:.2f}秒")
print(f"\n实验完成！")
