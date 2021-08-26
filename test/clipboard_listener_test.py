from clipboard_listener import ClipboardListener


def changeT(txt):
    return "#" + txt


ClipboardListener.handleClipboardChangeAndDoSomething(changeT)
