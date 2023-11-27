import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QFileDialog, QMainWindow, QSlider
from PyQt5.QtGui import QPixmap, QImage
import os
import pydicom
from PIL import Image
from PyQt5.QtCore import Qt


class UsuarioLoguin:
    def __init__(self):
        self.ValidarUsuario = {"usuario": "contrasena"}

    def verificaciones(self, usuario, contraseña):
        return usuario in self.ValidarUsuario and self.ValidarUsuario[usuario] == contraseña



class lectorDicom:
    def __init__(self):
        self.imagenCargada = ""
        self.archivo = []
        self.imagenIndex = 0

    def load_images(self):
        self.archivo = [f for f in os.listdir(self.imagenCargada) if f.lower().endswith(".dcm")]
        self.archivo.sort()


