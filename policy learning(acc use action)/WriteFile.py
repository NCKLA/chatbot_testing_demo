class WriteFile:
    def __init__(self):
        self.file_name_x = "data_before_go_bot_x.txt"
        self.file_name_y = "data_before_go_bot_y.txt"
        self.f1 = open(self.file_name_x, "a+")
        self.f2 = open(self.file_name_y, "a+")

    def write_file_for_data(self, x, y_true):
        self.f1.write(x)
        self.f1.write(y_true)

    def __del__(self):
        self.f1.close()
        self.f2.close()
