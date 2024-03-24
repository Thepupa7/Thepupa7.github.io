import jieba
from pyecharts import options as opts
from pyecharts.charts import WordCloud

# 待分析的文本和输出结果的文件名
txt_filename = './data/2024两会政府工作报告.txt'
result_filename = './output/2024两会热点.csv'

# 从文件读取待分析的文本
txt_file = open(txt_filename, 'r', encoding='utf-8')
content = txt_file.read()
txt_file.close()

# 忽略词列表
ignore_list = ['推进','加强','推动','加快','促进','提高','加大','我们','方面','今年','一批','坚持','行动','深入','实施','支持','做好','力度','制定','实现','化解','继续','特别','各位',
               '一年','一些','进一步']

# 不切割的词
jieba.suggest_freq('国务院',True)
jieba.suggest_freq('改革开放',True)
jieba.suggest_freq('科技创新',True)
jieba.suggest_freq('社会主义', True)
jieba.suggest_freq('现代化', True)
jieba.suggest_freq('小康社会', True)
jieba.suggest_freq('新冠肺炎', True)
jieba.suggest_freq('政府工作', True)
jieba.suggest_freq('一带一路', True)

# 分词
word_list = jieba.lcut(content)
print(word_list)

# 用字典统计每个词的出现次数
word_dict = {}
for w in word_list:
    if (len(w)) == 1:  # 跳过单字
        continue
    # 跳过在忽略词列表中的词
    if w in ignore_list:
        continue
    if w in word_dict.keys(): # 已在字典中的词，将出现次数增加1
        word_dict[w] = word_dict[w] + 1
    else:  # 未在字典中的词，表示是第一次出现，添加进字典，次数记为1
        word_dict[w] = 1

# 把字典转成列表，并按原先“键值对”中的“值”从大到小排序
items_list = list(word_dict.items())
items_list.sort(key=lambda x:x[1], reverse=True)

print(items_list)
total_num = len(items_list)
print('经统计，共有' + str(total_num) + '个不同的词')




cloud = WordCloud()

# 设置词云图
cloud.add('词频（次）',
          items_list[0:200], #元组列表，词和词频
          mask_image='./data/词云背景图-中国.jpg', # 轮廓图，第一次显示可能有问题，刷新即可
          is_draw_out_of_bound=False, #允许词云超出画布边界
          word_size_range=[8, 60], #字体大小范围
          textstyle_opts=opts.TextStyleOpts(font_family="华文行楷"),
          #字体：例如，微软雅黑，宋体，华文行楷，Arial
          )

# 设置标题
cloud.set_global_opts(title_opts=opts.TitleOpts(title="2024年两会政府工作报告热词"))

# render会生成HTML文件。默认是当前目录render.html，也可以指定文件名参数
out_filename = './output/wordcloud_opts.html'
cloud.render(out_filename)