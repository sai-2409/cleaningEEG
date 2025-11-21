import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QLabel,
    QVBoxLayout, 
    QWidget,
    QPushButton,
    QFileDialog,
)
from cleaning import cleaning

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cleaning EEG App")
        self.setGeometry(500, 200, 400, 400) ### x, y, width and height, settings for the window's initial size and position

        # Creating Qlabel for the title
        self.title_label = QLabel("Choose a Participant")
        # centering the text inside the QLabel itself
        self.title_label.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        # just styles for the label
        self.title_label.setStyleSheet("font-size: 24px; font-weight: bold;")

        central_widget = QWidget()
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        main_layout.addWidget(self.title_label, alignment = Qt.AlignTop | Qt.AlignHCenter)

        # creating "choose a file" button
        self.chooseBtn = QPushButton("Choose File")
        self.chooseBtn.setCursor(Qt.PointingHandCursor)
        self.chooseBtn.setMinimumSize(180, 50)
        self.chooseBtn.setMaximumWidth(260)

        self.pathLabel = QLabel("No file selected yet")
        self.pathLabel.setAlignment(Qt.AlignCenter)
        self.pathLabel.setWordWrap(True)

        # add button and label to layout
        main_layout.addWidget(self.chooseBtn, alignment=Qt.AlignHCenter)
        main_layout.addWidget(self.pathLabel)
        self.pathLabel.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

        # creating button for exitting
        self.exitButton = QPushButton("Exit")
        self.exitButton.setCursor(Qt.PointingHandCursor)
        self.exitButton.setMinimumSize(180, 50)
        self.chooseBtn.setMaximumWidth(260)

        main_layout.addWidget(self.exitButton, alignment=Qt.AlignHCenter)

        # closing the window when button clicked
        self.exitButton.clicked.connect(QApplication.instance().quit)

        # connecting our button to the function
        self.chooseBtn.clicked.connect(self.openFileDialog)

    def openFileDialog(self):
        filePath, _ = QFileDialog.getOpenFileName(
            self,
            "Select a file",
            "", # to start in the default folder
            "All files (*);;EEG Files (*.edf)"
        )
        if filePath: 
            self.pathLabel.setText(f"Selected: \n{filePath}")
            print("User selected:", filePath)
            self.setGeometry(100, 200, 1000, 800)

            # self.chooseBtn.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
            # self.pathLabel.setAlignment(Qt.AlignTop | Qt.AlignHCenter)

            # running the cleaning function here
            cleaning(filePath)

        else:
            self.pathLabel.setText("No file selected")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
