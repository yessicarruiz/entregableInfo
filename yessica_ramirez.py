import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QFileDialog, QMainWindow, QSlider
from PyQt5.QtGui import QPixmap, QImage
import os
import pydicom
from PIL import Image
from PyQt5.QtCore import Qt
from modelo import *
from vista import *


class ControlLoguin:
    def __init__(self, UsuarioLoguin, lectorDicom, ventanaLoguearse, vistaDicom):
        self.UsuarioLoguin = UsuarioLoguin
        self.lectorDicom= lectorDicom
        self.ventanaLoguearse = ventanaLoguearse
        self.vistaDicom = vistaDicom

        self.ventanaLoguearse.login_controller = self

    def login(self):
        usuario = self.ventanaLoguearse.entradaUsuario.text()
        contraseña = self.ventanaLoguearse.entradaContraseña.text()

        if self.UsuarioLoguin.verificaciones(usuario, contraseña):
            self.ventanaLoguearse.hide()
            self.lectorDicom.imagenCargada = self.seleccionarr()
            self.lectorDicom.cargarImagenes()
            self.vistaDicom.show()
        else:
            QMessageBox.warning(self.ventanaLoguearse, "Errorn", "Contraseña incorrectas")

    def seleccionarr(self):
        folder = QFileDialog.getExistingDirectory(self.ventanaLoguearse, "Seleccionar Carpeta")
        return folder

class controlDi:
    def __init__(self, lectorDicom, vistaDicom):
        self.lectorDicom = lectorDicom
        self.vistaDicom = vistaDicom

        self.vistaDicom.controlDi = self

    def seleccionarr(self):
        folder = QFileDialog.getExistingDirectory(self.vistaDicom, "Seleccionar Carpeta")
        return folder

    def cargarImagenes(self):
        try:
            self.lectorDicom.imagenCargada = self.seleccionarr()
            self.lectorDicom.cargarImagenes()
            self.vistaDicom.slider.setRange(0, len(self.lectorDicom.archivo) - 1)
            self.vistaDicom.mostrarImagen(1)
            self.vistaDicom.set_error_message("")
        except Exception as e:
            self.vistaDicom.set_error_message("Error")

    def mostrarImagen(self, index):
        try:
            self.lectorDicom.imagenIndex = index
            imagenPath = os.path.join(self.lectorDicom.imagenCargada,
                                      self.lectorDicom.archivo[self.lectorDicom.imagenIndex_index])
            dicom_data = pydicom.dcmread(imagenPath)

            pixel_array = dicom_data.pixel_array
            image = Image.fromarray(pixel_array)
            image = image.scaledToWidth(600)
            imagenQ = QImage(image.tobytes(), image.width, image.height, image.width * 3, QImage.Format_gray)
            pixmap = QPixmap.fromImage(imagenQ)

            self.vistaDicom.imagenVentana.setPixmap(pixmap)
            self.vistaDicom.set_error_message("erro")
        except Exception as e:
            self.vistaDicom.set_error_message("Error")
class DicomApp:
    def __init__(self):
        self.lectorDicom = lectorDicom
        self.vistaDicom = vistaDicom(self.lectorDicom, None)
        self.controlDi = controlDi(self.lectorDicom, self.vistaDicom)
        self.vistaDicom.controlDi = self.controlDi

        self.vistaDicom.show()
        self.controlDi.cargarImagenes()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dicom_app = DicomApp()
    ventanaLoguearse = ventanaLoguearse(UsuarioLoguin, lectorDicom, None)
    vistaDicom = vistaDicom(lectorDicom, None)
    login_controller = ControlLoguin(UsuarioLoguin, lectorDicom, ventanaLoguearse, vistaDicom)
    dicom_controller = controlDi(lectorDicom, vistaDicom)


    ventanaLoguearse.show()

    sys.exit(app.exec_())