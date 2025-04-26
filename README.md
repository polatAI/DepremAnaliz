Tabii, **katkıda bulunma** kısmını kaldırarak ve görsel kısmına bir URL ekleyerek güncellenmiş **`README.md`** dosyasını aşağıda bulabilirsiniz:

```markdown
# Deprem Uygulaması

Bu proje, **Kandilli Rasathanesi ve Deprem Araştırma Enstitüsü**'nden alınan verileri kullanarak, depremleri gerçek zamanlı olarak takip etmeyi amaçlayan bir **Web ve Masaüstü Uygulaması**'dır. Kullanıcılar, depremler hakkında anlık bilgi alabilir ve görselleştirmelerle daha detaylı analizler yapabilirler.

## İçerik

- **Web Uygulaması**: Flask kullanarak Kandilli Rasathanesi'nden alınan deprem verilerini sağlar.
- **Masaüstü Uygulaması**: PyQt6 ile geliştirilmiş modern bir GUI üzerinden deprem verilerini görüntüler.

## Proje Özellikleri

- **Gerçek zamanlı Deprem Takibi**: Kandilli Rasathanesi'nden alınan verilerle deprem verilerini anlık olarak takip etme.
- **Web Görselleştirmesi**: Flask backend'i kullanarak, depremlerin anlık verilerini web üzerinden görselleştirme.
- **PyQt6 GUI**: Masaüstü uygulaması üzerinden depremleri takip etme.
- **Kandilli Rasathanesi Verisi**: Gerçek verilerle yapılan analizler.

## Gereksinimler

Proje, aşağıdaki Python kütüphanelerine ihtiyaç duyar:

- **Flask**: Web uygulaması için.
- **PyQt6**: GUI oluşturmak için.
- **PyQtWebEngine**: Web içeriğini görüntülemek için.

## Kurulum

1. Python 3.x sürümünü yüklediğinizden emin olun.
2. Aşağıdaki komutları kullanarak gerekli bağımlılıkları yükleyin:

   ```bash
   pip install -r requirements.txt
   ```

   `requirements.txt` dosyasında aşağıdaki bağımlılıklar bulunmaktadır:
   - Flask
   - PyQt6
   - PyQtWebEngine
   - requests
   - beautifulsoup4
   - folium

3. Uygulamayı çalıştırmak için `main.py` dosyasını çalıştırın:

   ```bash
   python main.py
   ```

4. Web uygulamanızın çalıştığından emin olduktan sonra masaüstü uygulaması da açılacaktır.

## Kullanım

1. Web uygulamanızı `http://127.0.0.1:5000/` adresinde görebilirsiniz. Bu sayfa, Kandilli Rasathanesi'nden alınan deprem verilerini harita üzerinde gösterir.
2. Masaüstü uygulaması, deprem verilerini bir PyQt6 GUI üzerinden gösterir. Uygulama çalıştığında, web içeriğini bir web tarayıcısı gibi gösterir.

## Notlar

- Veriler, **Kandilli Rasathanesi ve Deprem Araştırma Enstitüsü**'nden alınmaktadır ve ticari amaçla kullanılmamaktadır.
- Eğer ticari amaçla kullanmayı planlıyorsanız, lütfen **Kandilli Rasathanesi'nden izin alınız**.

## Görsel

Aşağıdaki görsel, uygulamanın çalışma ekranını göstermektedir:

![Uygulama Görseli](https://i.hizliresim.com/1z0q41o.png?_gl=1*11wze0p*_ga*MjA3NDQ4NDM1MC4xNzQ1NzEwMzU5*_ga_M9ZRXYS2YN*MTc0NTcxMDM1OS4xLjEuMTc0NTcxMDM3OC40MS4wLjA.)
```

Burada **`https://i.hizliresim.com/1z0q41o.png?_gl=1*11wze0p*_ga*MjA3NDQ4NDM1MC4xNzQ1NzEwMzU5*_ga_M9ZRXYS2YN*MTc0NTcxMDM1OS4xLjEuMTc0NTcxMDM3OC40MS4wLjA.`** kısmına uygulamanızın veya projenizin görselini barındıran gerçek URL'yi koyabilirsiniz.