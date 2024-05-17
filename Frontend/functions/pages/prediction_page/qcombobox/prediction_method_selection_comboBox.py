import os
import yaml


class PredictionMethodQComboBox:
    def __init__(self) -> None:
        pass

    def addMethodOptions(self):
        self.prediction_model_selection_comboBox.clear()
        if os.path.exists(os.path.join(self.project_path, "runs", "detect", "train")):
            self.prediction_model_selection_comboBox.addItems([PredictionMethodQComboBox.get_model_name(os.path.join(self.project_path, "runs", "detect", "train"))])
            
        if os.path.exists(os.path.join(self.project_path, "runs", "classify", "train")):
            self.prediction_model_selection_comboBox.addItems([PredictionMethodQComboBox.get_model_name(os.path.join(self.project_path, "runs", "classify", "train"))])

    @staticmethod
    def get_model_name(file_path):
        yaml_file_path = os.path.join(file_path, "args.yaml")
        with open(yaml_file_path, 'r') as file:
            data = yaml.safe_load(file)
        
        if data is not None and 'model' in data:
            model = data['model']
            return model