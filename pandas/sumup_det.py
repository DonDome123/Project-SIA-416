import pandas as pd

def sum_columns_and_export(excel_path, column_names, output_excel_path):
    # Lade die Excel-Datei in ein Pandas DataFrame
    df = pd.read_excel(excel_path)

    # Überprüfe, ob die angegebenen Spalten im DataFrame vorhanden sind
    for column_name in column_names:
        if column_name not in df.columns:
            print(f"Die Spalte '{column_name}' wurde nicht gefunden.")
            return None

    # Berechne die Summe der Werte in den angegebenen Spalten
    column_sums = df[column_names].sum()

    print(f"Summe der Werte in den Spalten {column_names}: {column_sums}")

    # Erstelle ein neues DataFrame mit den Summen in einer neuen Zeile
    sum_row = pd.DataFrame({column_name: [column_sums[column_name]] for column_name in column_names}, index=['Summe'])
    
    # Hänge die Zeile mit den Summen an das bestehende DataFrame an
    df = pd.concat([df, sum_row])

    # Exportiere das DataFrame in die Excel-Datei (ohne den Index)
    df.to_excel(output_excel_path, index=False)

    print(f"Summen in Excel exportiert: {output_excel_path}")

    return column_sums

# Beispielaufruf
excel_path = '/Users/m.amstad/Desktop/Export_Daten_IFC.xlsx'
column_names = ['area', 'volume']  # Ersetzen Sie dies durch die tatsächlichen Namen Ihrer Spalten
output_excel_path = '/Users/m.amstad/Desktop/result_det.xlsx'  # Ersetzen Sie dies durch den gewünschten Ausgabepfad
result = sum_columns_and_export(excel_path, column_names, output_excel_path)
