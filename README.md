# 介绍
Listens on the contents of the clipboard and uses regular expressions to modify the contents
监听剪贴板的内容，并用正则表达式修改内容

# 用途
复制文献的时候或者一些PDF有时候会复制到一些奇奇怪怪的字符，这是因为源文件的OCR没弄好
手动修改是很麻烦的，所以弄了个监听剪贴板的工具，检测到字符自动修改，能剩下不少麻烦。


# 安装
## 1. 安装依赖
```python
pip install -r ./requirement.txt
```

## 2. 输入你要修改的内容
在main.py里面有个各种方法，想用哪个直接取消注释就行了
```python
s = trimUnKnownChar(s, [r'', r'', r''])
```
表示去掉''、''以及''这三个奇怪的字符



## 3. 运行
```
python main.py
```


# 方法说明


    def handleText(s):
        # 表示去掉 ''、'' 以及 '' 这三个奇怪的字符
        # s = trimUnKnownChar(s, [r'', r'', r''])

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