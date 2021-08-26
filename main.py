from utils.regex_utils import *
from utils.char_utils import *
from clipboard_listener import ClipboardListener
from utils.file_utils import writeFile


def handleText(s):
    # 表示去掉 ''、'' 以及 '' 这三个奇怪的字符
    s = trimUnKnownChar(s, [r'', r'', r''])

    # 去掉换行
    # s = trimEndOfLine(s)

    # 换行替换为空格
    # s = trimEndOfLineAsSpace(s)

    # 去掉所有的空格和换行（所有的内容会挤在一起）
    # s = trimSpaceAndEndOfLine(s)

    # 重新排版例如把 [1]xxx [2]xxx [3]xxx 变成了
    # [1] xxx
    # [2] xxx
    # [3] xxx
    # s =  reformatLineByReference(s)

    # 重新排版 例如把 （1）xxx （2）xxx （3）xxx 变成了
    # （1） xxx
    # （2） xxx
    # （3） xxx
    # 注意这是中文括号，如果要改请到方法里面修改
    # s = reformatLineByBraket(s)

    # 重新排版：多少个字符之后换行，例如这里输入30代表30个字符换行
    # s = reformatLine(s, 30)

    # 除了句号和逗号后面的空格和换行不去掉，其它的空格和换行全部去掉"
    # s = trimSpaceAndEndOfLineButNotCommaAndNotDot(s)

    # 读取文件而不是字符串
    # s = trimSpaceAndEndOfLine(getFile())

    # 全角转成半角
    s = full2half(s)

    # 半角转全角
    # s = half2full(s)

    # 所有的结果都会写入到文件`after_replace.txt`
    writeFile("after_replace.txt", s)

    # 字数统计(替换后的字数)
    print("\n字数：", len(s))
    return s


if __name__ == '__main__':
    ClipboardListener.handleClipboardChangeAndDoSomething(handleText)
