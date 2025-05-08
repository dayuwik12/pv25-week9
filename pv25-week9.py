import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QMainWindow,
    QAction, QFileDialog, QFontDialog, QTabWidget, QInputDialog
)
from PyQt5.QtGui import QFont

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Week 9 - QDialog, QTabWidget & MenuBar")
        self.setGeometry(600, 250, 800, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        main_layout = QVBoxLayout(self.central_widget)
        self.tabs = QTabWidget()

        # Variabel shared
        self.name = ""

        # Dua label terpisah untuk tab input nama dan tab pilih font
        self.name_label_input = QLabel("Nama: ")
        self.name_label_font = QLabel("Nama: ")

        # Tabs
        self.tabs.addTab(self.createInputTab(), "Input Nama")
        self.tabs.addTab(self.createFontTab(), "Pilih Font")
        self.tabs.addTab(self.createFileTab(), "Buka File")

        main_layout.addWidget(self.tabs)

        # Menu bar
        self.createMenuBar()

    # Menu bar untuk fitur input nama, pilih font, dan buka file
    def createMenuBar(self):
        menubar = self.menuBar()

        file_menu = menubar.addMenu("File")
        exit_action = QAction("Keluar", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        fitur_menu = menubar.addMenu("Fitur")

        input_action = QAction("Input Nama", self)
        input_action.triggered.connect(self.inputName)
        fitur_menu.addAction(input_action)

        font_action = QAction("Pilih Font", self)
        font_action.triggered.connect(self.chooseFont)
        fitur_menu.addAction(font_action)

        file_action = QAction("Buka File", self)
        file_action.triggered.connect(self.openFile)
        fitur_menu.addAction(file_action)

    # Tab input nama
    def createInputTab(self):
        tab = QWidget()
        layout = QVBoxLayout()

        input_button = QPushButton("Input Nama")
        input_button.clicked.connect(self.inputName)
        layout.addWidget(input_button)

        layout.addWidget(self.name_label_input)

        tab.setLayout(layout)
        return tab

    # Tab pilih font
    def createFontTab(self):
        tab = QWidget()
        layout = QVBoxLayout()

        font_button = QPushButton("Pilih Font")
        font_button.clicked.connect(self.chooseFont)
        layout.addWidget(font_button)

        layout.addWidget(self.name_label_font)

        tab.setLayout(layout)
        return tab

    # Tab buka file
    def createFileTab(self):
        tab = QWidget()
        layout = QVBoxLayout()

        file_button = QPushButton("Buka File")
        file_button.clicked.connect(self.openFile)
        layout.addWidget(file_button)

        self.file_content_label = QLabel("", self)
        self.file_content_label.setWordWrap(True)
        layout.addWidget(self.file_content_label)

        tab.setLayout(layout)
        return tab

    # Menggunakan QInputDialog untuk input nama
    def inputName(self):
        text, ok = QInputDialog.getText(self, "Input Nama", "Masukkan Nama:")
        if ok and text:
            self.name = text
            self.name_label_input.setText(f"Nama: {self.name}")
            self.name_label_font.setText(f"Nama: {self.name}")

    # Menggunakan QFontDialog untuk memilih font
    def chooseFont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.name_label_input.setFont(font)
            self.name_label_font.setFont(font)

    # Menggunakan QFileDialog untuk membuka file
    def openFile(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Buka File", "", "Text Files (*.txt);;All Files (*)")
        if file_path:
            with open(file_path, "r") as f:
                content = f.read()
                self.file_content_label.setText(content)

# Main function
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
