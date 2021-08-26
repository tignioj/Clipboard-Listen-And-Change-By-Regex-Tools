import re
from utils.file_utils import *
from utils.regex_utils import *

def testTrimEndOfLine():
    strToReplace = """
        中华文明历史悠久，博大精深，源远流长。传统中医学伴随着历史的发展一
    直流传至今，造福着古今中外的人们。与西方医学最大的不同之处在于，中医认
    为人体是一个有机的整体，医生需要从多方面了解和系统掌握疾病的相关信息，
    从而对患者进行有针对性的临床治疗。其独特的“望闻问切”四诊法是中国古代
    人民智慧的结晶，也是中华文化的瑰宝。面诊是中医望诊的重要环节，也是医生
    通过面象对病人体内病症进行定位、定性的一种有效的诊疗手段。近些年来，随
    着中医现代化的发展，人们对中医面诊手段有了新的要求。依托图像处理和计算
    机视觉技术的兴起，中医面诊客观化和定量化己经成为了必然的研究方向。利用
    图像处理的方法来实现中医面诊，能够有效避免外部条件的影响和医生知识水平、
    临床经验的干扰，从而更准确更科学地给予医生诊断的参考。因此，如何有效且
    高效地利用计算机视觉的方法实现自动化中医面诊成为了国内外诸多学者和医
    者密切关注的问题。
    """

    "删掉所有的换行"
    trimPattern = re.compile(r'[\n\s]')
    strAfterTrim = trimPattern.sub("", strToReplace)
    print(strAfterTrim)

def testRegex():
    p = re.compile(r'<img src="(.+?)"')
    s = p.sub(r'\1', r'<img src="http://www.baidu.com/1.jpg"')
    print(s)
    s = p.sub(r'\1', r'<img src="test"')
    print(s)

def testFile():
    s = getFile("../before_replace.txt")
    print(s)