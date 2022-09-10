# MeshVoid's Bone Helper addon settings

# TODO: Make sure that you can change naming convention of bone names and other parameters
# by directly changing values in MVBH_Scripts class
import bpy
import rna_keymap_ui


class MVBH_Preferences():
    def __init__(self):
        pass

    def execute(self, context):
        pass

    
    keys = {"MENU": [{"label": "Toggle Emulate 3 Button Mouse",
            "region_type": "WINDOW",
            "map_type": "KEYBOARD",
            "keymap": "Windows",
            "idname": "mvbh.main_menu",}]}