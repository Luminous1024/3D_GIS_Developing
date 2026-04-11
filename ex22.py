import pyvista as pv
import numpy as np
import pygeodesic

# -------------------- 1. 读取数据 --------------------
tin = pv.read(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\sh10.vtk') # 读取vtk文件，返回一个pyvista对象
pts = tin.points                     # 所有顶点坐标 (n,3)
faces = tin.faces.reshape(-1, 4)[:, 1:]  # 三角形面片索引 (m,3)

# -------------------- 2. 随机选取 10 个种子点 --------------------
np.random.seed(24)  # 固定随机种子，便于结果重现
n_seeds = 10
seed_indices = np.random.choice(len(pts), size=n_seeds, replace=False)
print(f"随机选取的种子点索引: {seed_indices}")

# -------------------- 3. 欧氏距离聚类 --------------------
print("正在计算欧氏距离聚类...")
seed_coords = pts[seed_indices]                     # (10,3)
# 计算每个点到所有种子点的欧氏距离，取最近种子的索引
# 利用广播计算 (n,10) 的距离矩阵
dist_euc = np.linalg.norm(pts[:, np.newaxis, :] - seed_coords[np.newaxis, :, :], axis=2)
euc_labels = np.argmin(dist_euc, axis=1)            # 每个点的簇标签 (0~9)

# -------------------- 4. 测地距离聚类 --------------------
print("正在计算测地距离聚类（可能需要一些时间）...")
# 创建测地距离计算对象
geo_algo = pygeodesic.geodesic.PyGeodesicAlgorithmExact(pts, faces)

# 存储每个种子点到所有点的测地距离
geo_distances = []
for i, seed_idx in enumerate(seed_indices):
    print(f"  计算种子 {i+1}/{n_seeds} ...")
    dist, _ = geo_algo.geodesicDistances([seed_idx])
    geo_distances.append(dist)          # dist 是长度为 n 的数组

# 转换为 (n_seeds, n) 的数组
geo_dist_matrix = np.array(geo_distances)   # shape (10, n)
geo_labels = np.argmin(geo_dist_matrix, axis=0)   # 每个点的最近种子索引

# -------------------- 5. 将结果添加到 PyVista 对象并可视化比较 --------------------
# 复制一份，分别保存两种聚类结果（避免相互覆盖）
tin_euc = tin.copy()
tin_geo = tin.copy()

tin_euc['Voronoi (Euclidean)'] = euc_labels
tin_geo['Voronoi (Geodesic)'] = geo_labels

# 设置活动标量，以便着色显示
tin_euc.set_active_scalars('Voronoi (Euclidean)')
tin_geo.set_active_scalars('Voronoi (Geodesic)')

# 创建多窗口可视化
plotter = pv.Plotter(shape=(1, 2))  # 一行两列

# 左图：欧氏距离 Voronoi
plotter.subplot(0, 0)
plotter.add_mesh(tin_euc, cmap='tab10', show_edges=True)
plotter.add_text("Euclidean Distance", position='upper_edge')
# 标记种子点位置
seed_points_euc = pv.PolyData(pts[seed_indices])
plotter.add_mesh(seed_points_euc, color='red', point_size=10, render_points_as_spheres=True)

# 右图：测地距离 Voronoi
plotter.subplot(0, 1)
plotter.add_mesh(tin_geo, cmap='tab10', show_edges=True)
plotter.add_text("Geodesic Distance", position='upper_edge')
seed_points_geo = pv.PolyData(pts[seed_indices])
plotter.add_mesh(seed_points_geo, color='red', point_size=10, render_points_as_spheres=True)

# 显示窗口
plotter.show()

# 可选：保存结果到文件（例如 VTK 格式）
tin_euc.save('voronoi_euclidean.vtk')
tin_geo.save('voronoi_geodesic.vtk')
print("结果已保存为 voronoi_euclidean.vtk 和 voronoi_geodesic.vtk")