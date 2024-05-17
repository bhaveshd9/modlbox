from PySide6.QtCore import QSize, QPropertyAnimation, QEasingCurve

class ResetPushButton:
    def resetOptions(self):
        self.method_comboBox.setCurrentIndex(0)
        self.detection_stage_comboBox.setCurrentIndex(0)
        self.gpu_comboBox.setCurrentIndex(0)
        self.epochs_spinBox.setValue(10)
        self.batch_size_spinBox.setValue(1)
        self.model_comboBox.setCurrentIndex(0)
        self.dataset_comboBox.setCurrentIndex(0)
        self.default_dataset_comboBox.setCurrentIndex(0)
        self.file_path_label.setText("File:")
    
