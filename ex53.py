# import vtk # 导入vtk库，用于创建多Data对象
# import pyvista as pv # 导入pyvista库，用于绘制多Data对象
# import numpy as np # 导入numpy库，用于处理数组
#
# box = vtk.vtkCubeSource() # 创建vtkCubeSource对象，用于创建立方体多Data对象
# box.SetCenter(0,0,0) # 设置立方体的中心坐标 —— 目标点所属的面的平面切割
# box.Update() # 更新立方体多Data对象，进行切割
# tri = vtk.vtkTriangleFilter() # 创建vtkTriangleFilter对象，用于将多边对象转换为三角形对象
# tri.SetInputConnection(box.GetOutputPort()) # 设置输入数据为立方体多Data对象 —— 目标点所属的面的平面切割
# tri.Update() # 更新三角形过滤器，进行转换
#
#
# sphere = vtk.vtkSphereSource() # 创建vtkSphereSource对象，用于创建球体多Data对象
# sphere.SetCenter(0,0,0) # 设置球体的中心坐标 —— 目标点所属的面的平面切割
# sphere.SetRadius(0.6) # 设置球体的半径 —— 目标点所属的面的平面切割
# sphere.SetPhiResolution(80) # 设置球体的Phi分辨率 —— 目标点所属的面的平面切割
# sphere.SetThetaResolution(80) # 设置球体的Theta分辨率 —— 目标点所属的面的平面切割
# sphere.Update() # 更新球体多Data对象，进行切割
#
# # 进行布尔交集操作
# bo = vtk.vtkBooleanOperationPolyDataFilter() # 创建vtkBooleanOperationPolyDataFilter对象，用于进行布尔操作
# bo.SetInputData(0,tri.GetOutput()) # 设置布尔操作的第一个输入为立方体多Data对象
# bo.SetInputData(1,sphere.GetOutput()) # 设置布尔操作的第二个输入为球体多Data对象
# bo.SetOperationToIntersection() # 设置布尔操作为交集操作
# bo.Update() # 更新布尔操作多Data对象，进行交集操作
#
# bo_diff = vtk.vtkBooleanOperationPolyDataFilter() # 创建vtkBooleanOperationPolyDataFilter对象，用于进行布尔操作
# bo_diff.SetInputData(0,tri.GetOutput()) # 设置布尔操作的第一个输入为立方体多Data对象
# bo_diff.SetInputData(0,tri.GetOutput()) # 设置布尔操作的第二个输入为立方体多Data对象
# bo_diff.SetInputData(1,sphere.GetOutput()) # 设置布尔操作的第三个输入为球体多Data对象
# bo_diff.SetOperationToDifference() # 设置布尔操作为差集操作
# bo_diff.Update() # 更新布尔操作多Data对象，进行差集操作
#
# # pb = pv.PolyData(box.GetOutput()) # 创建pyvista多Data对象，用于存储立方体多Data对象 —— 目标点所属的面的平面切割
# # pb.plot() # 绘制立方体多Data对象 —— 目标点所属的面的平面切割
#
# pb = pv.PolyData(tri.GetOutput()) # 创建pyvista多Data对象，用于存储立方体多Data对象 —— 目标点所属的面的平面切割
# ps = pv.PolyData(sphere.GetOutput()) # 创建pyvista多Data对象，用于存储球体多Data对象 —— 目标点所属的面的平面切割
# pb.plot() # 绘制立方体多Data对象 —— 目标点所属的面的平面切割
#
# pl = pv.Plotter() # 创建pyvistaPlotter对象，用于绘制多Data对象 —— 目标点所属的面的平面切割
# pl.add_mesh(pb,color = 'green') # 添加立方体多Data对象到pyvistaPlotter对象 —— 目标点所属的面的平面切割
# pl.add_mesh(ps,color = 'blue') # 添加球体多Data对象到pyvistaPlotter对象 —— 目标点所属的面的平面切割
# pl.add_mesh(bo.GetOutput(),color = 'red') # 添加布尔操作多Data对象到pyvistaPlotter对象 —— 目标点所属的面的平面切割
# pl.show() # 显示pyvistaPlotter对象 —— 目标点所属的面的平面切割
#
# pl2 = pv.Plotter() # 创建pyvistaPlotter对象，用于绘制多Data对象 —— 目标点所属的面的平面切割
# pl2.add_mesh(pb,color = 'green',opacity=0.3) # 添加立方体多Data对象到pyvistaPlotter对象 —— 目标点所属的面的平面切割
# pl2.add_mesh(ps,color = 'blue',opacity=0.3) # 添加球体多Data对象到pyvistaPlotter对象 —— 目标点所属的面的平面切割
# pl2.add_mesh(ps,color = 'blue',opacity=0.3) # 添加球体多Data对象到pyvistaPlotter对象 —— 目标点所属的面的平面切割
# pl2.add_mesh(bo_diff.GetOutput(),color = 'yellow') # 添加布尔操作多Data对象到pyvistaPlotter对象 —— 目标点所属的面的平面切割
# pl2.show() # 显示pyvistaPlotter对象 —— 目标点所属的面的平面切割

# vtkBool:
# 用于进行布尔操作的vtk类
# CGAL:
# 用于进行布尔操作的CGAL库

import vtk                          # 导入 VTK 库，用于三维几何对象的创建和布尔运算
import pyvista as pv                # 导入 PyVista 库，用于可视化 VTK 网格对象

# ==================== 1. 创建立方体并三角化 ====================
box = vtk.vtkCubeSource()           # 创建 VTK 立方体数据源对象
box.SetCenter(0, 0, 0)              # 设置立方体的中心坐标为原点
box.Update()                        # 执行更新，生成立方体数据

tri = vtk.vtkTriangleFilter()       # 创建三角形过滤器，用于将多边形网格转换为三角形网格
tri.SetInputConnection(box.GetOutputPort())  # 将立方体数据源连接到三角形过滤器的输入端口
tri.Update()                        # 执行过滤器，生成三角化后的立方体网格
cube_tri = tri.GetOutput()          # 获取三角化立方体的输出数据对象

# ==================== 2. 创建球体（提高分辨率） ====================
sphere_source = vtk.vtkSphereSource()       # 创建 VTK 球体数据源对象
sphere_source.SetCenter(0, 0, 0)            # 设置球体中心为原点
sphere_source.SetRadius(0.6)                # 设置球体半径为 0.6
sphere_source.SetPhiResolution(120)         # 提高纬度分辨率至120，使球体表面更光滑
sphere_source.SetThetaResolution(120)       # 提高经度分辨率至120，使球体表面更光滑
sphere_source.Update()                      # 执行更新，生成球体网格数据
sphere = sphere_source.GetOutput()          # 获取球体输出数据对象

# ==================== 3. 布尔交集 ====================
bo_intersect = vtk.vtkBooleanOperationPolyDataFilter()  # 创建 VTK 布尔运算过滤器
bo_intersect.SetInputData(0, cube_tri)                  # 设置第一个输入数据为三角化立方体
bo_intersect.SetInputData(1, sphere)                    # 设置第二个输入数据为球体
bo_intersect.SetOperationToIntersection()               # 设置运算类型为交集
bo_intersect.Update()                                   # 执行布尔运算
intersect_result = bo_intersect.GetOutput()             # 获取交集结果网格

# ==================== 4. 布尔差集 ====================
bo_diff = vtk.vtkBooleanOperationPolyDataFilter()   # 创建 VTK 布尔运算过滤器
bo_diff.SetInputData(0, cube_tri)                   # 第一个输入：被减数（立方体）
bo_diff.SetInputData(1, sphere)                     # 第二个输入：减数（球体）
bo_diff.SetOperationToDifference()                  # 设置运算类型为差集
bo_diff.Update()                                    # 执行布尔运算
diff_result_raw = bo_diff.GetOutput()               # 获取差集结果原始网格

# ==================== 5. 重新计算法线（优化表面） ====================
normals = vtk.vtkPolyDataNormals()                  # 创建法线计算过滤器
normals.SetInputData(diff_result_raw)               # 输入差集网格
normals.ComputePointNormalsOn()                     # 开启点法线计算（用于平滑着色）
normals.Update()                                    # 执行计算
diff_result = normals.GetOutput()                   # 获取优化后的差集网格

# ==================== 6. 转换为 PyVista 对象 ====================
pb = pv.PolyData(cube_tri)      # 将三角化立方体转换为 PyVista 的 PolyData 对象，便于可视化
ps = pv.PolyData(sphere)        # 将球体转换为 PyVista 的 PolyData 对象，便于可视化

# ==================== 7. 可视化：原始正方体（使用默认颜色） ====================
pl0 = pv.Plotter(window_size=[800, 600])            # 创建绘图器，用于显示原始正方体
pl0.add_mesh(pb, label='Original Cube')             # 添加立方体网格，不指定颜色（使用默认颜色）
pl0.add_legend()                                    # 添加图例
pl0.show()                                          # 显示窗口（关闭后继续执行后续代码）

# ==================== 8. 可视化：交集 ====================
pl1 = pv.Plotter(window_size=[800, 600])            # 创建 PyVista 绘图器，窗口尺寸 800×600
pl1.add_mesh(                                       # 向绘图器添加网格
    intersect_result,                               # 要添加的网格：交集结果
    color='red',                                    # 设置颜色为红色
    specular=0.5,                                   # 高光强度 0.5（0-1），增强金属质感
    specular_power=20,                              # 高光指数，控制高光范围
    smooth_shading=True,                            # 启用平滑着色，消除三角形棱边
    label='Intersection (Cube ∩ Sphere)'            # 图例标签
)
pl1.add_legend()                                    # 添加图例
pl1.show()                                          # 显示窗口

# ==================== 9. 可视化：差集 ====================
pl2 = pv.Plotter(window_size=[800, 600])            # 创建另一个绘图器
pl2.add_mesh(pb, color='green', opacity=0.2, label='Cube outline')  # 添加半透明立方体轮廓
pl2.add_mesh(                                       # 添加差集网格
    diff_result,                                    # 要添加的网格：优化后的差集结果
    color='blue',                                   # 设置颜色为蓝色
    smooth_shading=True,                            # 启用平滑着色
    label='Difference (Cube - Sphere)'              # 图例标签
)
pl2.add_legend()                                    # 添加图例
pl2.camera_position = 'xy'                          # 设置相机视角为从 xy 平面观察，便于看到内部空腔
pl2.show()                                          # 显示窗口
