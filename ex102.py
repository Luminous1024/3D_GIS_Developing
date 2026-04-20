import panel as pn # 导入Panel库,用于创建交互式可视化界面
import geopandas as gpd # 导入GeoPandas库,用于处理地理数据

df = gpd.read_file(r'C:\Users\吕梓源\Desktop\课程\大三上学期\数据分析程序设计（Python）\REG.shp',encoding = 'gbk') # 读取地理数据文件
print(df.columns) # 打印数据列名
header = df.columns[:8] # 选择前8列作为表头
tbl = pn.widgets.Tabulator(df[header],pagination = 'local',page_size = 20) # 创建表格组件
# tbl.show() # 显示表格组件

info = pn.pane.Str('no selection yet') # 创建信息面板组件

def sel_(e): # 定义选择回调函数
    info.object = 'item selected:' + str(e.new[0]) # 更新信息面板组件显示选中项索引

tbl.param.watch(sel_,'selection') # 监听表格组件的选择事件

pn.Column(tbl,info).show() # 显示表格组件和信息面板组件
