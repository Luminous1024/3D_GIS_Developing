import vtk # 引入vtk库，用于读取图像文件
import pyvista as pv # 引入pyvista库，用于可视化图像

c1 = vtk.vtkImageCanvasSource2D() # 创建vtkImageCanvasSource2D对象，用于创建2D图像
c1.SetExtent(0,400,0,600,0,0) # 设置图像的extent，即图像的范围
c1.SetScalarTypeToUnsignedChar() # 设置图像的标量类型为无符号字符
c1.SetNumberOfScalarComponents(3)
c1.SetDrawColor(0,0,0)
c1.FillBox(0,400,0,600)
c1.SetDrawColor(255,0,0)
c1.FillBox(10,300,10,500)
c1.Update()

pimg = pv.ImageData(c1.GetOutput()) # 创建pyvista对象，用于可视化图像
# pimg.plot() # 可视化图像，设置为默认模式
pimg.plot(rgb = True) # 可视化图像，设置为rgb模式
