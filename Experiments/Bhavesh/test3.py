from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the user interface
        self.setWindowTitle("Info Button Example")
        self.setGeometry(100, 100, 300, 200)

        # Create an info button
        self.info_button = QPushButton("Info", self)
        self.info_button.setGeometry(100, 80, 100, 30)

        # Connect the button's clicked signal to the display_info method
        self.info_button.clicked.connect(self.display_info)

    def display_info(self):
        # Display an information message box
        QMessageBox.information(self, "Information", "This is some information.")

if __name__ == "__main__":
    import sys

    # Create the application instance
    app = QApplication(sys.argv)

    # Create and show the main widget
    widget = MyWidget()
    widget.show()

    # Execute the application event loop
    sys.exit(app.exec())
