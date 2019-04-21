from deeppavlov.core.common.params import from_params



# # TODO:取的其他各个component  然后送到gobot　　　　取出之前用debug看一下是不是都 “train”和{}  【已知fasttext不是
# tokenizer: Component,
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

tracker_dict = \
    {
        "name": "featurized_tracker",
        "slot_names": ["pricerange", "this", "area", "food", "name"]
    }
tracker = from_params(tracker_dict, "train", {})
