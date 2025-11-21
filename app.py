import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QLabel,
    QVBoxLayout, 
    QWidget
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cleaning EEG App")
        self.setGeometry(100, 100, 400, 200)

        # Creating Qlabel for the title
        self.title_label = QLabel("Choose the Participant")
        # centering the text inside the QLabel itself
        self.title_label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        # just styles for the label
        self.title_label.setStyleSheet("font-size: 24px; font-weight: bold;")

        central_widget = QWidget()
        main_layout = QVBoxLayout()

        main_layout.addWidget(self.title_label, alignment = Qt.AlignTop | Qt.AlignHCenter)

        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)


    
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
