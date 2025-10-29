# MyLogger.py
class MyLogger:
    @staticmethod
    def banner(info: str):
        """
        打印一个高亮分隔块，用来在日志里显眼地展示一段信息。

        参数:
            info (str): 你要高亮输出的内容
        """
        print(f"\n################# {info} #################\n")


def banner(info):
    print(f"\n################# {info} #################\n")
    return None
