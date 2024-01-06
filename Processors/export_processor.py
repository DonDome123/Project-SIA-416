import os
import pandas as pd

def export_data(room_list):
    #conf_lst, export_folder
    #Export der Daten als Excel
    #Export Extracted Data to Excel

    if len(room_list) > 0:

        xls_file_name = "Export_Daten_IFC.xlsx"
        exp_path = os.path.join("./", xls_file_name)

        check_file = os.path.isfile(exp_path)

        if(not(check_file)):
            pd.DataFrame([]).to_excel(exp_path)
        
        col_lst = []
        col_lst.append("guid")
        col_lst.append("category")
        col_lst.append("name")
        col_lst.append("story")
        col_lst.append("site")
        col_lst.append("area")
        col_lst.append("volume")

        df = pd.DataFrame([room for room in room_list], columns = col_lst)

        df.to_excel(exp_path, sheet_name='rooms')  
                    
            
                

        print("Final Step: Finished Export Excel...")

if __name__ == '__main__':
    export_data([{'name': 'Gang', 'site': 'Gebäude', 'story': 'EG', 'guid': '1GTPWC8212uRs9oiCYvUYi', 'area': 39.70000000000001, 'volume': 115.13, 'category': 'VF'}, {'name': 'Auslauf 1', 'site': 'Gebäude', 'story': 'EG', 'guid': '34Hnm59az5iOn$NfzPyukf', 'area': 16.796, 'volume': 48.7084, 'category': 'HNF'}, {'name': 'Auslauf 3', 'site': 'Gebäude', 'story': 'EG', 'guid': '0U_vkcsAf0CAyOMNLgBLFV', 'area': 14.307, 'volume': 41.49030000000001, 'category': 'HNF'}, {'name': 'Auslauf 2', 'site': 'Gebäude', 'story': 'EG', 'guid': '1KRw3XB0X9Nhi3Gv$rEFme', 'area': 16.644, 'volume': 48.2676, 'category': 'HNF'}, {'name': 'Auslauf 4', 'site': 'Gebäude', 'story': 'EG', 'guid': '0Ai9B7fzn0Txli2rbwEjEh', 'area': 13.48999999999998, 'volume': 39.12099999999995, 'category': 'HNF'}, {'name': 'Stallbox 3', 'site': 'Gebäude', 'story': 'EG', 'guid': '3$va1VyQLFiBfYaeI6GolA', 'area': 14.514, 'volume': 42.0906, 'category': 'HNF'}, {'name': 'Stallbox 4', 'site': 'Gebäude', 'story': 'EG', 'guid': '04eW7uzZXEj8PNSrGoR1gQ', 'area': 14.514, 'volume': 42.09059999999999, 'category': 'HNF'}, {'name': 'Stallbox 1', 'site': 'Gebäude', 'story': 'EG', 'guid': '0QnopjzBXE5hcxua0z3v8f', 'area': 18.163, 'volume': 52.67270000000001, 'category': 'HNF'}, {'name': 'Stallbox 2', 'site': 'Gebäude', 'story': 'EG', 'guid': '10nYEhfhz2nuhhLN38zyx5', 'area': 17.91700000000001, 'volume': 51.95930000000003, 'category': 'HNF'}, {'name': 'Waschen', 'site': 'Gebäude', 'story': 'EG', 'guid': '3ZuSC9YvDEhhEuJkb2BL7X', 'area': 15.75, 'volume': 45.675, 'category': 'HNF'}, {'name': 'Abstellraum                                      ', 'site': 'Gebäude', 'story': 'EG', 'guid': '3iJXjtU9D8MecnuL6QHokQ', 'area': 15.00000000000001, 'volume': 43.50000000000003, 'category': 'HNF'}, {'name': 'Unterstand', 'site': 'Gebäude', 'story': 'EG', 'guid': '1blxsCHeX4GBZwBWx57aMQ', 'area': 55.517, 'volume': 160.9993, 'category': 'HNF'}])