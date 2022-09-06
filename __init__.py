import bpy
from . mvbh_methods import MVBH_Scripts
from . mvbh_info import MVBH_Messages
from . mvbh_operators import MV_BoneHelper
from . mvbh_ui import MV_BH_Menu

bl_info = {
    "name" : "MeshVoid Bone Helper",
    "author" : "Chingiz Jumagulov aka MeshVoid, meshvoid.com",
    "description" : "",
    "blender" : (3, 2, 2),
    "version" : (0, 0, 7),
    "location" : "View3D > Armature Edit Mode > PieMenu",
    "warning" : "",
    "doc_url" : "https://github.com/MeshVoid/Bone_Helper",
    "category" : "Rigging"
}

def register():
    MV_BoneHelper.register()
    MV_BH_Menu.register()

def unregister():
    MV_BoneHelper.unregister()
    MV_BH_Menu.unregister()