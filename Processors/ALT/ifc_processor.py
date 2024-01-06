#Import der relevanten Module

import ifcopenshell
import ifcopenshell.util
import ifcopenshell.util.element
from ifcopenshell.util.selector import Selector

import os
import Processors.Data_Helpers as hlp

#Globale Variablen - Listen

export_lst = []



def process_ifc_data(conf_lst):

    #IFC Datein Auswerten und Daten strukturiert speichern

    for _c in conf_lst:
        
    
        _source_file = "{}".format(_c.source)
        _source_folder = "{}".format(_c.folder)

        _source_path = os.path.join(_source_folder, _source_file)
        check_file = os.path.isfile(_source_path)

        if(check_file):

            ifc_file = ifcopenshell.open(_source_path)
            elements = ifc_file.by_type(_c.category)
            
            tmp_exp_data_from_current_config = []
           
            for _e in elements:
                print(_e.Name)                
                tmp_exp_data = []  
                
                act_prop = ifcopenshell.util.element.get_psets(_e, psets_only=False)
                act_info = _e.get_info()
                
                try:
                    tmp_exp_data.append(act_info.get("GlobalId"))
                    tmp_exp_data.append(act_info.get("type"))
    
                except:
                    continue       
                
            
                for _p in _c.prop_list:
                    print(str(_p.pset) != "nan")
                    
                    try:
                        if(str(_p.pset) != "nan"):
                            act_val = act_prop.get(_p.pset).get(_p.prop)
                        else:                     
                            act_val = act_info.get(_p.prop)
                            
                        print(act_val)

                        tmp_exp_data.append(act_val)

                    except:
                        act_val = "" 
                        tmp_exp_data.append(act_val)
 
                        
                tmp_exp_data_from_current_config.append(tmp_exp_data)

                        
            
            exp_holder = hlp.Exp_Holder(_c.branch, tmp_exp_data_from_current_config)
            export_lst.append(exp_holder)

    return export_lst