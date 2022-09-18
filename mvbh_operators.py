# MeshVoid's Bone Helper addon operators
import bpy
from .mvbh_methods import MVBH_Scripts
from .mvbh_info import MVBH_Messages
# TODO: DEFINE ALL OPERATORS TO BE USED IN ADDON


class MVBH_Operator():
    def __init__(self):
        self.script = MVBH_Scripts()
        self.info = MVBH_Messages()
        global replaced_bone_name
        self.replaced_bone_name = ""


    def check_errors(self):
        if not bool(bpy.context.selected_objects):
            self.info.display_err(2)
            self.report({"ERROR"}, self.info.errors[2])
            return {"CANCELLED"}
        if not bool(bpy.context.selected_bones):
            self.info.display_err(0)
            self.report({"ERROR"}, self.info.errors[0])
            return {"CANCELLED"}



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

    delete: bpy.props.BoolProperty(
        name="Delete Constraints",
        description="Delete constraints that have been previously assigned the the bone",
        default=False
    )

    def execute(self, context):
        if self.check_errors():
            return {"CANCELLED"}
        self.script.make_bone_group(
            prefix=self.script.def_prefix, deform=True)
        self.script.move_selected_bones_to_layer(
            layer_number=self.script.def_layer,
            layer_name=self.script.def_prefix)
        if self.delete:
            self.script.delete_all_constraints()
        self.info.display_msg(2)
        self.report({"OPERATOR"}, self.info.messages[2])
        return {"FINISHED"}


class MVBH_OT_set_tgt_bones(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.set_tgt_bones"
    bl_label = "Set Target bones"
    bl_description = "Set Target bone properties to selected bones"
    bl_options = {"REGISTER", "UNDO"}

    delete: bpy.props.BoolProperty(
        name="Delete Constraints",
        description="Delete constraints that have been previously assigned the the bone",
        default=False
    )

    def execute(self, context):
        if self.check_errors():
            return {"CANCELLED"}
        self.script.make_bone_group(
            prefix=self.script.tgt_prefix)
        self.script.move_selected_bones_to_layer(
            layer_number=self.script.tgt_layer,
            layer_name=self.script.tgt_prefix)
        if self.delete:
            self.script.delete_all_constraints()
        self.info.display_msg(3)
        self.report({"OPERATOR"}, self.info.messages[3])
        return {"FINISHED"}


class MVBH_OT_set_ctl_bones(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.set_ctl_bones"
    bl_label = "Set Control bones"
    bl_description = "Set Control bone properties to selected bones"
    bl_options = {"REGISTER", "UNDO"}

    delete: bpy.props.BoolProperty(
        name="Delete Constraints",
        description="Delete constraints that have been previously assigned the the bone",
        default=False
    )

    def execute(self, context):
        if self.check_errors():
            return {"CANCELLED"}
        self.script.make_bone_group(prefix=self.script.ctl_prefix)
        self.script.move_selected_bones_to_layer(
            layer_number=self.script.ctl_layer,
            layer_name=self.script.ctl_prefix)
        if self.delete:
            self.script.delete_all_constraints()
        self.info.display_msg(4)
        self.report({"OPERATOR"}, self.info.messages[4])
        return {"FINISHED"}


class MVBH_OT_set_mch_bones(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.set_mch_bones"
    bl_label = "Set Mechanism bones"
    bl_description = "Set Mechanism bone properties to selected bones"
    bl_options = {"REGISTER", "UNDO"}

    delete: bpy.props.BoolProperty(
        name="Delete Constraints",
        description="Delete constraints that have been previously assigned the the bone",
        default=False
    )

    def execute(self, context):
        if self.check_errors():
            return {"CANCELLED"}
        self.script.make_bone_group(prefix=self.script.mch_prefix)
        self.script.move_selected_bones_to_layer(
            layer_number=self.script.mch_layer,
            layer_name=self.script.mch_prefix)
        if self.delete:
            self.script.delete_all_constraints()
        self.info.display_msg(5)
        self.report({"OPERATOR"}, self.info.messages[5])
        return {"FINISHED"}


class MVBH_OT_set_left_suffix(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.set_left_suffix"
    bl_label = "Set Left side suffix"
    bl_description = "Set Left side suffix to selected bones"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        if self.check_errors():
            return {"CANCELLED"}
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
        if self.check_errors():
            return {"CANCELLED"}
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
        if self.check_errors():
            return {"CANCELLED"}
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
        self.script.toggle_mode(objectmode=True)
        if self.script.root_name in bpy.data.armatures[self.script.get_selected_armature()].bones.keys():
            self.info.display_err(3)
            self.report({"ERROR"}, self.info.errors[3])
            self.script.toggle_mode(editmode=True)
            return{"CANCELLED"}
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
        self.script.toggle_mode(objectmode=True)
        if self.script.prop_name in bpy.data.armatures[self.script.get_selected_armature()].bones.keys():
            self.info.display_err(4)
            self.report({"ERROR"}, self.info.errors[4])
            self.script.toggle_mode(editmode=True)
            return{"CANCELLED"}
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

    delete: bpy.props.BoolProperty(
        name="Delete Constraints",
        description="Delete constraints that have been previously assigned the the bone",
        default=False
    )

    def execute(self, context):
        if self.check_errors():
            return {"CANCELLED"}
        self.script.make_bone_group(
            prefix=self.script.def_prefix, duplicate=True, deform=True)
        self.script.move_selected_bones_to_layer(
            layer_number=self.script.def_layer,
            layer_name=self.script.def_prefix)
        if self.delete:
            self.script.delete_all_constraints()
        self.info.display_msg(9)
        self.report({"OPERATOR"}, self.info.messages[9])
        return {"FINISHED"}


class MVBH_OT_add_tgt_bones(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.add_tgt_bones"
    bl_label = "Add Target Bones"
    bl_description = "Add new Target bones based on the selection"
    bl_options = {"REGISTER", "UNDO"}

    delete: bpy.props.BoolProperty(
        name="Delete Constraints",
        description="Delete constraints that have been previously assigned the the bone",
        default=False
    )

    def execute(self, context):
        if self.check_errors():
            return {"CANCELLED"}
        self.script.make_bone_group(
            prefix=self.script.tgt_prefix, duplicate=True)
        self.script.move_selected_bones_to_layer(
            layer_number=self.script.tgt_layer,
            layer_name=self.script.tgt_prefix)
        if self.delete:
            self.script.delete_all_constraints()
        self.info.display_msg(27)
        self.report({"OPERATOR"}, self.info.messages[27])
        return {"FINISHED"}


class MVBH_OT_add_ctl_bones(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.add_ctl_bones"
    bl_label = "Add Control bones"
    bl_description = "Add new Control bones based on the selection"
    bl_options = {"REGISTER", "UNDO"}

    delete: bpy.props.BoolProperty(
        name="Delete Constraints",
        description="Delete constraints that have been previously assigned the the bone",
        default=False
    )

    def execute(self, context):
        if self.check_errors():
            return {"CANCELLED"}
        self.script.make_bone_group(
            prefix=self.script.ctl_prefix, duplicate=True)
        self.script.move_selected_bones_to_layer(
            layer_number=self.script.ctl_layer,
            layer_name=self.script.ctl_prefix)
        if self.delete:
            self.script.delete_all_constraints()
        self.info.display_msg(8)
        self.report({"OPERATOR"}, self.info.messages[4])
        return {"FINISHED"}


class MVBH_OT_add_mch_bones(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.add_mch_bones"
    bl_label = "Add Mechanism bones"
    bl_description = "Add new Mechanism bones based on the selection"
    bl_options = {"REGISTER", "UNDO"}

    delete: bpy.props.BoolProperty(
        name="Delete Constraints",
        description="Delete constraints that have been previously assigned the the bone",
        default=False
    )

    def execute(self, context):
        if self.check_errors():
            return {"CANCELLED"}
        self.script.make_bone_group(
            prefix=self.script.mch_prefix, duplicate=True)
        self.script.move_selected_bones_to_layer(
            layer_number=self.script.mch_layer,
            layer_name=self.script.mch_prefix)
        if self.delete:
            self.script.delete_all_constraints()
        self.info.display_msg(5)
        self.report({"OPERATOR"}, self.info.messages[5])
        return {"FINISHED"}


class MVBH_OT_set_copy_transforms_hierarchy(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.set_copy_transforms_hierarchy"
    bl_label = "Set Copy Transform Hierarchy"
    bl_description = "Set copy transforms constraints depending on the bone hierarchy selected by user that goes as follows: DEF<-TGT<-MCH<-CTL"
    bl_options = {"REGISTER", "UNDO"}

    use_local_space: bpy.props.BoolProperty(
        name="Use Local Space",
        description="Toggle Use Local Space instead of World Space",
        default=False,
    )

    def execute(self, context):
        if self.check_errors():
            return {"CANCELLED"}
        self.script.set_copy_constraint_hierarchy(
            copy_trans=True, local_space=self.use_local_space
            )
        self.info.display_msg(20)
        self.report({"OPERATOR"}, self.info.messages[20])
        return{"FINISHED"}


class MVBH_OT_set_copy_rotation_hierarchy(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.set_copy_rotation_hierarchy"
    bl_label = "Set Copy Rotation Hierarchy"
    bl_description = "Set copy rotation constraints depending on the bone hierarchy selected by user that goes as follows: DEF<-TGT<-MCH<-CTL"
    bl_options = {"REGISTER", "UNDO"}

    use_local_space: bpy.props.BoolProperty(
        name="Use Local Space",
        description="Toggle Use Local Space instead of World Space",
        default=False,
    )

    def execute(self, context):
        if self.check_errors():
            return {"CANCELLED"}
        self.script.set_copy_constraint_hierarchy(
            copy_rot=True, local_space=self.use_local_space
            )
        self.info.display_msg(22)
        self.report({"OPERATOR"}, self.info.messages[22])
        return{"FINISHED"}


class MVBH_OT_set_copy_location_hierarchy(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.set_copy_location_hierarchy"
    bl_label = "Set Copy Location Hierarchy"
    bl_description = "Set copy location constraints depending on the bone hierarchy selected by user that goes as follows: DEF<-TGT<-MCH<-CTL"
    bl_options = {"REGISTER", "UNDO"}

    use_local_space: bpy.props.BoolProperty(
        name="Use Local Space",
        description="Toggle Use Local Space instead of World Space",
        default=False,
    )

    def execute(self, context):
        if self.check_errors():
            return {"CANCELLED"}
        self.script.set_copy_constraint_hierarchy(
            copy_loc=True, local_space=self.use_local_space
            )
        self.info.display_msg(23)
        self.report({"OPERATOR"}, self.info.messages[23])
        return{"FINISHED"}


class MVBH_OT_set_copy_scale_hierarchy(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.set_copy_scale_hierarchy"
    bl_label = "Set Copy Scale Hierarchy"
    bl_description = "Set Copy Scale Constraints depending on the bone hierarchy selected by user that goes as follows: DEF<-TGT<-MCH<-CTL"
    bl_options = {"REGISTER", "UNDO"}

    use_local_space: bpy.props.BoolProperty(
        name="Use Local Space",
        description="Toggle Use Local Space instead of World Space",
        default=False,
    )

    def execute(self, context):
        if self.check_errors():
            return {"CANCELLED"}
        self.script.set_copy_constraint_hierarchy(
            copy_scale=True, local_space=self.use_local_space
            )
        self.info.display_msg(24)
        self.report({"OPERATOR"}, self.info.messages[24])
        return{"FINISHED"}


class MVBH_OT_set_def_tgt_hierarchy(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.set_def_tgt_hierarchy"
    bl_label = "Set Deform and Target bone Hierarchy"
    bl_description = "Set copy transforms constraints to all Deform and Target bones in armature and parent Deform bones to Root bone"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        if self.check_errors():
            return {"CANCELLED"}
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
        if self.check_errors():
            return {"CANCELLED"}
        self.script.parent_selected_bones_to_root()
        self.info.display_msg(7)
        self.report({"OPERATOR"}, self.info.messages[7])
        return{"FINISHED"}


class MVBH_OT_set_ik_suffix(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.set_ik_suffix"
    bl_label = "Set IK bone type suffix"
    bl_description = "Set IK bone suffix to currently selected bones"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        if self.check_errors():
            return {"CANCELLED"}
        self.script.set_bone_suffix(self.script.ik_suffix)
        self.script.move_selected_bones_to_layer(
            self.script.ik_layer, self.script.ik_suffix)
        self.info.display_msg(13)
        self.report({"OPERATOR"}, self.info.messages[13])
        return{"FINISHED"}


class MVBH_OT_set_fk_suffix(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.set_fk_suffix"
    bl_label = "Set FK bone type suffix"
    bl_description = "Set FK bone suffix to currently selected bones"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        if self.check_errors():
            return {"CANCELLED"}
        self.script.set_bone_suffix(self.script.fk_suffix)
        self.script.move_selected_bones_to_layer(
            self.script.ctl_layer, self.script.ctl_suffix)
        self.info.display_msg(14)
        self.report({"OPERATOR"}, self.info.messages[14])
        return{"FINISHED"}


class MVBH_OT_set_twk_suffix(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.set_twk_suffix"
    bl_label = "Set Tweak bone type suffix"
    bl_description = "Set Tweak bone suffix to currently selected bones"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        if self.check_errors():
            return {"CANCELLED"}
        self.script.set_bone_suffix(self.script.twk_suffix)
        self.script.move_selected_bones_to_layer(
            self.script.twk_layer, self.script.twk_suffix)
        self.info.display_msg(15)
        self.report({"OPERATOR"}, self.info.messages[15])
        return{"FINISHED"}


class MVBH_OT_set_swtch_suffix(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.set_swtch_suffix"
    bl_label = "Set Tweak bone type suffix"
    bl_description = "Set Tweak bone suffix to currently selected bones"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        if self.check_errors():
            return {"CANCELLED"}
        self.script.set_bone_suffix(self.script.swtch_suffix)
        self.script.move_selected_bones_to_layer(
            self.script.swtch_layer, self.script.swtch_suffix)
        self.info.display_msg(16)
        self.report({"OPERATOR"}, self.info.messages[16])
        return{"FINISHED"}


class MVBH_OT_set_pole_suffix(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.set_pole_suffix"
    bl_label = "Set Pole bone type suffix"
    bl_description = "Set Pole bone suffix to currently selected bones"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        if self.check_errors():
            return {"CANCELLED"}
        self.script.set_bone_suffix(self.script.pole_suffix)
        self.script.move_selected_bones_to_layer(
            self.script.pole_layer, self.script.pole_suffix)
        self.info.display_msg(18)
        self.report({"OPERATOR"}, self.info.messages[18])
        return{"FINISHED"}


class MVBH_OT_select_left(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.select_left"
    bl_label = "Select Left Side"
    bl_description = "Select bones with Left side suffix"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        self.script.select_all_bones_by_suffix(
            bone_suffix=self.script.left_suffix)
        return{"FINISHED"}


class MVBH_OT_select_right(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.select_right"
    bl_label = "Select Right Side"
    bl_description = "Select bones with Right side suffix"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        self.script.select_all_bones_by_suffix(
            bone_suffix=self.script.right_suffix)
        return{"FINISHED"}


class MVBH_OT_select_center(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.select_center"
    bl_label = "Select Center side"
    bl_description = "Select bones with Center side suffix"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        self.script.select_all_bones_by_suffix(
            bone_suffix=self.script.center_suffix)
        return{"FINISHED"}


class MVBH_OT_select_def(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.select_def"
    bl_label = "Select Deform bones"
    bl_description = "Select all Deform bones"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        self.script.select_all_bones_by_prefix(
            bone_prefix=self.script.def_prefix)
        return{"FINISHED"}


class MVBH_OT_select_tgt(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.select_tgt"
    bl_label = "Select Target bones"
    bl_description = "Select all Target bones"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        self.script.select_all_bones_by_prefix(
            bone_prefix=self.script.tgt_prefix)
        return{"FINISHED"}


class MVBH_OT_select_ctl(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.select_ctl"
    bl_label = "Select Control bones"
    bl_description = "Select all Control bones"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        self.script.select_all_bones_by_prefix(
            bone_prefix=self.script.ctl_prefix)
        return{"FINISHED"}


class MVBH_OT_select_mch(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.select_mch"
    bl_label = "Select Mechanism bones"
    bl_description = "Select all Mechanism bones"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        self.script.select_all_bones_by_prefix(
            bone_prefix=self.script.mch_prefix)
        return{"FINISHED"}


class MVBH_OT_select_ik(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.select_ik"
    bl_label = "Select IK bones"
    bl_description = "Select all IK bones"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        self.script.select_all_bones_by_suffix(
            bone_suffix=self.script.ik_suffix)
        return{"FINISHED"}


class MVBH_OT_select_fk(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.select_fk"
    bl_label = "Select IK bones"
    bl_description = "Select all FK bones"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        self.script.select_all_bones_by_suffix(
            bone_suffix=self.script.fk_suffix)
        return{"FINISHED"}


class MVBH_OT_select_twk(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.select_twk"
    bl_label = "Select Tweak bones"
    bl_description = "Select all Tweak bones"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        self.script.select_all_bones_by_suffix(
            bone_suffix=self.script.twk_suffix)
        return{"FINISHED"}


class MVBH_OT_select_swtch(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.select_swtch"
    bl_label = "Select Switch bones"
    bl_description = "Select all Switch bones"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        self.script.select_all_bones_by_suffix(
            bone_suffix=self.script.swtch_suffix)
        return{"FINISHED"}


class MVBH_OT_select_pole(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.select_pole"
    bl_label = "Select Pole bones"
    bl_description = "Select all Pole bones"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        self.script.select_all_bones_by_suffix(
            bone_suffix=self.script.pole_suffix)
        return{"FINISHED"}


class MVBH_OT_remove_zeroes(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.remove_zeroes"
    bl_label = "Remove Zeroes in bone names"
    bl_description = "Get rid of Zeroes in selected bones names"
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        if self.check_errors():
            return {"CANCELLED"}
        self.script.replace_in_bone_names(value="0", target="")
        self.info.display_msg(17)
        self.report({"OPERATOR"}, self.info.messages[17])
        return{"FINISHED"}


class MVBH_OT_enumerate_bones(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.enumerate_bones"
    bl_label = "Enumerate selected bones"
    bl_description = "Enumerate selected bones in consequential order"
    bl_option = {"REGISTER", "UNDO"}

    def execute(self, context):
        if self.check_errors():
            return {"CANCELLED"}
        self.script.enumerate_bones()
        return{"FINISHED"}


class MVBH_OT_replace_bone_name(bpy.types.Operator, MVBH_Operator):
    bl_idname = "mvbh.replace_bone_name"
    bl_label = "Replace bone name"
    bl_description = "Replace bone name to specified value in selected bones"
    bl_option = {"REGISTER", "UNDO"}

    target_name: bpy.props.StringProperty(
        name="Old Name",
        description="Old bone name to be replaced by new name",
        default="Bone",
    )

    new_name: bpy.props.StringProperty(
        name="New Name",
        description="Replace  old bone name to this value",
        default="Bone",
    )

    def execute(self, context):
        if self.check_errors():
            return {"CANCELLED"}
        selected_bones = self.script.get_selected_bones()
        check_list = ["Spine","Neck","Head","Jaw","Limb","Shoulder","UpperLimb","Arm","Forearm","Hand","Finger","Pelvis","Hip","LowerLimb","Leg","Thigh","Knee","Heel","Ankle","Toe","Tail","Ear","Claw","Eye"]
        for bone in selected_bones:
            bone.name = bone.name.replace(self.target_name, self.new_name)
            if "Bone" not in bone.name:
                for i in check_list:
                    if i in bone.name:
                        bone.name = bone.name.replace(i, self.new_name)
        return{"FINISHED"}