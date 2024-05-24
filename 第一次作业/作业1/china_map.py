"""
Date: 2024.3.24
Author: 梁玮诚

"""
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.globals import ChartType, SymbolType

# 处理数据
formatted_data = []

# 读取数据
with open("C:\\Users\\leung\\Documents\\GitHub\\kilo2127.github.io\\第一次作业\\作业1\\china_data.txt", 'r', encoding='utf-8') as f:
    for line in f:
        # Split each line into province and GDP value
        print(line)
        province, gdp = line.strip().split()
        # Convert GDP value to float and append to the list as a tuple
        formatted_data.append((province, float(gdp)))

print(formatted_data)

c = (
    Map()
    .add("GDP（单位：亿人民币）",
         formatted_data,
         maptype="china",
         is_map_symbol_show=False,
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="中国GDP地图"),
        visualmap_opts=opts.VisualMapOpts(min_=min(d[1] for d in formatted_data), 
                                          max_=max(d[1] for d in formatted_data)),
    )
)

c.render('C:\\Users\\leung\\Documents\\GitHub\\kilo2127.github.io\\第一次作业\\作业1\\output/map_gdp_china.html')