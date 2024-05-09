import bpy

# Get the current scene
scene = bpy.context.scene

# Iterate through all objects in the scene
for obj in scene.objects:
    # Check if the object is a text object
    if obj.type == 'FONT':
        # Hide the object
        obj.hide_set(True)