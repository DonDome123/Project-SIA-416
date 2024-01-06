import Processors.config_processor as conf_pro
import Processors.ifc_processor as ifc_p
import Processors.export_processor as exp_p
import tkinter as tk
from tkinter import ttk, filedialog

from tkInter.choose_ifc import open_ifc_file

#Globale Variablen - Listen
glb_conf_lst = []
glb_conf_folder = ""
glb_export_lst = []

def start_func():
    #Hauptfunktion zum Ausführen

    print("Hauptprogramm gestartet")

    glb_conf_set = conf_pro.read_source_data()
    glb_conf_lst = glb_conf_set[0]
    glb_conf_folder = glb_conf_set[1]

    glb_export_lst = ifc_p.process_ifc_data(glb_conf_lst)
    exp_p.export_data(glb_export_lst, glb_conf_lst, glb_conf_folder)

def main():
    root = tk.Tk()
    root.title("IFC Elemente pro Stock")

    btn_open = tk.Button(root, text="Choose IFC File", command=open_ifc_file)
    btn_open.pack(pady=50, side=tk.TOP)

    text_output = tk.Text(root, width=40, height=10)
    text_output.pack(pady=10)

    root.mainloop()

#Als Hauptprogramm ausführen
if __name__ == '__main__':
    main()