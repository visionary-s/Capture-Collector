import logging
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QTextBrowser


class LoggerBox(QTextBrowser):
    def __init__(self, parent=None):
        super().__init__(parent)

        # log to text box
        logBox = QTextEditLogger(self)
        # logBox.setContentsMargins(0, 0, 0, 0)
        logBox.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        logging.getLogger().addHandler(logBox)
        logging.getLogger().setLevel(logging.DEBUG)

        # log to file
        # fh = logging.FileHandler('execution.log')
        # fh.setLevel(logging.DEBUG)
        # logBox.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        # logging.getLogger().addHandler(fh)


class QTextEditLogger(logging.Handler, QtCore.QObject):
    new_log = QtCore.pyqtSignal(str)

    def __init__(self, parent):
        super().__init__()
        QtCore.QObject.__init__(self)
        self.widget = QTextBrowser(parent)
        self.widget.setReadOnly(True)
        self.widget.setGeometry(QtCore.QRect(0, 0, 191, 250))
        # self.setFormatter(LogFormatter())
        self.new_log.connect(self.widget.append)

    def emit(self, record):
        msg = self.format(record)
        self.new_log.emit(msg)


class LogFormatter(logging.Formatter):
    def color_format(self, record):
        if record.levelno >= 40:
            # error & critical
            color = '#ff0000'
        elif record.levelno >= 30:
            # warning
            color = '#afaf00'
        else:
            # info & debug
            color = '#000000'
        message = f'<span style="color:{color};">{record.msg}</span><br>'

        return message
