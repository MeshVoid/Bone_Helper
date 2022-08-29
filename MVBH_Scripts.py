import bpy


class MVBH_Scripts():
    """Class to run or test all the methods run by the addon"""

    def __init__(self):
        self.def_bone_prefix = "DEF-"
        self.tgt_bone_prefix = "TGT-"
        self.left_side_suffix = "-L"
        self.right_side_suffix = "-R"
        self.center_side_suffix = "-C"

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
        self.toggle_mode()
        bpy.ops.armature.bone_primitive_add(name="ROOT")
        bpy.ops.transform.rotate(value=1.5708, orient_axis='X', orient_type='GLOBAL', orient_matrix=((4.93038e-32, 1, 2.22045e-16), (2.22045e-16, 4.93038e-32, 1), (1, 2.22045e-16, 4.93038e-32)),
                                 orient_matrix_type='VIEW', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

        bpy.ops.armature.align()

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
        """Return currently selected armature"""
        self.toggle_mode(editmode=True)
        bpy.ops.armature.select_all()
        self.selected_armature = bpy.context.selected_objects[0]
        return self.selected_armature

    def set_xyz_rotation_mode(self, toggle_editmode=True):
        """Set selected bones rotation mode to 'XYZ' instead of quaternions"""
        self.toggle_mode(posemode=True)
        for bone in self.get_selected_pose_bones():
            bpy.context.object.pose.bones[bone.name].rotation_mode = 'XYZ'
        if toggle_editmode:
            bpy.ops.object.editmode_toggle()

    def set_left_suffix(self):
        """Adds self.left_side_suffix to selected bones."""
        self.toggle_mode(editmode=True)

        for bone in self.get_selected_bones():
            bone_name_ending = bone.name[-2:]

            if ".l" in bone_name_ending.lower() or "_l" in bone_name_ending.lower() or "-l" in bone_name_ending.lower():
                # display it in UI?
                print(
                    f"Bone already had a left side tag, changed it to: {self.left_side_suffix}.")
                bone.name = bone.name[:-2] + self.left_side_suffix
            elif ".r" in bone_name_ending.lower() or "_r" in bone_name_ending.lower() or "-r" in bone_name_ending.lower():
                # display it in UI
                print(
                    f"Bone already had a right side tag, changed it to: {self.left_side_suffix}.")
                bone.name = bone.name[:-2] + self.left_side_suffix
            else:
                bone.name = bone.name + self.left_side_suffix

    def set_right_suffix(self):
        """Adds self.right_side_suffix to selected bones."""
        self.toggle_mode(editmode=True)

        for bone in self.get_selected_bones():
            bone_name_ending = bone.name[-3:]

            if ".r" in bone_name_ending.lower() or "_r" in bone_name_ending.lower() or "-r" in bone_name_ending.lower():
                # display it in UI?
                print(
                    f"Bone already had a right side tag, changed it to: {self.right_side_suffix}.")
                bone.name = bone.name[:-2] + self.right_side_suffix
            elif ".l" in bone_name_ending.lower() or "_l" in bone_name_ending.lower() or "-l" in bone_name_ending.lower():
                # display it in UI
                print(
                    f"Bone already had a left side tag, changed it to: {self.right_side_suffix}.")
                bone.name = bone.name[:-2] + self.right_side_suffix
            else:
                bone.name = bone.name + self.right_side_suffix

    def set_def_bones(self):
        """Set deformation bones to selected bones"""
        self.toggle_mode(editmode=True)

        """Sets Deform value ON and adds a self.def_bone_prefix prefix to selected bones"""
        for bone in self.get_selected_bones():
            if "DEF" not in bone.name[:3]:
                # Check if "DEF" is not already in the name of the bone
                # Add "DEF_" Prefix to selected bones.
                new_name = self.def_bone_prefix + bone.name
                bone.name = new_name
            if "DEF" in bone.name[:3]:
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

            if "DEF" not in bone.name:
                bone.name = self.tgt_bone_prefix + bone.name  # Add "TGT_" suffix to name
                if ".00" in bone_name_ending:
                    # Remove redundant numerical endings
                    bone.name = bone.name[:-4]

            elif "DEF" in bone.name:
                # Check if "DEF" is not already in the name of the bone
                # Add "TGT_" Prefix to selected bones.
                # Replace "DEF_" prefix to "TGT"g
                bone.name = bone.name.replace("DEF", "TGT")
                if ".00" in bone_name_ending:
                    # Remove redundant numerical endings appearing after duplication
                    bone.name = bone.name[:-4]

        self.set_xyz_rotation_mode()

        # bpy.ops.object.posemode_toggle()  # go to pose mode
        # tgt_bones = self.get_selected_pose_bones()  # store a list of tgt bones

        # TODO: add CopyTransfrom constraints
        # i = 0

        # for bone in def_bones:
        #     bpy.ops.pose.constraint_add(type='COPY_TRANSFORMS')
        #     bpy.context.object.pose.bones[bone.name].constraints["Copy Transforms"].target = self.get_current_armature(
        #     )

        #     bpy.context.object.pose.bones[bone.name].constraints["Copy Transforms"].subtarget = tgt_bones[i].name
        #     bpy.ops.pose.select_hierarchy(direction='CHILD', extend=True)
        #     i += 1

        # how to set active bone to set constraint to?

    def set_def_tgt_hierarchy(self):
        """Set Deform-Target bone hierarchy with all necessary parameters"""
    # TODO: add CopyTransfrom constraints
        # go to pose bone
        # select pattern by bone.name and assign it to list DEF
        # select pattern by bone.name and assign it to list TGT
        # for bone in DEF

        #armature = self.get_selected_armature() # select current armature

        self.toggle_mode(posemode=True)
        # select all DEF bones in the armature and make a list
        bpy.ops.object.select_pattern(
            pattern=self.def_bone_prefix + '*', case_sensitive=True, extend=False)
        def_bones = self.get_selected_pose_bones()

        # select all TGT bones in the armature and make a list
        bpy.ops.object.select_pattern(
            pattern=self.tgt_bone_prefix + '*', case_sensitive=True, extend=False)
        tgt_bones = self.get_selected_pose_bones()
        print(tgt_bones)
        i = 0
        for bone in def_bones:
            bpy.ops.object.select_pattern(
                pattern=bone.name, case_sensitive=True, extend=False)
            bpy.ops.pose.constraint_add(type='COPY_TRANSFORMS')
            bpy.context.object.pose.bones[bone.name].constraints["Copy Transforms"].target = self.get_selected_armature()
            bpy.context.object.pose.bones[bone.name].constraints["Copy Transforms"].subtarget = tgt_bones[i].name
            i +=1


        
        


# Testing my functions here:
scripts = MVBH_Scripts()
scripts.set_def_tgt_hierarchy()

# scripts.set_def_bones()
# scripts.set_tgt_bones()
# bpy.ops.armature.select_all(action='SELECT')
# scripts.set_left_suffix()
# scripts.set_right_suffix()
# scripts.add_root_bone()


# if __name__ == '__main__':
#     action = MVBH_Actions()
#     action.set_def_bones()


# TODO:

# Add CopyTransform constraints to DEF bones TGT to be the target of the constraint bones
# Add CTRL_ Bones to TGT_Bones
# Display debug messages in the info panel
