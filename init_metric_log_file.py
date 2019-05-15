# 在train.py下的打印report下面紧接着一行加入这句


def write_file(log: dict, file_name="metric_log.txt"):
    f = open(file_name, "a+")
    f.write(str(log))
    f.write("\n")
    f.close()
