import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

app=QApplication(sys.argv)
ventana=QMainWindow()
ventana.setWindowTitle("Ventana Cooperativa")
#ventana.setFixedSize(400, 200)
ventana.resize(500, 200)
ventana.show()
sys.exit(app.exit())