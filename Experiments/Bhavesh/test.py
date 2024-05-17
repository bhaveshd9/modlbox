import sys
import subprocess
from PySide6.QtWidgets import QApplication, QMainWindow, QPlainTextEdit, QPushButton, QVBoxLayout, QWidget
from ultralytics import YOLO

class YOLOOutputWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YOLO Output Window")
        self.setGeometry(100, 100, 600, 400)

        self.layout = QVBoxLayout(self)

        self.output_terminal = QPlainTextEdit()
        self.output_terminal.setReadOnly(True)
        self.layout.addWidget(self.output_terminal)

        self.start_yolo_button = QPushButton("Start YOLO")
        self.start_yolo_button.clicked.connect(self.start_yolo)
        self.layout.addWidget(self.start_yolo_button)

    def start_yolo(self):
        try:
        # Run the YOLO command
            proc = subprocess.Popen(['yolo', 'detect', 'train', 'data=dota8.yaml', 'model=yolov8n.pt', 'epochs=10', 'imgsz=640'], stdout=subprocess.PIPE, universal_newlines=True)
        # Read and display the output in real-time
            for line in iter(proc.stdout.readline, ""):
                try:
                    decoded_line = line.decode('utf-8')  # Decode the line using utf-8 encoding
                    self.output_terminal.appendPlainText(decoded_line.strip())
                except UnicodeDecodeError:
                    self.output_terminal.appendPlainText("Error decoding line: " + repr(line))
                QApplication.processEvents()  # Update GUI to show real-time output
            proc.stdout.close()
            proc.wait()
        except Exception as e:
            self.output_terminal.appendPlainText("Error running YOLO: " + str(e))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = YOLOOutputWindow()
    window.show()
    sys.exit(app.exec_())