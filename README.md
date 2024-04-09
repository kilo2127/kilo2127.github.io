# sanda_codinghw
# 计算机科学与编程入门课程第一次作业
## 2000013071 梁玮诚

## 1. 作业1 《倚天屠龙记》前十出现人名词频分析
作业1首先读取指定路径下的小说《倚天屠龙记》文本文件，使用课上所学的jieba分词工具对txt文本进行初步分词，统计每个词在文本中出现的次数，之后按照观察与经验进行忽略词、添加词与合并词来增加分词精准度，即得到《倚天屠龙记》中前十出现人名的词频列表，程序会将排名前 N（由用户指定，默认为10，实际上也只保证前十的精准度）的词和它们的出现次数输出到屏幕上，并写入到output目录下的CSV 文件中（文件路径为 ./output/倚天屠龙记-人物词频.csv）。

而后再使用matplotlib库中的绘图工具读取output目录下统计到的前十出现人名的词频列表，将词频列表以柱状图形式展示（注意要先引入os库设置中文字体，否则展示图里无法显示中文字符），具体操作与展示结果可在第一次作业仓库链接里的github库中查看。


## 2. 作业2 全球GDP地图（map）展示
作业2中我们用了pyecharts库生成了一张世界地图图表，以百万美元为单位展示了各个国家的GDP。

我们首先从pyecharts库中导入了options模块，pyecharts.charts中的Map模块以及pyecharts.global中的ChartType和SymbolType模块来实现调整各项参数以及数据，然后从文本文件“gdp_data.txt”中读取数据，我们假定该文件包含各个国家/地区的 GDP 数据（作业中有附上示例数据）。 数据逐行读取，去除任何空白字符，并使用制表符作为分隔符拆分为多个字段，结果数据存储在名为数据（data）的列表中。

将数据列表转化为格式化数据列表（formatted_data），其中每一项都是一个包含国家名称（原始数据中的第一个字段）及其 GDP 值的元组。

按照老师上课使用的“地图（map）”类来创建地图图表，调整各项参数并渲染成html文件存入output目录下，具体操作与展示结果可在作业仓库链接里的github库中查看。

## 3. 作业3 国家人均GDP与恩格尔系数组合分析
首先需要说明的是，人均GDP一直被视为衡量一个国家经济水平，尤其是人均收入的重要指标，因此人均GDP在一定程度上反映各国的贫富情况；而恩格尔指数是国民食品支出占总消费支出的比例，一般认为越先进富足的国家的恩格尔指数会越小。

作业3里我们选择十个较为常见的国家作为分析对象，从世界银行和美国农业经济研究局里分别获取各国在2018年的人均GDP以及恩格尔指数。先按人均GDP从大到小排序，并用柱状图的方式呈现；恩格尔系数则用折线图的方式呈现，以此绘制出一份横坐标为国家，左侧纵坐标为人均GDP（柱状图），右侧纵坐标为恩格尔系数（折线图）的组合图表。此作业主要运用pyechart中的Bar与Line模组进行数据展示，最后用Grid将两个图表组合起来。

从最后的展示结果可以发现，人均GDP确实和恩格尔系数呈负相关的关系。具体操作与展示结果可在作业仓库链接里的github库中查看。

# 计算机科学与编程入门课程第二次作业
## 2000013071 梁玮诚

## 1. 作业1 实现某个搜索引擎的搜索功能
作业1中我们用html代码和外置的css文件创建了一个简单的网站，其中包含了两个搜索引擎的搜索框，让用户可以在一个页面上同时进行谷歌和百度搜索。具体操作如下：

1、引入一个外部样式表的链接，指向名为 "myGoodu_style.css" 的CSS文件，用于定义页面的样式。在此css文件中，我们让所有出现在网页上的元素都居中显示，并在说明文字上增加了楷体加粗的设定。
2、引入一个图片元素，用于显示名为 "Goodu_logo.png" 的图片，此图片来源于百度图片，用以表示该搜索引擎同时具有的两种搜索功能，如果图片无法显示，则显示 "图片未显示" 的替代文本。
3、创建一个搜索表单，用于向谷歌搜索引擎提交搜索请求。表单的 "action" 属性指定了搜索请求的目标URL， "method" 属性指定了请求的HTTP方法为 "get"。
4、创建一个文本输入框，用户可以在其中输入搜索关键词， "name" 属性指定了提交给服务器的参数名为 "q"。
5、创建一个提交按钮，用户点击后会将搜索关键词提交给服务器进行搜索，按钮上显示的文本为 "谷歌搜索"。
6、百度搜索的模板与谷歌搜索类似，便不再赘述。

具体代码可于作业仓库中“第二次作业/作业1/”中查看，点击下列链接可直接预览作业1的html网页。
[作业1网页展示链接]
(https://kilo2127.github.io/第二次作业/作业1/myGoodu.html)

## 2. 作业2 《倚天屠龙记》人物共现分析与网页设计
作业2主要分成以下3部分完成：

一、jieba.posseg对《倚天屠龙记》小说文本的人物共现分析
二、pyechart绘制共现分析图并渲染成html文件
三、对渲染完成的html文件进行简单设计，如增加标题文字以及插入剧照等

具体实现过程为：
一、jieba.posseg对《倚天屠龙记》小说文本的人物共现分析
1、读入小说《倚天屠龙记》的文本文件；
2、使用 jieba.posseg 对文本进行分词，并根据词性标注（nr表示人名）提取人物名字；
3、将同一段落内的人物列表保存在 line_name_list 中，并统计每个人物出现的次数；
4、对一些指代同一人物的名词进行合并，比如将无忌、张教主、教主等合并为张无忌；
5、最终将结果保存在两个 csv 文件中，一个文件保存人物节点，一个文件保存人物之间的共现关系。

二、pyechart绘制共现分析图并渲染成html文件
0、准备工作
指定输入文件和输出文件的文件名。

1、从文件读入节点和连接信息
打开指定的节点文件和连接文件，读取它们的内容。
逐行解析文件内容，并把节点信息和连接信息存入对应的列表中。
删除每个列表中的标题行。

2、解析读入的信息，存入列表
对于节点信息列表，解析每个元素，并将其转化为opts.GraphNode对象，存入node_in_graph列表中。其中，节点的name、value、symbol_size分别对应文件中的第1、2、3列，其中节点的value（节点的大小）按20为基础单位进行缩放。
对于连接信息列表，解析每个元素，并将其转化为opts.GraphLink对象，存入link_in_graph列表中。其中，连接的source、target、value分别对应文件中的第1、2、3列。

3、画图
创建一个Graph对象，命名为c。
使用Graph对象的add()方法，将节点信息和连接信息添加到图中。
使用Graph对象的render()方法，将图渲染成HTML格式，并保存到指定的输出文件中。
在渲染时，设置了一些图的属性，例如edge_length表示边的长度，repulsion表示节点间的斥力系数，layout表示布局方式（这里选用的是circular，即环形布局）。

三、对渲染完成的html文件进行简单设计，如增加标题文字以及插入剧照等
1、style里定义内部样式表，包含了一些CSS样式：.centered、.highlight_text、.normal、.illustrate、#Kai。这些都是CSS样式的类或ID选择器，用于定义不同的样式。
2、body利用.centered样式使得全部元素居中展示（但是无法使得渲染出来的环形共现分析图居中，不知道该怎么解决），加上标题、剧组图片、一段说明文字和一个人物共现分析图的标题。

具体代码可于作业仓库中“第二次作业/作业2/”中查看，点击下列链接可直接预览作业2的html网页。
[作业2网页展示链接]
(https://kilo2127.github.io/第二次作业/作业1/关系图-倚天屠龙记人物.html)