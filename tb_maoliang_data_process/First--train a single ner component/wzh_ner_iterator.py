# copy from deeppavlov dstc2_ner_iterator.py

from random import Random
from typing import List, Dict, Tuple, Any, Iterator
import logging
import json

from deeppavlov.core.commands.utils import expand_path
from deeppavlov.core.common.registry import register
from deeppavlov.core.data.data_learning_iterator import DataLearningIterator

from deeppavlov.extend.excel_2_list import read_data_from_xlsx

logger = logging.getLogger(__name__)


@register('wzh_ner_iterator')
class WzhNerIterator(DataLearningIterator):
    def __init__(self, data: List[Tuple] = None, dataset_path: str = None, seed: int = None, shuffle: bool = False):
        self.shuffle = shuffle
        self.random = Random(seed)
        # TODO: include slot vals to dstc2.tar.gz
        # dataset_path = expand_path(dataset_path) / 'slot_vals.json'
        # self._build_slot_vals(dataset_path)

        # TODO:这部分是单独训练ner的 所以从csv里面读取的数据，而数据从reader传上来已经是BIO格式了  这里直接改一下就行
        # with open(dataset_path, encoding='utf8') as f:
        #     self._slot_vals = json.load(f)
        # for data_type in ['train', 'test', 'valid']:
        #     bio_markup_data = self._preprocess(data.get(data_type, []))
        #     setattr(self, data_type, bio_markup_data)

        ner_data = read_data_from_xlsx()
        self.train = ner_data['train']
        self.valid = ner_data['valid']
        self.test = ner_data['test']

        self.data = {
            'train': self.train,
            'valid': self.valid,
            'test': self.test,
            'all': self.train + self.test + self.valid
        }
        self.shuffle = shuffle

# if True:
#     from deeppavlov.core.common.params import from_params
#     train_evaluate_model_from_config("E:/GithubSpace/DeepPavlov/deeppavlov/configs/ner/wzh_single_ner_config.json",
#                                      from_params({"name": "wzh_ner_iterator"}))
# 训练时手动配置迭代器


