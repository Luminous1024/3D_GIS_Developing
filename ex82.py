#----------方案一：遍历顶点计算距离，结果存入 PointData----------#

# import vtk
# import pyvista as pv
# import numpy as np

# r = vtk.vtkPolyDataReader()
# r.SetFileName(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\sh10.vtk')
# r.Update()

# pd = vtk.vtkPolyData()
# pd.ShallowCopy(r.GetOutput())

# bnds = np.zeros(6,dtype = float)
# pd.GetBounds(bnds)
# xr = bnds[1] - bnds[0]
# yr = bnds[3] - bnds[2]
# zr = (bnds[5] - bnds[4]) * 2

# dims = [100,100,100]

# dx = xr/(dims[0] - 1)
# dy = yr/(dims[1] - 1)
# dz = zr/(dims[2] - 1)

# img = vtk.vtkImageData()
# img.SetOrigin(bnds[0],bnds[2],bnds[4])
# img.SetDimensions(dims)
# img.SetSpacing(dx,dy,dz)
# img.AllocateScalars(vtk.VTK_FLOAT,1)

# cloc = vtk.vtkCellLocator()
# cloc.SetDataSet(pd)
# cloc.BuildLocator()

# print(img.GetNumberOfPoints())
# print(img.GetNumberOfCells())
# # print(img.GetNumberOfScalars())

# da = vtk.vtkFloatArray()
# da.SetName('distance')

# for i in range(img.GetNumberOfPoints()):
# # for i in range(img.GetNumberOfCells()): # 作业：换成GetNumberOfCells()怎么写？
#     p = np.zeros(3,dtype = float)
#     img.GetPoint(i,p)
#     x = np.zeros(3,dtype = float)
#     cid = vtk.reference(0)
#     sid = vtk.reference(0)
#     ds2 = vtk.reference(0.0)
#     cloc.FindClosestPoint(p,x,cid,sid,ds2)
#     da.InsertNextTuple1(np.sqrt(float(ds2)))

# pl = pv.Plotter()
# pl.add_mesh(pd,color = 'cyan')
# pimg = pv.ImageData(img)
# pimg.GetPointData().SetScalars(da)
# pimg.set_active_scalars('distance')

# # pl.add_volume(pimg)

# conf = vtk.vtkContourFilter()
# conf.SetInputData(pimg)
# conf.SetValue(0,700)
# conf.Update()

# pconf = pv.PolyData(conf.GetOutput())
# pl.add_mesh(pconf,color = 'green')

# pl.show()

#----------方案二：遍历单元格，计算每个单元格中心到地形的距离，存入 CellData，再转换为 PointData----------#

import vtk
import pyvista as pv
import numpy as np

# 读取地形网格数据
r = vtk.vtkPolyDataReader()
r.SetFileName(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\sh10.vtk')
r.Update()

pd = vtk.vtkPolyData()
pd.ShallowCopy(r.GetOutput())

# 获取地形边界并扩展 Z 范围（使格网包含地形上方空间）
bnds = np.zeros(6, dtype=float)
pd.GetBounds(bnds)
xr = bnds[1] - bnds[0]
yr = bnds[3] - bnds[2]
zr = (bnds[5] - bnds[4]) * 2

# 设置三维规则格网尺寸与间距
dims = [100, 100, 100]
dx = xr / (dims[0] - 1)
dy = yr / (dims[1] - 1)
dz = zr / (dims[2] - 1)

img = vtk.vtkImageData()
img.SetOrigin(bnds[0], bnds[2], bnds[4])
img.SetDimensions(dims)
img.SetSpacing(dx, dy, dz)
img.AllocateScalars(vtk.VTK_FLOAT, 1)

# 建立地形网格的空间搜索定位器
cloc = vtk.vtkCellLocator()
cloc.SetDataSet(pd)
cloc.BuildLocator()

print('格网点数量:', img.GetNumberOfPoints())
print('格网单元数量:', img.GetNumberOfCells())

# ------------------------------------------------------------
# 遍历单元格，计算每个单元格中心到地形的距离，
# 存入 CellData，再转换为 PointData
# ------------------------------------------------------------
da_cell = vtk.vtkFloatArray()
da_cell.SetName('distance_cell')

for i in range(img.GetNumberOfCells()):
    # 获取单元格边界 (xmin, xmax, ymin, ymax, zmin, zmax)
    bounds = img.GetCell(i).GetBounds()
    # 计算单元格中心坐标
    center = [(bounds[0] + bounds[1]) / 2.0,
              (bounds[2] + bounds[3]) / 2.0,
              (bounds[4] + bounds[5]) / 2.0]
    # 查找距离地形网格最近的点
    x = np.zeros(3, dtype=float)
    cid = vtk.reference(0)
    sid = vtk.reference(0)
    ds2 = vtk.reference(0.0)
    cloc.FindClosestPoint(center, x, cid, sid, ds2)
    da_cell.InsertNextTuple1(np.sqrt(float(ds2)))

# 将距离数组附加到格网的 CellData
img.GetCellData().SetScalars(da_cell)

# 使用 vtkCellDataToPointData 将单元属性转换为点属性
c2p = vtk.vtkCellDataToPointData()
c2p.SetInputData(img)
c2p.Update()

# 获取转换后的 ImageData，其中包含点属性 'distance_cell'
img_point = c2p.GetOutput()

# 包装为 PyVista 对象以便可视化
pimg = pv.ImageData(img_point)
pimg.set_active_scalars('distance_cell')

# ------------------------------------------------------------
# 可视化部分：地形网格 + 等值面
# ------------------------------------------------------------
pl = pv.Plotter()
pl.add_mesh(pd, color='cyan', opacity=0.7)

# 提取距离为 700 的等值面
conf = vtk.vtkContourFilter()
conf.SetInputData(pimg)
conf.SetValue(0, 700)
conf.Update()

pconf = pv.PolyData(conf.GetOutput())
pl.add_mesh(pconf, color='green', opacity=0.6)

pl.show()
