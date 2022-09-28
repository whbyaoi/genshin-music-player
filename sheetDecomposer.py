import os
from MyMap import DIGIT_TO_KEY, KEY_TO_DIGIT


class Note:
    """ 每次奏响的音符 """

    def __init__(self, keys: str, duration: float = 0.0):
        self.keys = keys
        self.duration = duration  # 节拍数 / 时值

    def add(self, ch):
        self.keys += ch


class sheetDecomposer:
    def __init__(self):
        self.sheet = []
        self.charStack = ''
        self.defaultDuration = 0.5

    def addNote(self, note, check=True):
        # 检查栈顶note是否有时值
        if self.sheet:
            if check and self.sheet[-1].keys[0] != '&' and self.sheet[-1].duration == 0.0:
                self.sheet[-1].duration = self.defaultDuration
        # print(note.keys)
        self.sheet.append(note)

    def export(self):
        rs = ''
        noteCount = 0
        for note in self.sheet:
            if note.keys[0] == '&':
                rs += note.keys + '&'
            else:
                noteCount += 1
                if len(note.keys) > 1:
                    rs += '('
                    for key in note.keys:
                        rs += KEY_TO_DIGIT[key]

                    rs += ')'
                else:
                    rs += KEY_TO_DIGIT[note.keys]
                rs += '={}='.format(note.duration)
                if noteCount % 4 == 0:
                    rs += '\n'
                if noteCount % 16 == 0:
                    rs += '\n'
        return rs

    def loadSheet(self, fileName: str):
        """ 载入乐谱 """
        self.sheet = []
        self.charStack = ''
        self.defaultDuration = 0.5
        curDir = os.getcwd()
        fileDir = curDir + '/sheets/{}'.format(fileName)
        file = open(fileDir, 'r', encoding='utf8')
        while line := file.readline():
            # 替换一些空字符
            line.replace(' ', '')
            line.replace('\n', '')
            if line:
                # 重置栈
                self.resetStack()
                for ch in line:
                    # 修改BPM
                    if ch == '&':
                        if self.charStack == '':
                            self.push(ch)
                        # BPM读取结束
                        elif self.charStack[0] == '&':
                            self.addNote(Note(self.charStack[0:], False))
                            self.popAll()
                        else:
                            pass
                    # 添加时值
                    elif ch == '=':
                        if self.charStack == '':
                            self.push(ch)
                        # 时值读取结束
                        elif self.charStack[0] == '=':
                            # 检查栈顶是否为待填时值的音符
                            if self.sheet[-1].keys[0] != '&' and self.sheet[-1].duration == 0.0:
                                self.sheet[-1].duration = float(self.charStack[1:])
                                self.popAll()
                            else:
                                pass
                        else:
                            pass
                    # 读取多个音符结束
                    elif ch == ')':
                        _stack = ''
                        note = Note('')
                        for _ch in self.charStack:
                            if _ch in ['-', '+']:
                                _stack += _ch
                            elif _ch in ['1', '2', '3', '4', '5', '6', '7']:
                                if _stack == '':
                                    note.add(DIGIT_TO_KEY[_ch])
                                elif _stack[0] in ['-', '+']:
                                    note.add(DIGIT_TO_KEY[_stack[0] + _ch])
                                    _stack = ''
                                # 异常情况
                                else:
                                    pass
                            # 异常情况
                            else:
                                pass
                        # 添加音符 and 重置栈
                        self.addNote(note)
                        self.popAll()
                    # 需要继续读取的情况，例如同时演奏多个音符，和升降调
                    elif ch in ['(', '-', '+']:
                        self.push(ch)
                    # 读取到数字与 .
                    elif ch in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']:
                        # 根据栈底内容运行
                        # 如果栈底为空
                        if self.charStack == '':
                            self.addNote(Note(DIGIT_TO_KEY[ch]))
                        # 如果是时值或修改BPM
                        elif self.charStack[0] in ['=', '&']:
                            self.push(ch)
                        # 如果是演奏多个音符的情况
                        elif self.charStack[0] == '(':
                            if ch in ['1', '2', '3', '4', '5', '6', '7']:
                                self.push(ch)
                        # 如果是升降调
                        elif self.charStack[0] in ['-', '+']:
                            # 检查读取数字是否在正常范围
                            if ch in ['1', '2', '3', '4', '5', '6', '7']:
                                self.addNote(Note(DIGIT_TO_KEY[self.charStack[0] + ch]))
                                self.popAll()
                            else:
                                pass

            # if line == '\n':
            #     continue
            # stack = ''
            # for op in line:
            #     if op in ['(', '-', '+']:
            #         # 进栈
            #         stack += op
            #     elif op == ')':
            #         # 出栈
            #         keys = ''
            #         _stack = ''
            #         for _op in stack[1:]:
            #             if _op in ['-', '+']:
            #                 _stack += _op
            #             elif _op in ['1', '2', '3', '4', '5', '6', '7']:
            #                 if _stack == '':
            #                     keys += DIGIT_TO_KEY[_op]
            #                 else:
            #                     keys += DIGIT_TO_KEY[_stack + _op]
            #                     _stack = ''
            #         self.sheet.append(keys)
            #         stack = ''
            #     elif op == '=':
            #         if stack == '':
            #             stack += '='
            #         elif stack[0] == '=':
            #             self.sheet.append(float(stack[1:]))
            #             stack = ''
            #     elif op == '&':
            #         if stack == '':
            #             stack += '&'
            #         elif stack[0] == '&':
            #             self.sheet.append(stack)
            #             stack = ''
            #     elif op in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']:
            #         if stack == '':
            #             self.sheet.append(DIGIT_TO_KEY[op])
            #         elif stack[0] in ['(', '=', '&']:
            #             stack += op
            #         elif stack[0] in ['-', '+']:
            #             stack += op
            #             self.sheet.append(DIGIT_TO_KEY[stack])
            #             stack = ''
            #     else:
            #         pass

    def loadSlice(self, slice: str):
        pass

    def resetStack(self):
        self.charStack = ''

    def push(self, ch: str):
        self.charStack += ch

    def pop(self):
        if self.charStack:
            popElement = self.charStack[-1]
            self.charStack = self.charStack[:-1]
            return popElement
        else:
            return None

    def popAll(self):
        if self.charStack:
            stackContent = self.charStack
            self.charStack = ''
            return stackContent
        else:
            return None


if __name__ == "__main__":
    sheetDec = sheetDecomposer()
    sheetDec.loadSheet('兰亭序_76_.txt')
    # print(sheetDec.sheet)
    sheetDec.export()
