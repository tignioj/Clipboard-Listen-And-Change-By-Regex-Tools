# -*- coding: cp936 -*-


from utils.file_utils import *
from idna import unichr
# ��л���£�
# ��Դ�� https://www.cnblogs.com/kaituorensheng/p/3554571.html

def full2half(ustring):
    """ȫ��ת���"""
    rstring = ""
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code == 12288:  # ȫ�ǿո�ֱ��ת��
            inside_code = 32
        elif (inside_code >= 65281 and inside_code <= 65374):  # ȫ���ַ������ո񣩸��ݹ�ϵת��
            inside_code -= 65248

        rstring += unichr(inside_code)
    return rstring


def half2full(ustring):
    """���תȫ��"""
    rstring = ""
    for uchar in ustring:
        inside_code = ord(uchar)
        if inside_code == 32:  # ��ǿո�ֱ��ת��
            inside_code = 12288
        elif inside_code >= 32 and inside_code <= 126:  # ����ַ������ո񣩸��ݹ�ϵת��
            inside_code += 65248

        rstring += unichr(inside_code)
    return rstring

# s = getFile()
# print(strQ2B(s))