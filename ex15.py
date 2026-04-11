import vtk # 导入vtk库，用于读取vtk文件
import pyvista as pv # 导入pyvista库，用于可视化vtk数据

# mt = pv.read(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\mt3.vtk') # 读取vtk文件，将其存储在PolyData对象mt中
# mt.plot(color='red') # 可视化PolyData对象mt，将其颜色设置为红色

r = vtk.vtkPolyDataReader() # 创建vtkPolyDataReader对象r，用于读取vtk文件
r.SetFileName(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\mt3.vtk') # 设置vtkPolyDataReader对象r的文件名，用于读取vtk文件
r.Update() # 更新vtkPolyDataReader对象r，将其输出存储在PolyData对象中

points = vtk.vtkPoints() # 创建vtkPoints对象points，用于存储点数据
points.ShallowCopy(r.GetOutput().GetPoints()) # 从PolyData对象中提取点数据，将其存储在vtkPoints对象points中

spl = vtk.vtkParametricSpline() # 创建vtkParametricSpline对象spl，用于拟合点数据
spl.SetPoints(points) # 设置vtkParametricSpline对象spl的点数据，用于拟合点数据

spf = vtk.vtkParametricFunctionSource() # 创建vtkParametricFunctionSource对象spf，用于生成拟合后的曲线
spf.SetParametricFunction(spl) # 设置vtkParametricFunctionSource对象spf的参数函数，用于生成拟合后的曲线
spf.Update() # 更新vtkParametricFunctionSource对象spf，将其输出存储在PolyData对象中

sf = vtk.vtkSplineFilter() # 创建vtkSplineFilter对象sf，用于拟合点数据
sf.SetInputData(spf.GetOutput()) # 设置vtkSplineFilter对象sf的输入数据，用于拟合点数据
sf.SetNumberOfSubdivisions(1000) # 设置vtkSplineFilter对象sf的子划分次数，用于拟合点数据
sf.Update() # 更新vtkSplineFilter对象sf，将其输出存储在PolyData对象中

pvd = pv.PolyData(spf.GetOutput()) # 创建pyvista PolyData对象pvd，用于可视化拟合后的曲线
pvd.plot(color = 'green') # 可视化PolyData对象pvd，将其颜色设置为绿色
