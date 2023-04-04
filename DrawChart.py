import pandas  as pd
from pyecharts.charts import Map,Bar,Page
from pyecharts import options as opts

#设置列对齐
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
#打开文件
df = pd.read_csv('data.csv')
#对省份进行统计
data2 = df['地区']
data2_list = list(data2)
data3 = df['确诊']
data3_list = list(data3)
data4 = df['治愈']
data4_list = list(data4)
data5 = df ['死亡']
data5_list = list(data5)
data6 = df ['死亡/确诊']
data6_list = list(data6)
data7 = df ['治愈/确诊']
data7_list = list(data7)


# 确诊人数
c = (
    Map()
    .add("确诊人数",[list(z) for z in zip(data2_list, data3_list)], "china")
    .set_global_opts(
        title_opts=opts.TitleOpts(),
        visualmap_opts=opts.VisualMapOpts(max_=100000),
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
)

cureBar = (
    Bar()
    .add_xaxis(data2_list)
    .add_yaxis('',data3_list, category_gap=0)
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False),barMaxHeight=30,barMinHeight=5)
    .set_global_opts(
        title_opts=opts.TitleOpts(title=""),
        xaxis_opts=opts.AxisOpts(axislabel_opts={"interval": 0, "rotate": 45})
    )
)


# c.render("confirm.html")


# 治愈/确诊比例
cure_confirm = (
    Map()
    .add("治愈/确诊", [list(z) for z in zip(data2_list, data7_list)], "china")
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}"))
    .set_global_opts(
        title_opts=opts.TitleOpts(),
        visualmap_opts=opts.VisualMapOpts(min_=0, max_=1, range_color=["#B22222" ,"#00FF00" ]),
    )
)

cureConfirmBar = (
    Bar()
    .add_xaxis(data2_list)
    .add_yaxis('',data7_list, category_gap=0)
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False),barMaxHeight=30,barMinHeight=5)
    .set_global_opts(
        title_opts=opts.TitleOpts(title=""),
        xaxis_opts=opts.AxisOpts(axislabel_opts={"interval": 0, "rotate": 45})
    )
)

# cure_confirm.render("cure_confirm.html")

# 死亡/确诊比例
death_confirm = (
    Map()
    .add("死亡/确诊", [list(z) for z in zip(data2_list, data6_list)], "china")
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}"))
    .set_global_opts(
        title_opts=opts.TitleOpts(),
        visualmap_opts=opts.VisualMapOpts(min_=0, max_=1, range_color=['#00FF00', '#FF0000']),
    )
)

deathConfirmBar = (
    Bar()
    .add_xaxis(data2_list)
    .add_yaxis('',data6_list, category_gap=0)
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False),barMaxHeight=30,barMinHeight=5)
    .set_global_opts(
        title_opts=opts.TitleOpts(title=""),
        xaxis_opts=opts.AxisOpts(axislabel_opts={"interval": 0, "rotate": 45})
    )
)

# death_confirm.render("death_confirm.html")

# 将确诊地图和柱状图合并在一个页面内
confirm = Page(layout=Page.SimplePageLayout)
confirm.add(c)
confirm.add(cureBar)
confirm.render("confirm.html")

# 将治愈/确诊地图和柱状图合并在一个页面内
cureConfirm = Page(layout=Page.SimplePageLayout)
cureConfirm.add(cure_confirm)
cureConfirm.add(cureConfirmBar)
cureConfirm.render("cureConfirm.html")

# 将死亡/确诊地图和柱状图合并在一个页面内
cureConfirm = Page(layout=Page.SimplePageLayout)
cureConfirm.add(death_confirm)
cureConfirm.add(deathConfirmBar)
cureConfirm.render("deathConfirm.html")