import re        # Regular Expressions
import datetime  # Datum/Zeit 
 
# Erklärungen zu diesem Code gibt es auch als Video hier:
# https://web.microsoftstream.com/video/4c478e5b-609d-4429-bc20-78b9f8abab93
# und für Datensparsame und solche ohne BLDSG-Account auch hier:
# https://fginfo.ksbg.ch/~ivo/videos/informatik/vierte-klasse/daten-extraktion-youtube-watchtime-extraktion.mp4
 
# Daten einlesen
# Entweder vollständiger Pfad zur Datei oder (wie z.B. C:\Users\Hansli\Desktop\watch-history.html) oder
# nur Dateiname, wenn die Datei im gleichen Verzeichnis wie das Pythonprogramm liegt.
f = open("watch-history.html", "r")
html = f.read()  # Alles einlesen
f.close()        # Datei schliessen

 
# Datum der Form Jan 6, 2021, 9:23:12 PM CET
# Alle nötigen Angaben werden in Klammern "ge-captured"
daten = re.findall(r"([A-Z][a-z][a-z]) (\d{1,2}), (\d{4}), (\d{1,2}):(\d{1,2}):(\d{1,2}) ([AP]M) CET", html)
 
#Erste 3 Einträge zur Kontrolle ausgeben
print(daten[0:3])
 
# Zuordnung der Monatsnamen zu Monatsnummern, z.B. ist mnum["Jul"] gleich 7
mnum = {"Jan":1, "Feb":2, "Mar":3, "Apr":4, "May":5, "Jun":6, "Jul":7, "Aug":8, "Sep":9, "Oct":10,"Nov":11, "Dec":12}; 
 
# Resultat, das am Schluss geschrieben werden soll
csv = ""   # Comma separated values
 
# Wie viele Kontrollausgaben?
debug = 10
 
# Alle Einträge durchgehen, d enthält jeweils den nächsten Eintrag
for d in daten:
    # Einträge in Zahlen umwandeln
    # Monat plus die anderen Einträge (ohne AM/PM) in Zahlen umgewandelt 
    #   Die Zeichenkette "42" ist nicht das gleiche wie die Zahl 42.
    e = [mnum[d[0]]] + [int(x) for x in d[1:-1]]
    if d[6]=="PM":  # Nachmittag? Plus 12 Stunden (Ausser Mitternacht = 0)
        e[3]=(e[3]+12) % 24
 
    if debug>0:
        # Ausgabe zur Kontrolle, sollte folgendes Format Produzieren
        print(e) # [1, 6, 2021, 21, 23, 12]
        debug -= 1  # Um 1 vermindern
 
    # Datum daraus generieren (macht die Datumsmanipulation einfacher).
    # Jahr, Monat, Tag, Stunde, Minute, Sekunde
    datum = datetime.datetime(e[2], e[0], e[1], e[3], e[4], e[5])
 
    if debug>0:
        # Ausgabe zur Kontrolle, produziert folgendes Format
        print(datum)   # 2021-01-06 21:23:12
        debug -= 1  # Um 1 vermindern
 
    # Wochentag (Mo=0, Di=1, ..., So=6)
    # Sämtliche Methoden für datetime-Objekte sind hier beschrieben: https://docs.python.org/3/library/datetime.html#datetime-objects
    wday = datum.weekday()
 
    # Formatierte Ausgabe des Datums, siehe https://www.w3schools.com/python/python_datetime.asp
    # \n heisst neue Zeile.
    csv += datum.strftime("%Y-%m-%d %H:%M:%S\n")  #Das Format soll so angepasst werden, damit die Tabellenkalkulation dann damit umgehen kann.
 
# Ausgabe in Datei schreiben
f = open("resultat.csv", "w")
f.write(csv)
f.close()
