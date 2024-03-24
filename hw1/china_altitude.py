from pyecharts import options as opts
from pyecharts.charts import Map

data ={
"广东省":218,
"山东省":90,
"河南省":246,
"四川省":2560,
"江苏省":15,
"河北省":509,
"湖南省":357,
"安徽省":195,
"湖北省":431,
"浙江省":303,
"广西壮族自治区":385,
"云南省":1892,
"江西省":246,
"辽宁省":224,
"福建省":482,
"陕西省":1130,
"黑龙江省":313,
"山西省":1160,
"贵州省":1108,
"重庆市":730,
"吉林省":404,
"甘肃省":2158,
"内蒙古自治区":999,
"新疆维吾尔自治区":1904,
"上海市":4,
"台湾省":778,
"北京市":365,
"天津市":22,
"海南省":191,
"香港特别行政区":121,
"宁夏回族自治区":1559,
"青海省":4049,
"西藏自治区":4737,
"澳门特别行政区":27,
"南海诸岛":3.8
}

map_data = list(data.items())

c = (
    Map()
    .add("全国各省平均海拔（单位：米）",
         data_pair=map_data,
         maptype="china",
         is_map_symbol_show=False, # 不描点
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="全国各省平均海拔示意图"),
        visualmap_opts=opts.VisualMapOpts(max_=5000),
    )
)

c.render('./output/全国各省平均海拔_map.html')