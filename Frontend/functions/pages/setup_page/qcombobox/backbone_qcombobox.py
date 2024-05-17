class BackBoneQComboBox:
    def __init__(self) -> None:
        self.x = 2
        
    def updateBackboneOptions(self):
        selected_method = self.method_comboBox.currentText()
        if selected_method == "Detection":
            self.backbone_comboBox.clear()
            self.backbone_comboBox.addItems([u"DarkNet"])
        else:
            self.backbone_comboBox.clear()
            self.backbone_comboBox.addItems([u"ResNet50"])