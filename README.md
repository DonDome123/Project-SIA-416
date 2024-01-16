# Project SIA 416

Mit dem vorliegenden Code kann der Benutzer durch sechs Klicks aus einer IFC Datei ein SIA416 Auszug mit einer Grobkostenschätzung in einer Excel Datei generieren. Dabei müssen in der IFC Datei lediglich die Räume vorhanden und dessen Raumkategorie definiert sein. Neben den definierten Nettogeschossflächen müssen die Geschossflächen ebenfalls als Raum gezeichnet und die lichte Raumhöhe bzw. die Geschosshöhe muss Richtig eingestellt sein (Volumenberechnung).

## Module

- tkInter
    - filedialog
    - tk.
- ifcopenshell
    - ifcopenshell.open
- openpyxl
    - openpyxl.load_workbook
- collections
    - collections.defaultdict

### tkInter

Mit dem tkInter wird ein Dialogfenster bereitgestellt, über welches die IFC Datei ausgewählt werden kann. Sobald ausgewählt, zeigt es in einer Textbox die Anzahl Räume pro Geschoss an. Falls relevante Informationen fehlen, wird das ebenfalls aufgelistet. Im nächsten Schritt kann durch die Optionenauswahl der Ausbaustandard (niedrig, mittel, hoch) sowie die Berechnungsart (nach Fläche oder Volumen) definiert werden. Anschliessend gelangt man durch einen Klick auf den "weiter" Knopf zur Auswahl des Speicherorts. Der Benutzer kann einen eigenen Namen für die generierte Excel Datei wählen und in entsprechendem Ordner abspeichern.

Achtung: Die Anzeige von tkInter funktioniert im macOS nur bedingt. Auf Windows wird es richtig angezeigt.

### ifcopenshell

Das ifcopenshell ermöglicht uns das öffnen, analysieren und bearbeiten von IFC Dateien. Die Abkürzung IFC steht für Industry Foundation Classes und bezeichnet einen primären, weltweiten, offenen Standard für den Datenaustausch in der Bauindustrie. Entwickelt wurde er von buildingSMART, unter deren Federführung er auch weiterentwickelt wird.

Im Project SIA 416 beziehungsweise im ifc_processor file lesen wir von allen Raum-Elementen folgende Informationen heraus: 
- GUID
- Raumkategorie
- Raumname
- Geschoss
- Raumfläche
- Raumvolumen
- Projektname

Im choose_ifc file wird die IFC Datei geöffnet und der Projektname sowie die Räume gelesen. Die Räume werden gezählt und geprüft, ob Informationen für die nachfolgenden Berechnungen fehlen. Falls etwas fehlt, wird dies im Dialogfeld via tkInter angezeigt.

### openpyxl

Mit openpyxl.load_workbook wird die bestehende Excel Vorlage Datei aufgerufen und die angegeben Zellen mit den berechneten Zahlen abgefüllt. So werden die Raumflächen, das Volumen, der Projektname sowie auch das Resultat der Kostenberechnung reingeschrieben.

### collections

Das collections.defaultdict ist ein Wörterbuch, das einen Standardwert für Keys bereitstellt, die nicht im bestehenden Wörterbuch vorhanden sind. Dabei werden die Flächen sowie Volumen summiert und als category_totals weiterverwendet. 

## Preisberechnung

Die totale Fläche und das Volumen werden mit bereits im Code festgelegten Preisen multipliziert. Der Anwender muss sich nicht mehr überlegen, welchen Preis er einsetzen soll und muss lediglich angeben, welchen Ausbaustandard er wünscht.

## Potenzial

Das Skript könnte man wie folgt weiterentwickeln:
- Aktuelle Preislisten verknüpfen
- Möglichkeit zum Einsetzen eigener Erfahrungswerte
- Berechnung der Konstruktionsfläche KF mittels Additionsverfahren
- Ausgabe als PDF
- User Interface mit Custom TkInter oder Website
