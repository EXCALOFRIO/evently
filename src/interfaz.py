import sys
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QInputDialog, QFileDialog
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5.uic import loadUi

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        loadUi('evently.ui', self)
        
        self.pushButton_Menu.clicked.connect(self.mover_Menu)
        
        #self.pushButton_Minimizar.hide()
        #self.pushButton_Mapa.clicked.connect(self.)
        #self.pushButton_Filtrado.connect(self.)
        #self.pushButton_Dispositivos.connect(self.)
        #self.pushButton_Fiesta.connect(self.)
        #self.pushButton_Resenna.connect(self.)
        """CONTROL BARRA TÍTULOS"""
        self.pushButton_Aumetar.clicked.connect(self.control_pushButton_Aumentar)
        self.pushButton_Cerrar.clicked.connect(lambda: self.close())
        self.pushButton_Minimizar.clicked.connect(self.control_pushButton_Minimizar)
        
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowOpacity(1)
        
        
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)
        
        """MOVER VENTANA"""
        self.frame_superior.mouseMoveEvent = self.mover_ventana
        
        """CONEXION BOTONES"""
        self.pushButton_Mapa.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(self.page_mapa))
        self.pushButton_Filtrado.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(self.page_filtrado))
        self.pushButton_AddDiscoteca.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(self.page_AddDiscoteca))
        self.pushButton_Fiesta.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(self.page_AddFiesta))
        self.pushButton_AddResenna.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(self.page_AddResenna))
        
        def control_pushButton_Minimizar(self):
            self.showMinimized()
        
        def control_pushButton_Aumentar(self):
            self.showMaximized()
            self.pushButton_Aumentar.hide()
            self.pushButton_Minimizar.show()
        
        def resizeEvent(self, event):
            rect = self.rect()
            self.grip.move(rect.right() - self.gripSize, rect.bottom() - self.gripSize)
            
        def mousePressEvent(self, event):
            self.click_position = event.globalPos()
        
        def mover_ventana(self, event):
            if self.isMaximized() == False:
                if event.buttons() == QtCore.Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.click_position)
                    self.click_position = event.globalPos()
                    event.accept()
            if event.globalPos().y <= 10:
                self.showMaximized()
                self.pushButton_Aumentar.hide()
                self.pushButton_Minimizar.show()
            else:
                self.showNormal()
                self.pushButton_Aumentar.show()
                self.pushButton_Minimizar.hide()
        
        def mover_menu(self):
            if True:
                width = self.frame_menu.width()
                normal = 0
                if width == 0:
                    extender = 200
                else:
                    extender = normal
                self.animacion = QPropertyAnimation(self.frame_menu, b"minimumWidth")
                self.animacion.setDuration(300)
                self.animacion.setStartValue(width)
                self.animacion.setEndValue(extender)
                self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
                self.animacion.start()
                
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mi_app = VentanaPrincipal()
    mi_app.show()
    sys.exit(app.exec_())