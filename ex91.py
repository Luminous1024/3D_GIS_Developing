#----------输出的折线矢量格式为vtk文件格式----------#

# import pandas as pd
# import vtk

# # 读取CSV
# df = pd.read_csv(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\polyline.csv')   # 确保文件路径正确
# x = df['x'].values
# y = df['y'].values
# z = df['z'].values

# # 创建VTK点集
# pts = vtk.vtkPoints()
# for i in range(len(x)):
#     pts.InsertNextPoint(x[i], y[i], z[i])
# print("点数:", pts.GetNumberOfPoints())

# # 创建单元数组
# ca1 = vtk.vtkCellArray()
# # 每相邻两点生成一条线段
# for i in range(pts.GetNumberOfPoints() - 1):
#     line = vtk.vtkLine()
#     line.GetPointIds().SetId(0, i)
#     line.GetPointIds().SetId(1, i+1)
#     ca1.InsertNextCell(line)

# # 构建 PolyData
# pd1 = vtk.vtkPolyData()
# pd1.SetPoints(pts)
# pd1.SetLines(ca1)

# # 保存为 VTK 文件
# writer1 = vtk.vtkPolyDataWriter()
# writer1.SetFileName("polyline_segments.vtk")
# writer1.SetInputData(pd1)
# writer1.Write()
# print("方法1保存完成：polyline_segments.vtk")

# # 创建 PolyLine 对象
# polyline = vtk.vtkPolyLine()
# polyline.GetPointIds().SetNumberOfIds(pts.GetNumberOfPoints())
# for i in range(pts.GetNumberOfPoints()):
#     polyline.GetPointIds().SetId(i, i)

# # 放入单元数组
# ca2 = vtk.vtkCellArray()
# ca2.InsertNextCell(polyline)

# pd2 = vtk.vtkPolyData()
# pd2.SetPoints(pts)
# pd2.SetLines(ca2)

# writer2 = vtk.vtkPolyDataWriter()
# writer2.SetFileName("polyline_polyline.vtk")
# writer2.SetInputData(pd2)
# writer2.Write()
# print("方法2保存完成：polyline_polyline.vtk")

# source = vtk.vtkPolyLineSource()
# source.SetPoints(pts)   # 直接设置点集
# source.Update()

# writer3 = vtk.vtkPolyDataWriter()
# writer3.SetFileName("polyline_source.vtk")
# writer3.SetInputConnection(source.GetOutputPort())
# writer3.Write()
# print("方法3保存完成：polyline_source.vtk")

#----------输出的折线矢量格式为vtp文件格式----------#

# import vtk
# import pandas as pd

# def read_points_from_csv(filename):
#     """读取CSV文件，返回x,y,z列表"""
#     df = pd.read_csv(filename)
#     return df['x'].values, df['y'].values, df['z'].values

# def method1_segments_vtp(x, y, z):
#     """方法1：线段组合（多个 vtkLine）输出为 .vtp"""
#     pts = vtk.vtkPoints()
#     for xi, yi, zi in zip(x, y, z):
#         pts.InsertNextPoint(xi, yi, zi)

#     ca = vtk.vtkCellArray()
#     for i in range(len(x) - 1):
#         line = vtk.vtkLine()
#         line.GetPointIds().SetId(0, i)
#         line.GetPointIds().SetId(1, i + 1)
#         ca.InsertNextCell(line)

#     polyData = vtk.vtkPolyData()
#     polyData.SetPoints(pts)
#     polyData.SetLines(ca)

#     # 使用 XML 格式写入器
#     writer = vtk.vtkXMLPolyDataWriter()
#     writer.SetFileName("polyline_segments.vtp")
#     writer.SetInputData(polyData)
#     writer.Write()
#     print(f"方法1输出: polyline_segments.vtp (Cell数量: {polyData.GetNumberOfCells()})")

# def method2_polyline_vtp(x, y, z):
#     """方法2：单条 vtkPolyLine 输出为 .vtp"""
#     pts = vtk.vtkPoints()
#     for xi, yi, zi in zip(x, y, z):
#         pts.InsertNextPoint(xi, yi, zi)

#     pln = vtk.vtkPolyLine()
#     pln.GetPointIds().SetNumberOfIds(len(x))
#     for i in range(len(x)):
#         pln.GetPointIds().SetId(i, i)

#     ca = vtk.vtkCellArray()
#     ca.InsertNextCell(pln)

#     polyData = vtk.vtkPolyData()
#     polyData.SetPoints(pts)
#     polyData.SetLines(ca)

#     writer = vtk.vtkXMLPolyDataWriter()
#     writer.SetFileName("polyline_polyline.vtp")
#     writer.SetInputData(polyData)
#     writer.Write()
#     print(f"方法2输出: polyline_polyline.vtp (Cell数量: {polyData.GetNumberOfCells()})")

# def method3_polylinesource_vtp(x, y, z):
#     """方法3：vtkPolyLineSource 正确用法 输出为 .vtp"""
#     pl = vtk.vtkPolyLineSource()
#     # ✅ 正确用法：先设定点数，再逐个设置坐标
#     pl.SetNumberOfPoints(len(x))
#     for i, (xi, yi, zi) in enumerate(zip(x, y, z)):
#         pl.SetPoint(i, xi, yi, zi)

#     writer = vtk.vtkXMLPolyDataWriter()
#     writer.SetFileName("polyline_source.vtp")
#     writer.SetInputConnection(pl.GetOutputPort())
#     writer.Write()
    
#     # 更新管道以获取输出信息
#     pl.Update()
#     print(f"方法3输出: polyline_source.vtp (Cell数量: {pl.GetOutput().GetNumberOfCells()})")

# def main():
#     filepath = r"C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\polyline.csv"
#     try:
#         x, y, z = read_points_from_csv(filepath)
#     except FileNotFoundError:
#         print("错误：未找到 polyline.csv 文件。")
#         return
#     except KeyError as e:
#         print(f"错误：CSV缺少列 {e}。")
#         return

#     print(f"成功读取 {len(x)} 个点。")
#     method1_segments_vtp(x, y, z)
#     method2_polyline_vtp(x, y, z)
#     method3_polylinesource_vtp(x, y, z)
#     print("\n.vtp 文件生成完毕，可在 ParaView 中打开。")

# if __name__ == "__main__":
#     main()

#----------径向基函数（RBF）插值重建----------#

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.interpolate import Rbf

# df = pd.read_csv(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\china_gdp.csv')
# x = df['Year'].values
# y = df['Value'].values

# # function 可选 'multiquadric', 'gaussian', 'thin_plate' 等
# rbf = Rbf(x, y, function='multiquadric')

# x_new = np.linspace(x.min(), x.max(), 200)
# y_new = rbf(x_new)

# plt.figure(figsize=(10,6))
# plt.plot(x, y, 'ro', label='Original Data')
# plt.plot(x_new, y_new, 'b-', label='RBF Interpolation')
# plt.xlabel('Year')
# plt.ylabel('GDP')
# plt.title('RBF Curve Fitting')
# plt.legend()
# plt.grid(True)
# plt.show()

#----------样条曲线----------#

# import pandas as pd
# import vtk
# import pyvista as pv

# df = pd.read_csv(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\polyline.csv')
# x = df['x'].values
# y = df['y'].values
# z = df['z'].values

# pts = vtk.vtkPoints()
# for i in range(len(x)):
#     pts.InsertNextPoint(x[i], y[i], z[i])

# spline = vtk.vtkParametricSpline()
# spline.SetPoints(pts)

# funcSource = vtk.vtkParametricFunctionSource()
# funcSource.SetParametricFunction(spline)
# funcSource.Update()

# splineFilter = vtk.vtkSplineFilter()
# splineFilter.SetInputData(funcSource.GetOutput())
# splineFilter.SetNumberOfSubdivisions(500)   # 细分次数
# splineFilter.Update()

# writer = vtk.vtkPolyDataWriter()
# writer.SetFileName("spline_curve.vtk")
# writer.SetInputData(splineFilter.GetOutput())
# writer.Write()

# # PyVista 快速查看
# mesh = pv.read("spline_curve.vtk")
# mesh.plot(color='green', line_width=3)

#----------交互式拾取并高亮邻域----------#

import vtk
import numpy as np

reader = vtk.vtkPolyDataReader()
reader.SetFileName(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\rb.vtk')
reader.Update()
polydata = reader.GetOutput()

# 渲染器、窗口、交互器
ren = vtk.vtkRenderer()
renWin = vtk.vtkRenderWindow()
renWin.AddRenderer(ren)
iren = vtk.vtkRenderWindowInteractor()
iren.SetRenderWindow(renWin)

# 原始网格的 Actor
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputData(polydata)
actor = vtk.vtkActor()
actor.SetMapper(mapper)
ren.AddActor(actor)

class CellPickerCallback:
    def __init__(self, polydata, renderer):
        self.polydata = polydata
        self.renderer = renderer
        self.highlight_actor = None   # 用于存储高亮Actor

    def execute(self, obj, event):
        # 获取鼠标点击位置
        x, y = obj.GetEventPosition()
        picker = vtk.vtkCellPicker()
        picker.Pick(x, y, 0, self.renderer)
        cell_id = picker.GetCellId()
        if cell_id == -1:
            return

        # 获取一阶邻域单元（共享至少一个顶点）
        neighbor_ids = vtk.vtkIdList()
        self.polydata.GetCellNeighbors(cell_id, vtk.vtkIdList(), neighbor_ids)

        # 合并选中单元和邻域单元
        all_ids = [cell_id]
        for i in range(neighbor_ids.GetNumberOfIds()):
            all_ids.append(neighbor_ids.GetId(i))

        # 创建高亮数据集：提取这些单元
        selection = vtk.vtkSelection()
        node = vtk.vtkSelectionNode()
        node.SetContentType(vtk.vtkSelectionNode.INDICES)
        node.SetFieldType(vtk.vtkSelectionNode.CELL)
        id_array = vtk.vtkIdTypeArray()
        for nid in all_ids:
            id_array.InsertNextValue(nid)
        node.SetSelectionList(id_array)
        selection.AddNode(node)

        extract = vtk.vtkExtractSelection()
        extract.SetInputData(0, self.polydata)
        extract.SetInputData(1, selection)
        extract.Update()

        # 如果已有高亮Actor，先移除再添加
        if self.highlight_actor:
            self.renderer.RemoveActor(self.highlight_actor)

        # 创建高亮Actor
        highlight_mapper = vtk.vtkDataSetMapper()
        highlight_mapper.SetInputData(extract.GetOutput())
        self.highlight_actor = vtk.vtkActor()
        self.highlight_actor.SetMapper(highlight_mapper)
        self.highlight_actor.GetProperty().SetColor(1, 0, 0)   # 红色高亮
        self.highlight_actor.GetProperty().SetOpacity(0.7)
        self.renderer.AddActor(self.highlight_actor)

        self.renderer.GetRenderWindow().Render()

# 创建回调对象并绑定到左键按下事件
callback = CellPickerCallback(polydata, ren)
iren.AddObserver("LeftButtonPressEvent", callback.execute)

# 初始渲染
renWin.Render()
iren.Start()
