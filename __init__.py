import bpy
from . mvbh_ui import *
from . mvbh_operators import *
from . mvbh_info import *
from . mvbh_settings import *

bl_info = {
    "name": "MeshVoid Bone Helper",
    "author": "Chingiz Jumagulov aka MeshVoid, meshvoid.com",
    "description": """MeshVoid's Bone Helper addon. Here to help 
    you with all your manual rigging bone managing needs.""",
    "blender": (3, 2, 2),
    "version": (0, 1, 3),
    "location": "View3D > Armature Edit Mode > Custom Menu Popup",
    "support": "COMMUNITY",
    "warning": "Report bugs on github: https://github.com/MeshVoid/Bone_Helper",
    "doc_url": "https://github.com/MeshVoid/Bone_Helper/",
    "category": "Rigging"
}

modules = [
    MVBH_Main_Menu,
    MVBH_Root_Menu,
    MVBH_Def_Menu,
    MVBH_Ctl_Menu,
    MVBH_Suffix_Menu,
    MVBH_Hierarchy_Menu,
    MVBH_OT_main_menu,
    MVBH_OT_add_def_bones,
    MVBH_OT_add_tgt_bones,
    MVBH_OT_add_ctl_bones,
    MVBH_OT_add_mch_bones,
    MVBH_OT_add_root_bone,
    MVBH_OT_add_prop_bone,
    MVBH_OT_set_def_bones,
    MVBH_OT_set_tgt_bones,
    MVBH_OT_set_ctl_bones,
    MVBH_OT_set_mch_bones,
    MVBH_OT_set_left_suffix,
    MVBH_OT_set_right_suffix,
    MVBH_OT_set_center_suffix,
    MVBH_OT_set_copy_transforms_hierarchy,
    MVBH_OT_set_def_tgt_hierarchy,
    MVBH_OT_parent_to_root_bone,
]


def register():
    for class_name in modules:
        bpy.utils.register_class(class_name)


def unregister():
    for class_name in modules:
        bpy.utils.unregister_class(class_name)


if __name__ == "__main__":
    register()
