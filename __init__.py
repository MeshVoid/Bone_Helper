import bpy
from . mvbh_ui import *
from . mvbh_operators import *

bl_info = {
    "name": "MeshVoid Bone Helper",
    "author": "Chingiz Jumagulov aka MeshVoid, meshvoid.com",
    "description": """MeshVoid's Bone Helper addon. Here to help you with all your manual rigging bone management needs.""",
    "blender": (3, 0, 0),
    "version": (0, 3, 0),
    "location": "View3D > Armature Edit\Pose Mode > Context Menu(RightClick)",
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
    MVBH_Bone_Type_Menu,
    MVBH_Hierarchy_Menu,
    MVBH_Selection_Menu,
    MVBH_Rename_Menu,
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
    MVBH_OT_remove_side_suffix,
    MVBH_OT_set_ik_suffix,
    MVBH_OT_set_fk_suffix,
    MVBH_OT_set_twk_suffix,
    MVBH_OT_set_swtch_suffix,
    MVBH_OT_set_pole_suffix,
    MVBH_OT_remove_function_suffix,
    MVBH_OT_set_copy_transforms_hierarchy,
    MVBH_OT_set_copy_rotation_hierarchy,
    MVBH_OT_set_copy_location_hierarchy,
    MVBH_OT_set_copy_scale_hierarchy,
    MVBH_OT_set_ik_chain,
    MVBH_OT_remove_all_constraints,
    MVBH_OT_set_def_tgt_hierarchy,
    MVBH_OT_parent_to_root_bone,
    MVBH_OT_remove_zeroes,
    MVBH_OT_enumerate_bones,
    MVBH_OT_replace_bone_name,
    MVBH_OT_remove_bone_prefix,
    MVBH_OT_remove_ghost_bones,
    MVBH_OT_select_left,
    MVBH_OT_select_right,
    MVBH_OT_select_center,
    MVBH_OT_select_def,
    MVBH_OT_select_tgt,
    MVBH_OT_select_ctl,
    MVBH_OT_select_mch,
    MVBH_OT_select_ik,
    MVBH_OT_select_fk,
    MVBH_OT_select_twk,
    MVBH_OT_select_swtch,
    MVBH_OT_select_pole,
]


def add_main_menu(self, context):
    self.layout.operator(
        "mvbh.main_menu", text="Bone Helper", icon="BONE_DATA")


def register():
    for class_name in modules:
        bpy.utils.register_class(class_name)

    bpy.types.VIEW3D_MT_armature_context_menu.append(add_main_menu)
    bpy.types.VIEW3D_MT_pose_context_menu.append(add_main_menu)


def unregister():
    for class_name in modules:
        bpy.utils.unregister_class(class_name)

    bpy.types.VIEW3D_MT_armature_context_menu.remove(add_main_menu)
    bpy.types.VIEW3D_MT_pose_context_menu.remove(add_main_menu)


if __name__ == "__main__":
    register()
