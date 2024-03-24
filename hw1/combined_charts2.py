from pyecharts import options as opts
from pyecharts.charts import Bar, Line,Page,Grid,Pie

#准备数据
x_data= ['1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月']
y_a = [38845,56921,39571,41459,23545,24932,18166,20535,28125,29535,42280,19865] #国内IOS端流水（万元）
y_b = [58268,85382,59357,62189,35318,37098,27249,30803,42188,44303,63420,29798] #国内安卓端流水（万元）
y_c = [106824,156533,108820,114012,64749,68013,49957,56471,77344,81221,116270,54629] #国内PC端流水（万元）
y_all = [203937,298836,207748,217660,123612,130043,95372,107809,147657,155059,221970,104292] #国内流水总和（万元）

x_pie = ['国内ios','国内安卓','国内PC','海外ios','海外安卓','海外PC/PS','云原神']
y_pie = [383779,575373,1054843,235376,240036,720613,39450]
def bar_line_combine() -> Bar: #柱状图和折线图组合
    bar = (
        Bar()
        .add_xaxis(x_data)
        .add_yaxis("ios端", y_a)
        .add_yaxis("安卓端", y_b)
        .add_yaxis("PC端", y_c)
        .set_global_opts(title_opts=opts.TitleOpts(title="2023年原神国内市场流水组合图"),
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
        .add_yaxis("总和",y_all)
    )
    bar.overlap(line)
    return bar

def pie_rosetype() -> Pie: #饼状图
    c = (
        Pie()
        .add(
            "收入（万元）",
            [list(z) for z in zip(x_pie,y_pie)],
            radius=["30%", "70%"], #玫瑰图半径最小最大值
            center=["50%", "50%"], #玫瑰图横坐标
            rosetype="radius",
            label_opts=opts.LabelOpts(is_show=True),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="2023年原神国内外市场流水分布玫瑰图"),
            legend_opts=opts.LegendOpts(orient="vertical", pos_top="10%", pos_left="80%"),
        )
    )
    return c

def page_simple_layout():
    page = Page(layout=Page.SimplePageLayout)#Page内置了两种布局：simple，draggable
    page.add(
        bar_line_combine(),
        pie_rosetype()
    )
    page.render("./output/page_simple_layout.html")


if __name__ == "__main__":
    page_simple_layout()