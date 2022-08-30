


import bpy


class MVBH_Scripts():
    """Class to run or test all the methods run by the addon. Change these to edit values executed by other functions of the addon. """

    def __init__(self):
        """Initialization values"""
        self.def_prefix = "DEF-"
        self.tgt_prefix = "TGT-"
        self.ctl_prefix = "CTL-"
        self.mch_prefix = "MCH-"
        self.ik_prefix = "IK-"
        self.fk_prefix = "FK-"
        self.root_name = "ROOT"
        
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


#____ Methods
    # NOTE: remove self. on return value names?
    def get_selected_bone_name(self):
        """Get single selected bone name"""
        self.selected_bone = bpy.context.selected_pose_bones[0].name
        return self.selected_bone
        
    def get_selected_bones(self):
        """Get all selected bones in the viewport"""
        self.selected_bones = bpy.context.selected_bones
        return self.selected_bones
    
    def get_selected_edit_bones(self):
        """Get selected edit bones and store them in the list edit_bones[]"""
        selection = bpy.context.selected_editable_bones
        self.edit_bones = []
        for bone in selection:
            self.edit_bones.append(bone)
        return self.edit_bones

    def get_selected_pose_bones(self):
        """Get selected pose bones and store them in the list pose_bones[]"""
        selection = bpy.context.selected_pose_bones
        self.pose_bones = []
        for bone in selection:
            self.pose_bones.append(bone)
        return self.pose_bones

    def get_selected_armature(self):
        """Return the name of a currently selected armature"""
        self.selected_armature = bpy.context.active_object.name
        return self.selected_armature

# _________SCRIPTS___________

    def select_all_def_bones(self):
        """Select all deform bones based on the user's prefix"""
        bpy.ops.object.select_pattern(
            pattern=self.def_prefix + '*', case_sensitive=True, extend=False)
        def_bones = self.get_selected_pose_bones()
        return def_bones

    def select_all_tgt_bones(self):
        """Select all traget bones based on the user's prefix"""
        bpy.ops.object.select_pattern(
            pattern=self.tgt_prefix + '*', case_sensitive=True, extend=False)
        tgt_bones = self.get_selected_pose_bones()
        return tgt_bones
    
    def select_bones_list(self):
        "Select specific bones in the list"

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

    def add_root_bone(self):
        """Add a root bone to the rig"""
        self.toggle_mode(editmode=True)
        bpy.ops.armature.bone_primitive_add(self.root_name)
        bpy.ops.transform.rotate(value=1.5708, orient_axis='X', orient_type='GLOBAL', orient_matrix=((4.93038e-32, 1, 2.22045e-16), (2.22045e-16, 4.93038e-32, 1), (1, 2.22045e-16, 4.93038e-32)),
                                 orient_matrix_type='VIEW', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

        bpy.ops.armature.align()

    def make_selected_bone_active(self):
        """Set selected bone in the viewport to active"""
        boneToSelect = bpy.data.objects[self.get_selected_armature(
        )].pose.bones[self.get_selected_bone_name()].bone
        # Set as active
        bpy.context.object.data.bones.active = boneToSelect
        #Select in viewport
        boneToSelect.select = True

    def set_xyz_rotation_mode(self, toggle_editmode=True):
        """Set selected bones rotation mode to 'XYZ' instead of quaternions"""
        self.toggle_mode(posemode=True)
        for bone in self.get_selected_pose_bones():
            bpy.context.object.pose.bones[bone.name].rotation_mode = 'XYZ'
        if toggle_editmode:
            bpy.ops.object.editmode_toggle()

    def set_copy_transforms_constraint(self, con_bones, con_targets):
        i = 0
        for bone in con_bones:
            bpy.ops.object.select_pattern(
                pattern=bone.name, case_sensitive=True, extend=False)
            # set currently selected bone in the viewport active

            self.make_selected_bone_active()

            bpy.ops.pose.constraint_add(type='COPY_TRANSFORMS')
            bpy.context.object.pose.bones[bone.name].constraints["Copy Transforms"].target = bpy.data.objects[self.get_selected_armature()]
            bpy.context.object.pose.bones[bone.name].constraints["Copy Transforms"].subtarget = con_targets[i].name
            i += 1   

    def set_left_suffix(self):
        """Adds self.left_suffix to selected bones."""
        self.toggle_mode(editmode=True)

        for bone in self.get_selected_bones():
            bone_name_ending = bone.name[-self.l_suffix_len:]

            if ".l" in bone_name_ending.lower() or "_l" in bone_name_ending.lower() or "-l" in bone_name_ending.lower():
                # display it in UI?
                print(
                    f"Bone already had a left side tag, changed it to: {self.left_suffix}.")
                bone.name = bone.name[:-self.l_suffix_len] + self.left_suffix
            elif ".r" in bone_name_ending.lower() or "_r" in bone_name_ending.lower() or "-r" in bone_name_ending.lower():
                # display it in UI
                print(
                    f"Bone already had a right side tag, changed it to: {self.left_suffix}.")
                bone.name = bone.name[:-self.l_suffix_len] + self.left_suffix
            else:
                bone.name = bone.name + self.left_suffix

    def set_right_suffix(self):
        """Adds self.right_suffix to selected bones."""
        self.toggle_mode(editmode=True)

        for bone in self.get_selected_bones():
            bone_name_ending = bone.name[-self.r_suffix_len:]

            if ".r" in bone_name_ending.lower() or "_r" in bone_name_ending.lower() or "-r" in bone_name_ending.lower():
                # display it in UI?
                print(
                    f"Bone already had a right side tag, changed it to: {self.right_suffix}.")
                bone.name = bone.name[:-self.r_suffix_len] + self.right_suffix
            elif ".l" in bone_name_ending.lower() or "_l" in bone_name_ending.lower() or "-l" in bone_name_ending.lower():
                # display it in UI
                print(
                    f"Bone already had a left side tag, changed it to: {self.right_suffix}.")
                bone.name = bone.name[:-self.r_suffix_len] + self.right_suffix
            else:
                bone.name = bone.name + self.right_suffix

    def set_def_bones(self):
        """Set deformation bones to selected bones"""
        self.toggle_mode(editmode=True)

        """Sets Deform value ON and adds a self.def_prefix prefix to selected bones"""
        for bone in self.get_selected_bones():
            if self.def_prefix not in bone.name[:self]:
                # Check if "DEF" is not already in the name of the bone
                # Add "DEF_" Prefix to selected bones.
                new_name = self.def_prefix + bone.name
                bone.name = new_name
            if self.def_prefix in bone.name[:self.def_prefix_len]:
                print("DEF is already in prefix, editing other attributes")

        for bone in self.get_selected_bones():
            # Set Deform value ON for selected bones.
            bone.use_deform = True

        self.set_xyz_rotation_mode()

    def set_tgt_bones(self):
        """Duplicates bones sets Deform value OFF and replaces DEF suffix to TGT, 
        applies CopyTransform constraints"""
        self.toggle_mode(editmode=True)

        bpy.ops.armature.duplicate()  # duplicate all bones

        for bone in self.get_selected_edit_bones():
            bone_name_ending = bone.name[-4:]
            bone.use_deform = False  # Set Deform value ON for selected bones.

            if self.def_prefix not in bone.name:
                bone.name = self.tgt_prefix + bone.name  # Add "TGT_" suffix to name
                if ".00" in bone_name_ending:
                    # Remove redundant numerical endings
                    bone.name = bone.name[:-4]

            elif self.def_prefix in bone.name:
                # Check if "DEF" is not already in the name of the bone
                # Add "TGT_" Prefix to selected bones.
                # Replace "DEF_" prefix to "TGT"g
                bone.name = bone.name.replace(
                    self.def_prefix, self.tgt_prefix)
                if ".00" in bone_name_ending:
                    # Remove redundant numerical endings appearing after duplication
                    bone.name = bone.name[:-4]

        self.set_xyz_rotation_mode()

    def set_def_tgt_hierarchy(self):
        """Set Deform-Target bone hierarchy with all necessary parameters"""
        self.toggle_mode(posemode=True)
        def_bones = self.select_all_def_bones()
        tgt_bones = self.select_all_tgt_bones()
        self.set_copy_transforms_constraint(def_bones, tgt_bones)

        # TODO: remove parents of selected bones



# Testing my functions here:
scripts = MVBH_Scripts()
#scripts.set_def_tgt_hierarchy()

scripts.set_def_bones()
# scripts.set_tgt_bones()
# bpy.ops.armature.select_all(action='SELECT')
# scripts.set_left_suffix()
# scripts.set_right_suffix()
# scripts.add_root_bone()

# if __name__ == '__main__':
#     action = MVBH_Actions()
#     action.set_def_bones()


# TODO:

# Add CTRL_ Bones to TGT_Bones
# Display debug messages in the info panel
