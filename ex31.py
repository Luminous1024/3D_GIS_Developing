import vtk
import math
import numpy as np

r = vtk.vtkPolyDataReader()
r.SetFileName(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\sh10.vtk')
r.Update()

pd = vtk.vtkPolyData()
pd.ShallowCopy(r.GetOutput())

a3 = 0
for i in range(pd.GetNumberOfPoints()):
    pis = vtk.vtkIdList()
    pd.GetCellPoints(i, pis)
    # for j in range(pis.GetNumberOfIds()):
    #     v = pis.GetId(j)
    v0 = pis.GetId(0)
    v1 = pis.GetId(1)
    v2 = pis.GetId(2)
    p0 = [0,0,0]
    pd.GetPoint(v0, p0)
    p1 = [0,0,0]
    pd.GetPoint(v1, p1)
    p2 = [0,0,0]
    pd.GetPoint(v2, p2)
    a = math.dist(p0,p1)
    b = math.dist(p1,p2)
    c = math.dist(p2,p0)
    s = (a + b + c) / 2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    a3 += area
print(a3)

a2 = 0
for i in range(pd.GetNumberOfCells()):
    pis = vtk.vtkIdList()
    pd.GetCellPoints(i, pis)
    v0 = pis.GetId(0)
    v1 = pis.GetId(1)
    v2 = pis.GetId(2)
    p0 = [0,0,0]
    pd.GetPoint(v0, p0)
    p0[2] = 0
    p1 = [0,0,0]
    pd.GetPoint(v1, p1)
    p1[2] = 0
    p2 = [0,0,0]
    pd.GetPoint(v2, p2)
    p2[2] = 0
    a = math.dist(p0,p1)
    b = math.dist(p1,p2)
    c = math.dist(p2,p0)
    s = (a + b + c) / 2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    a2 += area
print(a2)

print(a3/a2)