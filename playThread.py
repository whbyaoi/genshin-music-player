import time

import pykeyboard
from PySide6.QtCore import QThread, Signal


class playThread(QThread):
    endSignal = Signal()

    def __init__(self, sheet, bpm):
        super(playThread, self).__init__()
        self.keyboardUnit = pykeyboard.PyKeyboard()
        self.sheet = sheet
        self.defaultInterval = 60 / bpm
        self.tickCount = 4

    def run(self) -> None:
        waitInterval = True
        ticks = 0
        tickContent = []
        for note in self.sheet:
            # 检查操作类型
            if note.keys[0] == '&':
                self.defaultInterval = 60 / float(note.keys[1:])
                print('切换到{}BPM'.format(int(note.keys[1:])))
                continue
            else:
                for key in note.keys:
                    self.keyboardUnit.tap_key(key)
                time.sleep(note.duration * self.defaultInterval)
        self.endSignal.emit()

        # for clock in self.sheet:
        #     if isinstance(clock, float):
        #         time.sleep(clock * self.defaultInterval)
        #         ticks += clock
        #         waitInterval = False
        #     else:
        #         if clock[0] == '&':
        #             self.defaultInterval = 60 / float(clock[1:])
        #             print('切换到{}BPM'.format(int(clock[1:])))
        #             continue
        #         else:
        #             if waitInterval:
        #                 time.sleep(self.defaultInterval)
        #                 ticks += 1
        #             for key in clock:
        #                 self.keyboardUnit.tap_key(key)
        #             tickContent.append(clock)
        #             waitInterval = True
        #         if ticks == 4.0:
        #             print('{}拍已过, 内容{}'.format(self.tickCount, tickContent))
        #             tickContent = []
        #             ticks = 0


