from pyecharts import options as opts
from pyecharts.charts import Bar, Line,Tab

#准备数据
x_data= ['1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月']
y_a = [38845,56921,39571,41459,23545,24932,18166,20535,28125,29535,42280,19865] #国内IOS端流水（万元）
y_b = [58268,85382,59357,62189,35318,37098,27249,30803,42188,44303,63420,29798] #国内安卓端流水（万元）
y_c = [106824,156533,108820,114012,64749,68013,49957,56471,77344,81221,116270,54629] #国内PC端流水（万元）

bar = (
    Bar()
    .add_xaxis(x_data)
    .add_yaxis("ios端",y_a)
    .add_yaxis("安卓端",y_b)
    .add_yaxis("PC端",y_c)
    .set_global_opts(title_opts=opts.TitleOpts(title="2023年原神国内市场流水柱状图"),
                     datazoom_opts=[opts.DataZoomOpts()]
                     )
    .extend_axis(
        yaxis=opts.AxisOpts(
            name='收入（万元）',  # 柱形图y轴名称
            type_='value',
            position='left',  # 柱形图y轴在左边显示
        )
    )
)

line = (
    Line()
    .add_xaxis(x_data)
    .add_yaxis("ios端",y_a)
    .add_yaxis("安卓端",y_b)
    .add_yaxis("PC端",y_c)
    .set_global_opts(title_opts=opts.TitleOpts(title="2023年原神国内市场流水折线图"))
    .extend_axis(
        yaxis=opts.AxisOpts(
            name='收入（万元）',  # 柱形图y轴名称
            type_='value',
            position='left',  # 柱形图y轴在左边显示
        )
    )
)

tab = (
    Tab()
    .add(
        bar,
        "柱状图"
    )
    .add(
        line,
        "折线图"
    )
)

tab.render("./output/原神2023年国内流水.html")