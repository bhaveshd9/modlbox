from PySide6.QtCore import QSize, QThread
import os
from functions.model_threads.yolo_thread import yolo_export_thread

class ExportPushButton:
    @staticmethod
    def export(main_window):
        mw = main_window
        mw.ethread = yolo_export_thread(model_name="yolov8n.pt",format="onnx")
        mw.ethread.on_export_finished.connect(lambda: mw.terminal_textBrowser.append("Export finished"))
        # mw.ethread.on_export_finished.connect(lambda: mw.te_terminal.append("Export finished"))
        mw.ethread.on_export_finished.connect(lambda: mw.ethread.quit())
        # mw.ethread.stdout.connect(lambda x: mw.te_terminal.append(x))
        mw.ethread.start()
            
       