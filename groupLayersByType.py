import bpy

# Get the current scene
scene = bpy.context.scene

# Create collections for text and mesh objects
text_collection = bpy.data.collections.new("Text")
mesh_collection = bpy.data.collections.new("Mesh")

# Link collections to the scene
scene.collection.children.link(text_collection)
scene.collection.children.link(mesh_collection)

# Iterate through all objects in the scene
for obj in scene.objects:
    # Check if the object is a text object
    if obj.type == 'FONT':
        # Move the text object to the text collection
        text_collection.objects.link(obj)
    else:
        # Move the mesh object to the mesh collection
        mesh_collection.objects.link(obj)