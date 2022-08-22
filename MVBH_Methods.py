import bpy

selected_bones = bpy.context.selected_bones


def set_def_bones():
    """Sets Deform value ON and adds a DEF_ prefix to selected bones"""
    for bone in selected_bones:
        if "DEF" not in bone.name:
            # Check if "DEF" is not already in the name of the bone
            # Add "DEF_" Prefix to selected bones.
            new_name = "DEF-" + bone.name
            bone.name = new_name
        if "DEF" in bone.name:
            bpy

    for bone in selected_bones:
        # Set Deform value ON for selected bones.
        bone.use_deform = True


def set_tgt_bones():
    """Duplicates bones sets Deform value OFF and replaces DEF. suffix to TGT., 
    applies CopyTransform constraints"""
    bpy.ops.armature.duplicate()  # duplicate all bones

    for bone in selected_bones:
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
            # Replace "DEF_" prefix to "TGT"
            bone.name = bone.name.replace("DEF", "TGT")
            if ".00" in bone_name_ending:
                # Remove redundant numerical endings
                bone.name = bone.name[:-4]

    for bone in selected_bones:
        # TODO: add CopyTransfrom constraints
        pass


def set_l_suffix():
    """Adds .L suffix to selected bones."""
    for bone in selected_bones:
        bone_name_ending = bone.name[-2:]

        if ".l" in bone_name_ending.lower() or "_l" in bone_name_ending.lower():
            print("Bone already has a left side tag")  # display it in UI
        elif ".r" in bone_name_ending.lower() or "_r" in bone_name_ending.lower():
            # display it in UI
            print("Bone already has a right side tag, changed it to .L")
            bone.name = bone.name[:-2] + ".L"
        else:
            bone.name = bone.name + ".L"


def set_r_suffix():
    """Adds .R suffix to selected bones."""
    for bone in selected_bones:
        bone_name_ending = bone.name[-3:]

        if ".r" in bone_name_ending.lower() or "_r" in bone_name_ending.lower():
            print("Bone already has a right side tag")  # display it in UI
        elif ".l" in bone_name_ending.lower() or "_l" in bone_name_ending.lower():
            # display it in UI
            print("Bone already has a left side tag, changed it to .R")
            bone.name = bone.name[:-2] + ".R"
        else:
            bone.name = bone.name + ".R"


# Testing my functions here:

# set_l_suffix()
# set_r_suffix()

# set_def_bones()
set_tgt_bones()

# TODO:

# Add CopyTransform constraints to DEF bones TGT to be the target of the constraint bones
# Add CTRL_ Bones to TGT_Bones
# Display debug messages in the info panel
