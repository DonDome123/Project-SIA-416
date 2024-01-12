import tkinter as tk
from tkinter import ttk, filedialog
import ifcopenshell

from .ifc_processor import read_source_ifc
ifc_file = None
room_list = []

def open_ifc_file(file_path, text_output):
    global ifc_file
    global room_list

    ifc_file = ifcopenshell.open(file_path)
    list_elements_per_storey(text_output)
    room_list = read_source_ifc(file_path)
    for i, room in enumerate(room_list):
        missing = ",".join([key for key, val in room.items() if val is None])
        if missing != "":
            text_output.insert(tk.END, f"Room {i} is missing: {missing}\n")
    if missing != "":
        room_list = []
        return
    text_output.insert(tk.END, "")

def list_elements_per_storey(text_output):
    if not ifc_file:
        return

    storeys = ifc_file.by_type("IfcBuildingStorey")
    text_output.delete(1.0, tk.END)

    for storey in storeys:
        related_elements = [rel.RelatedElements for rel in storey.ContainsElements]
        element_count = sum(len(elem) for elem in related_elements)
        text_output.insert(tk.END, f"Stockwerk: {storey.Name} - Elemente: {element_count}\n")

def get_rooms():
    global room_list
    return room_list
# ifc_file = None

# root = tk.Tk()
# root.title("IFC Elemente pro Stock")

# btn_open = tk.Button(root, text="Choose IFC File", command=open_ifc_file)
# btn_open.pack(pady=50, side=tk.TOP)

# text_output = tk.Text(root, width=40, height=10)
# text_output.pack(pady=10)

# root.mainloop()
