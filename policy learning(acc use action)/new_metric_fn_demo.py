# @register_metric('pre_action_accuracy')
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


# @register_metric('per_item_dialog_bleu_kai')

# bleu use dialog sentence , not the action
def per_item_dialog_bleu_kai(y_true, y_predicted):
    from nltk.translate.bleu_score import corpus_bleu
    y_true = (y['text'] for dialog in y_true for y in dialog)
    return corpus_bleu([[y_t.lower().split()] for y_t in y_true],
                       [y_q.lower().split() for y_p in y_predicted for y_q in y_p])

# TODO：需要添加到记事本metrics_registry  可能还要写 @ 这个东西    明天就去改输出为action，记得注释写好的（4.26）


action_list = ['api_call', 'bye', 'canthear', 'canthelp_area', 'canthelp_area_food', 'canthelp_area_food_pricerange',
               'canthelp_area_pricerange', 'canthelp_food', 'canthelp_food_pricerange', 'confirm-domain',
               'expl-conf_area', 'expl-conf_food', 'expl-conf_pricerange',
               'impl-conf_area+impl-conf_pricerange+request_food', 'impl-conf_food+impl-conf_pricerange+request_area',
               'impl-conf_food+request_area', 'inform_addr+inform_food+offer_name',
               'inform_addr+inform_phone+inform_pricerange+offer_name', 'inform_addr+inform_phone+offer_name',
               'inform_addr+inform_postcode+offer_name', 'inform_addr+inform_pricerange+offer_name',
               'inform_addr+offer_name', 'inform_area+inform_food+inform_pricerange+offer_name',
               'inform_area+inform_food+offer_name', 'inform_area+inform_phone+offer_name',
               'inform_area+inform_postcode+offer_name', 'inform_area+inform_pricerange+offer_name',
               'inform_area+offer_name', 'inform_food+inform_pricerange+offer_name',
               'inform_food+offer_name', 'inform_phone+inform_postcode+offer_name',
               'inform_phone+inform_pricerange+offer_name', 'inform_phone+offer_name',
               'inform_postcode+inform_pricerange+offer_name', 'inform_postcode+offer_name',
               'inform_pricerange+offer_name', 'offer_name', 'repeat', 'reqmore', 'request_area', 'request_food',
               'request_pricerange', 'select_area', 'select_food', 'select_pricerange', 'welcomemsg']
# 在bot那里  把这个函数改成这样  当然  前面要自己声明一个action_list
#     def _decode_response(self, action_id):
#         return action_list[int(action_id)]

# 下面惯例先test一下
# test = {"y": [1, 2, 3, 4, 5], "y_pre": [[6], [7, 8], 9, 0, "test"]}
# for i in ["y", "y_pre"]:
#     print(*[test[i]])
#     print("\n")
# alist = [[1, 2], [8, 77], [9, 88], [7, 66]]
# x = [value for temp in alist for value in temp]
# print(x)
