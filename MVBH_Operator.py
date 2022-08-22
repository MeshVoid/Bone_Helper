import bpy

class MV_BoneHelper(bpy.types.Operator):
    """Operator that spawns a menu to help with bone management"""

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
    self.register()

    # test call
    bpy.ops.armature.mv_bonehelper()