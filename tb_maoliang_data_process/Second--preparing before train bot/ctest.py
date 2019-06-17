import json
import os


def delete_blank_dialog(data):
    # for i in range(len(data)):
    #     if len(data[i]) < 2:
    #         data.pop(i)
    #         i -= i
    #     if
    for data_list in data:
        if len(data_list) < 2:
            data.remove(data_list)
    return data


def add_blank_slot(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            for k in range(len(data[i][j]["dialog_acts"])):
                temp = data[i][j]["dialog_acts"][k]
                if isinstance(temp, str):
                    print("在第" + str(i) + "段对话的第" + str(j) + "句")
                if 'slots' not in temp.keys():
                    # pass
                    data[i][j]["dialog_acts"][k]["slots"] = []
                # else:
                #     data[i][j]["dialog_acts"][k]["slots"] = []

    return data


def init_bot_data():
    with open(os.path.abspath('../../') + r"\download\wzh_bot_data\all_tb_dialog_data.json", 'r'
              # , encoding="UTF-8"
              ) as load_f:
        load_dict = json.load(load_f)
        # print(load_dict)
    pre_data_all = []
    for order in load_dict:
        for dialog_dict in order:
            single_chat_record = []
            for sentence in dialog_dict["chat_record"]:
                sentence.pop("origin_text")
                single_chat_record.append(sentence)
            pre_data_all.append(single_chat_record)

    # TODO:这块用来放纠正函数
    # 删除句子少于2的对话
    pre_data_all = delete_blank_dialog(pre_data_all)
    # 给删除了slot的act加上一个为空的slot
    pre_data_all = add_blank_slot(pre_data_all)

    length = len(pre_data_all)
    data = {"train": tuple(pre_data_all[0:int(length*(1/2))]),
            "test":  tuple(pre_data_all[int(length*(1/2))+1:int(length*(3/4))]),
            "valid": tuple(pre_data_all[int(length*(3/4))+1:length])}
    return data

print(init_bot_data())



