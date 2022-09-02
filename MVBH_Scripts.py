# MeshVoid's Bone Helper addon scripts to be used by operators
import bpy


class MVBH_Scripts():
    """Class to run or test all the methods run by the addon. Change these to edit values executed by other functions of the addon. """

    def __init__(self):
        """Initialization values"""
        self.root_name = "ROOT"
        self.root_size = 2

        self.def_prefix = "DEF-"
        self.tgt_prefix = "TGT-"
        self.ctl_prefix = "CTL-"
        self.mch_prefix = "MCH-"
        self.ik_prefix = "IK-"
        self.fk_prefix = "FK-"

        self.left_suffix = "-L"
        self.right_suffix = "-R"
        self.center_suffix = "-C"

        self.def_prefix_len = len(self.def_prefix)
        self.tgt_prefix_len = len(self.tgt_prefix)
        self.ctl_prefix_len = len(self.ctl_prefix)
        self.mch_prefix_len = len(self.mch_prefix)
        self.ik_prefix_len = len(self.ik_prefix)
        self.fk_prefix_len = len(self.fk_prefix)

        self.l_suffix_len = len(self.left_suffix)
        self.r_suffix_len = len(self.right_suffix)
        self.c_suffix_len = len(self.center_suffix)

        self.def_prefix_checklist = [
            "def-", "def.", "def_", "deform", "d.", "d_", "d-"]
        self.l_suffix_checklist = []
        self.r_suffix_checklist = []
        self.c_suffix_checklist = []

        # Layer_management
        self.root_layer = 0
        self.def_layer = 1
        self.tgt_layer = 2
        self.ctl_layer = 3


# ____ BONE STORAGE AND SELECTION

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
        #selected_armature = bpy.context.active_object.name
        # won't require armature to be selected?
        selected_armature = bpy.context.view_layer.objects.active.name
        return selected_armature

    def select_all_def_bones(self, extend=False):
        """Select all deform bones in the viewport based on the user's prefix"""
        bpy.ops.object.select_pattern(
            pattern=self.def_prefix + '*', case_sensitive=True, extend=extend)
        def_bones = self.get_selected_bones()
        return def_bones

    def select_all_tgt_bones(self, extend=False):
        """Select all target bones in the viewport based on the user's prefix"""
        bpy.ops.object.select_pattern(
            pattern=self.tgt_prefix + '*', case_sensitive=True, extend=extend)
        tgt_bones = self.get_selected_bones()
        return tgt_bones

    def select_all_bones_by_prefix(self, bone_prefix=''):
        "Select specific bone/bones by specifying a certain prefix name"
        bpy.ops.object.select_pattern(
            pattern=bone_prefix + '*', case_sensitive=True, extend=False)
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
            bpy.ops.pose.select_all(action='DESELECT')
        elif bpy.context.mode == "EDIT_ARMATURE":
            bpy.ops.armature.select_all(action='DESELECT')

# _________SCRIPTS___________

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
            bpy.context.object.pose.bones[bone.name].rotation_mode = 'XYZ'
        if toggle_editmode:
            bpy.ops.object.editmode_toggle()

    def set_copy_transforms_constraint(self, con_bones, con_targets):
        i = 0
        for bone in con_bones:
            bpy.ops.object.select_pattern(
                pattern=bone.name, case_sensitive=True, extend=False)
            # set currently selected bone in the viewport active

            self.set_selected_bone_active()

            bpy.ops.pose.constraint_add(type='COPY_TRANSFORMS')
            bpy.context.object.pose.bones[bone.name].constraints[
                "Copy Transforms"].target = bpy.data.objects[self.get_selected_armature()]
            bpy.context.object.pose.bones[bone.name].constraints["Copy Transforms"].subtarget = con_targets[i].name
            i += 1

    def set_left_suffix(self):
        """Adds self.left_suffix to selected bones."""
        # TODO: make use of self.l_suffix_checklist
        self.toggle_mode(editmode=True)

        for bone in self.get_selected_bones():
            bone_name_ending = bone.name[-self.l_suffix_len:]

            if ".l" in bone_name_ending.lower() or "_l" in bone_name_ending.lower() or "-l" in bone_name_ending.lower():
                # display it in UI?
                #print(f"Bone already had a left side tag, changed it to: {self.left_suffix}.")
                bone.name = bone.name[:-self.l_suffix_len] + self.left_suffix
            elif ".r" in bone_name_ending.lower() or "_r" in bone_name_ending.lower() or "-r" in bone_name_ending.lower():
                # display it in UI
                #print(f"Bone already had a right side tag, changed it to: {self.left_suffix}.")
                bone.name = bone.name[:-self.l_suffix_len] + self.left_suffix
            else:
                bone.name = bone.name + self.left_suffix

    def set_right_suffix(self):
        """Adds self.right_suffix to selected bones."""
        # TODO: make use of self.r_suffix_checklist
        self.toggle_mode(editmode=True)

        for bone in self.get_selected_bones():
            bone_name_ending = bone.name[-self.r_suffix_len:]

            if ".r" in bone_name_ending.lower() or "_r" in bone_name_ending.lower() or "-r" in bone_name_ending.lower():
                # display it in UI?
                #print(f"Bone already had a right side tag, changed it to: {self.right_suffix}.")
                bone.name = bone.name[:-self.r_suffix_len] + self.right_suffix
            elif ".l" in bone_name_ending.lower() or "_l" in bone_name_ending.lower() or "-l" in bone_name_ending.lower():
                # display it in UI
                # print(
                #     f"Bone already had a left side tag, changed it to: {self.right_suffix}.")
                bone.name = bone.name[:-self.r_suffix_len] + self.right_suffix
            else:
                bone.name = bone.name + self.right_suffix

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

    def set_def_bones(self):
        """Sets Deform value ON and adds a self.def_prefix prefix to selected bones"""
        # TODO: make use of self.def_prefix_checklist
        self.toggle_mode(editmode=True)
        
        for bone in self.get_selected_bones():
            if self.def_prefix not in bone.name[:self.def_prefix_len]:
                # Check if "DEF" is not already in the name of the bone
                # Add "DEF_" Prefix to selected bones.
                new_name = self.def_prefix + bone.name
                bone.name = new_name
            # if self.def_prefix in bone.name[:self.def_prefix_len]:
                #print("DEF is already in prefix, editing other attributes")

        for bone in self.get_selected_bones():
            # Set Deform value ON for selected bones.
            bone.use_deform = True

        self.set_xyz_rotation_mode()

    def set_ctl_bones(self):
        """Sets Deform value OFF on selected bones and replaces any suffix on the bone
        to CTL-, applies CopyTransform constraints"""
        self.toggle_mode(editmode=True)
        



    def add_root_bone(self):
        """Add a root bone to the rig"""
        if bpy.context.mode == "POSE":
            self.toggle_mode(editmode=True)
        self.deselect_all_bones()
        bpy.ops.armature.bone_primitive_add(name=self.root_name)
        self.select_bone_by_name(bone_name=self.root_name)
        self.set_selected_bone_active()
        bpy.context.active_bone.tail[2] = 0
        bpy.context.active_bone.tail[1] = self.root_size
        bpy.ops.armature.roll_clear()
        self.set_xyz_rotation_mode()

    def add_tgt_bones(self):
        """Duplicates bones sets Deform value OFF and replaces DEF suffix to TGT, 
        applies CopyTransform constraints"""
        self.toggle_mode(editmode=True)

        bpy.ops.armature.duplicate()  # duplicate all bones

        for bone in self.get_selected_bones():
            bone_name_ending = bone.name[-4:]
            bone.use_deform = False  # Set Deform value ON for selected bones.

            if self.def_prefix not in bone.name:
                bone.name = self.tgt_prefix + bone.name  # Add "TGT_" suffix to name
                if ".00" in bone_name_ending:
                    # Remove redundant numerical endings
                    bone.name = bone.name[:-4]

            elif self.def_prefix in bone.name:
                # Check if "DEF" is not already in the name of the bone
                # Add "TGT_" Prefix to selected bones
                # Replace "DEF_" prefix to "TGT"
                bone.name = bone.name.replace(
                    self.def_prefix, self.tgt_prefix)
                if ".00" in bone_name_ending:
                    # Remove redundant numerical endings
                    bone.name = bone.name[:-4]

        self.set_xyz_rotation_mode()






    def set_def_tgt_hierarchy(self):
        """Set Deform-Target bone hierarchy with all necessary parameters"""
        self.toggle_mode(posemode=True)
        def_bones = self.select_all_def_bones()
        tgt_bones = self.select_all_tgt_bones()
        self.set_copy_transforms_constraint(def_bones, tgt_bones)

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
        


# Testing my functions here:
scripts = MVBH_Scripts()

# scripts.set_def_bones()
# scripts.set_left_suffix()
# scripts.set_right_suffix()

# scripts.add_tgt_bones()
# scripts.set_def_tgt_hierarchy()
# scripts.add_root_bone()
# scripts.parent_def_bones_to_root()

scripts.parent_selected_bones_to_root()


# TODO:

# Add CTRL_ Bones to TGT_Bones
# Display debug messages in the info panel
