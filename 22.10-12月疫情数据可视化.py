from pyecharts import options as opts
from pyecharts.charts import Bar
import csv

# 定义读取的csv
filename = "病例.csv"


# 通过文件循环读取数据

# 定义date变量，并用for循环从csv中读取日期
with open(filename) as f:
    reader = csv.reader(f)
    date = [row[0] for row in reader]

# 定义confirm变量，并用for循环从csv中读取确诊人数
with open(filename) as f:
    conf_reader = csv.reader(f)
    confirm = [row[1] for row in conf_reader]

# 定义dead变量，并用for循环从csv中读取死亡人数
with open(filename) as f:
    dead_reader = csv.reader(f)
    dead = [row[3] for row in dead_reader]

# 定义cure变量，并用for循环从csv中读取治愈人数
with open(filename) as f:
    cure_reader = csv.reader(f)
    cure = [row[4] for row in cure_reader]

# 删除变量中的无用元素
date.remove('date')
confirm.remove('confirm')
dead.remove('dead')
cure.remove('heal')

y1 = confirm
y2 = dead
y3 = cure

c = (
    Bar()
    .add_xaxis(date)
    .add_yaxis("确诊人数", y1, stack="stack1")
    .add_yaxis("死亡人数", y2, stack="stack2")
    .add_yaxis("治愈人数", y3, stack="stack3")
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title="2022年10月-12月疫情数据"))
    .render("2022年10月-12月疫情数据.html")
)
