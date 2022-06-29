# provbokning_trafikverket
Ett skript som automatiskt söker efter förarprov och reserverar dem i 15 minuter alternativt bokar dem åt dig.  

---

## Bot.py
Denna skript är lite enklare och vad den gör är att den söker efter tider och när den väl hittat en så reservas tiden i 15 minuter.  
Om du redan har en tid så kommer den nya tiden inte reserveras då detta kräver inloggning.  
Ett ljud kommer spelas upp när en tid har hittats i 15 minuter.  
Detta skript kräver inget BankID.

---

## Botv2.py - Helt automatisk provbokning
Denna skript är lite mer teknisk och inte klar till hundra procent så kan finnas buggar m.m.  
Kort förklarat så kommer den logga in med BankID. Du kommer behöva bekräfta i början och sen kör den på självständigt.  
Den kommer att boka första bästa tid med alternativt "Betala senare"  
Du kan avboka gratis om det är mer än 24 timmar till provtillfället så undvik att leta tider inom 24 timmar om du inte är helt hundra på att du kan vilken tid som helst på dagen.  
Ett ljud kommer spelar upp i cirka en minut och sen stängs allting ned. Trafikverket kommer maila m.m. om du lyckas boka en tid
Jag har inte hunnit skriva en guide specifikt för den men om du vill testa skriptet ändå behöver du:  
1. BankID  
2. Telefonnummer & mail registrerat hos trafikverket när du loggar in  
---

## Donationer & Hjälp
Om du vill vara lite snäll, Swisha gärna en slant :) 073 554 71 85  
Kontakta inte mig per telefon utan gör det helst via Discord Daky#6387  
Jag kommer förmodligen ignorera ditt försök att nå mig på telefon  
Vill du att jag hittar en tid åt dig, lägg till mig på discord. Jag tar betalt för den tjänsten.

---

## Installation (Windows)

### 1. Ladda ner alla filer
1. Ladda ner alla filer här: [master.zip](https://github.com/Daky60/provbokning_trafikverket/archive/master.zip)  
2. Packa upp mappen och lägg den på skrivbordet

### 2. Installera ChromeDriver
1. Ladda ner: https://sites.google.com/chromium.org/driver/  
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
Kör skriptet och ändra allteftersom

### 5. Kör skriptet
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
Lägg till vilket prov du vill boka (ex. Körprov, Kunskapsprov)

### 4. rent_or_language
Beroende på ifall du ska boka körprov eller kunskapsprov kommer det finnas alternativ för antingen språk eller hyrbil.  
Ange exakt vad som står som alternativ (ex. "Svenska" eller "Ja, manuell") för att det ska fungera ordentligt.
Om du ska boka ett prov utan någon av alternativen som exempelvis MC kort, ta bort eller kommentera ut raden med #

### 5. dates
Lägg till datum i par i ISO 8601 format (yyyy-mm-dd)  
Skriptet kommer leta efter tider mellan de två datumen  
Fler tidsperioder kan läggas till (ex. dates = ['2020-07-22', '2020-07-25', '2020-08-05', '2020-08-30'])

### 6. locations
Lägg till de orterna du vill boka provet vid (ex. locations = ['Järfälla', 'Sollentuna'])

---

## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Copyright 2020 © Daky
