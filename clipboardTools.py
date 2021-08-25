import pyperclip
import time


class ClipBoardTools:
    @staticmethod
    def handleClipboardText(changeText):
        """
        检测剪贴板变动，如果复制了文本，则处理文本后，再重新设置剪贴板
        :param changeText: 对文本进行处理
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
                    print("Clipboard change!", prev, "-->", nowText)
                    textAfterChange = changeText(nowText)
                    # 必须在重新设置剪贴板之前，把处理后的文本赋值到nowText表示当前剪贴板内容
                    nowText = textAfterChange
                    prev = nowText
                    ClipBoardTools.addToClipBoard(textAfterChange)
                    print("clipboard contentNow:\n", nowText)
            except pyperclip.PyperclipWindowsException:
                print("Error when open")


    @staticmethod
    def addToClipBoard(text):
        "添加文本到剪贴板"
        pyperclip.copy(text)
