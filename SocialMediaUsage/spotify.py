import re        # Regular Expressions
import datetime  # Datum/Zeit 
import os        # Files suchen
import json
# Erklärungen zu diesem Code sind Analog dem Youtube-Extraktor.

rootdir = "/Users/michael"

# Resultat, das am Schluss geschrieben werden soll
csv = ""   # Comma separated values
# Wie viele Kontrollausgaben?
debug = 100

# Alle HTML-Dateien im Verzeicznis anzeigen            
for root, dirs, files in os.walk(rootdir):
    for file in files:
        if file.endswith(".json"):
            filepath = os.path.join(root, file) 
            # Datei oeffnen
            
            f = open(filepath, "r")
            #html = f.read()  # Alles einlesen
            data=json.load(f)
            print(data)
            f.close()        # Datei schliessen

            for d in (data):
                # Einträge in Zahlen umwandeln
                # Monat plus die anderen Einträge (ohne AM/PM) in Zahlen umgewandelt 
                #   Die Zeichenkette "42" ist nicht das gleiche wie die Zahl 42.
            

                # Datum daraus generieren (macht die Datumsmanipulation einfacher).
                # Jahr, Monat, Tag, Stunde, Minute, Sekunde
    

                if debug>0:
                    # Ausgabe zur Kontrolle, produziert folgendes Format
                    print(d["endTime"])   # 2021-01-06 21:23:12
                    debug -= 1  # Um 1 vermindern


                # Formatierte Ausgabe des Datums, siehe https://www.w3schools.com/python/python_datetime.asp
                # \n heisst neue Zeile.
                csv += str(d["endTime"])+";"+str(d["msPlayed"])+"\n"

            # Ausgabe in Datei schreiben
        f = open("resultat_spotify.csv", "w")
        f.write(csv)
        f.close() 
