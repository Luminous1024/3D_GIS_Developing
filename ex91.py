#----------输出的折线矢量格式为vtk文件格式----------#

import vtk
import pandas as pd

def read_points_from_csv(filename):
    """读取CSV文件，返回x,y,z列表"""
    df = pd.read_csv(filename)
    return df['x'].values, df['y'].values, df['z'].values

def method1_segments(x, y, z):
    """方法1：线段组合（多个独立 vtkLine）"""
    pts = vtk.vtkPoints()
    for xi, yi, zi in zip(x, y, z):
        pts.InsertNextPoint(xi, yi, zi)

    ca = vtk.vtkCellArray()
    for i in range(len(x) - 1):
        line = vtk.vtkLine()
        line.GetPointIds().SetId(0, i)
        line.GetPointIds().SetId(1, i + 1)
        ca.InsertNextCell(line)

    polyData = vtk.vtkPolyData()
    polyData.SetPoints(pts)
    polyData.SetLines(ca)

    writer = vtk.vtkPolyDataWriter()
    writer.SetFileName("polyline_segments.vtk")
    writer.SetInputData(polyData)
    writer.Write()
    print("方法1输出: polyline_segments.vtk (Cell数量应为: {})".format(polyData.GetNumberOfCells()))

def method2_polyline(x, y, z):
    """方法2：单条 vtkPolyLine"""
    pts = vtk.vtkPoints()
    for xi, yi, zi in zip(x, y, z):
        pts.InsertNextPoint(xi, yi, zi)

    pln = vtk.vtkPolyLine()
    pln.GetPointIds().SetNumberOfIds(len(x))
    for i in range(len(x)):
        pln.GetPointIds().SetId(i, i)

    ca = vtk.vtkCellArray()
    ca.InsertNextCell(pln)

    polyData = vtk.vtkPolyData()
    polyData.SetPoints(pts)
    polyData.SetLines(ca)

    writer = vtk.vtkPolyDataWriter()
    writer.SetFileName("polyline_polyline.vtk")
    writer.SetInputData(polyData)
    writer.Write()
    print("方法2输出: polyline_polyline.vtk (Cell数量应为: 1)")

def method3_polylinesource(x, y, z):
    """方法3：vtkPolyLineSource 正确用法"""
    pl = vtk.vtkPolyLineSource()
    # ✅ 正确步骤：先设定点数，再逐个设置点
    pl.SetNumberOfPoints(len(x))
    for i, (xi, yi, zi) in enumerate(zip(x, y, z)):
        pl.SetPoint(i, xi, yi, zi)
    # 注意：这里不需要手动创建 Cell，vtkPolyLineSource 内部会自动生成一条 PolyLine

    writer = vtk.vtkPolyDataWriter()
    writer.SetFileName("polyline_source.vtk")
    writer.SetInputConnection(pl.GetOutputPort())
    writer.Write()
    
    # 验证一下输出
    pl.Update()
    print("方法3输出: polyline_source.vtk (Cell数量应为: 1)")

def main():
    try:
        x, y, z = read_points_from_csv(r"C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\polyline.csv")
    except FileNotFoundError:
        print("错误：未找到 polyline.csv 文件。")
        return
    except KeyError as e:
        print(f"错误：CSV缺少列 {e}。")
        return

    print(f"成功读取 {len(x)} 个点。")
    method1_segments(x, y, z)
    method2_polyline(x, y, z)
    method3_polylinesource(x, y, z)
    print("\n文件生成完毕。请在 ParaView 中查看 Information 标签页的 Number of Cells 验证差异。")

if __name__ == "__main__":
    main()

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
