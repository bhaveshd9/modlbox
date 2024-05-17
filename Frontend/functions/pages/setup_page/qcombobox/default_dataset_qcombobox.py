from enum import Enum

class DefaultDatasetQComboBox:
    def updateDefaultDatasetOptions(self):
        selected_method = self.method_comboBox.currentText()
        
        selected_model = self.model_comboBox.currentText()
        selected_model_index = self.model_comboBox.currentIndex()
        self.default_dataset_comboBox.clear()
        default_detection_datasets = ["COCO8", "DOTA8", "VOC", "GlobalWheat2020",  "VisDrone"]
        default_classification_datasets = ["Flowers102", "Country211", "ImageNet10", "ImageWoof320"]
        if selected_method == "Detection" and selected_model in ["YOLOv3", "YOLOv4", "YOLOv5", "YOLOv6", "YOLOv7", "YOLOv9"]:
            # COCO8 - 1MB; DOTA8 - 1.5MB; VOC - 2.8 GB; GlobalWheat - 7.5 GB; Argoverse - 31.5 GB; LVIS - 20.1 GB
            #SKIP DOTA8 IF NOT YOLOV8
            self.default_dataset_comboBox.addItems(filter(lambda x: x != default_detection_datasets[1], default_detection_datasets))
        elif selected_method == "Detection" and selected_model in ["YOLOv8"]:
            self.default_dataset_comboBox.clear()
            self.default_dataset_comboBox.addItems(default_detection_datasets)
                        
        elif selected_method == "Classification":
            if selected_model == "AlexNet":
                self.default_dataset_comboBox.clear()
                self.default_dataset_comboBox.addItems([u"Flowers102", u"Country211"])
            elif selected_model == "YOLOv8":
                self.default_dataset_comboBox.clear()
                self.default_dataset_comboBox.addItems(default_classification_datasets[2:])

class detection_datasets(Enum):
    COCO8 = 0
    DOTA8 = 1

class classification_datasets(Enum):
    FLOWERS102 = 0
    COUNTRY211 = 1
