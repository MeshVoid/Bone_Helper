import bpy

class MV_BH_Menu(bpy.types.Menu):
    bl_label = "MV Bone Helper Menu"
    bl_idname = "OBJECT_MT_MV_BoneHelperMenu"
    
    def draw(self, context):
        layout = self.layout
        layout.operator("wm.open_mainfile")

def register():
     bpy.utils.register_class(MVBoneHelperMenu)

def unregister():
     bpy.utils.unregister_class(MVBoneHelperMenu)

if __name__ == "__main__":
     register()
