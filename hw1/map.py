

from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Geo, Map
from pyecharts.globals import ChartType, SymbolType

with open('./data/world_pop.txt','r',encoding='utf-8') as file:
    content = file.read()
lines = content.split('\n') #按照换行符分割内容

print(type(lines))
data = {} #创建一个空的字典，用于存储键值对
#for line in lines:
 #   key, value = line.strip().split(':')
  #  data[key] = int(value) #

#print(data)
#data = dict(data)
#print(data)


for line in lines:
    if line.strip():  # 跳过空行
        key, value = line.strip().split(':')
        data[key.strip()] = int(value.strip()) # 去除空格并转换值为整数
print(data)
map_data = list(data.items())

c = (
    Map()
    .add("2023年世界人口（单位：千）",
         data_pair=map_data,
         maptype="world",
         is_map_symbol_show=False, # 不描点
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="2023年世界人口数据分级设色图"),
        visualmap_opts=opts.VisualMapOpts(min_=1, max_=1500000, is_piecewise=True),
    )
)

c.render('./output/世界人口数据地图_map.html')
