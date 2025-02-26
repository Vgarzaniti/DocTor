from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel
from db.database import get_db  # Importar la función get_db desde el archivo database.py
from modelos.models import ObraSocial, Paciente  # Importar los modelos definidos

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplicación de Gestión de Pacientes")

        # Crear la interfaz gráfica
        self.init_ui()

    def init_ui(self):
        # Crear un widget y un layout
        widget = QWidget(self)
        layout = QVBoxLayout(widget)

        # Etiqueta de bienvenida
        self.label = QLabel("Conexión con la base de datos establecida.", self)
        layout.addWidget(self.label)


        # Configurar el layout y el widget
        self.setCentralWidget(widget)

    def load_patient_data(self):
        # Obtener la sesión de la base de datos
        db_session = next(get_db())  # Llama a la función get_db para obtener una sesión

        db_session.close()

# Iniciar la aplicación
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
