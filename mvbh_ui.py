# MeshVoid's Bone Helper addon user interface
import bpy


class MVBH_Main_Menu(bpy.types.Menu):
    bl_idname = "VIEW3D_MT_MVBH_Main_Menu"
    bl_label = "MVBH Main Menu"

    def draw(self, context):
        layout = self.layout
        row = layout.row(align=True)
        split = layout.split()
        col = split.column()

        # use existing memu
        layout.menu("VIEW3D_MT_MVBH_Root_Menu",
                    icon="PMARKER_ACT", text="ROOT/PROP")
        layout.menu("VIEW3D_MT_MVBH_Def_Menu",
                    icon="BONE_DATA", text="DEF->TGT")
        layout.menu("VIEW3D_MT_MVBH_Ctl_Menu",
                    icon="GROUP_BONE", text="CTL->MCH")
        layout.menu("VIEW3D_MT_MVBH_Suffix_Menu",
                    icon="ARROW_LEFTRIGHT", text="SUFFIX")
        layout.menu("VIEW3D_MT_MVBH_Hierarchy_Menu",
                    icon="NODETREE", text="CNSTRNTS")


class MVBH_Def_Menu(bpy.types.Menu):
    bl_idname = "VIEW3D_MT_MVBH_Def_Menu"
    bl_label = "DEF Bones Sub Menu"

    def draw(self, context):
        layout = self.layout
        row = layout.row(align=True)
        split = layout.split()
        col = split.column()
        layout.operator("mvbh.set_def_bones", text="SET DEF", icon="BONE_DATA")
        layout.operator("mvbh.add_tgt_bones", text="ADD TGT", icon="BONE_DATA")
        layout.operator("mvbh.set_def_tgt_hierarchy",
                        text="DEF->TGT->ROOT", icon="BONE_DATA")

class MVBH_Ctl_Menu(bpy.types.Menu):
    bl_idname = "VIEW3D_MT_MVBH_Ctl_Menu"
    bl_label = "CTL Bones Sub Menu"

    def draw(self, context):
        layout = self.layout
        row = layout.row(align=True)
        split = layout.split()
        col = split.column()
        layout.operator("mvbh.add_ctl_bones", text="ADD CTL", icon="BONE_DATA")
        layout.operator("mvbh.set_ctl_bones", text="SET CTL", icon="BONE_DATA")
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


class MVBH_Root_Menu(bpy.types.Menu):
    bl_idname = "VIEW3D_MT_MVBH_Root_Menu"
    bl_label = "Root and property menu"

    def draw(self, context):
        layout = self.layout
        layout.operator("mvbh.add_root_bone", text="ROOT", icon="BONE_DATA")
        layout.operator("mvbh.add_prop_bone", text="PROP", icon="BONE_DATA")
        layout.operator("mvbh.parent_to_root_bone",
                text="Parent->Bone->Root", icon="BONE_DATA")


class MVBH_Hierarchy_Menu(bpy.types.Menu):
    bl_idname = "VIEW3D_MT_MVBH_Hierarchy_Menu"
    bl_label = "Hierarchy of constraint menu"

    def draw(self, context):
        layout = self.layout
        layout.operator("mvbh.set_copy_transforms_hierarchy",
                        text="CopyTranform Hierarchy", icon="NODETREE")

