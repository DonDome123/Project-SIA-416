import Processors.config_processor as conf_pro
import Processors.ALT.ifc_processor as ifc_p
import Processors.export_processor as exp_p
import tkinter as tk
from tkinter import ttk, filedialog

from tkInter.choose_ifc import open_ifc_file as open_ifc_file
from tkInter.choose_ifc import get_rooms
from Processors.export_processor import export_data
from tkInter.choose_options import main as choose_options_main
import collections
import openpyxl

#Globale Variablen - Listen
glb_conf_lst = []
glb_conf_folder = ""
glb_export_lst = []
glb_rooms = []

# def start_func():
#     #Hauptfunktion zum Ausführen

#     print("Hauptprogramm gestartet")

#     glb_conf_set = conf_pro.read_source_data()
#     glb_conf_lst = glb_conf_set[0]
#     glb_conf_folder = glb_conf_set[1]

#     glb_export_lst = ifc_p.process_ifc_data(glb_conf_lst)
#     exp_p.export_data(glb_export_lst, glb_conf_lst, glb_conf_folder)


def calculate_category_totals(room_list):
    category_totals = {"area": collections.defaultdict(int), "volume": collections.defaultdict(int)}
    for room in room_list:
        category = room["category"]
        category_totals["area"][category] += room["area"]
        category_totals["volume"][category] += room["volume"]
    return category_totals

def main():

    def get_ifc():
        file_path = filedialog.askopenfilename(filetypes=[("IFC Files", "*.ifc")])
        if not file_path:
            return
        open_ifc_file(file_path, text_output)
        btn_open.destroy()  # Remove the "Choose IFC File" button
        global glb_rooms
        glb_rooms = get_rooms()
        options = ["Niedrig", "Mittel", "Hoch"]  # Liste der Optionen, die du anzeigen möchtest
        selected_option = tk.StringVar()
        selected_option.set(options[0])  # Standardmäßig die erste Option auswählen
        # Erstellen des OptionMenu-Widgets
        option_menu = tk.OptionMenu(root, selected_option, *options)
        option_menu.pack()
        btn_next = tk.Button(root, text="Weiter", command=lambda: calculate_prices(selected_option.get().lower()))
        btn_next.pack()

# Preise einfügen
    def calculate_prices(ausbaustandard):
        prices = {
            "area": {
                "niedrig": 5,
                "mittel": 10,
                "hoch": 15
            },
            "volume": {
                "niedrig": 5,
                "mittel": 10,
                "hoch": 15
            }
        }
        category_totals = calculate_category_totals(glb_rooms)
        price_area = category_totals["area"]["GF"] * prices["area"][ausbaustandard]
        price_volume = category_totals["volume"]["GF"] * prices["volume"][ausbaustandard]
# Richtige Zellen angeben
        ziel_excel = openpyxl.load_workbook("HS23_SCRIPT_SIA416_Flaechen.xlsx")
        ziel_arbeitsblatt = ziel_excel["Tabelle1"]
        cells = ["A9", "A15", "B15", "C13", "D13", "A25", "B25"]
        values = [category_totals["area"][value] for value in ("GF", "HNF", "NNF", "VF", "FF")]
        values.extend([price_area, price_volume])
        for cell, value in zip(cells, values):
            ziel_arbeitsblatt[cell].value = round(value, 3)

        file_path = filedialog.asksaveasfilename(filetypes=[("Excel", "*.xlsx"), ("PDF", "*.pdf")])
        
        if file_path:
            ziel_excel.save(file_path)
            ziel_excel.close()


            
    
    def export_to_excel():
        global glb_rooms
        exp_p.export_data(glb_rooms)

    root = tk.Tk()
    root.title("IFC Elemente pro Stock")
    btn_open = tk.Button(root, text="Choose IFC File", command=get_ifc)
    btn_open.pack(pady=50)


    text_output = tk.Text(root, width=40, height=10, bg = 'red')
    text_output.pack()
    
    

    root.mainloop()





#Als Hauptprogramm ausführen
if __name__ == '__main__':
    main()