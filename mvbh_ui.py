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
        layout.operator("mvbh.remove_ghost_bones",
                        text="Remove Ghosts", icon="CANCEL")


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
        layout.operator("mvbh.remove_bone_prefix",
                        text="Remove", icon="CANCEL")


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
        layout.operator("mvbh.remove_bone_prefix",
                        text="Remove", icon="CANCEL")


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
        layout.operator("mvbh.remove_side_suffix",
                        text="Remove", icon="CANCEL")


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
        layout.operator(
            "mvbh.set_copy_transforms_hierarchy", text="CopyTranform Hierarchy", icon="CON_TRANSLIKE")
        layout.operator(
            "mvbh.set_copy_rotation_hierarchy", text="CopyRotation Hierarchy", icon="CON_ROTLIKE")
        layout.operator(
            "mvbh.set_copy_location_hierarchy", text="CopyLocation Hierarchy", icon="CON_LOCLIKE")
        layout.operator(
            "mvbh.set_copy_scale_hierarchy", text="CopyScale Hierarchy", icon="CON_SIZELIKE")
        layout.operator("mvbh.set_ik_chain", text="IK Chain", icon="CON_KINEMATIC")
        layout.operator(
            "mvbh.remove_all_constraints", text="Remove", icon="CANCEL")


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
        layout.operator("mvbh.remove_function_suffix",
                        text="Remove", icon="CANCEL")


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
        col_flow = layout.column_flow(columns=2, align=False)
        grid = layout.grid_flow(row_major=True, columns=2,
                                even_columns=True, even_rows=True, align=True)
        row = layout.row(align=True)
        split = layout.split(align=True)

        col_flow.operator(
            "mvbh.remove_zeroes", text="Remove 0", icon="LINENUMBERS_ON")
        # List of names is here ->  MVBH_OT_replace_bone_name in operators.py
        col_flow.separator()
        props = col_flow.operator(
            "mvbh.replace_bone_name", text="Bone->Spine", icon="FILE_TEXT")
        props.new_name = "Spine"
        props = col_flow.operator(
            "mvbh.replace_bone_name", text="Bone->Torso", icon="FILE_TEXT")
        props.new_name = "Torso"
        props = col_flow.operator(
            "mvbh.replace_bone_name", text="Bone->Chest", icon="FILE_TEXT")
        props.new_name = "Chest"
        props = col_flow.operator(
            "mvbh.replace_bone_name", text="Bone->Neck", icon="FILE_TEXT")
        props.new_name = "Neck"
        props = col_flow.operator(
            "mvbh.replace_bone_name", text="Bone->Head", icon="FILE_TEXT")
        props.new_name = "Head"
        props = col_flow.operator(
            "mvbh.replace_bone_name", text="Bone->Jaw", icon="FILE_TEXT")
        props.new_name = "Jaw"
        col_flow.separator()
        props = col_flow.operator(
            "mvbh.replace_bone_name", text="Bone->Upper_limb", icon="FILE_TEXT")
        props.new_name = "Upper_limb"
        props = col_flow.operator(
            "mvbh.replace_bone_name", text="Bone->Limb", icon="FILE_TEXT")
        props.new_name = "Limb"
        props = col_flow.operator(
            "mvbh.replace_bone_name", text="Bone->Shoulder", icon="FILE_TEXT")
        props.new_name = "Shoulder"
        props = col_flow.operator(
            "mvbh.replace_bone_name", text="Bone->Arm", icon="FILE_TEXT")
        props.new_name = "Arm"
        props = col_flow.operator(
            "mvbh.replace_bone_name", text="Bone->Forearm", icon="FILE_TEXT")
        props.new_name = "Forearm"
        props = col_flow.operator(
            "mvbh.replace_bone_name", text="Bone->Hand", icon="FILE_TEXT")
        props.new_name = "Hand"
        props = col_flow.operator(
            "mvbh.replace_bone_name", text="Bone->Finger", icon="FILE_TEXT")
        props.new_name = "Finger"
        props = col_flow.operator(
            "mvbh.replace_bone_name", text="Bone->Thumb", icon="FILE_TEXT")
        props.new_name = "Thumb"
        col_flow.operator(
            "mvbh.enumerate_bones", text="Enumerate", icon="LINENUMBERS_ON")
        col_flow.separator()
        props = col_flow.operator(
            "mvbh.replace_bone_name", text="Bone->Pelvis", icon="FILE_TEXT")
        props.new_name = "Pelvis"
        props = col_flow.operator(
            "mvbh.replace_bone_name", text="Bone->Hip", icon="FILE_TEXT")
        props.new_name = "Hip"
        props = col_flow.operator(
            "mvbh.replace_bone_name", text="Bone->Lower_limb", icon="FILE_TEXT")
        props.new_name = "Lower_limb"
        props = col_flow.operator(
            "mvbh.replace_bone_name", text="Bone->Leg", icon="FILE_TEXT")
        props.new_name = "Leg"
        props = col_flow.operator(
            "mvbh.replace_bone_name", text="Bone->Thigh", icon="FILE_TEXT")
        props.new_name = "Thigh"
        props = col_flow.operator(
            "mvbh.replace_bone_name", text="Bone->Knee", icon="FILE_TEXT")
        props.new_name = "Knee"
        props = col_flow.operator(
            "mvbh.replace_bone_name", text="Bone->Shin", icon="FILE_TEXT")
        props.new_name = "Shin"
        props = col_flow.operator(
            "mvbh.replace_bone_name", text="Bone->Ankle", icon="FILE_TEXT")
        props.new_name = "Ankle"
        props = col_flow.operator(
            "mvbh.replace_bone_name", text="Bone->Foot", icon="FILE_TEXT")
        props.new_name = "Foot"
        props = col_flow.operator(
            "mvbh.replace_bone_name", text="Bone->Toe", icon="FILE_TEXT")
        props.new_name = "Toe"
        col_flow.separator()
        props = col_flow.operator(
            "mvbh.replace_bone_name", text="Bone->Tail", icon="FILE_TEXT")
        props.new_name = "Tail"
        props = col_flow.operator(
            "mvbh.replace_bone_name", text="Bone->Ear", icon="FILE_TEXT")
        props.new_name = "Ear"
        props = col_flow.operator(
            "mvbh.replace_bone_name", text="Bone->Claw", icon="FILE_TEXT")
        props.new_name = "Claw"
        col_flow.separator
        props = col_flow.operator(
            "mvbh.replace_bone_name", text="Bone->Eye", icon="FILE_TEXT")
        props.new_name = "Eye"
