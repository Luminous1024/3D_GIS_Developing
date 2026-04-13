import rasterio as rio
import vtk
import pyvista as pv
import numpy as np

raster = rio.open(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\su2.tif') # 打开su2.tif文件
# print(raster) # 打印raster对象，查看文件信息
print(raster.meta) # 打印raster元数据，查看文件信息
print(raster.shape) # 打印raster的shape，查看文件的维度
print(raster.height,raster.width) # 打印raster的高度和宽度，查看文件的维度
band0 = raster.read(1) #gdal.band # 读取第1个波段的数据

X = [] # 存储x坐标列表，用于后续可视化
Y = [] # 存储y坐标列表，用于后续可视化
Z = [] # 存储z坐标列表，用于后续可视化

for i in range(raster.height): # 遍历raster的高度
    for j in range(raster.width): # 遍历raster的宽度
        z = band0[i,j] # 获取当前像素的值
        x,y = raster.xy(i,j) # 获取当前像素的x,y坐标
        X.append(x) # 将x坐标添加到X列表中
        Y.append(y) # 将y坐标添加到Y列表中
        Z.append(z) # 将z坐标添加到Z列表中
pts = np.array([X,Y,Z]).T # 将x,y,z坐标列表转换为numpy数组，用于后续可视化
pd = pv.PolyData(pts) # 创建pyvista对象，用于可视化图像
pd['elevation'] = Z # 将z坐标列表添加到pyvista对象中，用于后续可视化
pd.set_active_scalars('elevation') # 设置活动标量为elevation，即z坐标
pd.plot() # 可视化图像，设置为默认模式
