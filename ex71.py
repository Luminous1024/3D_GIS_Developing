import vtk # 引入vtk库，用于读取图像文件
import pyvista as pv # 引入pyvista库，用于可视化图像

# r = vtk.vtkPNGReader() # 创建vtkPNGReader对象，用于读取png文件
r = vtk.vtkTIFFReader() # 创建vtkTIFFReader对象，用于读取tiff文件
# r.SetFileName(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\su7.tif') # 设置读取的文件文件名
r.SetFileName(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\su2.tif') # 设置读取的文件文件名
r.Update() # 更新数据，确保读取到的数据是最新的

img = vtk.vtkImageData() # vtkStructuredPoints # 创建vtkImageData对象，用于存储图像数据
img.ShallowCopy(r.GetOutput()) # 将读取到的图像数据img对象中

# pimg = pv.ImageData(img) # 创建pyvista对象，用于可视化图像
# pimg.plot(rgb = True) # 可视化图像，设置为rgb模式

print(img.GetExtent()) # 获取图像的extent，即图像的范围
print(img.GetOrigin()) # 获取图像的origin，即图像的原点坐标
print(img.GetSpacing()) # 获取图像的spacing，即图像的间距
print(img.GetDimensions()) # 获取图像的dimensions，即图像的维度
print(img.GetScalarType()) # 获取图像的scalar type，即图像的标量类型
print(img.GetNumberOfScalarComponents()) # 获取图像的number of scalar components，即图像的标量组件数量
