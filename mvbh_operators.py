# MeshVoid's Bone Helper addon operators
import bpy
from .mvbh_methods import MVBH_Scripts
from .mvbh_info import MVBH_Messages
# TODO: DEFINE ALL OPERATORS TO BE USED IN ADDON


class MVBH_Operator():
    def __init__(self):
        self.script = MVBH_Scripts()
        self.info = MVBH_Messages()
        

class MVBH_OT_main_menu(bpy.types.Operator):
    bl_idname = "mvbh.main_menu"
    bl_label = "MeshVoid Bone Helper Menu"
    bl_description = "Show's MeshVoid Bone Helped addon Main Menu"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        bpy.ops.wm.call_menu(name="VIEW3D_MT_MVBH_Main_Menu")
        return {"FINISHED"}


class MVBH_OT_set_def_bones(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.set_def_bones"
    bl_label = "Set Deform bones"
    bl_description = "Set Deform bone properties to selected bones"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        self.script.make_bone_group(
            prefix=self.script.def_prefix, deform=True)
        self.script.move_selected_bones_to_layer(
            layer_number=self.script.def_layer, 
            layer_name=self.script.def_prefix)
        self.info.display_msg(2)
        self.report({"OPERATOR"}, self.info.messages[2])
        return {"FINISHED"}


class MVBH_OT_set_tgt_bones(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.set_tgt_bones"
    bl_label = "Set Target bones"
    bl_description = "Set Target bone properties to selected bones"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        self.script.make_bone_group(
            prefix=self.script.tgt_prefix)
        self.script.move_selected_bones_to_layer(
            layer_number=self.script.tgt_layer, 
            layer_name=self.script.tgt_prefix)
        self.info.display_msg(3)
        self.report({"OPERATOR"}, self.info.messages[3])
        return {"FINISHED"}


class MVBH_OT_set_ctl_bones(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.set_ctl_bones"
    bl_label = "Set Control bones"
    bl_description = "Set Control bone properties to selected bones"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        self.script.make_bone_group(prefix=self.script.ctl_prefix)
        self.script.move_selected_bones_to_layer(
        layer_number=self.script.ctl_layer, 
        layer_name=self.script.ctl_prefix)
        self.info.display_msg(4)
        self.report({"OPERATOR"}, self.info.messages[4])
        return {"FINISHED"}


class MVBH_OT_set_mch_bones(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.set_mch_bones"
    bl_label = "Set Mechanism bones"
    bl_description = "Set Mechanism bone properties to selected bones"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        self.script.make_bone_group(prefix=self.script.mch_prefix)
        self.script.move_selected_bones_to_layer(
        layer_number=self.script.mch_layer, 
        layer_name=self.script.mch_prefix)
        self.info.display_msg(5)
        self.report({"OPERATOR"}, self.info.messages[5])
        return {"FINISHED"}


class MVBH_OT_set_left_suffix(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.set_left_suffix"
    bl_label = "Set Left side suffix"
    bl_description = "Set Left side suffix to selected bones"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        self.script.set_side_suffix(side=self.script.left_suffix)
        self.info.display_msg(10)
        self.report({"OPERATOR"}, self.info.messages[10])
        return {"FINISHED"}


class MVBH_OT_set_right_suffix(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.set_right_suffix"
    bl_label = "Set Right side suffix"
    bl_description = "Set Right side suffix to selected bones"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        self.script.set_side_suffix(side=self.script.right_suffix)
        self.info.display_msg(11)
        self.report({"OPERATOR"}, self.info.messages[11])
        return {"FINISHED"}


class MVBH_OT_set_center_suffix(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.set_center_suffix"
    bl_label = "Set Center bone side suffix"
    bl_description = "Set Center side suffix to selected bones"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        self.script.set_side_suffix(side=self.script.center_suffix)
        self.info.display_msg(12)
        self.report({"OPERATOR"}, self.info.messages[11])
        return {"FINISHED"}


class MVBH_OT_add_root_bone(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.add_root_bone"
    bl_label = "Add Root bone"
    bl_description = "Add a Root bone to currently selected Armature"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        self.script.add_root_bone()
        self.script.move_selected_bones_to_layer(
        layer_number=self.script.root_layer, 
        layer_name=self.script.root_name)
        self.info.display_msg(0)
        self.report({"OPERATOR"}, self.info.messages[0])
        return {"FINISHED"}


class MVBH_OT_add_prop_bone(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.add_prop_bone"
    bl_label = "Add Property bone"
    bl_description = "Add a Property bone to currently selected Armature"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        self.script.add_prop_bone()
        self.script.move_selected_bones_to_layer(
        layer_number=self.script.prop_layer, 
        layer_name=self.script.prop_name)
        self.info.display_msg(1)
        self.report({"OPERATOR"}, self.info.messages[1])
        return {"FINISHED"}


class MVBH_OT_add_def_bones(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.add_def_bones"
    bl_label = "Add Deform Bones"
    bl_description = "Add new Deform bones based on the selection"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        self.script.make_bone_group(
            prefix=self.script.def_prefix, duplicate=True, deform=True)
        self.script.move_selected_bones_to_layer(
        layer_number=self.script.def_layer, 
        layer_name=self.script.def_name)
        self.info.display_msg(3)
        self.report({"OPERATOR"}, self.info.messages[3])
        return {"FINISHED"}


class MVBH_OT_add_tgt_bones(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.add_tgt_bones"
    bl_label = "Add Target Bones"
    bl_description = "Add new Target bones based on the selection"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        self.script.make_bone_group(
            prefix=self.script.tgt_prefix, duplicate=True)
        self.script.move_selected_bones_to_layer(
        layer_number=self.script.tgt_layer, 
        layer_name=self.script.tgt_name)
        self.info.display_msg(3)
        self.report({"OPERATOR"}, self.info.messages[3])
        return {"FINISHED"}


class MVBH_OT_add_ctl_bones(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.add_ctl_bones"
    bl_label = "Add Control bones"
    bl_description = "Add new Control bones based on the selection"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        self.script.make_bone_group(
            prefix=self.script.ctl_prefix, duplicate=True)
        self.script.move_selected_bones_to_layer(
        layer_number=self.script.ctl_layer, 
        layer_name=self.script.ctl_name)
        self.info.display_msg(8)
        self.report({"OPERATOR"}, self.info.messages[4])
        return {"FINISHED"}


class MVBH_OT_add_mch_bones(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.add_mch_bones"
    bl_label = "Add Mechanism bones"
    bl_description = "Add new Mechanism bones based on the selection"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        self.script.make_bone_group(
            prefix=self.script.mch_prefix, duplicate=True)
        self.script.move_selected_bones_to_layer(
        layer_number=self.script.mch_layer, 
        layer_name=self.script.mch_name)
        self.info.display_msg(5)
        self.report({"OPERATOR"}, self.info.messages[5])
        return {"FINISHED"}


class MVBH_OT_set_copy_transforms_hierarchy(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.set_copy_transforms_hierarchy"
    bl_label = "Set Copy Transform Hierarchy"
    bl_description = "Set copy transforms constraints depending on the bone hierarchy selected by user that goes as follows: DEF<-TGT<-MCH/IK/FK<-CTL"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        self.script.set_copy_transforms_hierarchy()
        self.info.display_msg(20)
        self.report({"OPERATOR"}, self.info.messages[20])
        return{"FINISHED"}


class MVBH_OT_set_def_tgt_hierarchy(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.set_def_tgt_hierarchy"
    bl_label = "Set Deform and Target bone Hierarchy"
    bl_description = "Set copy transforms constraints to all Deform and Target bones in armature and parent Deform bones to Root bone"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        self.script.set_def_tgt_hierarchy()
        self.info.display_msg(21)
        self.report({"OPERATOR"}, self.info.messages[21])
        return{"FINISHED"}


class MVBH_OT_parent_to_root_bone(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.parent_to_root_bone"
    bl_label = "Parent to Root bone"
    bl_description = "Parent all currently selected bones to ROOT bone"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        self.script.parent_selected_bones_to_root()
        self.info.display_msg(7)
        self.report({"OPERATOR"}, self.info.messages[7])
        return{"FINISHED"}
