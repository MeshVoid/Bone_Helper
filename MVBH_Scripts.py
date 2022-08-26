import bpy


class MVBH_Scripts():
    """Class to run or test all the methods run by the addon"""

    def __init__(self):
        self.selected_bones = bpy.context.selected_bones

    def mode_toggle(self):
        """Toggle to edit mode from pose or object mode"""
        if bpy.context.mode == "POSE":  # toggle from pose mode to edit
            bpy.ops.object.editmode_toggle()  # go to edit mode
        elif bpy.context.mode == "OBJECT":
            bpy.ops.object.editmode_toggle()  # go to edit mode

    def add_root_bone(self):
        """Add a root bone to the rig"""
        self.mode_toggle()
        bpy.ops.armature.bone_primitive_add(name="ROOT")
        bpy.ops.transform.rotate(value=1.5708, orient_axis='X', orient_type='GLOBAL', orient_matrix=((4.93038e-32, 1, 2.22045e-16), (2.22045e-16, 4.93038e-32, 1), (1, 2.22045e-16, 4.93038e-32)), orient_matrix_type='VIEW', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

        bpy.ops.armature.align()

    def get_selected_bones(self):
        """Get selected bones in a list"""
        self.selected_bones = bpy.context.selected_bones1
        return self.selected_bones

    def get_edit_bone_list(self):
        """Get selected edit bones and store them in the list edit_bones"""
        selection = bpy.context.selected_editable_bones
        self.edit_bones = []
        for bone in selection:
            self.edit_bones.append(bone)
        return self.edit_bones

    def get_selected_pose_bones(self):
        """Get selected pose bones and store them in the list"""
        selection = bpy.context.selected_pose_bones
        self.pose_bones = []
        for bone in selection:
            self.pose_bones.append(bone)
        return self.pose_bones

    def set_l_suffix(self):
        """Adds .L suffix to selected bones."""
        for bone in self.get_selected_bones():
            bone_name_ending = bone.name[-2:]

            if ".l" in bone_name_ending.lower() or "_l" in bone_name_ending.lower():
                print("Bone already has a left side tag")  # display it in UI
            elif ".r" in bone_name_ending.lower() or "_r" in bone_name_ending.lower():
                # display it in UI
                print("Bone already has a right side tag, changed it to .L")
                bone.name = bone.name[:-2] + ".L"
            else:
                bone.name = bone.name + ".L"

    def set_r_suffix(self):
        """Adds .R suffix to selected bones."""
        for bone in self.get_selected_bones():
            bone_name_ending = bone.name[-3:]

            if ".r" in bone_name_ending.lower() or "_r" in bone_name_ending.lower():
                print("Bone already has a right side tag")  # display it in UI
            elif ".l" in bone_name_ending.lower() or "_l" in bone_name_ending.lower():
                # display it in UI
                print("Bone already has a left side tag, changed it to .R")
                bone.name = bone.name[:-2] + ".R"
            else:
                bone.name = bone.name + ".R"

    def set_def_bones(self):
        """Set deformation bones to selected bones"""
        self.mode_toggle()

        """Sets Deform value ON and adds a DEF- prefix to selected bones"""
        for bone in self.get_selected_bones():
            if "DEF" not in bone.name:
                # Check if "DEF" is not already in the name of the bone
                # Add "DEF_" Prefix to selected bones.
                new_name = "DEF-" + bone.name
                bone.name = new_name
            if "DEF" in bone.name:
                bpy

        for bone in self.get_selected_bones():
            # Set Deform value ON for selected bones.
            bone.use_deform = True
            bpy.context.object.pose.bones[bone.name].rotation_mode = 'XYZ'

    def select_one_object(self, obj):
        bpy.ops.pose.select_all(action='DESELECT')
        bpy.context.view_layer.objects.active = obj
        obj.select_set(True)

    def set_tgt_bones(self):
        """Duplicates bones sets Deform value OFF and replaces DEF suffix to TGT, 
        applies CopyTransform constraints"""
        current_armature = bpy.context.selected_objects[0]

        if bpy.context.mode == "EDIT_ARMATURE":
            bpy.ops.object.posemode_toggle()  # go to pose mode
            def_bones = self.get_selected_pose_bones()  # store a list of def bones

        elif bpy.context.mode == "POSE":
            def_bones = self.get_selected_pose_bones()  # store a list of def

        bpy.ops.object.editmode_toggle()  # go to edit mode
        bpy.ops.armature.duplicate()  # duplicate all bones

        for bone in self.get_edit_bone_list():
            bone_name_ending = bone.name[-4:]
            bone.use_deform = False  # Set Deform value ON for selected bones.

            if "DEF" not in bone.name:
                bone.name = "TGT-" + bone.name  # Add "TGT_" suffix to name
                if ".00" in bone_name_ending:
                    # Remove redundant numerical endings
                    bone.name = bone.name[:-4]

            elif "DEF" in bone.name:
                # Check if "DEF" is not already in the name of the bone
                # Add "TGT_" Prefix to selected bones.
                # Replace "DEF_" prefix to "TGT"g
                bone.name = bone.name.replace("DEF", "TGT")
                if ".00" in bone_name_ending:
                    # Remove redundant numerical endings\
                    bone.name = bone.name[:-4]

        bpy.ops.object.posemode_toggle()  # go to pose mode
        tgt_bones = self.get_selected_pose_bones()  # store a list of tgt bones

        for bone in tgt_bones:
            # set rotation_mode to XYZ
            bpy.context.object.pose.bones[bone.name].rotation_mode = 'XYZ'

        # TODO: add CopyTransfrom constraints
        i = 0
        for bone in tgt_bones:
            bpy.ops.pose.constraint_add(type='COPY_TRANSFORMS')
            bpy.context.object.pose.bones[bone.name].constraints["Copy Transforms"].target = current_armature

            bpy.context.object.pose.bones[bone.name].constraints["Copy Transforms"].subtarget = def_bones[i].name
            bpy.ops.pose.select_hierarchy(direction='CHILD', extend=True)
            i += 1



            # how to set active bone to set constraint to?


        def set_def_tgt_bones():
            self.set_def_bones()
            self.set_tgt_bones()


# Testing my functions here:
scripts = MVBH_Scripts()
# scripts.set_def_bones()
scripts.set_tgt_bones()
#scripts.add_root_bone()


# if __name__ == '__main__':
#     action = MVBH_Actions()
#     action.set_def_bones()


# set_l_suffix()
# set_r_suffix()

# set_def_bones()
# set_tgt_bones()
# get_edit_bone_list()

# TODO:

# Add CopyTransform constraints to DEF bones TGT to be the target of the constraint bones
# Add CTRL_ Bones to TGT_Bones
# Display debug messages in the info panel
