import panel as pn # 导入panel库，用于创建交互式可视化界面

til = pn.pane.Str('hello, web gis') # 创建一个字符串面板，显示"hello, web gis"
til2 = pn.pane.Str('hello,ecut') # 创建一个字符串面板，显示"hello,ecut"
til.object = 'hello,ecut' # 设置til面板的对象为"hello,ecut"

pn.Column(til,til2).show() # 显示til面板和til2面板的列布局
