from enum import Enum
class ModelQComboBox:
    def updateModelOptions(self):
        selected_method = self.method_comboBox.currentText()
        selected_stage = self.detection_stage_comboBox.currentText()
        self.model_comboBox.clear()
        if selected_method == "Detection" and selected_stage == "One-Stage":
            self.model_comboBox.addItems([u"YOLOv3", u"YOLOv5", u"YOLOv6", u"YOLOv8", u"YOLOv9"])
            
        elif selected_method == "Detection" and selected_stage == "Two-Stage":
            self.model_comboBox.addItems([u"Faster R-CNN", u"Mask R-CNN"])
            
        else:
            self.model_comboBox.addItems([u"AlexNet", "YOLOv8"])
         
class detection_models(Enum):
    YOLOv8 = 0
    FASTER_R_CNN = 1

class classification_models(Enum):
    ALEXNET = 0
# Path: Frontend/functions/body/pages/setup_page/qcombobox/backbone_qcombobox.py   
            
