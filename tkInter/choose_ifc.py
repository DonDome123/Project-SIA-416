import tkinter as tk
import ifcopenshell
import collections
from .ifc_processor import read_source_ifc

room_list = []
project_name = ""

def open_ifc_file(file_path, text_output):
    global room_list
    global project_name

    text_output.delete("1.0", tk.END)

    ifc_file = ifcopenshell.open(file_path)
    room_list = read_source_ifc(file_path)

    project_name = ifc_file.by_type("IfcProject")[0].get_info()["Name"]
    
    rooms_per_story = collections.defaultdict(int)
    for room in room_list:
        rooms_per_story[room["story"]] += 1
    for story, num_rooms in rooms_per_story.items():
        text_output.insert(tk.END, f"Story {story} contains: {num_rooms} rooms\n")
        
    for i, room in enumerate(room_list):
        missing = ",".join([key for key, val in room.items() if val is None])
        if missing != "":
            text_output.insert(tk.END, f"Room {i} is missing: {missing}\n")
    if missing != "":
        room_list = []
        return

def get_rooms():
    global room_list
    return room_list

def get_project_name():
    return project_name
