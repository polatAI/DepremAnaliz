import sys
import threading
from PyQt6.QtWidgets import QApplication
from gui import MainWindow 
from app import EarthquakeApp  

def start_flask():
    """Flask sunucusunu ayrı bir thread'de çalıştır"""
    earthquake_app = EarthquakeApp()
    
    # Flask sunucusunun çalıştırılması
    from app import app
    app.run(debug=False, use_reloader=False)  

def main():

    flask_thread = threading.Thread(target=start_flask)
    flask_thread.daemon = True
    flask_thread.start()

    # GUI'yi başlatıyoruz
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec()) 

if __name__ == "__main__":
    main()
