def write_file_for_data(x: str, y: str):
    f1, f2 = _init_file()
    f1.write(x)
    f2.write(y)
    f1.close()
    f2.close()


def _init_file():
    file_name_x = "data_before_go_bot_x.txt"
    file_name_y = "data_before_go_bot_y.txt"
    f1 = open(file_name_x, "a+")
    f2 = open(file_name_y, "a+")
    return f1, f2


def read_file_for_data():
    file_name_x = "data_before_go_bot_x.txt"
    file_name_y = "data_before_go_bot_y.txt"
    f1 = open(file_name_x, "r")
    f2 = open(file_name_y, "r")
    origin_x = f1.read()
    origin_y = f2.read()
    return origin_x.split("\n"), origin_y.split("\n")



