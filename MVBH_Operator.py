import bpy


class MV_BoneHelper_OP(bpy.types.Operator):
    """Operator that spawns a menu to help with bone management"""

    bl_idname = "object.mv_bonehelper"
    bl_label = "MV_BoneHelper"

    def execute(self, context):
        return {'FINISHED'}
