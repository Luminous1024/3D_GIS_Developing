import pyvista as pv # 导入pyvista库，用于可视化
import pygeodesic # 导入pygeodesic库，用于计算 geodesic距离
import numpy as np # 导入numpy库，用于处理数组

tin = pv.read(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\sh10.vtk') # 读取vtk文件，返回一个pyvista对象
pts = tin.points # 获取对象的点坐标数组，形状为(n,3)，n为点的数量
fcs = tin.faces.reshape(-1,4)[:,1:] # 获取对象的面数组，形状为(m,4)，m为面的数量
eg = pygeodesic.geodesic.PyGeodesicAlgorithmExact(pts,fcs) # 创建一个geodesic算法对象，传入点坐标数组和面数组

smp = np.random.choice(len(pts),2) # 随机选择两个点的索引，形状为(2,)
i0 = smp[0] # 第一个点的索引
i1 = smp[1] # 第二个点的索引

d0,_ = eg.geodesicDistances([i0]) # 计算第一个点到所有点的geodesic距离，返回一个数组，形状为(n,)，n为点的数量
d1,_ = eg.geodesicDistances([i1]) # 计算第二个点到所有点的geodesic距离，返回一个数组，形状为(n,)，n为点的数量

vo = [] # 创建一个空列表，用于存储每个点所属的voronoi区域索引，形状为(n,)，n为点的数量
for i in range(len(pts)): # 遍历每个点
    if d0[i] < d1[i]: # 如果第一个点到当前点的geodesic距离小于第二个点到当前点的geodesic距离
        vo.append(0) # 则当前点所属的voronoi区域索引为0
    else:
        vo.append(1) # 否则当前点所属的voronoi区域索引为1

tin['voronoi'] = vo # 给对象添加一个名为voronoi的数组，值为voronoi值
tin.set_active_scalars('voronoi') # 设置活动标量为voronoi
tin.plot() # 可视化对象，使用默认颜色映射
