class SwitchPage:
    def switch_to_filePage(main_window):
        main_window.stackedWidget.setCurrentIndex(0)
        main_window.test_label.setText("File Page")
        
    def switch_to_setupPage(main_window):
        main_window.stackedWidget.setCurrentIndex(1)
        main_window.test_label.setText("Setup Page")
        
    def switch_to_analyzePage(main_window):
        main_window.stackedWidget.setCurrentIndex(2)
        main_window.test_label.setText("Analyze Page")
        
    def switch_to_aboutPage(main_window):
        main_window.stackedWidget.setCurrentIndex(3)
        main_window.test_label.setText("About Page")
