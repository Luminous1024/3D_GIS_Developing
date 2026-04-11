# import vtk
# import numpy as np
# import pyvista as pv
#
# r = vtk.vtkPolyDataReader()
# r.SetFileName(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\sh10.vtk')
# r.Update()
# pd = vtk.vtkPolyData()
# pd.ShallowCopy(r.GetOutput())
#
# ug = vtk.vtkMutableUndirectedGraph()
# for i in range(pd.GetNumberOfPoints()):
#     ug.AddVertex()
#
# es = set()
# for i in range(pd.GetNumberOfCells()):
#     pis = vtk.vtkIdList()
#     pd.GetCellPoints(i, pis)
#     v0 = pis.GetId(0)
#     v1 = pis.GetId(1)
#     v2 = pis.GetId(2)
#     e0 = tuple(sorted((v0, v1)))
#     e1 = tuple(sorted((v0, v2)))
#     e2 = tuple(sorted((v1, v2)))
#     if e0 not in es:
#         es.Add(e0)
#         ug.AddEdge(e0[0], e0[1])
#     if e1 not in es:
#         es.Add(e1)
#         ug.AddEdge(e1[0], e1[1])
#     if e2 not in es:
#         es.Add(e2)
#         ug.AddEdge(e2[0], e2[1])
# print(ug.GetNumberOfEdges())
#
# ew = []
# for i in range(ug.GetNumberOfEdges()):
#     v0 = ug.GetSourceVertex(i)
#     v1 = ug.GetTargetVertex(i)
#     p0 = [0,0,0]
#     pd.GetPoint(v0, p0)
#     p1 = [0,0,0]
#     pd.GetPoint(v1, p1)
#     ew.append(map.dist(p0, p1))

import vtk # 导入vtk库，用于读取vtk文件
import numpy as np # 导入numpy库，用于处理数组
import pyvista as pv # 导入pyvista库，用于可视化数据
import math # 导入math库，用于计算距离

r = vtk.vtkPolyDataReader() # 创建vtk文件读取器
r.SetFileName(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\sh10.vtk') # 设置读取的vtk文件路径
r.Update() # 更新读取器，读取文件内容
pd = vtk.vtkPolyData() # 创建vtk多Data对象，用于存储读取的vtk文件内容
pd.ShallowCopy(r.GetOutput()) # 深拷贝读取器的输出数据到多Data对象
N = pd.GetNumberOfPoints() # 获取多Data对象中的点的数量

ug = vtk.vtkMutableUndirectedGraph() # 创建vtk无向图对象
print(ug.GetNumberOfVertices()) # 获取无向图对象中的顶点的数量
for i in range(N): # 遍历多Data对象中的点
    ug.AddVertex() # 添加顶点到无向图对象
print(ug.GetNumberOfVertices()) # 获取无向图对象中的顶点的数量

es = set() # 创建一个空集合，用于存储边
for i in range(pd.GetNumberOfCells()): # 遍历多Data对象中的单元
    pis = vtk.vtkIdList() # 创建vtkId列表对象，用于存储单元中的点的索引
    pd.GetCellPoints(i, pis) # 获取单元中的点的索引
    v0 = pis.GetId(0) # 获取单元中的第一个点的索引
    v1 = pis.GetId(1) # 获取单元中的第二个点的索引
    v2 = pis.GetId(2) # 获取单元中的第三个点的索引
    e0 = tuple(sorted((v0, v1))) # 创建边e0，排序后确保边的顺序
    e1 = tuple(sorted((v0, v2))) # 创建边e1，排序后确保边的顺序
    e2 = tuple(sorted((v1, v2))) # 创建边e2，排序后确保边的顺序
    if e0 not in es:
        es.add(e0) # 如果边e0不在集合es中，则添加到集合es中
        ug.AddEdge(e0[0], e0[1]) # 添加边e0到无向图对象
    if e1 not in es:
        es.add(e1) # 如果边e1不在集合es中，则添加到集合es中
        ug.AddEdge(e1[0], e1[1]) # 添加边e1到无向图对象
    if e2 not in es:
        es.add(e2) # 如果边e2不在集合es中，则添加到集合es中
        ug.AddEdge(e2[0], e2[1]) # 添加边e2到无向图对象
print(ug.GetNumberOfEdges()) # 获取无向图对象中的边的数量

# Djikstra算法与C.Berge算法的区别：
    # 1. Djikstra算法是单源最短路径算法，而C.Berge算法是多源最短路径算法
    # 2. Djikstra算法只能处理非负边权图，而C.Berge算法可以处理负边权图
    # 3. Djikstra算法的时间复杂度为O(V^2)，而C.Berge算法的时间复杂度为O(V^3)
    # 4. Djikstra算法的内存复杂度为O(V)，而C.Berge算法的内存复杂度为O(V^2)
    # 5. Djikstra算法的实现相对简单，而C.Berge算法的实现相对复杂

# Bellman-Ford算法
    # 1. Bellman-Ford算法是一种单源最短路径算法，可以处理负边权图
    # 2. Bellman-Ford算法的时间复杂度为O(VE)，而V是顶点的数量，E是边的数量
    # 3. Bellman-Ford算法的内存复杂度为O(V)
    # 4. Bellman-Ford算法的实现相对复杂，需要处理负边权图的情况

ew = [] # 创建一个空列表，用于存储边的权重
for i in range(ug.GetNumberOfEdges()): # 遍历无向图对象中的边
    v0 = ug.GetSourceVertex(i) # 获取边i的源顶点的索引
    v1 = ug.GetTargetVertex(i) # 获取边i的目标顶点的索引
    p0 = [0,0,0] # 创建一个空列表，用于存储点v0的坐标
    p1 = [0,0,0] # 创建一个空列表，用于存储点v1的坐标
    pd.GetPoint(v0,p0) # 获取点v0的坐标
    pd.GetPoint(v1,p1) # 获取点v1的坐标
    ew.append(math.dist(p0,p1)) # 计算边i的权重，将其添加到列表ew中
dist = [float('inf')] * N # 创建一个空列表，用于存储顶点到源顶点的最短路径长度
dist[4703] = 0.0 # 源顶点到源顶点的最短路径长度为0.0
updated = True # 初始化updated为True，用于判断是否需要继续更新最短路径长度
while updated: # 当updated为True时，循环继续执行，直到没有更新最短路径长度
    updated = False # 初始化updated为False，用于判断是否需要继续更新最短路径长度
    for i in range(ug.GetNumberOfEdges()): # 遍历无向图对象中的边
        el = ew[i] # 获取边i的权重
        v0 = ug.GetSourceVertex(i) # 获取边i的源顶点的索引
        v1 = ug.GetTargetVertex(i) # 获取边i的目标顶点的索引

        if dist[v1] > dist[v0] + el: # 如果边i的权重小于当前顶点到源顶点的最短路径长度
            dist[v1] = dist[v0] + el # 更新目标顶点到源顶点的最短路径长度
            updated = True # 标记为需要继续更新最短路径长度
        if dist[v0] > dist[v1] + el: # 如果边i的权重小于当前顶点到源顶点的最短路径长度
            dist[v0] = dist[v1] + el # 更新源顶点到源顶点的最短路径长度
            updated = True # 标记为需要继续更新最短路径长度

pvd = pv.PolyData(pd) # 创建vtk多Data对象，用于存储读取的vtk文件内容
pvd['dist'] = dist # 将dist列表添加到多Data对象中，用于存储顶点到源顶点的最短路径长度
pvd.set_active_scalars('dist') # 设置dist列表为多Data对象的活动标量，用于可视化
pvd.plot() # 可视化多Data对象，显示dist列表的值
