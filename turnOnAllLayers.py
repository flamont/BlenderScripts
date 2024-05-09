import bpy

# Get the current scene
scene = bpy.context.scene

# Iterate through all collections in the scene
for collection in scene.collection.children:
    # Set the "hide_viewport" property to False to make the collection visible
    collection.hide_viewport = False