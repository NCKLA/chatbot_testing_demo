from deeppavlov.WriteFile import read_file_for_data
from deeppavlov.core.common.params import from_params
import deeppavlov.models.go_bot.bot as gob

# TODO:取的其他各个component  然后送到gobot　　　　取出之前用debug看一下是不是都 “train”和{}

#                  tokenizer: Component,
#                  tracker: Tracker,
#                  network_parameters: Dict[str, Any],
#                  template_path: str,
#                  save_path: str,
#                  load_path: str = None,
#                  template_type: str = "DefaultTemplate",
#                  word_vocab: Component = None,
#                  bow_embedder: Component = None,
#                  embedder: Component = None,
#                  slot_filler: Component = None,
#                  intent_classifier: Component = None,
#                  database: Component = None,
#                  api_call_action: str = None,
#                  use_action_mask: bool = False,
#                  debug: bool = False,
bot_dict = {
        "name": "go_bot",
        "in": ["x"],
        "in_y": ["y"],
        "out": ["y_predicted"],
        "word_vocab": {
            "name": "default_vocab",
            "id": "token_vocab",
            "load_path": "vocabs/token.dict",
            "save_path": "vocabs/token.dict",
            "fit_on": ["x"],
            "level": "token",
            "tokenizer": {
                "name": "split_tokenizer"
            }
        },
        "bow_embedder": {
            "name": "bow"
        },
        "embedder": {
            "id": "my_embedder",
            "name": "fasttext",
            "load_path": "embeddings/dstc2_fastText_model.bin",
            "save_path": "embeddings/dstc2_fastText_model.bin",
            "dim": 100,
            "chainer": {
                "pipe": [{
                    "name": "default_vocab",
                    "id": "token_vocab",
                    "load_path": "vocabs/token.dict",
                    "save_path": "vocabs/token.dict",
                    "fit_on": ["x"],
                    "level": "token",
                    "tokenizer": {
                        "name": "split_tokenizer"
                    }
                }]
            }
        },
        "slot_filler": {
            "config_path": "E:\\GithubSpace\\DeepPavlov\\deeppavlov/../deeppavlov/configs/ner/slotfill_dstc2.json"
        },
        "template_path": "dstc2/dstc2-templates.txt",
        "template_type": "DualTemplate",
        "database": {
            "name": "sqlite_database",
            "id": "restaurant_database",
            "save_path": "dstc2/resto.sqlite",
            "primary_keys": ["name"],
            "table_name": "mytable"
        },
        "api_call_action": "api_call",
        "load_path": "gobot_dstc2_full/model",
        "save_path": "gobot_dstc2_full/model",
        "network_parameters": {
            "load_path": "gobot_dstc2_full/model",
            "save_path": "gobot_dstc2_full/model",
            "dense_size": 64,
            "hidden_size": 128,
            "learning_rate": 0.002,
            "attention_mechanism": {
                "action_as_key": True,
                "depth": 3,
                "hidden_size": 32,
                "max_num_tokens": 100,
                "projected_align": False,
                "type": "cs_bahdanau"
            }
        },
        "tokenizer": {
            "name": "stream_spacy_tokenizer",
            "lowercase": False
        },
        "tracker": {
            "name": "featurized_tracker",
            "slot_names": ["pricerange", "this", "area", "food", "name"]
        },
        "main": True,
        "debug": False
    }

mode_train = {"mode": "train"}

tracker = from_params(bot_dict["tracker"], "train")

tokenizer = from_params(bot_dict["tokenizer"], "train")

network_parameters = bot_dict["network_parameters"]

template_path = bot_dict["template_path"]
save_path = bot_dict["save_path"]
load_path = bot_dict["load_path"]
template_type = bot_dict["template_type"]

# 'str' object has no attribute 'items'
word_vocab = from_params(bot_dict["word_vocab"], "train")

bow_embedder = from_params(bot_dict["bow_embedder"], "train")

embedder = from_params(bot_dict["embedder"], "train")

database = from_params(bot_dict["database"], "train")

slot_filler = from_params(bot_dict["database"], "train")

# intent_classifier: Component = None,

api_call_action = bot_dict["api_call_action"]

# use_action_mask: bool = False,
debug = bot_dict["debug"]

model = gob.GoalOrientedBot(tokenizer, tracker, network_parameters, template_path, save_path, load_path, template_type,\
                            word_vocab, bow_embedder, embedder, slot_filler, None, database, api_call_action, False, \
                            False)

# print(model)
# print(type(model))

# list_x, list_y = read_file_for_data()
# for x, y in zip(list_x, list_y):
#     loss = model.train_on_batch(list(x), list(y))

# print(type(embedder))

# from deeppavlov.WriteFile import write_file_for_data
#
# x = "test x666"
# y = "test y222"
# write_file_for_data(str(x)+"\n", str(y)+"\n")
