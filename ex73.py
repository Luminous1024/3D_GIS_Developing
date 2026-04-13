import vtk # 引入vtk库，用于读取图像文件
import pyvista as pv # 引入pyvista库，用于可视化图像

c1 = vtk.vtkImageCanvasSource2D() # 创建vtkImageCanvasSource2D对象，用于创建2D图像
c1.SetExtent(0,400,0,600,0,0) # 设置图像的extent，即图像的范围
c1.SetScalarTypeToUnsignedChar() # 设置图像的标量类型为无符号字符
c1.SetNumberOfScalarComponents(3) # 设置图像的标量组件数量为3，即RGB颜色
c1.SetDrawColor(0,0,0) # 设置绘制颜色为黑色
c1.FillBox(0,400,0,600) # 填充图像为黑色
c1.SetDrawColor(255,0,0) # 设置绘制颜色为红色
c1.FillBox(10,300,10,500) # 填充红色矩形
c1.Update() # 更新数据，确保读取到的数据是最新的

c2 = vtk.vtkImageCanvasSource2D() # 创建vtkImageCanvasSource2D对象，用于创建2D图像
c2.SetExtent(0,400,0,600,0,0) # 设置图像的extent，即图像的范围
c2.SetScalarTypeToUnsignedChar() # 设置图像的标量类型为无符号字符
c2.SetNumberOfScalarComponents(3) # 设置图像的标量组件数量为3，即RGB颜色
c2.SetDrawColor(0,0,0) # 设置绘制颜色为黑色
c2.FillBox(0,400,0,600) # 填充图像为黑色
c2.SetDrawColor(255,0,0) # 设置绘制颜色为红色
c2.FillBox(20,200,20,400) # 填充红色矩形
c2.Update() # 更新数据，确保读取到的数据是最新的

diff = vtk.vtkImageDifference() # 创建vtkImageDifference对象，用于计算图像差异
diff.SetInputData(0,c1.GetOutput()) # 设置输入数据为c1的输出数据
diff.SetInputData(1,c2.GetOutput()) # 设置输入数据为c2的输出数据
diff.Update() # 更新数据，确保读取到的数据是最新的

pimg = pv.ImageData(diff.GetOutput()) # 创建pyvista对象，用于可视化图像
# pimg.plot() # 可视化图像，设置为默认模式
pimg.plot(rgb = True) # 可视化图像，设置为rgb模式
