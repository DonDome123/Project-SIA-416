import tkinter as tk
from tkinter import filedialog

def choose_save_location():
    options = ["Zusammengefasst", "Detailliert"]  # Liste der Optionen, die du anzeigen möchtest
    selected_option = tk.StringVar()
    selected_option.set(options[0])  # Standardmäßig die erste Option auswählen

    # Erstellen des OptionMenu-Widgets
    option_menu = tk.OptionMenu(root, selected_option, *options)
    option_menu.pack(pady=10)

    # Der ausgewählte Wert wird hier angezeigt (kann für deine Zwecke angepasst werden)
    print(f"Ausgewählte Option: {selected_option.get()}")


    options = ["low", "medium", "high"]  # Liste der Optionen, die du anzeigen möchtest
    selected_option = tk.StringVar()
    selected_option.set(options[1])  # Standardmäßig die erste Option auswählen

    # Erstellen des OptionMenu-Widgets
    option_menu = tk.OptionMenu(root, selected_option, *options)
    option_menu.pack(pady=10)

    # Der ausgewählte Wert wird hier angezeigt (kann für deine Zwecke angepasst werden)
    print(f"Ausgewählte Option: {selected_option.get()}")


    options = ["PDF", "Excel"]  # Liste der Optionen, die du anzeigen möchtest
    selected_option = tk.StringVar()
    selected_option.set(options[0])  # Standardmäßig die erste Option auswählen

    # Erstellen des OptionMenu-Widgets
    option_menu = tk.OptionMenu(root, selected_option, *options)
    option_menu.pack(pady=10)

    # Der ausgewählte Wert wird hier angezeigt (kann für deine Zwecke angepasst werden)
    print(f"Ausgewählte Option: {selected_option.get()}")

root = tk.Tk()
root.title("Auswahlfenster mit Optionen")

btn_choose_location = tk.Button(root, text="Voreinstellungen", command=choose_save_location)
btn_choose_location.pack(pady=50)

root.mainloop()
