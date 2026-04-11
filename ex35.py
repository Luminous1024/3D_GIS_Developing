import pyvista as pv

# ================= 1. 加载你的地形模型 =================
terrain = pv.read(r'D:\ex\ex3\sh10.vtk')   # 你的 sh10.vtk 文件

# ================= 2. 加载你的 DOM 影像 =================
# 已自动填充你提供的正射影像路径
dom_path = r'D:\ex\ex3\b3119313b07eca80557425439f2397dda1448324.jpg'
dom_texture = pv.read_texture(dom_path)

# ================= 3. 计算纹理坐标 =================
# 如果你的模型已有纹理坐标，可跳过这步
terrain.texture_map_to_plane(use_bounds=True, inplace=True)

# ================= 4. 可视化 =================
plotter = pv.Plotter()
plotter.add_mesh(terrain, texture=dom_texture, smooth_shading=True)
plotter.camera_position = 'xy'   # 先俯视检查映射效果
plotter.show()