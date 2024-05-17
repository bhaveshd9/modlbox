from PySide6.QtCore import QUrl
class Tensorboard:
    def show_graph(webEngineView):
        webEngineView.setUrl(QUrl("http://localhost:6006/"))