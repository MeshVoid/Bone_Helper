# MeshVoid's Bone Helper addon operators

import bpy
from MVBH_Scripts import MVBH_Scripts

class MV_BoneHelper(MVBH_Scripts):
    """Main BoneHelper class"""
    def __init__(self):
        self.scripts = MVBH_Scripts()

    bl_options = {"REGISTER", "UNDO"}

class MVBH_DEF_bone(MV_BoneHelper, bpy.types.Operator):
    """Operator to turn selected bones into Deform bones"""
    bl_idname = "MVBH_set_def_bones"
    bl_label = "MV_BoneHelper"

    def execute(self, context):
        self.scripts.set_def_bones()
        return {'FINISHED'}

class MV_BoneHelper(bpy.types.Operator):
    

    bl_idname = "armature.mv_bonehelper"
    bl_label = "MV BoneHelper Operator"


    def menu_func(self, context):
        # add operator to a certain menu currently not used anywhere!
        self.layout.operator(MV_BoneHelper.bl_idname, text=MV_BoneHelper.bl_label)

# Register operator():
def register():
    bpy.utils.register_class(MV_BoneHelper)

def unregister():
    bpy.utils.unregister_class(MV_BoneHelper)

if __name__ == "__main__":
    register()

    # test call
    bpy.ops.armature.mv_bonehelper()
    
