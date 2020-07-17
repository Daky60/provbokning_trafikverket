# provbokning_trafikverket
Ett skript som automatiskt söker efter förarprov och reserverar dem i 15 minuter.  
Ett ljud kommer spelas upp i ca 1 minut när en tid har hittats.

---

## VIKTIGT
Skriptet har endast testats vid ett fåtal bokningar, då främst för förarprov B.  

---

## Donationer
Fattig student osv. Bidra med en slant om du kan och vill. Det uppskattas:  
  
[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=H76THWVZQ7KA4)  

---

## Installation (Windows)

### 1. Ladda ner alla filer
1. Ladda ner alla filer här: [master.zip](https://github.com/Daky60/provbokning_trafikverket/archive/master.zip)  
2. Packa upp mappen och lägg den på skrivbordet

### 2. Installera ChromeDriver
1. Ladda ner: https://sites.google.com/a/chromium.org/chromedriver/downloads  
2. Installera samma version som du har på Google Chrome (Gå till chrome://settings/help i Chrome)  
3. Lägg chromedriver.exe i provbokning_trafikverket-master

### 3. Installera Python
1. Ladda ner Python här: https://www.python.org/downloads/  
2. Öppna CMD i provbokning_trafikverket-master 
> SHIFT + Högerklick + W (gör detta i provbokning_trafikverket-master)  

Alternativ lösning: öppna cmd och skriv:  
> cd desktop/provbokning_trafikverket-master  
3. Skriv nedanstående kommando i CMD för att installera alla nödvändiga paket  
> pip install -r requirements.txt

### 4. Fyll i config.py
Döp om config.sample.py till config.py  
Texten måste matcha som det står på trafikverkets hemsida.  
Gå igenom sidan manuellt från https://fp.trafikverket.se/boka/#/licence och kontrollera, alternativt,  
Kör skripten och ändra allteftersom

### 5. Kör skripten
1. Skriv nedanstående kommando i CMD (Se #3 om du stängde ned rutan)  
> python bot.py
2. Skripten kan avbrytas med CTRL + C

---

## config.py

### 1. social_security
Fyll i ditt personnummer med formatet yyyymmddxxxx (Inga mellanrum, bindestreck osv)

### 2. license_type
Lägg till behörigheten du vill boka prov inför (ex. B, B96, Buss etc)

### 3. exam
Lägg till vilket prov du vill boka (ex. Körprov B, Kunskapsprov B)

### 4. rent_option
Välj mellan ex. "Nej", "Ja, automat" eller "Ja, manuell".  
Radera eller kommentera (#) om inte används (ex. vid kunskapsprov B eller MC)  
Ta bort # ifall används

### 5. language_option
Välj språk, ex. Svenska, Engelska.  
Radera eller kommentera (#) om inte används (ex. vid körprov B eller MC)  
Ta bort # ifall används

### 5. dates
Lägg till 2 datum i ISO 8601 format (yyyy-mm-dd)  
Skripten kommer leta efter tider mellan de två datumen

### 6. locations
Lägg till de orterna du vill boka provet vid

---

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Copyright 2020 © Daky