import ifcopenshell
from tkinter import filedialog
import tkinter as tk
from reportlab.pdfgen import canvas

def extract_project_name(ifc_file_path):
    print(ifc_file_path)
    ifc_file = ifcopenshell.open(ifc_file_path)

    # Iterate over each schema in the IFC file
    for item in ifc_file.by_type("IfcProject"):
        return item.Name

    return None

def write_to_pdf(project_name):
    pdf_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])

    if pdf_path:
        # Create a PDF file
        c = canvas.Canvas(pdf_path)

        # Write the project name to the PDF
        c.drawString(100, 750, "Projektname:")
        c.drawString(200, 750, project_name)

        c.save()
        print(f"Projektnamen in PDF geschrieben: {pdf_path}")

def choose_ifc_file_and_process():
    ifc_file_path = filedialog.askopenfilename(filetypes=[("IFC files", "*.ifc")])

    if ifc_file_path:
        project_name = extract_project_name(ifc_file_path)
        if project_name:
            write_to_pdf(project_name)
        else:
            print("Projektname konnte nicht gefunden werden.")
    else:
        print("IFC-Datei nicht ausgewählt.")

root = tk.Tk()
root.title("IFC Projektname in PDF schreiben")

btn_choose_ifc_and_process = tk.Button(root, text="IFC-Datei auswählen und verarbeiten", command=choose_ifc_file_and_process)
btn_choose_ifc_and_process.pack(pady=50)

root.mainloop()
