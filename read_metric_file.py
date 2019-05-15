import json

from pyecharts.charts.line import Line


def draw_line(train_logs, valid_logs):
    line = Line('intent_classfier_log')
    train_x = [train_log["train"]["epochs_done"] for train_log in train_logs]
    train_y = [train_log["train"]["metrics"]["sets_accuracy"] for train_log in train_logs]
    line.add('train', train_x, train_y,
             # mark_point=['average', 'max', 'min'],  # 标注点：平均值，最大值，最小值
             # mark_point_symbol='diamond',  # 标注点：钻石形状
             mark_point_textcolor = '#40ff27') #标注点：标注文本颜色
    valid_x = [valid_log["valid"]["epochs_done"] for valid_log in valid_logs]
    valid_y = [valid_log["valid"]["metrics"]["sets_accuracy"] for valid_log in valid_logs]
    line.add('valid', valid_x, valid_y, mark_point_textcolor ='#170B3B')
    line.render('line01.html')


def read_file(file_name):
    f = open(file_name, "r")
    string_logs = f.read()
    string_logs = string_logs[:-1]
    logs = string_logs.split("\n")
    train_logs = []
    valid_logs = []
    for string_log in logs:
        log = json.loads(string_log)
        if log.__contains__("valid"):
            valid_logs.append(log)
        if log.__contains__("train"):
            train_logs.append(log)
    draw_line(train_logs, valid_logs)


read_file("metric_log_file/intent_classfier_log.txt")
