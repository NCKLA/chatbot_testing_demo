from deeppavlov.core.commands.infer import build_model_from_config
import thulac as thu

model = build_model_from_config("E:/GithubSpace/DeepPavlov/deeppavlov/configs/ner/wzh_single_ner_config.json")
thu1 = thu.thulac(seg_only=True, user_dict="user_DIY_words.txt")
s0 = thu1.cut("双十一期间全场包邮买100立减30", text=True)
# s0 = s0.split(" ")
# print(s0)
# ss = str(input("请输入： "))
# s0 = thu1.cut(ss, text=True)
# print(s0.split(" "))
for i in range(50):
    # print(model(input("请输入： ")))
    s1 = input("请输入： ")
    s2 = thu1.cut(s1, text=True)
    print(model([s2.split(" ")]))
    # print(model([input("请输入： ")]))

# 训练语句如下，要手动把迭代器送进去  因为配置文件没读取器
# from deeppavlov.core.common.params import from_params
# train_evaluate_model_from_config("E:/GithubSpace/DeepPavlov/deeppavlov/configs/ner/wzh_single_ner_config.json",
#                                  from_params({"name": "wzh_ner_iterator"}))
