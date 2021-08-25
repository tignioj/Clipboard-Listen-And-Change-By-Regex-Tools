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
    # 表示去掉 ''、'' 以及 '' 这三个奇怪的字符
    # s = RegexTool.trimUnKnownChar(s, [r'', r'', r''])

    # 去掉换行
    # s = RegexTool.trimEndOfLine(s)

    # 换行替换为空格
    # s = RegexTool.trimEndOfLineAsSpace(s)

    # 去掉所有的空格和换行（所有的内容会挤在一起）
    # s = RegexTool.trimSpaceAndEndOfLine(s)

    # 重新排版例如把 [1]xxx [2]xxx [3]xxx 变成了
    # [1] xxx
    # [2] xxx
    # [3] xxx
    # s =  RegexTool.reformatLineByReference(s)
    
    # 重新排版 例如把 （1）xxx （2）xxx （3）xxx 变成了
    # （1） xxx
    # （2） xxx
    # （3） xxx
    # 注意这是中文括号，如果要改请到方法里面修改
    # s = RegexTool.reformatLineByBraket(s)

    # 重新排版：多少个字符之后换行，例如这里输入30代表30个字符换行
    # s = RegexTool.reformatLine(s, 30)

    # 除了句号和逗号后面的空格和换行不去掉，其它的空格和换行全部去掉"
    # s = RegexTool.trimSpaceAndEndOfLineButNotCommaAndNotDot(s)

    # 读取文件夹而不是字符串
    # s = RegexTool.trimSpaceAndEndOfLine(getFile())

    # 所有的结果都会写入到文件`after_replace.txt`
    writeFile(s)

    # 字数统计(替换后的字数)
    print("\n字数：", len(s))
    return s

if __name__ == '__main__':
    ClipBoardTools.handleClipboardText(handleText)
