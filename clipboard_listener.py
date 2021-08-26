import pyperclip
import time


class ClipboardListener:
    @staticmethod
    def handleClipboardChangeAndDoSomething(callBackFunction):
        """
        检测剪贴板变动，如果复制了文本，则处理文本后，再重新设置剪贴板
        :param callBackFunction: 剪贴板变更后调用的函数
        :return:
        """
        prev = pyperclip.paste()
        print(prev)
        while True:
            time.sleep(0.1)
            # 把新的剪贴板文本拿到，和旧的做对比，如果不一样则进行处理
            # 当剪贴板为非文本的时候，获取的是空字符串
            try:
                nowText = pyperclip.paste()
                if (nowText != prev) and (nowText != ''):
                    print("Clipboard has changed!, from:", prev, "--to-->", nowText)
                    textAfterChange = callBackFunction(nowText)
                    # 必须在重新设置剪贴板之前，把处理后的文本赋值到nowText表示当前剪贴板内容
                    nowText = textAfterChange
                    prev = nowText
                    ClipboardListener.addToClipBoard(textAfterChange)
                    print("clipboard content now:\n", nowText)
            except pyperclip.PyperclipWindowsException as e:
                print("Error:", e)


    @staticmethod
    def addToClipBoard(text):
        "添加文本到剪贴板"
        pyperclip.copy(text)
