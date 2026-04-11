import vtk # 导入vtk库，用于读取vtk文件
import math # 导入math库，用于计算距离
import numpy as np # 导入numpy库，用于处理数组
import time # 导入time库，用于计算时间差

r = vtk.vtkPolyDataReader() # 创建vtk文件读取器
r.SetFileName(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\c15_mid_pd.vtk') # 设置读取的vtk文件路径
r.Update() # 更新读取器，读取文件内容
pd = vtk.vtkPolyData() # 创建vtk多Data对象，用于存储读取的vtk文件内容
pd.ShallowCopy(r.GetOutput()) # 深拷贝读取器的输出数据到多Data对象
N = pd.GetNumberOfPoints() # 获取多Data对象中的点的数量
sN = N // 4 # 采样点数，交叉验证

smp = np.random.choice(N,sN) # 从多Data对象中的点中随机选择sN个点，作为采样点

nB = 12 # 聚类数
pwr = 2.5 # 聚类参数

loc = vtk.vtkPointLocator()
loc.SetDataSet(pd)
loc.BuildLocator()

rz = [] # real z
iz = [] # simulated z
for i in smp:
    p0 = [0,0,0]
    pd.GetPoint(i,p0)
    rz.append(p0[2])

    ids = vtk.vtkIdList()
    loc.FindClosestNPoints(nB,p0,ids)

    sw = 0
    for j in range(ids.GetNumberOfIds()):
        tj = ids.GetId(j)
        if tj == i:
            continue
        p1 = [0,0,0]
        pd.GetPoint(tj,p1)
        d = math.dist(p0,p1)
        w = 1 / (d ** pwr)
        sw += w

    sz = 0
    for j in range(ids.GetNumberOfIds()):
        tj = ids.GetId(j)
        if tj == i:
            continue
        p1 = [0, 0, 0]
        pd.GetPoint(tj, p1)
        d = math.dist(p0, p1)
        w = 1 / (d ** pwr)
        w = w / sw
        sz += w * p1[2]
    iz.append(sz)
diff = np.array(iz) - np.array(rz)
rmse = np.sqrt(np.mean(diff**2))
print(rmse)
