import os

source_folder = input("Pfad zum Basisordner eingeben >>> ")
xls_file_name = "Elementplan.xlsx"
xls_file = os.path.join(source_folder, xls_file_name)

print(xls_file)