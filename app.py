import requests
from bs4 import BeautifulSoup
import json
import folium
from flask import Flask, render_template
import threading
import time

class EarthquakeApp:
    def __init__(self):
        self.earthquake_data = []
        self.load_data()

    def load_data(self):
        """Veriyi Kandilli Rasathanesi'nden çek ve JSON dosyasına kaydet"""
        url = "http://www.koeri.boun.edu.tr/scripts/lst9.asp"
        response = requests.get(url)
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.content, "html.parser")
        pre_tag = soup.find("pre")
        if pre_tag is None:
            raise ValueError("PRE etiketi bulunamadı!")

        pre_text = pre_tag.get_text()
        deprem_listesi = []
        satirlar = pre_text.split("\n")
        
        for satir in satirlar:
            if satir.strip() == "":
                continue
            if satir.startswith("202"):  # Deprem verileri 2024.04.26 gibi başlıyor
                try:
                    parts = satir.split()
                    if len(parts) < 8:
                        continue

                    tarih = parts[0]
                    saat = parts[1]
                    enlem = float(parts[2])
                    boylam = float(parts[3])
                    derinlik = float(parts[4])
                    try:
                        ml = float(parts[6]) if parts[6] != "-.-" else 0.0
                    except ValueError:
                        ml = 0.0

                    yer = " ".join(parts[8:])

                    deprem = {
                        "Tarih": tarih,
                        "Saat": saat,
                        "Enlem": enlem,
                        "Boylam": boylam,
                        "Derinlik(km)": derinlik,
                        "ML": ml,
                        "Yer": yer
                    }
                    deprem_listesi.append(deprem)
                except Exception as e:
                    print(f"Hata oluştu: {e}")
                    print(f"Problemli satır: {satir}")

        self.earthquake_data = deprem_listesi
        with open("data/depremler.json", "w", encoding="utf-8") as f:
            json.dump(deprem_listesi, f, ensure_ascii=False, indent=4)
        print(f"{len(deprem_listesi)} adet deprem verisi depremler.json dosyasına kaydedildi.")

    def get_color_by_magnitude(self, magnitude):
        try:
            magnitude = float(magnitude)
        except:
            magnitude = 0.0
        if magnitude < 3.0:
            return "green"
        elif magnitude < 5.0:
            return "yellow"
        elif magnitude < 7.0:
            return "orange"
        else:
            return "red"

    def create_map(self):
        m = folium.Map(location=[39.0, 35.0], zoom_start=6, tiles="CartoDB dark_matter")
        
        for eq in self.earthquake_data:
            magnitude = eq.get("ML", "0")
            color = self.get_color_by_magnitude(magnitude)

            popup_html = f"""
            <div style="font-size: 12px; width: 200px; padding: 5px;">
                <b>Yer:</b> {eq.get('Yer', 'Bilinmiyor')}<br>
                <b>Büyüklük (ML):</b> {eq.get('ML', '0')}<br>
                <b>Enlem:</b> {eq.get('Enlem', 0)}<br>
                <b>Boylam:</b> {eq.get('Boylam', 0)}<br>
            </div>
            """
            
            icon_html = f"""
            <div class="pulse-marker" style="width: 10px; height: 10px; background-color: {color};"></div>
            """
            icon = folium.DivIcon(html=icon_html)
            
            folium.Marker(
                location=[eq.get("Enlem", 0), eq.get("Boylam", 0)],
                popup=folium.Popup(popup_html, max_width=250),
                icon=icon
            ).add_to(m)
        
        return m.get_root().render()

# Flask App Setup
app = Flask(__name__)
earthquake_app = EarthquakeApp()

@app.route("/")
def index():
    map_html = earthquake_app.create_map()
    return render_template("index.html", map_html=map_html)

def update_earthquake_data():
    """5 dakikada bir veriyi güncelle"""
    while True:
        earthquake_app.load_data()  # Veriyi günceller
        time.sleep(300)  # 5 dakika bekler
        print("Veriler Güncellendi")

if __name__ == "__main__":
    # Güncellemeyi ayrı bir thread'de çalıştır
    update_thread = threading.Thread(target=update_earthquake_data)
    update_thread.daemon = True
    update_thread.start()

    app.run(debug=True)
