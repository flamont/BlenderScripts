import bpy

# Iterate over all materials in the current blend file
for material in bpy.data.materials:
    # Check if the material uses nodes
    if material.use_nodes:
        # Clear existing nodes
        nodes = material.node_tree.nodes
        nodes.clear()

        # Create a new Principled BSDF node
        principled_bsdf = nodes.new(type='ShaderNodeBsdfPrincipled')
        principled_bsdf.inputs['Base Color'].default_value = (1.0, 1.0, 1.0, 1.0)  # RGBA

        # Create an output node
        output_node = nodes.new(type='ShaderNodeOutputMaterial')

        # Link the Principled BSDF to the output node
        links = material.node_tree.links
        links.new(principled_bsdf.outputs['BSDF'], output_node.inputs['Surface'])