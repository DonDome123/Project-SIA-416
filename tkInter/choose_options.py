import tkinter as tk
from tkinter import ttk, filedialog
import os
import openpyxl
from reportlab.pdfgen import canvas
import pandas as pd

def create_sia416_folder():
    current_directory = os.getcwd()
    sia416_folder = os.path.join(current_directory, "SIA416")

    # Überprüfe, ob der Ordner bereits existiert, andernfalls erstelle ihn
    if not os.path.exists(sia416_folder):
        os.makedirs(sia416_folder)

    return sia416_folder

def _create_df(room_list):
    col_lst = []
    col_lst.append("guid")
    col_lst.append("category")
    col_lst.append("name")
    col_lst.append("story")
    col_lst.append("site")
    col_lst.append("area")
    col_lst.append("volume")

    df = pd.DataFrame([room for room in room_list], columns = col_lst)
    return df   


def extract_and_export_data(selected_option, export_format, sia416_folder, entry_projekt_name, entry_datei_name, room_list):
    # Simuliere Datenextraktion aus einer anderen Quelle (z. B. einem anderen Code)
    df = _create_df(room_list)

    if selected_option == "Zusammengefasst":
        result_df = df.head(1)
    elif selected_option == "Detailliert":
        result_df = df

    print("Ausgewählte Zeilen:")
    print(result_df)

    projekt_name = entry_projekt_name.get()
    datei_name = entry_datei_name.get()

    if export_format == "PDF":
        export_to_pdf(result_df, sia416_folder, projekt_name, datei_name)
    elif export_format == "Excel":
        export_to_excel(result_df, sia416_folder, projekt_name, datei_name)

def export_to_pdf(dataframe, sia416_folder, projekt_name, datei_name):
    pdf_path = os.path.join(sia416_folder, f"{datei_name}_{projekt_name}_sia416.pdf")

    c = canvas.Canvas(pdf_path)
    c.drawString(100, 750, "Ausgewählte Zeilen:")
    c.drawString(200, 750, str(dataframe))
    c.save()

    print(f"Daten in PDF exportiert: {pdf_path}")

def export_to_excel(dataframe, sia416_folder, projekt_name, datei_name):
    excel_path = os.path.join(sia416_folder, f"{datei_name}_{projekt_name}_sia416.xlsx")

    with pd.ExcelWriter(excel_path, engine='openpyxl') as writer:
        dataframe.to_excel(writer, sheet_name='Ausgewählte_Zeilen', index=False)

    print(f"Daten in Excel exportiert: {excel_path}")

def main(root, room_list):
    sia416_folder = create_sia416_folder()

    #root = tk.Tk()
    root.title("Datenoptionen auswählen und exportieren")

    # Label für Projektname
    label_projekt_name = tk.Label(root, text="Projektname:")
    label_projekt_name.pack(pady=5)

    entry_projekt_name = tk.Entry(root, width=20)
    entry_projekt_name.insert(0, "ProjektName")
    entry_projekt_name.pack(pady=5)

    # Label für Dateiname
    label_datei_name = tk.Label(root, text="Dateiname:")
    label_datei_name.pack(pady=5)

    entry_datei_name = tk.Entry(root, width=20)
    entry_datei_name.insert(0, "DateiName")
    entry_datei_name.pack(pady=5)

    # Label für Exportformat
    label_export_format = tk.Label(root, text="Exportformat:")
    label_export_format.pack(pady=5)

    options_export_format = ["PDF", "Excel"]
    selected_export_format = tk.StringVar()
    selected_export_format.set(options_export_format[0])

    option_menu_export_format = tk.OptionMenu(root, selected_export_format, *options_export_format)
    option_menu_export_format.pack(pady=10)

    # Label für Datenextraktion
    label_data_extraction = tk.Label(root, text="Detaillierungsgrad")
    label_data_extraction.pack(pady=5)

    options_data_extraction = ["Zusammengefasst", "Detailliert"]
    selected_data_extraction = tk.StringVar()
    selected_data_extraction.set(options_data_extraction[0])

    option_menu_data_extraction = tk.OptionMenu(root, selected_data_extraction, *options_data_extraction)
    option_menu_data_extraction.pack(pady=10)

    btn_extract_rows = tk.Button(root, text="Auswerten", command=lambda: extract_and_export_data(selected_data_extraction.get(), selected_export_format.get(), sia416_folder, entry_projekt_name, entry_datei_name, room_list))
    btn_extract_rows.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
