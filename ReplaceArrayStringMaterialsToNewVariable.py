import bpy

# List of materials to replace
materials_to_replace = ["Bone.010", "Bone.007", "Bone.008", "Bone.009", "Bone.011",]  # Change these to your material names
new_material_name = "Bone"  # Change this to your target material name

# Get the new material to apply
new_material = bpy.data.materials.get(new_material_name)

if new_material is None:
    print(f"Material '{new_material_name}' not found.")
else:
    # Iterate through all objects
    for obj in bpy.context.scene.objects:
        # Check if the object has materials
        if obj.data and hasattr(obj.data, 'materials'):
            # Iterate through the materials of the object
            for i in range(len(obj.data.materials)):
                current_material = obj.data.materials[i]
                # Replace specified materials with the new material
                if current_material and current_material.name in materials_to_replace:
                    obj.data.materials[i] = new_material
                    print(f"Replaced '{current_material.name}' in '{obj.name}' with '{new_material_name}'.")

print("Material replacement complete.")