from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Deprem Uygulaması")
        self.setGeometry(100, 100, 1024, 768)

        # WebEngineView
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://127.0.0.1:5000/"))  # Flask uygulamanızın adresi

        layout = QVBoxLayout()
        layout.addWidget(self.browser)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Temayı siyah yapmak için stil ayarları
        self.setStyleSheet("""
            QMainWindow {
                background-color: #121212;
            }
            QWebEngineView {
                background-color: #121212;
                color: white;
            }
            QWidget {
                background-color: #121212;
                color: white;
            }
        """)

# Main method to run the application
def run_gui():
    # QApplication ile doğru başlatma
    app = QApplication(sys.argv)

    # Create and show the main window
    window = MainWindow()
    window.show()

    # Start the application event loop
    sys.exit(app.exec())  # QApplication'ın event loop'u burada başlatılıyor
