import bpy

# TODO: finish all messages to display to user

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
            8: "",
            9: "",
            10: "Assigned Left side suffix to selected bones",
            11: "Assigned Right side suffix to selected bones",
            12: "Assigned Center position suffix to selected bones",

            }

        self.errors = {
            0: "Nothing is selected in the viewport, please select Armature object",
            1: "Make sure you are in either Edit or Pose armature modes",
            2: "No object is selected, therefore I cannot proceed",
        
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
        self.report({'OPERATOR'}, self.show_info.messages[text])
            
