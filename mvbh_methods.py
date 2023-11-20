# MeshVoid's Bone Helper addon scripts to be used by operators
import bpy
from .mvbh_info import MVBH_Messages


class MVBH_Scripts():
    """Class to run or test all the methods run by the addon. Change these to edit values executed by other parts of the addon. """

    def __init__(self):
        """Initialization values. Change these properties to modify your naming convention and other parameters."""
        self.root_name = "ROOT"
        self.root_size = 2
        self.prop_name = "PROP"
        self.prop_size = 0.5

        self.def_prefix = "DEF-"
        self.tgt_prefix = "TGT-"
        self.ctl_prefix = "CTL-"
        self.mch_prefix = "MCH-"

        self.ik_suffix = "-IK"
        self.fk_suffix = "-FK"
        self.twk_suffix = "-TWK"
        self.swtch_suffix = "-SWITCH"
        self.pole_suffix = "-POLE"

        self.left_suffix = "-L"
        self.right_suffix = "-R"
        self.center_suffix = "-C"

        # Layer numbers
        self.def_layer = 0
        self.tgt_layer = 1
        self.ctl_layer = 2
        self.mch_layer = 3
        self.ik_layer = 4
        self.twk_layer = 5
        self.pole_layer = 6
        self.swtch_layer = 7
        self.root_layer = 31
        self.prop_layer = 30

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

    def get_armature_name(self):
        """Return the name of currently selected Armature data value!"""
        current_object = bpy.context.object
        if current_object.type == "ARMATURE":
            armature = current_object.data
        return armature.name

    def get_armature_object_name(self):
        """Return the name of a currently selected Armature Object!"""
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

    def select_all_bones_by_prefix(self, bone_prefix='', extend=False):
        "Select specific bone/bones by specifying a certain prefix name"
        bpy.ops.object.select_pattern(
            pattern=bone_prefix + "*", case_sensitive=True, extend=extend)
        selected_bones = self.get_selected_bones()
        return selected_bones

    def select_all_bones_by_suffix(self, bone_suffix='', extend=False):
        "Select specific bone/bones by specifying a certain prefix name"
        bpy.ops.object.select_pattern(
            pattern="*" + bone_suffix, case_sensitive=True, extend=extend)
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

    def get_selected_bone_type(self, suffix):
        """Get selected bone ty by it's suffix name and store all bone values in bone_group list"""
        selected_bones = self.get_selected_bones()
        bone_group = []
        for bone in selected_bones:
            if suffix in bone.name:
                bone_group.append(bone)
        return bone_group

# =====================================================================
#                          ***SCRIPTS***
# =====================================================================

    def toggle_mode(self, posemode=False, editmode=False, objectmode=False):
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
        if objectmode:
            if bpy.context.mode == "EDIT_ARMATURE":
                bpy.ops.object.editmode_toggle()
            elif bpy.context.mode == "POSE":
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
        armature_name = self.get_armature_name()
        layers_list = [False] * 32
        layers_list[layer_number] = True
        bpy.ops.armature.bone_layers(layers=layers_list)

        bpy.context.object.data.layers[layer_number] = True
        # Strip layer_name from special symbols
        layer_name = ''.join(i for i in layer_name if i.isalpha())
        # assing custom property name and number
        bpy.data.armatures[armature_name][f'layer_name_{layer_number}'] = layer_name

    def set_copy_transforms_constraint(self, con_bones, con_targets, local=False):
        """Set copy transforms constraints con_bones - target bones list, con_targets - subtarget bones list"""
        i = 0
        for bone in con_bones:
            bpy.ops.object.select_pattern(
                pattern=bone.name, case_sensitive=True, extend=False)
            # set currently selected bone in the viewport active

            self.set_selected_bone_active()

            bpy.ops.pose.constraint_add(type="COPY_TRANSFORMS")
            bpy.context.object.pose.bones[bone.name].constraints[
                "Copy Transforms"].target = bpy.data.objects[self.get_armature_object_name()]
            bpy.context.object.pose.bones[bone.name].constraints["Copy Transforms"].subtarget = con_targets[i].name

            if local == True:
                bpy.context.object.pose.bones[bone.name].constraints["Copy Transforms"].target_space = "LOCAL"
                bpy.context.object.pose.bones[bone.name].constraints["Copy Transforms"].owner_space = "LOCAL"
            i += 1

    def set_copy_rotation_constraint(self, con_bones,
                                     con_targets, local=False):
        """Set copy rotation constraints con_bones - target bones list, con_targets - subtarget bones list"""
        i = 0
        for bone in con_bones:
            bpy.ops.object.select_pattern(
                pattern=bone.name, case_sensitive=True, extend=False)
            self.set_selected_bone_active()
            bpy.ops.pose.constraint_add(type="COPY_ROTATION")
            bpy.context.object.pose.bones[bone.name].constraints[
                "Copy Rotation"].target = bpy.data.objects[self.get_armature_object_name
                                                           ()]
            bpy.context.object.pose.bones[bone.name].constraints["Copy Rotation"].subtarget = con_targets[i].name

            if local == True:
                bpy.context.object.pose.bones[bone.name].constraints["Copy Rotation"].target_space = "LOCAL"
                bpy.context.object.pose.bones[bone.name].constraints["Copy Rotation"].owner_space = "LOCAL"
            i += 1

    def set_copy_location_constraint(self, con_bones,
                                     con_targets, local=False):
        """Set copy location constraints con_bones - target bones list, con_targets - subtarget bones list"""
        i = 0
        for bone in con_bones:
            bpy.ops.object.select_pattern(
                pattern=bone.name, case_sensitive=True, extend=False)
            self.set_selected_bone_active()
            bpy.ops.pose.constraint_add(type="COPY_LOCATION")
            bpy.context.object.pose.bones[bone.name].constraints[
                "Copy Location"].target = bpy.data.objects[self.get_armature_object_name
                                                           ()]
            bpy.context.object.pose.bones[bone.name].constraints["Copy Location"].subtarget = con_targets[i].name

            if local == True:
                bpy.context.object.pose.bones[bone.name].constraints["Copy Location"].target_space = "LOCAL"
                bpy.context.object.pose.bones[bone.name].constraints["Copy Location"].owner_space = "LOCAL"
            i += 1

    def set_copy_scale_constraint(self, con_bones,
                                  con_targets, local=False):
        """Set copy scale constraints con_bones - target bones list, con_targets - subtarget bones list"""
        i = 0
        for bone in con_bones:
            bpy.ops.object.select_pattern(
                pattern=bone.name, case_sensitive=True, extend=False)
            self.set_selected_bone_active()
            bpy.ops.pose.constraint_add(type="COPY_SCALE")
            bpy.context.object.pose.bones[bone.name].constraints[
                "Copy Scale"].target = bpy.data.objects[self.get_armature_object_name
                                                        ()]
            bpy.context.object.pose.bones[bone.name].constraints["Copy Scale"].subtarget = con_targets[i].name

            if local == True:
                bpy.context.object.pose.bones[bone.name].constraints["Copy Scake"].target_space = "LOCAL"
                bpy.context.object.pose.bones[bone.name].constraints["Copy Scale"].owner_space = "LOCAL"
            i += 1

    def set_copy_constraint_hierarchy(
            self, copy_trans=False, copy_rot=False, copy_loc=False, copy_scale=False, local_space=False):
        """Set copy transforms/rotation/scale constraints depending on the bone hierarchy selected by user that goes as follows: DEF<-TGT<-MCH<-CTL"""
        if bpy.context.mode == "EDIT_ARMATURE":
            self.toggle_mode(posemode=True)

        def_bones = self.get_selected_bone_group(prefix=self.def_prefix)
        tgt_bones = self.get_selected_bone_group(prefix=self.tgt_prefix)
        ctl_bones = self.get_selected_bone_group(prefix=self.ctl_prefix)
        mch_bones = self.get_selected_bone_group(prefix=self.mch_prefix)
        ik_bones = self.get_selected_bone_type(suffix=self.ik_suffix)
        fk_bones = self.get_selected_bone_type(suffix=self.fk_suffix)

        if copy_trans:
            set_constraint = self.set_copy_transforms_constraint
        elif copy_rot:
            set_constraint = self.set_copy_rotation_constraint
        elif copy_loc:
            set_constraint = self.set_copy_location_constraint
        elif copy_scale:
            set_constraint = self.set_copy_scale_constraint

        if def_bones and tgt_bones:
            set_constraint(def_bones, tgt_bones, local_space)
        if tgt_bones and ctl_bones:
            set_constraint(tgt_bones, ctl_bones, local_space)
        if tgt_bones and mch_bones:
            set_constraint(tgt_bones, mch_bones, local_space)
        if mch_bones and ctl_bones:
            set_constraint(mch_bones, ctl_bones, local_space)
        # NOTE: this causes double constraint assignment, probably
        # better not to use it.
        # if ik_bones and ctl_bones:
        #     set_constraint(ik_bones, ctl_bones, local_space)
        # if fk_bones and ctl_bones:
        #     set_constraint(fk_bones, ctl_bones, local_space)

    def delete_all_constraints(self):
        self.toggle_mode(posemode=True)
        constr_dict = {
            "COPY_LOCATION": "Copy Location", "COPY_ROTATION": "Copy Rotation", "COPY_SCALE": "Copy Scale", 'COPY_TRANSFORMS': "Copy Transforms", "LIMIT_DISTANCE": "Limit Distance", "LIMIT_LOCATION": "Limit Location", "LIMIT_ROTATION": "Limit Rotation",
            "LIMIT_SCALE": "Limit Scale", "MAINTAIN_VOLUME": "Maintain Volume", "TRANSFORM": "Transformation", "TRANSFORM_CACHE": "Transform Cache", "CLAMP_TO": "Clamp To", "DAMPED_TRACK": "Damped Track", "IK": "IK", "LOCKED_TRACK": "Locked Track", "SPLINE_IK": "Spline IK", "STRETCH_TO": "Stretch To", "TRACK_TO": "Track To", "ACTION": "Action", "ARMATURE": "Armature", "CHILD_OF": "Child Of", "FLOOR": "Floor", "FOLLOW_PATH": "Follow Path", "PIVOT": "Pivot", "SHRINKWRAP": "Shrinkwrap",
        }
        selected_bones = self.get_selected_bones()
        for bone in selected_bones:
            bpy.ops.object.select_pattern(
                pattern=bone.name, case_sensitive=True, extend=False)
            self.set_selected_bone_active()
            cont_exist = bool(bpy.data.objects[self.get_armature_object_name
                                               ()].pose.bones[bone.name].constraints)
            cont_num = len(bpy.data.objects[self.get_armature_object_name
                                            ()].pose.bones[bone.name].constraints)
            if cont_exist:
                for constr in range(cont_num):
                    cont_type = bpy.data.objects[self.get_armature_object_name
                                                 ()].pose.bones[bone.name].constraints[0].type
                    if cont_type in constr_dict:
                        bpy.ops.constraint.delete(
                            constraint=constr_dict[cont_type], owner='BONE')
        self.toggle_mode(editmode=True)

    def set_side_suffix(self, side):
        """Adds specific Side suffix to selected bones."""
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

    def set_bone_suffix(self, bone_suffix):
        """Adds specific Bone type suffix to selected bones."""
        self.toggle_mode(editmode=True)
        check_lst = [self.ik_suffix, self.fk_suffix,
                     self.twk_suffix, self.swtch_suffix]
        for bone in self.get_selected_bones():
            to_add = True
            to_rename = False
            for i in check_lst:
                if i in bone.name:
                    to_rename = True
                if to_rename:
                    bone.name = bone.name.replace(i, bone_suffix)
                    to_rename = False
                    to_add = False
            if to_add:
                if bone.name.endswith(self.left_suffix):
                    bone.name = bone.name.replace(self.left_suffix, "")
                    bone.name = bone.name + bone_suffix + self.left_suffix
                elif bone.name.endswith(self.right_suffix):
                    bone.name = bone.name.replace(self.right_suffix, "")
                    bone.name = bone.name + bone_suffix + self.right_suffix
                elif bone.name.endswith(self.center_suffix):
                    bone.name = bone.name.replace(self.center_suffix, "")
                    bone.name = bone.name + bone_suffix + self.center_suffix
                else:
                    bone.name = bone.name + bone_suffix

    def set_selected_bone_active(self):
        """Set selected bone to active depending on the mode the viewport is in"""
        if bpy.context.mode == "POSE":
            boneToSelect = bpy.data.objects[self.get_armature_object_name()].pose.bones[self.get_selected_bone_name()].bone
            # Set as active
            bpy.context.object.data.bones.active = boneToSelect
            #Select in viewport
            boneToSelect.select = True

        elif bpy.context.mode == "EDIT_ARMATURE":
            boneToSelect = bpy.data.armatures[self.get_armature_name()].edit_bones[self.get_selected_bone_name()]
            bpy.data.armatures[self.get_armature_name()].edit_bones.active = boneToSelect
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
        self.select_bone_by_name(bone_name=self.prop_name)

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
                if ".0" in bone_suffix:
                    bone.name = bone.name[:-4]
            bone.use_deform = deform
        if xyz:
            self.set_xyz_rotation_mode()

    def set_def_tgt_hierarchy(self):
        """Set Deform-Target bone hierarchy with all necessary parameters"""
        self.toggle_mode(posemode=True)
        # def_bones = self.select_all_bones_by_prefix(
        #     bone_prefix=self.def_prefix, extend=False)
        # tgt_bones = self.select_all_bones_by_prefix(
        #     bone_prefix=self.tgt_prefix, extend=False)

        def_bones = self.get_selected_bone_group(self.def_prefix)
        tgt_bones = self.get_selected_bone_group(self.tgt_prefix)
        self.set_copy_transforms_constraint(def_bones, tgt_bones)
        # if there's a root bone, parent def bones to root bone
        if bpy.data.armatures[self.get_armature_name()].bones[self.root_name]:
            self.toggle_mode(editmode=True)
            self.select_bone_by_name(bone_name=self.root_name)
            self.set_selected_bone_active()
            for bone in def_bones:
                self.select_bone_by_name(bone_name=bone.name,extend=True)
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

    def replace_in_bone_names(self, value, target=""):
        """Replaces specified value parameter with target parameter string value"""
        self.toggle_mode(editmode=True)
        sel_bones = self.get_selected_bones()
        for bone in sel_bones:
            bone.name = bone.name.replace(str(value), str(target))

    def enumerate_bones(self):
        """Enumerate selected bones in consequential order"""
        selected_bones = self.get_selected_bones()
        i = 1
        for bone in selected_bones:
            digitless_name = "".join((x for x in bone.name if not x.isdigit()))
            if "." in digitless_name:
                digitless_name = digitless_name.replace(".", "")
            bone.name = f"{digitless_name}{i}"
            i += 1

    def delete_orphan_data(self):
        "Delete all orphan data"
        bpy.ops.outliner.orphans_purge(
            do_local_ids=True, do_linked_ids=True, do_recursive=False)
        bpy.ops.outliner.orphans_purge(
            do_local_ids=True, do_linked_ids=True, do_recursive=True)
        bpy.ops.outliner.orphans_purge(
            do_local_ids=False, do_linked_ids=True, do_recursive=False)
        bpy.ops.outliner.orphans_purge(
            do_local_ids=False, do_linked_ids=True, do_recursive=True)
        bpy.ops.outliner.orphans_purge(
            do_local_ids=True, do_linked_ids=False, do_recursive=False)
        bpy.ops.outliner.orphans_purge(
            do_local_ids=True, do_linked_ids=False, do_recursive=True)

    def delete_side_suffixes(self):
        "Delete side suffixes if they correspond to the naming convention"
        selected_bones = self.get_selected_bones()
        for bone in selected_bones:
            if bone.name.endswith(self.center_suffix):
                bone.name = bone.name[:-len(self.center_suffix)]
            elif bone.name.endswith(self.left_suffix):
                bone.name = bone.name[:-len(self.left_suffix)]
            elif bone.name.endswith(self.right_suffix):
                bone.name = bone.name[:-len(self.right_suffix)]
            else:
                self.info.display_msg(28)

    def delete_function_suffixes(self):
        "Delete bone function suffixes if they correspond to the naming convention"
        selected_bones = self.get_selected_bones()
        for bone in selected_bones:
            if self.ik_suffix in bone.name:
                bone.name = bone.name.replace(self.ik_suffix, "")
            elif self.fk_suffix in bone.name:
                bone.name = bone.name.replace(self.fk_suffix, "")
            elif self.twk_suffix in bone.name:
                bone.name = bone.name.replace(self.twk_suffix, "")
            elif self.swtch_suffix in bone.name:
                bone.name = bone.name.replace(self.swtch_suffix, "")
            elif self.pole_suffix in bone.name:
                bone.name = bone.name.replace(self.pole_suffix, "")
            else:
                self.info.display_msg(29)

    def remove_bone_prefix(self):
        "Delete bone prefix if it corresponds to standard naming convention"
        selected_bones = self.get_selected_bones()
        for bone in selected_bones:
            if bone.name.startswith(self.def_prefix):
                bone.name = bone.name.replace(self.def_prefix, "")
            elif bone.name.startswith(self.tgt_prefix):
                bone.name = bone.name.replace(self.tgt_prefix, "")
            elif bone.name.startswith(self.mch_prefix):
                bone.name = bone.name.replace(self.mch_prefix, "")
            elif bone.name.startswith(self.ctl_prefix):
                bone.name = bone.name.replace(self.ctl_prefix, "")

    def add_ik_hierarchy(self, chain_len=2):
        "Add IK Hierarchy to bones with: MCH-prefix and IK-suffix, CTL-prefix and IK-suffix, CTL-prefix and Pole-suffix"
        self.toggle_mode(posemode=True)
        selected_bones = self.get_selected_bones()
        rig_name = self.get_armature_object_name()
        for bone in selected_bones:
            if self.mch_prefix in bone.name and self.ik_suffix in bone.name:
                mch_bone = bone.name
            elif self.ctl_prefix in bone.name and self.ik_suffix in bone.name:
                ctl_bone = bone.name
            elif self.ctl_prefix in bone.name and self.pole_suffix in bone.name:
                pole_bone = bone.name

        for bone in selected_bones:
            if bone.name == mch_bone:
                self.set_selected_bone_active()
                bpy.ops.pose.constraint_add(type='IK')
                bpy.context.object.pose.bones[mch_bone].constraints["IK"].target = bpy.data.objects[rig_name]
                bpy.context.object.pose.bones[mch_bone].constraints["IK"].subtarget = ctl_bone
                bpy.context.object.pose.bones[mch_bone].constraints["IK"].pole_target = bpy.data.objects[rig_name]
                bpy.context.object.pose.bones[mch_bone].constraints["IK"].pole_subtarget = pole_bone
                bpy.context.object.pose.bones[mch_bone].constraints["IK"].pole_angle = -1.5708
                bpy.context.object.pose.bones[mch_bone].constraints["IK"].chain_count = chain_len

                
            
        
        # #set Ik target to MCH bone
        #     bpy.context.object.pose.bones["MCH-Bone.001-IK-L"].constraints["IK"].target = bpy.data.objects["Rig"]
        # # set subtarget_for_IK
        # bpy.context.object.pose.bones["MCH-Bone.001-IK-L"].constraints["IK"].subtarget = "CTL-Bone.002-IK-L"
        # # set target for pole object
        # bpy.context.object.pose.bones["MCH-Bone.001-IK-L"].constraints["IK"].pole_target = bpy.data.objects["Rig"]
        # # set pole
        # bpy.context.object.pose.bones["MCH-Bone.001-IK-L"].constraints["IK"].pole_subtarget = "CTL-Bone-POLE"
        # # set pole angle
        # bpy.context.object.pose.bones["MCH-Bone.001-IK-L"].constraints["IK"].pole_angle = -1.5708





