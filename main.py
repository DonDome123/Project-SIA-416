import tkinter as tk
from tkinter import filedialog
from tkInter.choose_ifc import open_ifc_file
from tkInter.choose_ifc import get_rooms, get_project_name
import collections
import openpyxl

#Globale Variablen - Listen
glb_rooms = []

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
        global glb_rooms
        glb_rooms = get_rooms()
        if len(glb_rooms) == 0:
            return
        
        btn_open.destroy()  # Remove the "Choose IFC File" button

        ausbaustandard_title = tk.Label(root, text="Wähle den Ausbaustandard")
        ausbaustandard_title.pack()
        options = ["Niedrig", "Mittel", "Hoch"]  # Liste der Optionen, die du anzeigen möchtest
        selected_option = tk.StringVar()
        selected_option.set(options[0])  # Standardmäßig die erste Option auswählen
        # Erstellen des OptionMenu-Widgets
        option_menu = tk.OptionMenu(root, selected_option, *options)
        option_menu.pack()
        
        berechnung_title = tk.Label(root, text="Berechnung nach:")
        berechnung_title.pack()
        options = ["m2", "m3"]
        selected_option_price = tk.StringVar()
        selected_option_price.set(options[0])  # Standardmäßig die erste Option auswählen
        # Erstellen des OptionMenu-Widgets
        option_menu_price = tk.OptionMenu(root, selected_option_price, *options)
        option_menu_price.pack()

        btn_next = tk.Button(root, text="Weiter", command=lambda: calculate_prices(selected_option.get().lower(), selected_option_price.get()))
        btn_next.pack()

    # Preise einfügen
    def calculate_prices(ausbaustandard, price_type):
        prices = {
            "m2": {
                "niedrig": 2300,
                "mittel": 3000,
                "hoch": 3700
            },
            "m3": {
                "niedrig": 650,
                "mittel": 800,
                "hoch": 1000
            }
        }
        category_totals = calculate_category_totals(glb_rooms)
        if price_type == "m2":
            price = category_totals["area"]["GF"] * prices[price_type][ausbaustandard]
        else:
            price = category_totals["volume"]["GF"] * prices[price_type][ausbaustandard]
        
        # Richtige Zellen angeben
        ziel_excel = openpyxl.load_workbook("HS23_DC-Script_PSIA416_Excel-Vorlage_230114.xlsx")
        ziel_arbeitsblatt = ziel_excel["Tabelle1"]
        cells = ["A9", "A15", "B15", "C13", "D13", "A33", "A25"] 
        values = [category_totals["area"][value] for value in ("GF", "HNF", "NNF", "VF", "FF")]
        values.extend([price, category_totals["volume"]["GF"]])
        for cell, value in zip(cells, values):
            ziel_arbeitsblatt[cell].value = round(value, 3)
        ziel_arbeitsblatt["B3"].value = get_project_name()
        ziel_arbeitsblatt["E31"].value = price_type

        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel", "*.xlsx")])
        if file_path:
            ziel_excel.save(file_path)
            ziel_excel.close()
            root.quit()

    root = tk.Tk()
    root.title("SIA 416 Auszug")
    btn_open = tk.Button(root, text="Wähle IFC Datei", command=get_ifc)
    btn_open.pack(pady=50)

    text_output = tk.Text(root, width=40, height=10, bg='gray',)
    text_output.pack()

    root.mainloop()


#Als Hauptprogramm ausführen
if __name__ == '__main__':
    main()