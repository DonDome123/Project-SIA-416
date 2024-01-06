import Processors.config_processor as conf_pro
import Processors.ALT.ifc_processor as ifc_p
import Processors.export_processor as exp_p
import tkinter as tk
from tkinter import ttk, filedialog

from tkInter.choose_ifc import open_ifc_file as open_ifc_file
from tkInter.choose_ifc import get_rooms
from Processors.export_processor import export_data
from tkInter.choose_options import main as choose_options_main

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

def main():

    def open_choose_options():
        choose_options_main(root, glb_rooms)

    def get_ifc():
        file_path = filedialog.askopenfilename(filetypes=[("IFC Files", "*.ifc")])
        if file_path:
            open_ifc_file(file_path, text_output)
            btn_open.pack_forget()  # Remove the "Choose IFC File" button
            btn_options.pack(pady=50)  # Add the "Choose Options" button
            global glb_rooms
            glb_rooms = get_rooms()
    
    def export_to_excel():
        global glb_rooms
        exp_p.export_data(glb_rooms)

    root = tk.Tk()
    root.title("IFC Elemente pro Stock")
    btn_open = tk.Button(root, text="Choose IFC File", command=get_ifc)
    btn_open.pack(pady=50)
    btn_export = tk.Button(root, text="Export Excel", command=export_to_excel)
    btn_export.pack(pady=60)


    

    btn_options = tk.Button(root, text="Choose Options", command=open_choose_options)
    text_output = tk.Text(root, width=40, height=10)
    text_output.pack(pady=10)
    
    

    root.mainloop()





#Als Hauptprogramm ausführen
if __name__ == '__main__':
    main()