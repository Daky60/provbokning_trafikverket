# boka_prov_trafikverket
Skript som söker efter förarprov inom de uppsatta ramarna.
Skripten bokar inga tider själv utan tiden läggs i varukorgen som då blir reserverad i 15 minuter.



## Varning
Skripten har endast testats vid bokning av körprov B men bör funka för de flesta proven.
Se LICENSE

### 1. Installera nödvändiga paket
> pip install -r requirements.txt

### 2. Installera chromedriver
Se: https://sites.google.com/a/chromium.org/chromedriver/home
Installera samma version som du har på google chrome

### 3. Fyll i config.py
Döp om config_sample.py till config.py
Texten måste matcha den på hemsidan. Gå igenom manuellt och fyll i.

#### 1. chromedriver_location
Lägg chromedriver.exe i C:/ eller ändra config.py till filens sökväg

#### 2. license_type
Lägg till behörigheten du vill boka prov inför (ex. B, B96, Buss etc)

#### 3. exam
Lägg till vilket prov du vill boka (ex. Körprov B, Kunskapsprov B)

#### 4. rent_option
Välj mellan ex. "Nej", "Ja, automat" eller "Ja, manuell". Ta bort eller kommentera (#) om inte används (ex. vid körprov eller MC)

#### 5. language_option
Välj språk, ex. Svenska, Engelska. Ta bort eller kommentera (#) om inte används (ex. vid körprov eller MC)

#### 5. dates
Lägg till 2 datum. Skripten kommer leta prov mellan dem två

#### 6. locations
Lägg till de orterna du vill boka provet vid

