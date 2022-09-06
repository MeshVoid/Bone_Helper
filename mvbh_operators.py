# MeshVoid's Bone Helper addon operators
import bpy
from .mvbh_methods import MVBH_Scripts
from .mvbh_info import MVBH_Messages
# TODO: DEFINE ALL OPERATORS TO BE USED IN ADDON


class MVBH_Operator():
    def __init__(self):
        self.run_script = MVBH_Scripts()
        self.show_info = MVBH_Messages()


class MVBH_OT_main_menu(bpy.types.Operator):
    """Display MV Bone Helper Addon's Main Menu"""
    bl_idname = "mvbh.main_menu"
    bl_label = "Show Mesh Void Bone helper Bone Menu"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="VIEW3D_MT_MVBH_Main_Menu")
        return {'FINISHED'}


# class MVBH_OT_sub_menu(bpy.types.Operator):
#     """Show MVBH Sub Menu"""
#     bl_idname = "mvbh.sub_menu"
#     bl_label = "Show Mesh Void Bone helper Sub Menu"
#     bl_options = {"REGISTER", "UNDO"}

#     def execute(self, context):
#         bpy.ops.wm.call_menu(name="VIEW3D_MT_MVBH_Sub_Menu")
#         return {'FINISHED'}


class MVBH_OT_set_def_bones(bpy.types.Operator, MVBH_Operator):
    """Set Deform bone naming convention and properties to selected bones"""
    bl_idname = "mvbh.set_def_bones"
    bl_label = "Set Deform bone properties to selected bones in the viewport."
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        self.run_script.set_def_bones()
        self.show_info.display_msg(2)
        self.report({'OPERATOR'}, self.show_info.messages[2])
        return {'FINISHED'}


class MVBH_OT_set_ctl_bones(bpy.types.Operator, MVBH_Operator):
    """Set Control bones to the selected bones"""
    bl_idname = "mvbh.set_ctl_bones"
    bl_label = "Set selected bones as Control bones."
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        self.run_script.set_ctl_bones()
        self.show_info.display_msg(4)
        self.report({'OPERATOR'}, self.show_info.messages[4])
        return {'FINISHED'}


class MVBH_OT_add_tgt_bones(bpy.types.Operator, MVBH_Operator):
    """Add new Target bones with appropriate properties and naming convention to selected bones"""
    bl_idname = "mvbh.add_tgt_bones"
    bl_label = "Add Target bones with appropriate naming convention and properties based on the selection."
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        self.run_script.add_tgt_bones()
        self.show_info.display_msg(3)
        self.report({'OPERATOR'}, self.show_info.messages[3])

        return {'FINISHED'}


class MVBH_OT_add_ctl_bones(bpy.types.Operator, MVBH_Operator):
    """Add Control bones to the selected bones"""
    bl_idname = "mvbh.add_ctl_bones"
    bl_label = "Add Control bones and set appropriate naming convention and properties based on the selection."
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        self.run_script.add_ctl_bones()
        self.show_info.display_msg(4)
        self.report({'OPERATOR'}, self.show_info.messages[4])

        return {'FINISHED'}
