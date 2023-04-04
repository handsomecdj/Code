import pyecharts.options as opts
from pyecharts.charts import Line
import pandas as pd



# 数据
x_data = ['2020.1', '2020.2', '2020.3', '2020.4', '2020.5', '2020.6', '2020.7', '2020.8', '2020.9',
          '2020.10', '2020.11', '2020.12', '2021.1', '2021.2', '2021.3', '2021.4', '2021.5', '2021.6',
          '2021.7', '2021.8', '2021.9', '2021.10', '2021.11', '2021.12', '2022.1', '2022.2', '2022.3',
          '2022.4', '2022.5', '2022.6', '2022.7', '2022.8', '2022.9', '2022.10', '2022.11', '2022.12']
y_data = [14380.0, 65646.0, 1563.0, 1286.0, 147.0, 515.0, 848.0, 681.0, 358.0, 597, 530, 542, 2501, 329,
          303, 460, 460, 664, 1293, 1823, 1277, 1111, 1583, 3608, 3697, 3548, 43482, 64220, 6719, 1576, 3954, 14121, 6978, 10171, 66993, 69231]



# 创建折线图对象
line = (
    Line()
    .add_xaxis(xaxis_data=x_data)
    .add_yaxis(
        series_name="新增确诊人数",
        y_axis=y_data,
        symbol="emptyCircle",
        is_symbol_show=True,
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(),
        legend_opts=opts.LegendOpts(is_show=False),
        tooltip_opts=opts.TooltipOpts(is_show=True),
        xaxis_opts=opts.AxisOpts(type_="category",axislabel_opts={"interval": 0, "rotate": 45}),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
    )
)

# 渲染图像
line.render("MonthlyLine.html")
