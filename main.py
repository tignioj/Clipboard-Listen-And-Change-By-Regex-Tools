from regexTools import RegexTool
from clipboardTools import ClipBoardTools
import cchardet as chardet

def getFile():
    str = ""
    with open("before_replace.txt", encoding="utf-8") as f:
        content = f.readlines()
    for line in content:
        str += line
    return str


def writeFile(str="0x123:Nothing"):
    with open("after_replace.txt", mode="w", encoding="utf-8") as f:
        f.write(str)


# 获取文件编码类型
def get_encoding(file):
    # 二进制方式读取，获取字节数据，检测类型
    with open(file, 'rb') as f:
        return chardet.detect(f.read())['encoding']


def handleText(s):
    # s = getFile()
    s = RegexTool.trimEndOfLine(s)
    # s = RegexTool.trimSpaceAndEndOfLine(s)
    # s = RegexTool.trimUnKnownChar(s, [r'', r'', r''])
    # s =  RegexTool.reformatLineByReference(s)
    # s = RegexTool.reformatLineByBraket(s)
    # s = RegexTool.reformatLine(s, 30)
    # s = RegexTool.trimSpaceAndEndOfLineButNotCommaAndNotDot(getFile())
    # s = RegexTool.trimSpaceAndEndOfLine(getFile())
    writeFile(s)
    return s

if __name__ == '__main__':
    ClipBoardTools.loopCheckClipBoard(handleText)
