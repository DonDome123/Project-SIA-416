import tkinter as tk
from tkinter import filedialog
import os

def choose_save_location():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_name = "SIA416"  # Ändere dies auf den gewünschten Ordnernamen
        full_path = os.path.join(folder_path, folder_name)

        try:
            os.makedirs(full_path)
            print(f"Ordner erstellt: {full_path}")
        except FileExistsError:
            print(f"Der Ordner {full_path} existiert bereits.")

root = tk.Tk()
root.title("Speicherort wählen")

btn_choose_location = tk.Button(root, text="Speicherort wählen", command=choose_save_location)
btn_choose_location.pack(pady=50)

root.mainloop()
