from functions.tools.qpushbutton.start_qpushbutton import StartPushButton

class StopPushButton:
    def stop(self):
        StartPushButton.thread_finish(self)