import os

import pandas as pd
import Helpers.Data_Helpers as hlp

def export_data(export_lst, conf_lst, export_folder):

    #Export der Daten als Excel
    #Export Extracted Data to Excel

    if len(export_lst) > 0:

        xls_file_name = "Export_Daten_IFC.xlsx"
        exp_path = os.path.join(export_folder, xls_file_name)

        check_file = os.path.isfile(exp_path)

        if(not(check_file)):
            pd.DataFrame([]).to_excel(exp_path)

        for exp_set in export_lst:
        
            col_lst = []
            col_lst.append("GUID")
            col_lst.append("Kategorie")
            
            _target_obj = hlp.filterConfig(exp_set.branch, conf_lst)
            print(_target_obj)
            
            if _target_obj != None:
                
                for _p_l in _target_obj.prop_list:
                    #print(_p_l)
                    _ps = _p_l.pset
                    _pr = _p_l.prop
                    
                    if(str(_ps) == "nan"):
                        _title = "{}".format(_pr)
                    else:
                        _title = "{}:{}".format(_ps, _pr)
                    
                    col_lst.append(_title)
                    print(_title)


                df = pd.DataFrame(exp_set.data, columns = col_lst)
                print(exp_set.data)
                df = pd.DataFrame(exp_set.data)
                
                with pd.ExcelWriter(exp_path, engine='openpyxl', if_sheet_exists='replace', mode='a') as writer:  
                    df.to_excel(writer, sheet_name=exp_set.branch, index=False)
                    
            
                

        print("Final Step: Finished Export Excel...")