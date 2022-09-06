import bpy
from . mvbh_ui import MVBH_Main_Menu, MVBH_Def_Menu, MVBH_Ctl_Menu, MVBH_Suffix_Menu
from . mvbh_operators import MVBH_OT_main_menu, MVBH_OT_set_def_bones, MVBH_OT_add_tgt_bones, MVBH_OT_add_ctl_bones, MVBH_OT_set_ctl_bones

bl_info = {
    "name": "MeshVoid Bone Helper",
    "author": "Chingiz Jumagulov aka MeshVoid, meshvoid.com",
    "description": "",
    "blender": (3, 2, 2),
    "version": (0, 0, 7),
    "location": "View3D > Armature Edit Mode > Custom Menu Popup",
    "warning": "",
    "doc_url": "https://github.com/MeshVoid/Bone_Helper",
    "category": "Rigging"
}

modules = [
    MVBH_Main_Menu,
    MVBH_Def_Menu,
    MVBH_Ctl_Menu,
    MVBH_Suffix_Menu,
    MVBH_OT_main_menu,
    MVBH_OT_set_def_bones,
    MVBH_OT_add_tgt_bones,
    MVBH_OT_add_ctl_bones,
    MVBH_OT_set_ctl_bones,
]


def register():
    for class_name in modules:
        bpy.utils.register_class(class_name)


def unregister():
    for class_name in modules:
        bpy.utils.unregister_class(class_name)


if __name__ == "__main__":
    register()
