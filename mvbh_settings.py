# MeshVoid's Bone Helper addon settings

# TODO: Make sure that you can change naming convention of bone names and other parameters
# by directly changing values in MVBH_Scripts class
import bpy

class OBJECT_OT_addon_prefs(Operator):
    """Display example preferences"""
    bl_idname = "object.addon_prefs"
    bl_label = "Add-on Preferences Example"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        preferences = context.preferences
        addon_prefs = preferences.addons[__name__].preferences

        info = ("Path: %s, Number: %d, Boolean %r" %
                (addon_prefs.filepath, addon_prefs.number, addon_prefs.boolean))

        self.report({'INFO'}, info)
        print(info)

        return {'FINISHED'}

