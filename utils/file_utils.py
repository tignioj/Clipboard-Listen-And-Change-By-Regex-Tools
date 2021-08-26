import chardet


def getFile(fp="before_replace.txt"):
    str = ""
    with open(fp, encoding="utf-8") as f:
        content = f.readlines()
    for line in content:
        str += line
    return str


def writeFile(fp="after_replace.txt",str="0x123:Nothing"):
    with open(fp, mode="w", encoding="utf-8") as f:
        f.write(str)


# 获取文件编码类型
def get_encoding(file):
    # 二进制方式读取，获取字节数据，检测类型
    with open(file, 'rb') as f:
        return chardet.detect(f.read())['encoding']
