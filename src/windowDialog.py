from PyQt6.QtWidgets import (QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLabel, QGridLayout, 
 QTextEdit, QLineEdit, QFormLayout, QDialog, QDialogButtonBox, QSpinBox)

class AddPointDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Adicionar Ponto")
        
        self.layout = QVBoxLayout()
        self.form_layout = QFormLayout()
        self.layout.addLayout(self.form_layout)
        self.setLayout(self.layout)
        
        # Campos para coordenadas X e Y
        self.x_spinbox = QSpinBox()
        self.x_spinbox.setRange(0, 10000)  # Ajuste o intervalo conforme necessário
        self.x_spinbox.setValue(0)  # Valor inicial
        self.x_spinbox.lineEdit().setReadOnly(True) 

        self.y_spinbox = QSpinBox()
        self.y_spinbox.setRange(0, 10000)  # Ajuste o intervalo conforme necessário
        self.y_spinbox.setValue(0)  # Valor inicial
        self.y_spinbox.lineEdit().setReadOnly(True) # Ocultar o editor de texto do QSpinBox

        x_label = QLabel("Ponto x:")
        y_label = QLabel("Ponto y:")
        
        container_widget = QWidget()
        container_layout = QHBoxLayout()
        
        container_layout.addWidget(x_label)
        container_layout.addWidget(self.x_spinbox)
        
        container_layout.addWidget(y_label)
        container_layout.addWidget(self.y_spinbox)

        self.form_layout.addRow(container_widget)
        container_widget.setLayout(container_layout)

        # Botões de aceitar e cancelarcls
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        self.layout.addWidget(button_box)
        self.setLayout(self.layout)

    def get_coordinates(self):
        # Obtenha os valores dos QSpinBox diretamente
        x = self.x_spinbox.value()
        y = self.y_spinbox.value()
        return x, y
    
class AddLineDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Adicionar Linha")
        
        self.layout = QVBoxLayout()
        self.form_layout = QFormLayout()
        self.layout.addLayout(self.form_layout)
        self.setLayout(self.layout)

        # Campos para coordenadas x1, y1, x2, y2
        self.x1_spinbox = QSpinBox()
        self.x1_spinbox.setRange(0, 10000)  # Ajuste o intervalo conforme necessário
        self.x1_spinbox.setValue(0)  # Valor inicial
        self.x1_spinbox.lineEdit().setReadOnly(True)  # Ocultar o editor de texto do QSpinBox

        self.y1_spinbox = QSpinBox()
        self.y1_spinbox.setRange(0, 10000)  # Ajuste o intervalo conforme necessário
        self.y1_spinbox.setValue(0)  # Valor inicial
        self.y1_spinbox.lineEdit().setReadOnly(True)  # Ocultar o editor de texto do QSpinBox

        self.x2_spinbox = QSpinBox()
        self.x2_spinbox.setRange(0, 10000)  # Ajuste o intervalo conforme necessário
        self.x2_spinbox.setValue(0)  # Valor inicial
        self.x2_spinbox.lineEdit().setReadOnly(True)  # Ocultar o editor de texto do QSpinBox

        self.y2_spinbox = QSpinBox()
        self.y2_spinbox.setRange(0, 10000)  # Ajuste o intervalo conforme necessário
        self.y2_spinbox.setValue(0)  # Valor inicial
        self.y2_spinbox.lineEdit().setReadOnly(True)  # Ocultar o editor de texto do QSpinBox

        x1_label = QLabel("Ponto x1:")
        y1_label = QLabel("Ponto y1:")
        
        x2_label = QLabel("Ponto x2:")
        y2_label = QLabel("Ponto y2:")
        
        container_widget = QWidget()
        container_layout = QHBoxLayout()
        
        container_layout.addWidget(x1_label)
        container_layout.addWidget(self.x1_spinbox)
        
        container_layout.addWidget(y1_label)
        container_layout.addWidget(self.y1_spinbox)

        container_layout.addWidget(x2_label)
        container_layout.addWidget(self.x2_spinbox)
 
        container_layout.addWidget(y2_label)
        container_layout.addWidget(self.y2_spinbox)
        
        self.form_layout.addRow(container_widget)
        container_widget.setLayout(container_layout)

        # Botões de aceitar e cancelar
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        self.layout.addWidget(button_box)


    def get_coordinates(self):
        # Obtenha os valores dos QSpinBox diretamente
        x1 = self.x1_spinbox.value()
        y1 = self.y1_spinbox.value()
        x2 = self.x2_spinbox.value()
        y2 = self.y2_spinbox.value()
        return x1, y1, x2, y2

class AddPolygonDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Adicionar Polígono")

        self.layout = QVBoxLayout()
        self.form_layout = QFormLayout()
        self.layout.addLayout(self.form_layout)
        self.setLayout(self.layout)

        # Lista para armazenar os widgets e suas labels associadas
        self.coordinate_widgets = []

        # Adicionar campos para coordenadas (x, y) dos pontos
        self.add_button = QPushButton("Adicionar Coordenada")
        self.add_button.clicked.connect(self.add_coordinate)
        self.layout.addWidget(self.add_button)

        self.remove_button = QPushButton("Remover Coordenada")
        self.remove_button.clicked.connect(self.remove_coordinate)
        self.layout.addWidget(self.remove_button)
        self.remove_button.setEnabled(False)

        # Adiciona inicialmente 3 pares de coordenadas
        for _ in range(3):
            self.add_coordinate()

        # Botões de aceitar e cancelar
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        self.layout.addWidget(button_box)

    def add_coordinate(self):
        x_spinbox = QSpinBox()
        x_spinbox.setRange(0, 10000)  # Ajuste o intervalo conforme necessário
        x_spinbox.setValue(0)  # Valor inicial
        x_spinbox.lineEdit().setReadOnly(True)  # Ocultar o editor de texto do QSpinBox

        y_spinbox = QSpinBox()
        y_spinbox.setRange(0, 10000)  # Ajuste o intervalo conforme necessário
        y_spinbox.setValue(0)  # Valor inicial
        y_spinbox.lineEdit().setReadOnly(True)  # Ocultar o editor de texto do QSpinBox

        row_index = len(self.coordinate_widgets) + 1
        x_label = QLabel(f"Ponto {row_index} X:")
        y_label = QLabel(f"Ponto {row_index} Y:")

        # Container para manter a label e o spinbox juntos
        container_widget = QWidget()
        container_layout = QHBoxLayout()
        container_layout.addWidget(x_label)
        container_layout.addWidget(x_spinbox)
        container_layout.addWidget(y_label)
        container_layout.addWidget(y_spinbox)
        container_widget.setLayout(container_layout)

        self.form_layout.addRow(container_widget)

        # Adicionar o container na lista de widgets
        self.coordinate_widgets.append(container_widget)

        # Habilita o botão de remover se houver mais de 3 coordenadas
        if len(self.coordinate_widgets) > 3:
            self.remove_button.setEnabled(True)

    def remove_coordinate(self):
        if len(self.coordinate_widgets) > 3:
            # Remove o último container de coordenada
            widget_to_remove = self.coordinate_widgets.pop()

            # Remove o widget do layout
            self.form_layout.removeWidget(widget_to_remove)

            # Delete o widget e todos os seus filhos
            widget_to_remove.deleteLater()

            # Desabilita o botão de remover se restarem apenas 3 coordenadas
            if len(self.coordinate_widgets) <= 3:
                self.remove_button.setEnabled(False)
            
            # Atualiza o layout e ajusta o tamanho da janela
            self.form_layout.update()
            self.adjustSize()
            self.updateGeometry()
            
            # Atualiza o layout do widget principal
            self.layout.update()
            self.resize(self.sizeHint())  # Ajusta o tamanho da janela ao tamanho sugerido


    def get_coordinates(self):
        coordinates = []
        for widget in self.coordinate_widgets:
            items = widget.findChildren(QSpinBox)
            if len(items) == 2:
                x_spinbox, y_spinbox = items
                x = x_spinbox.value()
                y = y_spinbox.value()
                coordinates.append((x, y))
        return coordinates