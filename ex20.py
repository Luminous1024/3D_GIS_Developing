import vtk # 导入vtk库，用于读取vtk文件
import numpy as np # 导入numpy库，用于处理数组
import pyvista as pv # 导入pyvista库，用于可视化

# 读取vtk文件，返回一个pyvista对象
dem = pv.read(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\sh10.vtk') # 读取vtk文件，返回一个pyvista对象
pts = dem.points # 获取对象的点坐标数组，形状为(n,3)，n为点的数量
ele = pts[:,2] # 提取数组的第三列，即高程值，形状为(n,)
rng = np.max(ele) - np.min(ele) # 计算高程值的范围，即最大高程值与最小高程值的差
bw = rng/4 # 计算每个bin的宽度，即范围除以10
es = [] # 创建一个空列表，用于存储每个高程值所属的bin索引
for i in range(len(ele)): # 遍历每个高程值
    es.append(ele[i]//bw) # 计算每个高程值所属的bin索引，即高程值除以bin宽度取整

dem['elevation'] = es# 给对象添加一个名为elevation的数组，值为高程值
dem.set_active_scalars('elevation') # 设置活动标量为elevation
dem.plot() # 可视化对象，使用默认颜色映射

# r = vtk.vtkPolyDataReader()
# r.SetFileName(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\sh10.vtk')
# r.Update()
#
# pd = vtk.vtkPolyData()
# pd.ShallowCopy(r.GetOutput())
#
# z = []
# for i in range(pd.GetNumberOfCells()):
#     p = [0,0,0,]
