class TopRightButtons:
    @staticmethod
    def minimize_window(parent):
        parent.showMinimized()

    @staticmethod
    def maximize_window(parent):
        if parent.isMaximized():
            parent.showNormal()
        else:
            parent.showMaximized()

    @staticmethod
    def close_window(parent):
        parent.close()
