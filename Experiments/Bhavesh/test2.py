import psutil
import os
import platform
import sys
from pathlib import Path
from subprocess import call

from PySide6 import QtCore
from PySide6.QtCore import *
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QApplication

platform = platform.system()
print(str(platform))

term_dir = Path(os.path.abspath(os.path.dirname(__file__))) / 'terminus'

if platform == 'Windows':
    term_bin = str(term_dir) + '/' + str(platform.lower()) + '/' + 'terminus.exe'

print(term_bin)


class embeddedTerminal(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self._processes = []
        self.resize(800, 600)
        self.terminal = QWidget(self)
        layout = QVBoxLayout(self)
        layout.addWidget(self.terminal)
        self._stop_process()
        self._start_process(
            'xterm',
            ['-into', str(self.terminal.winId()),
             '-e', 'tmux', 'new', '-s', 'my_session']
        )
        button = QPushButton('List files')
        layout.addWidget(button)
        button.clicked.connect(self._list_files)

    def _start_process(self, prog, args):
        child = QProcess()
        self._processes.append(child)
        child.start(prog, args)

    def _list_files(self):
        self._start_process(
            'tmux', ['send-keys', '-t', 'my_session:0', 'ls', 'Enter'])

    @classmethod
    def _stop_process(self):
        call(["tmux", "kill-session", "-t", "my_session"])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = embeddedTerminal()
    main.show()
    sys.exit(app.exec_())