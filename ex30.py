import vtk
import numpy as np

r = vtk.vtkPolyDataReader()
r.SetFileName(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\sh10.vtk')
r.Update()

pd = vtk.vtkPolyData()
pd.ShallowCopy(r.GetOutput())

x = []
y = []
z = []
for i in range(pd.GetNumberOfPoints()):
    p = [0,0,0]
    pd.GetPoints().GetPoint(i, p)
    x.append(p[0])
    y.append(p[1])
    z.append(p[2])

xmin,xmax = np.min(x),np.max(x)
ymin,ymax = np.min(y),np.max(y)
zmin,zmax = np.min(z),np.max(z)