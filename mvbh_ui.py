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
     layout.menu("VIEW3D_MT_MVBH_Def_Menu", icon="BONE_DATA", text="DEF->TGT")
     layout.menu("VIEW3D_MT_MVBH_Ctl_Menu", icon="BONE_DATA", text="CTL->MCH")
     layout.menu("VIEW3D_MT_MVBH_Suffix_Menu", icon="BONE_DATA", text="SUFFIX")



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
     layout.operator("mvbh.add_tgt_bones", text="ADD TGT", icon="BONE_DATA")
     layout.operator("mvbh.set_def_bones", text="SET DEF", icon="BONE_DATA")

class MVBH_Suffix_Menu(bpy.types.Menu):
    bl_idname = "VIEW3D_MT_MVBH_Suffix_Menu"
    bl_label = "Bones Suffix Menu"
    
    
    def draw(self, context):
     layout = self.layout
     row = layout.row(align=True)
     split = layout.split()
     col = split.column()
     layout.operator("mvbh.add_ctl_bones", text="ADD CTL", icon="BONE_DATA")
     layout.operator("mvbh.set_ctl_bones", text="SET CTL", icon="BONE_DATA")
     layout.operator("mvbh.add_tgt_bones", text="ADD TGT", icon="BONE_DATA")
     layout.operator("mvbh.set_def_bones", text="SET DEF", icon="BONE_DATA")  
