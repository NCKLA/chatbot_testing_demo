import json

from pyecharts.charts.line import Line
from collections import OrderedDict


def draw_line(train_logs, valid_logs, html_name, graph_name):
    line = Line(graph_name)

    # g = OrderedDict([('pre_action_accuracy', 0.7458)])
    # dict((y, x) for x, y in g)

    # 只需要传2个集合

    train_x = [train_log["train"]["epochs_done"] for train_log in train_logs]
    train_y = [train_log["train"]["metrics"]["policy_f1"] for train_log in train_logs]
    line.add('train', train_x, train_y,
             # mark_point=['average', 'max', 'min'],  # 标注点：平均值，最大值，最小值
             # mark_point_symbol='diamond',  # 标注点：钻石形状
             mark_point_textcolor='#40ff27')  # 标注点：标注文本颜色
    valid_x = [valid_log["valid"]["epochs_done"] for valid_log in valid_logs]
    # valid_y = [dict((x, y) for x, y in valid_log["valid"]["metrics"]["pre_action_accuracy"])
    # for valid_log in valid_logs]
    valid_y = [valid_log["valid"]["metrics"]["policy_f1"] for valid_log in valid_logs]
    line.add('valid', valid_x, valid_y, mark_point_textcolor='#170B3B')
    line.render(html_name)


def read_file(file_name, html_name, graph_name):
    f = open(file_name, "r")
    string_logs = f.read()
    string_logs = string_logs[:-1]
    logs = string_logs.split("\n")
    train_logs = []
    valid_logs = []
    for string_log in logs:

        # json.loads（）有问题  换成eval之后好了

        log = eval(string_log)
        # log = json.loads(string_log)
        # log = dict(string_log)
        if log.__contains__("valid"):
            valid_logs.append(log)
        if log.__contains__("train"):
            train_logs.append(log)
    draw_line(train_logs, valid_logs, html_name, graph_name)


# 三个参数  文件名   ，   网页名（要加HTML后缀）    ，图名
read_file("metric_log_file/policy_log3.txt", "html_policy_acc.html", "policy_acc")


