import tkinter as tk
from tkinter import filedialog
import pandas as pd

def calculate_category_totals(room_df):
    category_totals = {}

    for _, row in room_df.iterrows():
        category = row["category"]
        area = row["area"]

        if category in category_totals:
            category_totals[category] += area
        else:
            category_totals[category] = area

    return category_totals

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("excel files", "*.xlsx")])
    if file_path:
        room_df = pd.read_excel(file_path)

        category_totals = calculate_category_totals(room_df)

        # Display the summary
        for category, total_area in category_totals.items():
            result_label.config(text=f"{category}: {total_area} square units")

        # Create a new DataFrame with the totals
        totals_df = pd.DataFrame(list(category_totals.items()), columns=["category", "total area"])

        # Export the totals to a new Excel file
        save_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
        if save_path:
            totals_df.to_excel(save_path, index=False)

# GUI setup
root = tk.Tk()
root.title("Room Category Area Summary")

# Browse button
browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Start the GUI
root.mainloop()
