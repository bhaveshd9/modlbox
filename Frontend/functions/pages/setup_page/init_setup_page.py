from .qcombobox.method_qcombobox import MethodQComboBox
from .qcombobox.model_qcombobox import ModelQComboBox
from .qcombobox.dataset_qcombobox import DatasetQComboBox   
from .qcombobox.default_dataset_qcombobox import DefaultDatasetQComboBox
from .qcombobox.detection_stage_qcombobox import DetectionStageQComboBox
from .qcombobox.gpu_qcombobox import GPUQComboBox
from .qpushbutton.open_file_qpushbutton import OpenFileQPushButton

class SetupPage:
    @staticmethod
    def initSetupPage(self):
        MethodQComboBox.addMethodOptions(self)
        self.method_comboBox.currentIndexChanged.connect(lambda: ModelQComboBox.updateModelOptions(self))
        ModelQComboBox.updateModelOptions(self)
        DatasetQComboBox.addDatasetOptions(self)
        self.method_comboBox.currentIndexChanged.connect(lambda: DefaultDatasetQComboBox.updateDefaultDatasetOptions(self))
        DefaultDatasetQComboBox.updateDefaultDatasetOptions(self)
        self.model_comboBox.currentIndexChanged.connect(lambda: DefaultDatasetQComboBox.updateDefaultDatasetOptions(self))
        DefaultDatasetQComboBox.updateDefaultDatasetOptions(self)
        DetectionStageQComboBox.addDetectionStageOptions(self)
        GPUQComboBox.updateGPUOptions(self)

        # self.method_comboBox.currentIndexChanged.connect(lambda: SetupPage.showDetectionStageFrame(self))
        self.dataset_comboBox.currentIndexChanged.connect(lambda: SetupPage.showDatasetFrame(self))
        
        self.detection_stage_comboBox.currentIndexChanged.connect(lambda: ModelQComboBox.updateModelOptions(self))
        
        
        self.open_file_pushButton.clicked.connect(lambda: OpenFileQPushButton.openFile(self))


    @staticmethod
    def showDetectionStageFrame(self):
        if (self.method_comboBox.currentIndex() == 1):
            self.detection_stage_frame.setHidden(False)
        else:
            self.detection_stage_frame.setHidden(True)

    @staticmethod
    def showDatasetFrame(self):     
        if (self.dataset_comboBox.currentIndex() == 1):
            self.custom_dataset_frame.setEnabled(True)
            self.custom_dataset_frame.setHidden(False)
            self.default_dataset_frame.setEnabled(False)
            self.default_dataset_frame.setHidden(True)
        else:
            self.custom_dataset_frame.setEnabled(False)
            self.custom_dataset_frame.setHidden(True)
            self.default_dataset_frame.setEnabled(True)
            self.default_dataset_frame.setHidden(False)

