# MeshVoid's Bone Helper addon operators
import bpy
from .mvbh_methods import MVBH_Scripts
from .mvbh_info import MVBH_Messages
# TODO: DEFINE ALL OPERATORS TO BE USED IN ADDON


class MVBH_Operator():
    def __init__(self):
        self.run_script = MVBH_Scripts()
        self.show_info = MVBH_Messages()

# TODO: Make it work?
    # def check_for_errors(self,
    #                      check_mode=False, check_selection=False,
    #                      check_bone_selection=False):
    #     """Check if user forgot to select anything or enter edit mode or something"""
    #     if check_mode:
    #         if bpy.context.mode == "OBJECT":
    #             self.show_info.display_err(1)
    #             return False
    #         if check_bone_selection:
    #             if bpy.context.selected_objects is None:
    #                 self.show_info.display_err(0)
    #                 return False
    #     if check_selection:
    #         if bpy.context.selected_objects is None:
    #             self.show_info.display_err(2)
    #             return False
    #     else:
    #         return True


class MVBH_OT_main_menu(bpy.types.Operator):
    bl_idname = "mvbh.main_menu"
    bl_label = "Show Mesh Void Bone helper Bone Menu"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="VIEW3D_MT_MVBH_Main_Menu")
        return {"FINISHED"}


class MVBH_OT_set_def_bones(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.set_def_bones"
    bl_label = "Set Deform bone properties to selected bones in the viewport."
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        self.run_script.set_def_bones()
        self.show_info.display_msg(2)
        self.report({"OPERATOR"}, self.show_info.messages[2])
        return {"FINISHED"}


class MVBH_OT_set_ctl_bones(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.set_ctl_bones"
    bl_label = "Set selected bones as Control bones."
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        self.run_script.set_ctl_bones()
        self.show_info.display_msg(4)
        self.report({"OPERATOR"}, self.show_info.messages[4])
        return {"FINISHED"}


class MVBH_OT_set_left_suffix(bpy.types.Operator, MVBH_Operator):
    bl_label = "Adds Left side suffix to selected bones."
    bl_idname = "mvbh.set_left_suffix"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        self.run_script.set_left_suffix()
        self.show_info.display_msg(10)
        self.report({"OPERATOR"}, self.show_info.messages[10])
        return {"FINISHED"}


class MVBH_OT_set_right_suffix(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.set_right_suffix"
    bl_label = "Adds Right side suffix to selected bones."
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        self.run_script.set_right_suffix()
        self.show_info.display_msg(11)
        self.report({"OPERATOR"}, self.show_info.messages[11])
        return {"FINISHED"}


class MVBH_OT_add_root_bone(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.add_root_bone"
    bl_label = "Add a Root bone to currently selected Armature object."
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        #        proceed = self.check_for_errors(check_mode= True,
        #                 check_selection=True)
        self.run_script.add_root_bone()
        self.show_info.display_msg(0)
        self.report({"OPERATOR"}, self.show_info.messages[0])
        return {"FINISHED"}


class MVBH_OT_add_prop_bone(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.add_prop_bone"
    bl_label = "Add a Property bone to currently selected Armature object."
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        self.run_script.add_prop_bone()
        self.show_info.display_msg(1)
        self.report({"OPERATOR"}, self.show_info.messages[1])
        return {"FINISHED"}


class MVBH_OT_add_tgt_bones(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.add_tgt_bones"
    bl_label = "Add Target bones with appropriate naming convention and properties based on the selection."
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        self.run_script.add_tgt_bones()
        self.show_info.display_msg(3)
        self.report({"OPERATOR"}, self.show_info.messages[3])
        return {"FINISHED"}


class MVBH_OT_add_ctl_bones(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.add_ctl_bones"
    bl_label = """Add Control bones and set appropriate naming 
        convention and properties based on the selection."""
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        self.run_script.add_ctl_bones()
        self.show_info.display_msg(4)
        self.report({"OPERATOR"}, self.show_info.messages[4])
        return {"FINISHED"}


class MVBH_OT_set_copy_transforms_hierarchy(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.set_copy_transforms_hierarchy"
    bl_label = """Set copy transforms constraints depending on the bone hierarchy selected by user that goes as follows: DEF<-TGT<-MCH/IK/FK<-CTL"""
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        self.run_script.add_ctl_bones()
        self.show_info.display_msg(20)
        self.report({"OPERATOR"}, self.show_info.messages[20])
        return{"FINISHED"}


class MVBH_OT_set_def_tgt_hierarchy(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.set_def_tgt_hierarchy"
    bl_label = """Set copy transforms constraints to all DEF and TGT bones in armature"""
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        self.run_script.set_def_tgt_hierarchy()
        self.show_info.display_msg(21)
        self.report({"OPERATOR"}. self.show_info.messages[21])
        return{"FINISHED"}


class MVBH_OT_parent_to_root_bone(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.parent_to_root_bone"
    bl_label = """Parent all currently selected bones to ROOT bone"""
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        self.run_script.parent_selected_bones_to_root()
        self.show_info.display_msg(7)
        self.report({"OPERATOR"}. self.show_info.messages[7])
        return{"FINISHED"}
