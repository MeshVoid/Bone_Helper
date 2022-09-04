import bpy

# TODO: finish all messages to display to user

class MVBH_Messages():
    def __init__(self):
        """List of messages and errors to show to user"""
    # id : message
        self.messages = {
            0: "Successfully created Root bone!", 
            1: "Successfully assigned Defrorm bone naming convention and properties to selected bones!", 
            2: "Successfully assigned Target bone naming convention and properties to selected bones!"}

        self.errors = {0: "Nothing is selected in the viewport, please select Armature object"}
    

    def display_msg(self, msg_id=0, title="MeshVoid Bone Helper Notifications", icon='INFO'):
        """Display simple info messages based on the message id"""
        message = self.messages
        text = f"{message[msg_id]}"
        def draw(self, context):
            self.layout.label(text=text)
        bpy.context.window_manager.popup_menu(draw, title=title, icon=icon)

    def display_err(self, err_id=0, title="MeshVoid Bone Helper Errors", icon="ERROR"):
        """Display error messages based on the message id"""
        error = self.errors
        text = f"{error[err_id]}"
        def draw(self, context):
            self.layout.label(text=text)
        bpy.context.window_manager.popup_menu(draw, title=title, icon=icon)
