# ifc_importer.py
import ifcopenshell

def read_source_ifc(source_path):

    file = ifcopenshell.open(source_path)
    products = file.by_type("IfcProduct")
    spaces =[]
    for i in products:
        if i.is_a("IfcSpace"):
            spaces.append(i)

    room_list = []

    for room in spaces:
        values =ifcopenshell.util.element.get_psets(room, qtos_only=True)
        name = room.get_info()["LongName"]
        site = getBuilding(room)
        story = getStorey(room)
        guid = room.get_info()["GlobalId"]
        area = values["BaseQuantities"]["NetFloorArea"]
        volume = values["BaseQuantities"]["GrossVolume"]
        values =ifcopenshell.util.element.get_psets(room)
        category = values["Pset_SpaceCommon"]["Category"]
        room_info = {
            "name": name,
            "site": site,
            "story": story,
            "guid": guid,
            "area": area,
            "volume": volume,
            "category": category
        }
        room_list.append(room_info)

    return room_list

def getStorey(ele):
    lev_name = ""

    if ele.is_a('IfcSpatialStructureElement'):
        lev_name = ele.Decomposes[0][4].Name
    else:
        lev_obj = ifcopenshell.util.element.get_container(ele)
        lev_name = lev_obj.Name

    return lev_name

def getBuilding(ele):

    building_name = ""

    if ele.is_a('IfcSpatialStructureElement'):
        lev_obj = ele.Decomposes[0][4]

    else:
        lev_obj = ifcopenshell.util.element.get_container(ele)

    building_obj = lev_obj.Decomposes[0][4]
    building_name = building_obj.Name

    return building_name


if __name__ == "__main__":
    read_source_ifc("./ARC_Modell_NEST_230328.ifc")
