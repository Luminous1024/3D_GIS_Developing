import pyvista as pv # 导入PyVista库,用于处理3D数据
import panel as pn # 导入Panel库,用于创建交互式可视化界面
from IPython.display import IFrame # 导入IFrame组件,用于显示PyVista可视化结果

mesh = pv.read(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\sh10.vtk') # 读取地形网格数据
points = mesh.points # 获取地形网格点坐标
mesh['elevation'] = points[:,2] # 提取地形网格点的 Z 坐标作为高度值
mesh.set_active_scalars('elevation') # 设置活动标量为高度值

pl = pv.Plotter(notebook = True) # 创建交互式可视化环境

a = pl.add_mesh(mesh) # actor对象,用于显示地形网格

def pv_hdl(e,src,**kwargs): # 定义PyVista处理函数
    return IFrame(src,width = '100%',height = '100%') # 返回IFrame组件,用于显示PyVista可视化结果

pvv = pl.show(return_viewer = True, # 返回PyVista可视化环境对象
              jupyter_backend = 'client', # 使用客户端端后端,在Jupyter Notebook中显示可视化结果 # server,trame
              jupyter_kwargs = dict(handler = pv_hdl),)

pn.panel(pvv,sizing_mode = 'stretch_both').show() # 显示PyVista可视化环境组件,并拉伸宽度和高度
