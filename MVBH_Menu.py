import bpy
from MVBH_Operator import *

class MV_BH_Menu(bpy.types.Menu):
    bl_label = "MV Bone Helper Menu"
    bl_idname = "OBJECT_MT_MV_BoneHelperMenu"
    
    def draw(self, context):
        layout = self.layout
        layout.label(text="Hello world!", icon="WORLD_DATA")
        layout.operator("MVBH_set_def_bones")
        layout.label(text="DEF Bones", icon="BONE_DATA")
        layout.label(text="DEF->TGT", icon="BONE_DATA")
        

def draw_item(self,context):
     layout = self.layout
     layout.menu(MV_BH_Menu.bl_idname)

def register():
     bpy.utils.register_class(MV_BH_Menu)

def unregister():
     bpy.utils.unregister_class(MV_BH_Menu)

if __name__ == "__main__":
     register()
     
    # The menu can also be called from scripts
     bpy.ops.wm.call_menu(name=MV_BH_Menu.bl_idname)