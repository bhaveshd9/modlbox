import sys
import subprocess
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QRadioButton, QFileDialog, QComboBox, QLineEdit, QLabel, QHBoxLayout, QPushButton
from PySide6.QtGui import QIntValidator


class DropDownExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MODL BOX")

        # Create a central widget and set a layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Create the first dropdown button
        self.method_label = QLabel("Method:")
        self.dropdown_button_1 = QComboBox()
        self.dropdown_button_1.addItem("Classification")
        self.dropdown_button_1.addItem("Detection")
        self.dropdown_button_1.currentIndexChanged.connect(self.on_dropdown_1_selection_changed)
        layout.addWidget(self.method_label)
        layout.addWidget(self.dropdown_button_1)

        # Create the second dropdown button (initially hidden)
        self.dropdown_button_2 = QComboBox()
        self.dropdown_button_2.addItem("1 stage")
        self.dropdown_button_2.addItem("2 stage")
        self.dropdown_button_2.hide()
        layout.addWidget(self.dropdown_button_2)

        # Create radio buttons and file dialog
        self.dataset_label = QLabel("Dataset:")
        self.file_radio_button = QRadioButton('Custom')
        self.file_radio_button.setChecked(True)  # Initially checked
        self.file_radio_button.toggled.connect(self.toggle_file_radio_button)

        self.dropdown_radio_button = QRadioButton('Default')
        self.dropdown_radio_button.toggled.connect(self.toggle_dropdown_radio_button)

        self.file_button = QFileDialog(self)
        self.file_button.setNameFilter("All Files (*)")
        self.file_button.setFileMode(QFileDialog.ExistingFile)
        self.file_button.setFixedSize(600, 400)  # Set fixed size for the file dialog window
        self.file_button.fileSelected.connect(self.file_selected)

        self.dropdown = QComboBox()
        self.dropdown.addItems(['Option 1', 'Option 2', 'Option 3'])
        self.dropdown.setEnabled(False)  # Initially disabled

        # Add radio buttons to the layout
        layout.addWidget(self.dataset_label)
        layout.addWidget(self.file_radio_button)
        layout.addWidget(self.dropdown_radio_button)

        # Add a layout for file selection
        file_layout = QHBoxLayout()
        file_layout.addWidget(self.file_button)
        layout.addLayout(file_layout)
        # Add dropdown to the layout
        layout.addWidget(self.dropdown)

        # Create a label and QLineEdit for entering epochs
        self.epoch_label = QLabel("Epochs:")
        self.epoch_input = QLineEdit()
        self.epoch_input.setValidator(QIntValidator(1, 10000))  # Set validator for integer input
        self.epoch_input.setText("1")  # Set default value to 1
        self.epoch_input.textChanged.connect(self.validate_epoch_input)

        # Add epochs label and input to the layout
        layout.addWidget(self.epoch_label)
        layout.addWidget(self.epoch_input)

        # Create a label and QLineEdit for entering batch size
        self.batch_size_label = QLabel("Batch Size:")
        self.batch_size_input = QLineEdit()
        self.batch_size_input.setValidator(QIntValidator(1, 100))  # Set validator for integer input
        self.batch_size_input.setText("1")  # Set default value to 1
        self.batch_size_input.textChanged.connect(self.validate_batch_size_input)
        layout.addWidget(self.batch_size_label)
        layout.addWidget(self.batch_size_input)

        # Add label and dropdown for GPU
        gpu_label = QLabel("GPU:")
        self.gpu_dropdown = QComboBox()
        self.populate_gpu_dropdown()  # Populate GPU dropdown
        layout.addWidget(gpu_label)
        layout.addWidget(self.gpu_dropdown)

        # Add label and dropdown for Backbone
        backbone_label = QLabel("Backbone:")
        self.backbone_dropdown = QComboBox()
        self.backbone_dropdown.addItems(['ResNet', 'MobileNet', 'VGG', 'DenseNet'])  # Example options
        layout.addWidget(backbone_label)
        layout.addWidget(self.backbone_dropdown)

        # Add start button
        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start_training)
        layout.addWidget(self.start_button)

    def populate_gpu_dropdown(self):
        self.gpu_dropdown.addItem("None")  # Add "None" as the default option
        try:
            gpu_info = subprocess.check_output(['wmic', 'path', 'win32_videocontroller', 'get', 'caption'], universal_newlines=True)
            gpu_list = gpu_info.strip().split('\n')[1:]  # Skip the header
            gpu_count = len([gpu.strip() for gpu in gpu_list if gpu.strip()])  # Count non-empty GPU entries
            self.gpu_dropdown.addItem(str(gpu_count))  # Add the count to the dropdown
        except Exception as e:
            print(f"Error occurred while populating GPU dropdown: {e}")

    def on_dropdown_1_selection_changed(self, index):
        # Show the second dropdown button if "detection" is selected
        if index == 1:
            self.dropdown_button_2.show()
        else:
            self.dropdown_button_2.hide()

    def toggle_file_radio_button(self, checked):
        self.file_button.setEnabled(checked)

    def toggle_dropdown_radio_button(self, checked):
        self.dropdown.setEnabled(checked)

    def file_selected(self, file):
        print(f'File selected: {file}')

    def validate_epoch_input(self, text):
        try:
            epoch = int(text)
            if 1 <= epoch <= 10000:
                self.epoch_input.setStyleSheet("")
            else:
                self.epoch_input.setStyleSheet("QLineEdit { background-color: red; }")
        except ValueError:
            self.epoch_input.setStyleSheet("QLineEdit { background-color: red; }")
    
    def validate_batch_size_input(self, text):
        try:
            batch_size = int(text)
            if 1 <= batch_size <= 100:
                self.batch_size_input.setStyleSheet("")
            else:
                self.batch_size_input.setStyleSheet("QLineEdit { background-color: red; }")
        except ValueError:
            self.batch_size_input.setStyleSheet("QLineEdit { background-color: red; }")

    def start_training(self):
        # Add functionality to start training
        print("Training started...")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DropDownExample()
    window.setGeometry(100, 100, 300, 200)
    window.show()
    sys.exit(app.exec())
