# MeshVoid's Bone Helper addon scripts to be used by operators
import bpy
from .mvbh_info import MVBH_Messages

# TODO: Learn how to show error messages in info view
# TODO: Finish writing logic for adding and setting bones
# TODO: Finish writing logic for layer hierarchy
# TODO: Refactor all [:len(suffix.bla_bla_bla)] to endswith() and startswith() <- because of PEP8 compliance


class MVBH_Scripts():
    """Class to run or test all the methods run by the addon. Change these to edit values executed by other parts of the addon. """

    def __init__(self):
        """Initialization values. Change these properties to modify your naming convention and other parameters."""
        self.root_name = "ROOT"
        self.root_size = 2
        self.prop_name = "PROPS"
        self.prop_size = 0.5

    # NOTE: DEF/TGT/CTL/MCH - Always come before IK/FK
    # MCH-SWITCH
    # CTL-FK

        self.def_prefix = "DEF-"
        self.tgt_prefix = "TGT-"
        self.ctl_prefix = "CTL-"
        self.mch_prefix = "MCH-"

        # NOTE: I think IK, FK, TWEAK and SWITCH Should be suffixes
        # Maybe call the helper bones?

        self.ik_suffix = "-IK"
        self.fk_suffix = "-FK"
        self.twk_suffix = "-TWK"
        self.swtch_suffix = "-SWITCH"

        # self.ik_prefix = "IK-"
        # self.fk_prefix = "FK-"
        # self.twk_prefix = "TWK-"
        # self.ctl_fk_prefix = "CTL-FK-"
        # self.mch_ik_prefix = "MCH-IK-"
        # self.mch_fk_prefix = "MCH-FK-"
        # self.mch_swt_prefix = "MCH-SWITCH-" # do you need it?

        self.left_suffix = "-L"
        self.right_suffix = "-R"
        self.center_suffix = "-C"

        # Layer numbers
        self.root_layer = 0
        self.prop_layer = 1
        self.def_layer = 2
        self.tgt_layer = 3
        self.ctl_layer = 4
        self.mch_layer = 5
        self.ik_layer = 6
        self.twk_layer = 7

        self.info = MVBH_Messages()

        self.sides_checklist = [
            "-l", ".l", "_l", "-left", ".left", "_left", "-lft", ".lft", "_lft", "-lt", ".lt", "_lt", "-r", ".r", "_r", "-right", ".right", "_right", "-rght", ".rght", "._rght", "-rt", ".rt", "_rt",
            "-c", ".c", "_c", "-center", ".center", "_center", "-cnt", ".cnt", "_cnt", "-ct", ".ct", "_ct", "-cent", ".cent", "_cent",
        ]

# =====================================================================
#                ***BONE AND SELECTION LISTS***
#                  METHODS WITH RETURN VALUES
# =====================================================================

    def get_selected_bone_name(self):
        """Get single selected bone name"""
        if bpy.context.mode == "POSE":
            bone_name = bpy.context.selected_pose_bones[0].name
            return bone_name
        elif bpy.context.mode == "EDIT_ARMATURE":
            bone_name = bpy.context.selected_editable_bones[0].name
            return bone_name

    def get_selected_bones(self):
        """Get selected bones in either pose or edit mode and store them in edit_bones[] or pose_bones[] lists"""
        if bpy.context.mode == "POSE":
            selection = bpy.context.selected_pose_bones
            pose_bones = []
            for bone in selection:
                pose_bones.append(bone)
            return pose_bones
        elif bpy.context.mode == "EDIT_ARMATURE":
            selection = bpy.context.selected_editable_bones
            edit_bones = []
            for bone in selection:
                edit_bones.append(bone)
            return edit_bones

    def get_selected_armature(self):
        """Return the name of a currently selected armature"""
        selected_armature = bpy.context.view_layer.objects.active.name
        return selected_armature

    def get_all_bone_names(self):
        """Return full list of names in currently selected armature"""
        bones_list = bpy.context.active_object.pose.bones[:]
        for bone in bones_list:
            bones_list.append(bone.name)
        return bones_list

    def select_all_def_bones(self, extend=False):
        """Select all deform bones in the viewport based on the user's prefix"""
        bpy.ops.object.select_pattern(
            pattern=self.def_prefix + "*", case_sensitive=True, extend=extend)
        def_bones = self.get_selected_bones()
        return def_bones

    def select_all_tgt_bones(self, extend=False):
        """Select all target bones in the viewport based on the user's prefix"""
        bpy.ops.object.select_pattern(
            pattern=self.tgt_prefix + "*", case_sensitive=True, extend=extend)
        tgt_bones = self.get_selected_bones()
        return tgt_bones

    def select_all_bones_by_prefix(self, bone_prefix=''):
        "Select specific bone/bones by specifying a certain prefix name"
        bpy.ops.object.select_pattern(
            pattern=bone_prefix + "*", case_sensitive=True, extend=False)
        selected_bones = self.get_selected_bones()
        return selected_bones

    def select_bone_by_name(self, bone_name='', deselect=False, extend=False, case_sensitive=True):
        "Select specific bone/bones by specifying a name"
        if deselect:
            self.deselect_all_bones()
        bpy.ops.object.select_pattern(
            pattern=bone_name, case_sensitive=case_sensitive, extend=extend)
        selected_bones = self.get_selected_bones()
        return selected_bones

    def deselect_all_bones(self):
        """Deselect all bones in current armature bone mode"""
        if bpy.context.mode == "POSE":
            bpy.ops.pose.select_all(action="DESELECT")
        elif bpy.context.mode == "EDIT_ARMATURE":
            bpy.ops.armature.select_all(action="DESELECT")

    def get_selected_bone_group(self, prefix):
        """Get selected bone group by it's prefix name and store all bone values in bone_group list"""
        selected_bones = self.get_selected_bones()
        bone_group = []
        for bone in selected_bones:
            if bone.name.startswith(prefix):
                bone_group.append(bone)
        return bone_group

# =====================================================================
#                          ***SCRIPTS***
# =====================================================================

    def toggle_mode(self, posemode=False, editmode=False):
        """Toggle to edit mode from other modes or toggle to pose mode from other modes, set args: posemode or editmode to TRUE"""
        if editmode:
            if bpy.context.mode == "POSE":
                bpy.ops.object.editmode_toggle()
            elif bpy.context.mode == "OBJECT":
                bpy.ops.object.editmode_toggle()
        if posemode:
            if bpy.context.mode == "EDIT_ARMATURE":
                bpy.ops.object.posemode_toggle()
            elif bpy.context.mode == "OBJECT":
                bpy.ops.object.posemode_toggle()

    def set_xyz_rotation_mode(self, toggle_editmode=True):
        """Set selected bones rotation mode to 'XYZ' instead of quaternions"""
        self.toggle_mode(posemode=True)
        for bone in self.get_selected_bones():
            bpy.context.object.pose.bones[bone.name].rotation_mode = "XYZ"
        if toggle_editmode:
            bpy.ops.object.editmode_toggle()

    def move_selected_bones_to_layer(self, layer_number, layer_name):
        """Set bones list to a specified bone layer and assign a layer_name"""
        layers_list = [False] * 32
        layers_list[layer_number] = True 
        bpy.ops.armature.bone_layers(layers=layers_list)
        bpy.context.object.data.layers[layer_number] = True
        #assing custom property name and number
        bpy.data.armatures[self.get_selected_armature(
        )][f'layer_name_{layer_number}'] = layer_name


    def set_copy_transforms_constraint(self, con_bones, con_targets):
        """Set copy transforms constraints con_bones - target bones list, con_targets - subtarget
        bones list"""
        i = 0
        for bone in con_bones:
            bpy.ops.object.select_pattern(
                pattern=bone.name, case_sensitive=True, extend=False)
            # set currently selected bone in the viewport active

            self.set_selected_bone_active()

            bpy.ops.pose.constraint_add(type="COPY_TRANSFORMS")
            bpy.context.object.pose.bones[bone.name].constraints[
                "Copy Transforms"].target = bpy.data.objects[self.get_selected_armature()]
            bpy.context.object.pose.bones[bone.name].constraints["Copy Transforms"].subtarget = con_targets[i].name
            i += 1

    def set_copy_transforms_hierarchy(self):
        """Set copy transforms constraints depending on the bone hierarchy selected by user that goes as follows: DEF<-TGT<-MCH/IK/FK<-CTL"""
        if bpy.context.mode == "EDIT_ARMATURE":
            self.toggle_mode(posemode=True)

        def_bones = self.get_selected_bone_group(prefix=self.def_prefix)
        tgt_bones = self.get_selected_bone_group(prefix=self.tgt_prefix)
        ctl_bones = self.get_selected_bone_group(prefix=self.ctl_prefix)
        mch_bones = self.get_selected_bone_group(prefix=self.mch_prefix)
        ik_bones = self.get_selected_bone_group(prefix=self.ik_prefix)
        fk_bones = self.get_selected_bone_group(prefix=self.fk_prefix)
        # NOTE: check if it works now
        if def_bones and tgt_bones:
            self.set_copy_transforms_constraint(def_bones, tgt_bones)
        if tgt_bones and ctl_bones:
            self.set_copy_transforms_constraint(tgt_bones, ctl_bones)
        if tgt_bones and mch_bones:
            self.set_copy_transforms_constraint(tgt_bones, mch_bones)
        if mch_bones and ctl_bones:
            self.set_copy_transforms_constraint(mch_bones, ctl_bones)
        if ik_bones and ctl_bones:
            self.set_copy_transforms_constraint(ik_bones, ctl_bones)
        if fk_bones and ctl_bones:
            self.set_copy_transforms_constraint(fk_bones, ctl_bones)

    def set_side_suffix(self, side):
        """Adds specific Side suffix to selected bones."""
        # NOTE: Not working properly, but nice try
        to_rename = False
        to_add = False
        self.toggle_mode(editmode=True)
        for bone in self.get_selected_bones():
            suffix = bone.name[-len(side):]
            for i in self.sides_checklist:
                if i.lower() in suffix.lower():
                    to_rename = True
            if to_rename:
                bone.name = bone.name.replace(suffix, side)
                to_rename = False
            elif side.lower() not in bone.name[-len(side)]:
                to_add = True
            if to_add:
                bone.name = bone.name + side
                to_add = False

    def set_selected_bone_active(self):
        """Set selected bone to active depending on the mode the viewport is in"""
        if bpy.context.mode == "POSE":
            boneToSelect = bpy.data.objects[self.get_selected_armature(
            )].pose.bones[self.get_selected_bone_name()].bone
            # Set as active
            bpy.context.object.data.bones.active = boneToSelect
            #Select in viewport
            boneToSelect.select = True

        elif bpy.context.mode == "EDIT_ARMATURE":
            boneToSelect = bpy.data.armatures[self.get_selected_armature(
            )].edit_bones[self.get_selected_bone_name()]
            bpy.data.armatures[self.get_selected_armature(
            )].edit_bones.active = boneToSelect
            boneToSelect.select = True

    def add_root_bone(self):
        """Add a root bone to the rig"""
        self.toggle_mode(editmode=True)
        self.deselect_all_bones()
        bpy.ops.armature.bone_primitive_add(name=self.root_name)
        self.select_bone_by_name(bone_name=self.root_name)
        self.set_selected_bone_active()
        bpy.context.active_bone.tail[2] = 0
        bpy.context.active_bone.tail[1] = self.root_size
        bpy.ops.armature.roll_clear()
        bpy.context.active_bone.use_deform = False
        self.set_xyz_rotation_mode()

    def add_prop_bone(self):
        """Add a property bone to the rig"""
        self.toggle_mode(editmode=True)
        self.deselect_all_bones()
        bpy.ops.armature.bone_primitive_add(name=self.prop_name)
        self.select_bone_by_name(bone_name=self.prop_name)
        self.set_selected_bone_active()
        bpy.context.active_bone.head[2] = 4
        bpy.context.active_bone.tail[2] = 4.5
        bpy.context.active_bone.length = self.prop_size
        bpy.ops.armature.roll_clear()
        self.set_xyz_rotation_mode()
        self.parent_selected_bones_to_root()

    def make_bone_group(self, prefix, deform=False, duplicate=False, xyz=True):
        """Sets or adds bone prefix and specified parameters to selected bones"""
        self.toggle_mode(editmode=True)
        if duplicate:
            bpy.ops.armature.duplicate()
        for bone in self.get_selected_bones():
            bone_suffix = bone.name[-4:]
            if not bone.name.startswith(prefix):
                if bone.name.startswith(self.def_prefix):
                    bone.name = bone.name.replace(
                        self.def_prefix, prefix)
                if bone.name.startswith(self.ctl_prefix):
                    bone.name = bone.name.replace(
                        self.ctl_prefix, prefix)
                if bone.name.startswith(self.tgt_prefix):
                    bone.name = bone.name.replace(
                        self.tgt_prefix, prefix)
                if bone.name.startswith(self.mch_prefix):
                    bone.name = bone.name.replace(
                        self.mch_prefix, prefix)
                if not bone.name.startswith(prefix):
                    bone.name = prefix + bone.name
            if duplicate:
                if ".00" in bone_suffix:
                    bone.name = bone.name[:-4]
            bone.use_deform = deform
        if xyz:
            self.set_xyz_rotation_mode()

    def set_def_tgt_hierarchy(self):
        """Set Deform-Target bone hierarchy with all necessary parameters"""
        self.toggle_mode(posemode=True)
        def_bones = self.select_all_def_bones()
        tgt_bones = self.select_all_tgt_bones()
        self.set_copy_transforms_constraint(def_bones, tgt_bones)
        # if there's a root bone, parent def bones to root bone
        if bpy.data.armatures[self.get_selected_armature()].bones[self.root_name]:
            self.toggle_mode(editmode=True)
            self.parent_def_bones_to_root()

    def parent_def_bones_to_root(self):
        """Clear DEF bones parental relationships and parent them to root"""
        self.select_bone_by_name(bone_name=self.root_name)
        self.set_selected_bone_active()
        self.select_all_def_bones(extend=True)
        bpy.ops.armature.parent_set(type="OFFSET")

    def parent_tgt_bones_to_root(self):
        """Parent all TGT bones to root bone for whatever reason"""
        self.select_bone_by_name(bone_name=self.root_name)
        self.set_selected_bone_active()
        self.select_all_tgt_bones(extend=True)
        bpy.ops.armature.parent_set(type="OFFSET")

    def parent_selected_bones_to_root(self):
        """Parent any selected bones/bone in edit mode to root bone"""
        self.toggle_mode(editmode=True)
        selected_bones = self.get_selected_bones()
        self.select_bone_by_name(bone_name=self.root_name, deselect=True)
        self.set_selected_bone_active()
        for bone in selected_bones:
            self.select_bone_by_name(bone_name=bone.name, extend=True)
        bpy.ops.armature.parent_set(type="OFFSET")

    def remove_zeroes_name(self):
        """Remove zeroes from all the bones in the armature"""
        self.toggle_mode(editmode=True)
        bpy.ops.armature.select_all()
        self.get_selected_bones()
        
        # TODO:FINISH IT
