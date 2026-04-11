import vtk # 导入vtk库，用于读取vtk文件
import pyvista as pv # 导入pyvista库，用于读取vtk文件
import numpy as np # 导入numpy库，用于处理数组

mesh = pv.read(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\sh10.vtk') # 读取vtk文件
points = mesh.points # 纯Python数组 —— 顶点表
faces = mesh.faces.reshape(-1,4)[:,1:] # 从第 2 列开始，每个元素减去 1# —— 面表

cid = 1234 # 点cid的索引，从0开始计数 —— 目标点的索引
# pis = vtk.vtkIdList() # 创建vtkIdList对象，用于存储点的索引 —— 目标点的索引列表
# v0 = pis.GetId(0) # 目标点所属的面的索引列表的第一个元素 —— 目标点所属的面的第一个顶点的索引
# v1 = pis.GetId(1) # 目标点所属的面的索引列表的第二个元素 —— 目标点所属的面的第二个顶点的索引
# v2 = pis.GetId(2) # 目标点所属的面的索引列表的第三个元素 —— 目标点所属的面的第三个顶点的索引
pis = faces[cid] # 目标点的索引列表 —— 目标点所属的面的索引列表
v0 = pis[0] # 目标点所属的面的索引列表的第一个元素 —— 目标点所属的面的第一个顶点的索引
v1 = pis[1] # 目标点所属的面的索引列表的第二个元素 —— 目标点所属的面的第二个顶点的索引
v2 = pis[2] # 目标点所属的面的索引列表的第三个元素 —— 目标点所属的面的第三个顶点的索引
p0 = points[v0] # 目标点所属的面的第一个顶点的坐标 —— 目标点所属的面的第一个顶点的坐标
p1 = points[v1] # 目标点所属的面的第二个顶点的坐标 —— 目标点所属的面的第二个顶点的坐标
mp = (p0 + p1) / 2 # 目标点所属的面的中心坐标 —— 目标点所属的面的中心坐标
mp[2] += 1000 # 改变目标点所属的面的中心坐标，使目标点所属的面的中心坐标在z轴上移动1000个单位
ap = mp - p0 # 目标点所属的面的中心坐标到目标点所属的面的第一个顶点的坐标 —— 目标点所属的面的中心坐标到目标点所属的面的第一个顶点的坐标
bp = mp - p1 # 目标点所属的面的中心坐标到目标点所属的面的第二个顶点的坐标 —— 目标点所属的面的中心坐标到目标点所属的面的第二个顶点的坐标
n = np.cross(ap,bp) # 目标点所属的面的法向量 —— 目标点所属的面的法向量

pln = vtk.vtkPlane() # 创建vtkPlane对象，用于存储平面的参数 —— 目标点所属的面的平面
pln.SetOrigin(p0) # 设置平面的原点 —— 目标点所属的面的中心坐标
pln.SetNormal(n) # 设置平面的法向量 —— 目标点所属的面的法向量

cutter = vtk.vtkPolyDataPlaneCutter() # 创建vtkPolyDataPlaneCutter对象，用于切割多Data对象 —— 目标点所属的面的平面切割
cutter.SetInputData(mesh) # 设置输入数据 —— 目标点所属的面的平面切割
cutter.SetPlane(pln) # 设置平面 —— 目标点所属的面的平面切割
cutter.Update() # 更新切割器，进行切割

clipper = vtk.vtkClipPolyData() # 创建vtkClipPolyData对象，用于裁剪多Data对象，保留平面一侧的网格
clipper.SetInputData(mesh) # 设置输入数据
clipper.SetClipFunction(pln) # 设置裁剪平面
clipper.SetValue(0.0) # 设置裁剪值
clipper.Update() # 更新裁剪器，进行裁剪

pc = pv.PolyData(cutter.GetOutput()) # 创建pyvista多Data对象，用于存储切割线（交线）
pcl = pv.PolyData(clipper.GetOutput()) # 创建pyvista多Data对象，用于存储裁剪后的剩余网格
pl = pv.Plotter() # 创建pyvistaPlotter对象，用于绘制多Data对象
pl.add_mesh(pc,color = 'red',line_width=5) # 绘制切割线（交线），红色，加粗
pl.add_mesh(pcl,color = 'green',opacity=0.7) # 绘制裁剪后的剩余网格，绿色，半透明
pl.show() # 显示绘制结果
# pc.plot() # 绘制切割后的多Data对象 —— 目标点所属的面的平面切割
