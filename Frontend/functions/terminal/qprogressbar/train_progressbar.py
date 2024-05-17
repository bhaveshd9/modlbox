from PySide6.QtCore import QThread, Signal
import csv
import time

class Progress_Bar_Thread(QThread):
    progress = Signal(int)

    def __init__(self, method, dataset):
        super().__init__()
        self.method = method
        self.dataset = dataset

    def stop(self):
        self.running = False

    def run(self):
        self.running = True
        row_count = 0
        file_path = ''
        if (self.method == 'Detection'):
            file_path = 'runs/detect/train/results.csv'
        else:
            file_path = 'runs/classify/train/results.csv'
        while row_count < 100 and self.running:
            try:
                with open(file_path, 'r', newline='', encoding='utf-8') as file:
                    reader = csv.reader(file)
                    row_count = sum(1 for row in reader) - 1
                    self.progress.emit(row_count)
            except FileNotFoundError:
                pass
            time.sleep(1)

            
class TrainProgressBar:
    def update_progress_bar(self, value):
        max_value = self.epochs_spinBox.value()
        self.train_progressBar.setValue((value/max_value)*100)