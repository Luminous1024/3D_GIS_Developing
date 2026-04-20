import vtk # 导入vtk库，用于处理图像数据
import pyvista as pv # 导入pyvista库，用于可视化图像
import numpy as np # 导入numpy库，用于处理数组

r = vtk.vtkPNGReader() # 创建vtk读取器对象，用于读取png文件
# r.SetFileName(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\su7.png') # 设置su7.png文件的路径
r.SetFileName(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\nevada.png') # 设置nevada.png文件的路径
r.Update() # 更新读取器对象，读取文件内容

img = vtk.vtkImageData() # 创建vtk图像数据对象，用于存储图像数据
img.ShallowCopy(r.GetOutput()) # 将读取器对象的输出数据浅拷贝到图像数据对象中

print(img.GetNumberOfPoints()) # 打印图像数据对象的点数，查看文件的维度
print(img.GetNumberOfCells()) # 打印图像数据对象的单元数，查看文件的维度
print(img.GetBounds()) # 打印图像数据对象的边界框，查看文件的维度
print(img.GetScalarType()) # 打印
print(img.GetNumberOfScalarComponents()) # 
print(img.GetDimensions()) # 

for i in range(img.GetDimensions()[0]): # 
    for j in range(img.GetDimensions()[1]):
        if i > 200 and i < 400 and j > 200 and j < 400:
            img.SetScalarComponentFromFloat(i,j,0,0,0)
            img.SetScalarComponentFromFloat(i,j,0,1,0)
            img.SetScalarComponentFromFloat(i,j,0,2,0)
            img.SetScalarComponentFromFloat(i,j,0,3,0)

pimg = pv.ImageData(r.GetOutput()) # 创建pyvista对象，用于可视化图像
# pimg.plot() # 可视化图像，设置为默认模式
pimg.plot(rgb = True) # 可视化图像，设置为rgb模式
# img.SetScalarComponentFromFloat()
# img.SetScalarComponentFromDouble()