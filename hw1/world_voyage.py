from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType,GeoType

geo = Geo()

# 添加坐标点
geo.add_coordinate(name="桑卢卡尔-德巴拉梅达",longitude=-6.3542,latitude=36.7788)
geo.add_coordinate(name="加得利群岛",longitude=-15.44083,latitude=28.11250)
geo.add_coordinate(name="里约热内卢湾",longitude=-43.2096,latitude=-22.9035)
geo.add_coordinate(name="拉普拉塔河",longitude=-58.39361,latitude=-34.00139)
geo.add_coordinate(name="圣胡利安港",longitude=-67.716667,latitude=-49.3)
geo.add_coordinate(name="维尔赫纳斯角",longitude=-68.3499986,latitude=-52.333332)
geo.add_coordinate(name="希望角",longitude=-74.7333,latitude=-52.7333)
geo.add_coordinate(name="普卡普卡岛",longitude=-165.85,latitude=-10.883333)
geo.add_coordinate(name="沃斯托克岛",longitude=-152.900,latitude=-10.083)
geo.add_coordinate(name="马里亚纳群岛",longitude=145.931389,latitude=16.794022)
geo.add_coordinate(name="萨马",longitude=125,latitude=11.83125)
geo.add_coordinate(name="霍蒙洪",longitude=125.716667,latitude=10.733333)
geo.add_coordinate(name="利马萨瓦",longitude=125.075,latitude=9.9078)
geo.add_coordinate(name="宿雾",longitude=123.9,latitude=10.3)
geo.add_coordinate(name="麦克坦",longitude=123.966667,latitude=10.3)
geo.add_coordinate(name="巴拉望",longitude=118.3975,latitude=9.5275)
geo.add_coordinate(name="文莱",longitude=114.942217,latitude=4.890283)
geo.add_coordinate(name="蒂多雷",longitude=127.4,latitude=0.683333)
geo.add_coordinate(name="安汶岛",longitude=128.117222,latitude=-3.638056)
geo.add_coordinate(name="帝汶",longitude=124.933333,latitude=-9.233333)
geo.add_coordinate(name="好望角",longitude=18.490769,latitude=-34.3547)
geo.add_coordinate(name="佛得角群岛",longitude=-23.61308,latitude=16.78529)
geo.add_coordinate(name="塞维利亚港",longitude=-5.986944,latitude=37.443889)
geo.add_coordinate(name="中间点1",longitude=-180,latitude=0)
geo.add_coordinate(name="中间点2",longitude=180,latitude=0)
# 添加数据项（设置地图范围）
geo.add_schema(maptype="world")

# 添加数据
geo.add("",
        [
            ("桑卢卡尔-德巴拉梅达","1519年9月20日"),
            ("加得利群岛","1519年9月26日"),
            ("里约热内卢湾","1519年12月13日"),
            ("拉普拉塔河","1520年1月12日"),
            ("圣胡利安港","1520年3月31日"),
            ("维尔赫纳斯角","1520年10月21日"),
            ("希望角","1520年11月28日"),
            ("普卡普卡岛","1521年1月21日"),
            ("沃斯托克岛","1521年2月4日"),
            ("马里亚纳群岛","1521年3月6日"),
            ("萨马","1521年3月16日"),
            ("霍蒙洪","1521年3月17日"),
            ("利马萨瓦","1521年3月28日"),
            ("宿雾","1521年4月7日"),
            ("麦克坦","1521年4月27日 (麦哲伦逝世)"),
            ("巴拉望","暂无时间信息"),
            ("文莱","暂无时间信息"),
            ("蒂多雷","1521年11月8日"),
            ("安汶岛","1521年12月29日"),
            ("帝汶","1522年1月25日"),
            ("好望角","1522年5月19日"),
            ("佛得角群岛","1522年7月9日"),
            ("塞维利亚港","1522年9月6日")
        ],
        type_=ChartType.SCATTER,
        label_opts=opts.LabelOpts(formatter="{b}", is_show=True),  # 标签格式，显示地点名称和字符串
)

# 添加流向图
geo.add("",
        [
            ("桑卢卡尔-德巴拉梅达","加得利群岛"),
            ("加得利群岛","里约热内卢湾"),
            ("里约热内卢湾","拉普拉塔河"),
            ("拉普拉塔河","圣胡利安港"),
            ("圣胡利安港","维尔赫纳斯角"),
            ("维尔赫纳斯角","希望角"),
            ("希望角","普卡普卡岛"),
            ("普卡普卡岛","沃斯托克岛"),
            ("沃斯托克岛","中间点1"),
            ("中间点2","马里亚纳群岛"),
            ("马里亚纳群岛","萨马"),
            ("萨马","霍蒙洪"),
            ("霍蒙洪","利马萨瓦"),
            ("利马萨瓦","宿雾"),
            ("宿雾","麦克坦"),
            ("麦克坦","巴拉望"),
            ("巴拉望","文莱"),
            ("文莱","蒂多雷"),
            ("蒂多雷","安汶岛"),
            ("安汶岛","帝汶"),
            ("帝汶","好望角"),
            ("好望角","佛得角群岛"),
            ("佛得角群岛","塞维利亚港")
        ],
        type_=ChartType.LINES,
        effect_opts=opts.EffectOpts(symbol=SymbolType.ARROW,symbol_size=5, color="#4682B4"),
        linestyle_opts=opts.LineStyleOpts(curve=0.2,color="#5F9EA0"),
        label_opts=opts.LabelOpts(is_show=False)
)

geo.set_global_opts(title_opts=opts.TitleOpts(title="麦哲伦环球航行路线图"))
geo.render('./output/麦哲伦环球航行路线图.html')


