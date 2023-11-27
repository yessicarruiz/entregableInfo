import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QFileDialog, QMainWindow, QSlider
from PyQt5.QtGui import QPixmap, QImage
import os
import pydicom
from PIL import Image
from PyQt5.QtCore import Qt

class ventanaLoguearse(QWidget):
    def __init__(self, login_model, lectorDicom, login_controller):
        super().__init__()

        self.login_model = login_model
        self.lectorDicom = lectorDicom
        self.login_controller = login_controller

        self.setWindowTitle("Iniciar Sesin")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.ventana_usuario = QLabel("Usuario:")
        self.entradaUsuario = QLineEdit()

        self.contraseñaUsuario = QLabel("Contraseña:")
        self.entradaContraseña = QLineEdit()
        self.entradaContraseña.setEchoMode(QLineEdit.contraseña)

        self.botonLoguearse = QPushButton("Iniciar Sesión")
        self.botonLoguearse.clicked.connect(self.login_controller.login)

        layout.addWidget(self.ventana_usuario)
        layout.addWidget(self.entradaUsuario)
        layout.addWidget(self.password_label)
        layout.addWidget(self.entradaContraseña)
        layout.addWidget(self.botonLoguearse)

        self.setLayout(layout)


class vistaDicom(QWidget):
    def __init__(self, lectorDicom, controlDi):
        super().__init__()

        self.lectorDicom = lectorDicom
        self.controlDi = controlDi

        self.setWindowTitle("Dicom Viewer")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout(self)

        self.imagenVentana = QLabel(self)
        self.imagenVentana.setAlignment(Qt.AlignCenter)

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.valueChanged.connect(self.controlDi.mostrarImagen)

        layout.addWidget(self.imagenVentana)
        layout.addWidget(self.slider)

        self.controlError = QLabel(self)
        layout.addWidget(self.controlError)

    def set_error_message(self, message):
        self.controlError.setText(message)

