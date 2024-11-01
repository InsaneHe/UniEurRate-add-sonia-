from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QSizePolicy
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

class AboutDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About")
        self.setWindowIcon(QIcon('icon.png'))
        self.setGeometry(200, 200, 400, 200)  # Set dialog position and size
        self.setStyleSheet("background-color: #CBCBCB; font-weight: bold;")  # Set background color of dialog

        # Dialog layout
        dialog_layout = QVBoxLayout(self)

        # Title label
        title_label = QLabel("", self)
        title_label.setStyleSheet("color: black; font-size: 20px; padding: 10px;border: 1px solid; border-color:black; font-weight: bold;")
        dialog_layout.addWidget(title_label)

        # Version label
        version_label = QLabel("Version 1.0", self)
        version_label.setStyleSheet("color: black; font-size: 18px; padding: 10px;border: 1px solid; border-color:black; font-weight: bold;")
        dialog_layout.addWidget(version_label)

        # Created by label
        created_by_label = QLabel("Functions: Get Sonia | Tonar | Euribor", self)
        created_by_label.setStyleSheet("color: black; font-size: 18px; padding: 10px;border: 1px solid; border-color:black; font-weight: bold;")
        dialog_layout.addWidget(created_by_label)

        # Close button
        close_button = QPushButton("Close", self)
        close_button.setStyleSheet("QPushButton {" "background-color: #7289da; ""color: #fff; ""font-weight: bold; ""font-size: 18px; ""}""QPushButton:hover {" "background-color: #4e6eff; ""}")
        close_button.clicked.connect(self.close)
        dialog_layout.addWidget(close_button)
