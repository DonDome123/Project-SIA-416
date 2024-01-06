import tkinter as tk
from tkinter import ttk, filedialog
import ifcopenshell


def open_ifc_file():
    global ifc_file
    file_path = filedialog.askopenfilename(filetypes=[("IFC files", "*.ifc")])
    if file_path:
        ifc_file = ifcopenshell.open(file_path)
        list_elements_per_storey()

def list_elements_per_storey():
    if not ifc_file:
        return

    storeys = ifc_file.by_type("IfcBuildingStorey")
    text_output.delete(1.0, tk.END)

    for storey in storeys:
        related_elements = [rel.RelatedElements for rel in storey.ContainsElements]
        element_count = sum(len(elem) for elem in related_elements)
        text_output.insert(tk.END, f"Stockwerk: {storey.Name} - Elemente: {element_count}\n")

ifc_file = None

root = tk.Tk()
root.title("IFC Elemente pro Stock")

btn_open = tk.Button(root, text="Choose IFC File", command=open_ifc_file)
btn_open.pack(pady=50, side=tk.TOP)

text_output = tk.Text(root, width=40, height=10)
text_output.pack(pady=10)

root.mainloop()
