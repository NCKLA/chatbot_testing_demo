from overrides import overrides


from deeppavlov.core.common.registry import register
from deeppavlov.core.models.component import Component
from deeppavlov.core.common.log import get_logger
# from nltk import word_tokenize

import thulac as thu1

log = get_logger(__name__)


@register('thulac_tokenizer')
class ThulacTokenizer(Component):
    def __init__(self, **kwargs):
        pass

    @overrides
    def __call__(self, batch, *args, **kwargs):
        if len(batch) > 0 and isinstance(batch[0], str):
            # s2 = thu1.cut(s1, text=True)
            # print(model([s2.split(" ")]))
            batch = [thu1.cut(utt, text=True).split(" ") for utt in batch]
        return batch
