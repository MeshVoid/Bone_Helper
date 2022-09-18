# MeshVoid's Bone Helper addon user interface
import bpy


class MVBH_Main_Menu(bpy.types.Menu):
    bl_idname = "VIEW3D_MT_MVBH_Main_Menu"
    bl_label = "MV BoneHelper"

    def draw(self, context):
        layout = self.layout
        row = layout.row(align=True)
        split = layout.split()
        col = split.column()

        # use existing menus
        layout.menu("VIEW3D_MT_MVBH_Root_Menu",
                    icon="PMARKER_ACT", text="ROOT/PROP")
        layout.menu("VIEW3D_MT_MVBH_Def_Menu",
                    icon="BONE_DATA", text="DEF/TGT")
        layout.menu("VIEW3D_MT_MVBH_Ctl_Menu",
                    icon="BONE_DATA", text="CTL/MCH")
        layout.menu("VIEW3D_MT_MVBH_Bone_Type_Menu", text="FUNCTION",
                    icon="GROUP_BONE")
        layout.menu("VIEW3D_MT_MVBH_Suffix_Menu",
                    icon="ARROW_LEFTRIGHT", text="SIDES")
        layout.menu("VIEW3D_MT_MVBH_Hierarchy_Menu",
                    icon="CONSTRAINT_BONE", text="HIERARCHY")
        layout.menu("VIEW3D_MT_MVBH_Selection_Menu",
                    icon="RESTRICT_SELECT_OFF", text="SELECT")
        layout.menu("VIEW3D_MT_MVBH_Rename_Menu",
                    icon="FILE_TEXT", text="RENAME")


class MVBH_Def_Menu(bpy.types.Menu):
    bl_idname = "VIEW3D_MT_MVBH_Def_Menu"
    bl_label = "DEF Bones Sub Menu"

    def draw(self, context):
        layout = self.layout
        row = layout.row(align=True)
        split = layout.split()
        col = split.column()
        layout.operator("mvbh.add_def_bones", text="ADD DEF", icon="BONE_DATA")
        layout.operator("mvbh.set_def_bones", text="SET DEF", icon="BONE_DATA")
        layout.separator()
        layout.operator("mvbh.add_tgt_bones", text="ADD TGT", icon="BONE_DATA")
        layout.operator("mvbh.set_tgt_bones", text="SET TGT", icon="BONE_DATA")
        layout.separator()
        layout.operator("mvbh.set_def_tgt_hierarchy",
                        text="DEF->TGT->ROOT", icon="CONSTRAINT_BONE")


class MVBH_Ctl_Menu(bpy.types.Menu):
    bl_idname = "VIEW3D_MT_MVBH_Ctl_Menu"
    bl_label = "CTL Bones Sub Menu"

    def draw(self, context):
        layout = self.layout
        layout.operator("mvbh.add_ctl_bones", text="ADD CTL", icon="BONE_DATA")
        layout.operator("mvbh.set_ctl_bones", text="SET CTL", icon="BONE_DATA")
        layout.separator()
        layout.operator("mvbh.add_mch_bones", text="ADD MCH", icon="BONE_DATA")
        layout.operator("mvbh.set_mch_bones", text="SET MCH", icon="BONE_DATA")


class MVBH_Suffix_Menu(bpy.types.Menu):
    bl_idname = "VIEW3D_MT_MVBH_Suffix_Menu"
    bl_label = "Bones Suffix Menu"

    def draw(self, context):
        layout = self.layout
        row = layout.row(align=True)
        split = layout.split()
        col = split.column()
        layout.operator("mvbh.set_left_suffix", text="Left", icon="EVENT_L")
        layout.operator("mvbh.set_right_suffix", text="Right", icon="EVENT_R")
        layout.operator("mvbh.set_center_suffix",
                        text="Center", icon="EVENT_C")


class MVBH_Root_Menu(bpy.types.Menu):
    bl_idname = "VIEW3D_MT_MVBH_Root_Menu"
    bl_label = "Root and property menu"

    def draw(self, context):
        layout = self.layout
        layout.operator("mvbh.add_root_bone", text="ROOT", icon="PMARKER_ACT")
        layout.operator("mvbh.add_prop_bone", text="PROP", icon="PMARKER_SEL")
        layout.separator()
        layout.operator("mvbh.parent_to_root_bone",
                        text="Parent->Bone->Root", icon="GROUP_BONE")


class MVBH_Hierarchy_Menu(bpy.types.Menu):
    bl_idname = "VIEW3D_MT_MVBH_Hierarchy_Menu"
    bl_label = "Hierarchy of constraint menu"

    def draw(self, context):
        layout = self.layout
        layout.operator("mvbh.set_copy_transforms_hierarchy",
                        text="CopyTranform Hierarchy", icon="CON_TRANSLIKE")
        layout.operator("mvbh.set_copy_rotation_hierarchy",
                        text="CopyRotation Hierarchy", icon="CON_ROTLIKE")
        layout.operator("mvbh.set_copy_location_hierarchy",
                        text="CopyLocation Hierarchy", icon="CON_LOCLIKE")
        layout.operator("mvbh.set_copy_scale_hierarchy",
                        text="CopyScale Hierarchy", icon="CON_SIZELIKE")


class MVBH_Bone_Type_Menu(bpy.types.Menu):
    bl_idname = "VIEW3D_MT_MVBH_Bone_Type_Menu"
    bl_label = "Bone type menu"

    def draw(self, context):
        layout = self.layout
        layout.operator("mvbh.set_ik_suffix", text="IK", icon="EVENT_I")
        layout.operator("mvbh.set_fk_suffix", text="FK", icon="EVENT_F")
        layout.operator("mvbh.set_twk_suffix", text="TWEAK", icon="EVENT_T")
        layout.operator("mvbh.set_swtch_suffix", text="SWTCH", icon="EVENT_S")
        layout.operator("mvbh.set_pole_suffix", text="POLE", icon="EVENT_P")


# TODO: FINISH SELECTION AND RENAME MENUS - SEPARATE SELECTION AND
# RENAMING COMMON NAMES
class MVBH_Selection_Menu(bpy.types.Menu):
    bl_idname = "VIEW3D_MT_MVBH_Selection_Menu"
    bl_label = "Selection menu"
    bl_description = "Contains operations for selecting bone groups"

    def draw(self, context):
        layout = self.layout
        layout.operator("mvbh.select_left", text="Left", icon="EVENT_L")
        layout.operator("mvbh.select_right", text="Right", icon="EVENT_R")
        layout.operator("mvbh.select_center", text="Center", icon="EVENT_C")
        layout.separator()
        layout.operator("mvbh.select_def", text="DEF", icon="BONE_DATA")
        layout.operator("mvbh.select_tgt", text="TGT", icon="BONE_DATA")
        layout.operator("mvbh.select_ctl", text="CTL", icon="BONE_DATA")
        layout.operator("mvbh.select_mch", text="MCH", icon="BONE_DATA")
        layout.separator()
        layout.operator("mvbh.select_ik", text="IK", icon="GROUP_BONE")
        layout.operator("mvbh.select_fk", text="FK", icon="GROUP_BONE")
        layout.operator("mvbh.select_twk", text="TWEAK", icon="GROUP_BONE")
        layout.operator("mvbh.select_swtch", text="SWITCH", icon="GROUP_BONE")
        layout.operator("mvbh.select_pole", text="POLE", icon="GROUP_BONE")


class MVBH_Rename_Menu(bpy.types.Menu):
    bl_idname = "VIEW3D_MT_MVBH_Rename_Menu"
    bl_space_type = "VIEW_3D"
    bl_label = "Rename menu"
    bl_description = "Contains operations for renaming selected bones"

    def draw(self, context):
        layout = self.layout
        row = layout.row(align=True)
        layout.operator("mvbh.remove_zeroes", text="Remove 0",
                        icon="LINENUMBERS_ON")
        layout.operator("mvbh.enumerate_bones",
                        text="Enumerate", icon="LINENUMBERS_ON")
        layout.separator()

        # List of names is here ->  MVBH_OT_replace_bone_name in operators.py
        props = layout.operator("mvbh.replace_bone_name", text="Bone->Spine")
        props.new_name = "Spine"
        props = layout.operator("mvbh.replace_bone_name", text="Bone->Neck")
        props.new_name = "Neck"
        props = layout.operator("mvbh.replace_bone_name", text="Bone->Head")
        props.new_name = "Head"
        props = layout.operator("mvbh.replace_bone_name", text="Bone->Jaw")
        props.new_name = "Jaw"
        props = layout.operator("mvbh.replace_bone_name", text="Bone->Limb")
        props.new_name = "Limb"
        layout.separator()
        props = layout.operator(
                            "mvbh.replace_bone_name",text="Bone->Shoulder")
        props.new_name = "Shoulder"
        props = layout.operator(
                            "mvbh.replace_bone_name", text="Bone->UpperLimb")
        props.new_name = "UpperLimb"
        props = layout.operator("mvbh.replace_bone_name", text="Bone->Arm")
        props.new_name = "Arm"
        props = layout.operator("mvbh.replace_bone_name", text="Bone->Forearm")
        props.new_name = "Forearm"
        props = layout.operator("mvbh.replace_bone_name", text="Bone->Hand")
        props.new_name = "Hand"
        props = layout.operator("mvbh.replace_bone_name", text="Bone->Finger")
        props.new_name = "Finger"
        layout.separator()
        props = layout.operator("mvbh.replace_bone_name", text="Bone->Pelvis")
        props.new_name = "Pelvis"
        props = layout.operator("mvbh.replace_bone_name", text="Bone->Hip")
        props.new_name = "Hip"
        props = layout.operator(
                        "mvbh.replace_bone_name",text="Bone->LowerLimb")
        props.new_name = "LowerLimb"
        props = layout.operator("mvbh.replace_bone_name", text="Bone->Leg")
        props.new_name = "Leg"
        props = layout.operator("mvbh.replace_bone_name", text="Bone->Thigh")
        props.new_name = "Thigh"
        props = layout.operator("mvbh.replace_bone_name", text="Bone->Knee")
        props.new_name = "Knee"
        props = layout.operator("mvbh.replace_bone_name", text="Bone->Heel")
        props.new_name = "Heel"
        props = layout.operator("mvbh.replace_bone_name", text="Bone->Ankle")
        props.new_name = "Ankle"
        props = layout.operator("mvbh.replace_bone_name", text="Bone->Toe")
        props.new_name = "Toe"
        layout.separator()
        props = layout.operator("mvbh.replace_bone_name", text="Bone->Tail")
        props.new_name = "Tail"
        props = layout.operator("mvbh.replace_bone_name", text="Bone->Ear")
        props.new_name = "Ear"
        props = layout.operator("mvbh.replace_bone_name", text="Bone->Claw")
        props.new_name = "Claw"
        layout.separator
        props = layout.operator("mvbh.replace_bone_name", text="Bone->Eye")
        props.new_name = "Eye"       
