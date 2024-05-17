from PySide6.QtCore import QTimer
import csv
import os

class Terminal:
    previous_output = None

    @staticmethod
    def append_text(self, text):
        if not text.startswith("0%"):
            if Terminal.previous_output != text:
                self.terminal_textBrowser.append(text)
                Terminal.previous_output = text

