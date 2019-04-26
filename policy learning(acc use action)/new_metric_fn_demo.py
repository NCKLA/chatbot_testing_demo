def pre_action_accuracy(y_true, y_predict):
    # 进来的数据是list   里面包含4个list  这四个list里面是一整段对话  改了代码之后y_predict应该输入的是
    y_true = [y['act'] for dialog in y_true for y in dialog]
    # y_predicted = itertools.chain(*y_predicted)
    y_predicted = [value for temp in y_predict for value in temp]
    # TODO:可能这里不是action（英文），而是index
    # for temp in y_predict:
    #     for value in temp:
    #         y_predicted.append(value)
    examples_len = len(y_true)
    correct = sum([y1.strip().lower() == y2.strip().lower() for y1, y2 in zip(y_true, y_predicted)])
    return correct / examples_len if examples_len else 0

# TODO：需要添加到记事本metrics_registry  可能还要写 @ 这个东西    明天就去改输出为action，记得注释写好的（4.26）

# 下面惯例先test一下
# test = {"y": [1, 2, 3, 4, 5], "y_pre": [[6], [7, 8], 9, 0, "test"]}
# for i in ["y", "y_pre"]:
#     print(*[test[i]])
#     print("\n")
# alist = [[1, 2], [8, 77], [9, 88], [7, 66]]
# x = [value for temp in alist for value in temp]
# print(x)
