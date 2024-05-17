from .tensorboard import Tensorboard

class GraphPage:
    def initGraphPage(webEngineView):
        Tensorboard.show_graph(webEngineView)
        


    