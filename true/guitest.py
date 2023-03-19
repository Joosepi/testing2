import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QMessageBox

class ColorTrackerGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        # set up the GUI
        self.setWindowTitle("Color Tracker")

        self.start_button = QPushButton("Start", self)
        self.start_button.clicked.connect(self.start_tracking)

        self.color_label = QLabel(self)
        self.color_label.setAlignment(Qt.AlignCenter)
        self.color_label.setStyleSheet("background-color: black; color: white; font-size: 24px;")

        layout = QVBoxLayout()
        layout.addWidget(self.start_button)
        layout.addWidget(self.color_label)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # set up the "Yes" button to start color tracking
        self.yes_button = QPushButton("Yes", self)
        self.yes_button.setGeometry(150, 150, 100, 50)
        self.yes_button.clicked.connect(self.start_tracking)

    def start_tracking(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = ColorTrackerGUI()
    gui.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    gui = ColorTrackerGUI()
    gui.run()
