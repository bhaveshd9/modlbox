from functions.pages.prediction_page.qpushbutton.open_image_file_qpushbutton import OpenImageFileButton
from functions.pages.prediction_page.qpushbutton.clear_image_selection_file_qpushButton import ClearImageFileSelectionButton
from ui_mainwindow import Ui_MainWindow


class PredictionPage:
    def initPredictionPage(main_window: Ui_MainWindow):
        mw = main_window
        mw.open_image_file_pushButton.clicked.connect(lambda: OpenImageFileButton.openImageFile(main_window))
        mw.clear_image_selection_file_pushButton.clicked.connect(lambda: ClearImageFileSelectionButton.clearImageSelection(main_window))   
        