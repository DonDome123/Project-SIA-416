import tkinter as tk
from tkinter import ttk, filedialog
import ifcopenshell

def choose_save_location():
    file_path = filedialog.asksaveasfilename(defaultextension=".ifc", filetypes=[("IFC files", "*.ifc")])
    if file_path:
        print(f"Gewählter Speicherort: {file_path}")

root = tk.Tk()
root.title("Speicherort wählen")

btn_choose_location = tk.Button(root, text="Speicherort wählen", command=choose_save_location)
btn_choose_location.pack(pady=100)

root.mainloop()

