class SwitchPage:
        
    def switchToSetupPage(self):
        self.page_list.setCurrentIndex(0)
        self.page_follow_label.setText("Setup Page")
        self.setup_page_pushButton.setChecked(True)
        
        
    def switchToGraphPage(self):
        self.page_list.setCurrentIndex(1)
        self.page_follow_label.setText("Graph Page")
        self.graph_page_pushButton.setChecked(True)
        
    def switchToPredictionPage(self):
        self.page_list.setCurrentIndex(2)
        self.page_follow_label.setText("Prediction Page")
        self.prediction_page_pushButton.setChecked(True)
