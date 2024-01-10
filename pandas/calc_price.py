import pandas as pd

def multiply_numbers_in_excel_and_export(excel_path, column_name1, column_name2, price1, price2, output_excel_path):
    # Lade die Excel-Datei in ein Pandas DataFrame
    df = pd.read_excel(excel_path)

    # Überprüfe, ob die angegebenen Spalten im DataFrame vorhanden sind
    if column_name1 not in df.columns or column_name2 not in df.columns:
        print(f"Die Spalten '{column_name1}' oder '{column_name2}' wurden nicht gefunden.")
        return None

    # Erstelle eine Kopie des ursprünglichen DataFrames
    df_copy = df.copy()

    # Multipliziere die Werte in den angegebenen Spalten der Kopie mit den Preisen
    df_copy[column_name1] = df_copy[column_name1] * price1
    df_copy[column_name2] = df_copy[column_name2] * price2

    # Füge eine neue Zeile mit dem Ergebnis hinzu
    kosten_row = pd.DataFrame({
        column_name1: [df_copy[column_name1].sum()],
        column_name2: [df_copy[column_name2].sum()]
    }, index=['Kosten'])

    # Füge die Kosten-Zeile zum ursprünglichen DataFrame hinzu
    df = pd.concat([df, kosten_row])

    # Speichere das aktualisierte DataFrame in der Excel-Datei
    df.to_excel(output_excel_path, index=False)

    print(f"Zahlen in den Spalten '{column_name1}' und '{column_name2}' mit den Preisen {price1} und {price2} multipliziert und in Excel gespeichert: {output_excel_path}")

# Beispielaufruf
excel_path = '/Users/m.amstad/Desktop/result_tot.xlsx'
column_name1 = 'area'  # Ersetzen Sie dies durch den tatsächlichen Namen Ihrer ersten Spalte
column_name2 = 'volume'  # Ersetzen Sie dies durch den tatsächlichen Namen Ihrer zweiten Spalte
price1 = 800  # Passen Sie den Preis für die erste Spalte an
price2 = 2000  # Passen Sie den Preis für die zweite Spalte an
output_excel_path = '/Users/m.amstad/Desktop/Kosten.xlsx'
multiply_numbers_in_excel_and_export(excel_path, column_name1, column_name2, price1, price2, output_excel_path)
