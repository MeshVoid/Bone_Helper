import bpy  # do i need to import it here?
# TODO: finish all messages to display to user
#import mvbh_methods


class MVBH_Messages():
    def __init__(self):
        """List of messages and errors to show to user"""
    # id : message
        self.messages = {
            0: "Created Root bone!",
            1: "Created Properties bone",
            2: "Assigned Deform bone naming convention and properties to selected bones!",
            3: "Assigned Target bone naming convention and properties to selected bones!",
            4: "Assigned Control bone naming convention and properties to selected bones!",
            5: "Assigned Mechanism bone naming convention and properties to selected bones!",
            6: "Parented Deform bones to Root bone!",
            7: "Parented selected bones to Root bone!",
            8: "Added new Control bones with appropriate naming covention and properties based on the seleced bones!",
            9: "Added new Deform bones based on the selection with appropriate properties!",
            10: "Assigned Left side suffix to selected bones!",
            11: "Assigned Right side suffix to selected bones!",
            12: "Assigned Center position suffix to selected bones!",
            13: "Assigned IK bone suffix to selected bones!",
            14: "Assigned FK bone suffix to selected bones!",
            15: "Assigned Tweak bone suffix to selected bones!",
            16: "Assigned Switch bone suffix to selected bones!",
            17: "Zeroes in the names of all armature bones are removed!",
            18: "Assigned Pole bone suffix to selected bones!",
            19: "Replaced 'Bone' to 'Leg' in the names of the selected bones",
            20: "Copy Transforms Constraint hierarchy has been assigned to selected bones!",
            21: "Set up copy transforms constraint hierarchy between all Deformation and Target bones of the rig!",
            22: "Replaced 'Bone' to 'Limb' in the names of the selected bones",
            23: "Replaced 'Bone' to 'Spine' in the names of the selected bones",
            24: "Replaced 'Bone' to 'Pelvis' in the names of the selected bones",
            25: "Replaced 'Bone' to 'Thigh' in the names of the selected bones",         
            26: "Replaced 'Bone' to 'Shin' in the names of the selected bones",                  
        }

        self.errors = {
            0: "No bones are selected in the viewport, please select some!",
            1: "Make sure you are in either Edit or Pose armature modes!",
            2: "No object is selected, therefore I cannot proceed!",

        }

    def display_msg(self, msg_id, title="MeshVoid Bone Helper Notifications", icon='INFO'):
        """Display simple info messages based on the message id"""
        message = self.messages
        text = f"{message[msg_id]}"

        def draw(self, context):
            self.layout.label(text=text)
        bpy.context.window_manager.popup_menu(draw, title=title, icon=icon)

    def display_err(self, err_id, title="MeshVoid Bone Helper Errors", icon="ERROR"):
        """Display error messages based on the message id"""
        error = self.errors
        text = f"{error[err_id]}"

        def draw(self, context):
            self.layout.label(text=text)
        bpy.context.window_manager.popup_menu(draw, title=title, icon=icon)
