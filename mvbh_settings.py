# MeshVoid's Bone Helper addon settings

# TODO: Make sure that you can change naming convention of bone names and other parameters
# by directly changing values in MVBH_Scripts class
import bpy
import rna_keymap_ui


# Keymap Code

# First, set up a dictionary of key mappings.

keys = {"MENU": [{"label": "MV Bone Helper Main Menu",
                  "region_type": "WINDOW",
                  "space_type": "VIEW_3D",
                  "map_type": "KEYBOARD",
                  "keymap": "Armature",
                  "idname": "mvbh.main_menu",
                  "type": "B",
                  "ctrl": False,
                  "alt": False,
                  "shift": False,
                  "oskey": False,
                  "value": "PRESS"
                  }]}


def get_keys():
    keylists = []
    keylists.append(keys["MENU"])
    return keylists


def register_keymaps(keylists):
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon

    keymaps = []

    for keylist in keylists:
        for item in keylist:
            keymap = item.get("keymap")
            space_type = item.get("space_type", "EMPTY")
            region_type = item.get("region_type", "WINDOW")

            if keymap:
                km = kc.keymaps.new(
                    name=keymap, space_type=space_type, region_type=region_type)
                # km = kc.keymaps.new(name=keymap, space_type=space_type)

                if km:
                    idname = item.get("idname")
                    type = item.get("type")
                    value = item.get("value")

                    shift = item.get("shift", False)
                    ctrl = item.get("ctrl", False)
                    alt = item.get("alt", False)
                    oskey = item.get("oskey", False)

                    kmi = km.keymap_items.new(
                        idname, type, value, shift=shift, ctrl=ctrl, alt=alt, oskey=oskey)

                    if kmi:
                        properties = item.get("properties")

                        if properties:
                            for name, value in properties:
                                setattr(kmi.properties, name, value)

                        keymaps.append((km, kmi))
    return keymaps


# Define a function to unregister the keymaps
def unregister_keymaps(keymaps):
    for km, kmi in keymaps:
        km.keymap_items.remove(kmi)


def register():
    global keymaps
    keys = get_keys()
    keymaps = register_keymaps(keys)


def unregister():
    global keymaps
    for km, kmi in keymaps:
        km.keymap_items.remove(kmi)