import pandas  as pd
from pyecharts.charts import Map,Page
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



c = (
    Map()
    .add("治愈",[list(z) for z in zip(data2_list, data4_list)], "china")
    .add("确诊",[list(z) for z in zip(data2_list, data3_list)], "china")
    .add("死亡",[list(z) for z in zip(data2_list, data5_list)], "china")
    .set_global_opts(
        title_opts=opts.TitleOpts(title='全国疫情数据总览',subtitle='数据截止自2022年12月22日'),
        visualmap_opts=opts.VisualMapOpts(max_=100000),
    )
)
c.render()

# Cumulative = (
#     Map()
#     .add("累计确诊", [list(z) for z in zip(data2_list, data3_list)], "china")
#     .set_global_opts(
#         title_opts=opts.TitleOpts(),
#         visualmap_opts=opts.VisualMapOpts(max_=200),
#     )
# )
#
# death = (
#     Map()
#     .add("死亡", [list(z) for z in zip(data2_list, data5_list)], "china")
#     .set_global_opts(
#         title_opts=opts.TitleOpts(),
#         visualmap_opts=opts.VisualMapOpts(max_=200),
#     )
# )
#
# cure = (
#     Map()
#     .add("治愈", [list(z) for z in zip(data2_list, data5_list)], "china")
#     .set_global_opts(
#         title_opts=opts.TitleOpts(),
#         visualmap_opts=opts.VisualMapOpts(max_=200),
#     )
# )
#
# page = Page(layout=Page.DraggablePageLayout)
# page.add(
#     Cumulative,
#     death,
#     cure,
# )
# # 先生成render.html文件
# page.render()