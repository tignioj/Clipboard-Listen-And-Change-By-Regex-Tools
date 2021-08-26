import re

# "正则表达式处理文本工具：针对CAJViewer的复制粘贴格式错乱问题"

def trimSpaceAndEndOfLineButNotCommaAndNotDot(str=""):
    "除了句号和逗号后面的空格和换行不去掉，其它的空格和换行全部去掉"
    pat = re.compile(r'(?<![，。])[\s\n]')
    s = pat.sub("", str)
    return s


def trimEndOfLine(strToReplace):
    "删除换行"
    trimPattern = re.compile(r'[\r\n]')
    strAfterTrim = trimPattern.sub("", strToReplace)
    return strAfterTrim


def trimEndOfLineAsSpace(strToReplace):
    "删除换行, 替换为空格"
    trimPattern = re.compile(r'[\r\n]')
    strAfterTrim = trimPattern.sub(" ", strToReplace)
    return strAfterTrim


def trimSpaceAndEndOfLine(strToReplace):
    "删掉所有的空格和换行"
    trimPattern = re.compile(r'[\s\n]')
    strAfterTrim = trimPattern.sub("", strToReplace)
    return strAfterTrim


def trimUnKnownChar(strToReplace, unKnownCharList):
    """
    删除乱码符号，比如,
    :param strToReplace: 要替换的文本
    :param unKnownCharList: 乱码字符数组，格式[r'',r'']
    :return: 替换后的文本
    """
    pat = r"("
    i = 0
    while i < len(unKnownCharList):
        unKnownChar = unKnownCharList[i]
        if i == len(unKnownCharList) - 1:
            pat += unKnownChar + r")"
        else:
            pat += unKnownChar + r"|"
        i += 1

    trimPattern = re.compile(pat)
    strAfterTrim = trimPattern.sub("", strToReplace)
    return strAfterTrim


def reformatLine(strToReplace="", count=10):
    """
    :param strToReplace: 要替换的字符串
    :param count: 第几个字就换行
    :return: 替换后的字符串
    """
    endOfLineCount = 0
    newStr = strToReplace
    index = count
    while index < (len(strToReplace)):
        indexPlusCount = index + endOfLineCount
        newStr = newStr[:indexPlusCount] + '\n' + newStr[indexPlusCount:]
        endOfLineCount += 1
        index += count
    return newStr


def reformatLineByReference(strToReplace):
    """
    重新排版例如把 [1]xxx [2]xxx [3]xxx 变成了
    [1]xxx
    [2]xxx
    [3]xxx
    :param strToReplace:
    :return:
    """
    # newStr = re.compile(r'(［\d+］)').sub(r'\n\1', strToReplace)
    newStr = re.compile(r'(\[\d+\])').sub(r'\n\1', strToReplace)
    return newStr


def reformatLineByBraket(strToReplace):
    "根据括号划分行"
    # newStr = re.compile(r'(［\d+］)').sub(r'\n\1', strToReplace)
    newStr = re.compile(r'(（\d+）)').sub(r'\n\1', strToReplace)
    # newStr = re.compile(r'(\(\d+\))').sub(r'\n\1', strToReplace)
    return newStr
