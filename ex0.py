# import vtk
#
# r = vtk.vtkPolyDataReader()
# r.SetFileName(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\klein.vtk')
# r.Update()
#
# pd = vtk.vtkPolyData()
# pd.ShallowCopy(r.GetOutput())
#
# actor = vtk.vtkActor()
# m = vtk.vtkPolyDataMapper()
# m.SetInputData(pd)
# actor.SetMapper(m)
#
# ren = vtk.vtkRenderer()
# ren.AddActor(actor)
#
# rw = vtk.vtkRenderWindow()
# rw.AddRenderer(ren)
#
# ri = vtk.vtkRenderWindowInteractor()
# ri.SetRenderWindow(rw)
# ri.Render()
#
# ri.Start()

#--------------------#

# import pyvista as pv
#
# # 读取模型
# mesh = pv.read(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\klein.vtk')
#
# # 创建绘图器
# p = pv.Plotter()
#
# # 添加网格：蓝色线框模式
# p.add_mesh(mesh, color='blue', style='wireframe', line_width=2)
#
# # 添加个人信息（请替换为真实姓名和学号）
# p.add_text("Name:Ziyuan Lv\nclass:2327201\nstd_ID:2023211033", position='upper_left', font_size=12, color='black')
#
# # 显示窗口
# p.show()

#--------------------#

# import vtk
#
# # 1. 读取模型文件
# reader = vtk.vtkPolyDataReader()
# reader.SetFileName(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\klein.vtk')
# reader.Update()
#
# # 2. 获取数据并构建Mapper
# polydata = vtk.vtkPolyData()
# polydata.ShallowCopy(reader.GetOutput())
#
# mapper = vtk.vtkPolyDataMapper()
# mapper.SetInputData(polydata)
#
# # 3. 创建Actor并设置颜色和线框样式
# actor = vtk.vtkActor()
# actor.SetMapper(mapper)
# actor.GetProperty().SetColor(0.0, 0.5, 1.0)          # 亮蓝色
# actor.GetProperty().SetRepresentationToWireframe()   # 线框模式
# actor.GetProperty().SetLineWidth(2)                  # 可选线宽
#
# # 4. 创建Renderer并添加Actor
# renderer = vtk.vtkRenderer()
# renderer.AddActor(actor)
# renderer.SetBackground(0.1, 0.1, 0.2)                # 深色背景
#
# # 5. 添加个人信息文本（使用AddViewProp替代AddActor2D）
# textActor = vtk.vtkTextActor()
# textActor.SetInput("Name:Ziyuan Lv\nclass:2327201\nstd_ID:2023211033")   # 替换为真实信息
# textProp = textActor.GetTextProperty()
# textProp.SetFontSize(16)
# textProp.SetColor(1.0, 1.0, 1.0)                     # 白色文字
# textActor.SetDisplayPosition(20, 20)                  # 左下角偏移量
#
# renderer.AddViewProp(textActor)                        # 替换AddActor2D
#
# # 6. 创建渲染窗口和交互器
# renderWindow = vtk.vtkRenderWindow()
# renderWindow.AddRenderer(renderer)
# renderWindow.SetSize(800, 600)
# renderWindow.SetWindowName("Klein Bottle - VTK Visualization")
#
# interactor = vtk.vtkRenderWindowInteractor()
# interactor.SetRenderWindow(renderWindow)
#
# # 7. 开始渲染与交互
# renderWindow.Render()
# interactor.Start()

#--------------------#

# import pyvista as pv # 导入pyvista库
#
# mesh = pv.read(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\klein.vtk') # 读取模型文件
# mesh.plot() # 显示网格

#--------------------#

# import vtk # 导入vtk库，用于构建点集、顶点集和多边形数据集
#
# r = vtk.vtkPolyDataReader() # 构建一个多边形数据集读取器
# r.SetFileName(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\klein.vtk') # 设置读取文件名
# r.Update() # 更新读取器，读取模型文件
#
# pd = vtk.vtkPolyData() # 构建一个多边形数据集
# pd.ShallowCopy(r.GetOutput()) # 从读取器r获取输出并浅拷贝到多边形数据集pd
#
# actor = vtk.vtkActor() # 构建一个演员
# m = vtk.vtkPolyDataMapper() # 构建一个多边形数据集映射器
# m.SetInputData(pd) # 为映射器m添加多边形数据集pd
# actor.SetMapper(m) # 为演员actor设置映射器m
#
# ren = vtk.vtkRenderer() # 构建一个渲染器
# ren.AddActor(actor) # 为渲染器ren添加演员actor
#
# # 创建渲染窗口
# rw = vtk.vtkRenderWindow() # 构建一个渲染窗口
# rw.AddRenderer(ren)  # 为渲染窗口rw添加渲染器ren
# rw.SetWindowName("Klein Bottle - VTK Visualization") # 设置渲染窗口标题
#
# # 创建渲染窗口交互器，用于处理用户与3D模型的交互
# ri = vtk.vtkRenderWindowInteractor()  # 实例化交互器对象
# ri.SetRenderWindow(rw)  # 将交互器与渲染窗口关联
# ri.Render()  # 触发初始渲染
#
# ri.Start()  # 启动交互循环，开始接收用户输入事件

#--------------------#