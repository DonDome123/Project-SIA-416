import openpyxl

# Pfad zur Excel-Datei
excel_datei_pfad = "Pfad\\zur\\Ihrer\\Excel-Datei.xlsx"

# Zielarbeitsblatt
ziel_arbeitsblatt_name = "Ihr_Arbeitsblatt"

# Liste mit Zahlen (Gesamtfläche, Volumen, Kosten)
zahlen_liste = [10, 20, 30, 40, 50]

# Zellen, die Sie füllen möchten (Beispiel: A1, B2, C3)
ziel_zellen = ['A1', 'B2', 'C3', 'D4', 'E5']

# Öffnen Sie die Excel-Datei
ziel_excel = openpyxl.load_workbook(excel_datei_pfad)
ziel_arbeitsblatt = ziel_excel[ziel_arbeitsblatt_name]

# Füllen Sie die Zellen mit den Zahlen aus der Liste
for index, zelle in enumerate(ziel_zellen):
    ziel_arbeitsblatt[zelle].value = zahlen_liste[index]

# Speichern Sie die Änderungen
ziel_excel.save(excel_datei_pfad)

# Schließen Sie die Excel-Datei
ziel_excel.close()
