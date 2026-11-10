import bpy
import os
import math
from mathutils import Vector


def clear_scene():
    """Clear the current scene of all objects."""
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()


def create_text_object(text="Blender", name="TextObject", location=(0, 0, 0), 
                       size=1.0, extrude=0.0, bevel_depth=0.0, bevel_resolution=0):
    """Create a basic text object.
    
    Args:
        text: The text content.
        name: Name for the text object.
        location: (x, y, z) tuple for object location.
        size: Font size.
        extrude: Extrusion depth.
        bevel_depth: Bevel depth (for rounded edges).
        bevel_resolution: Bevel resolution (subdivisions).
        
    Returns:
        The created text object.
    """
    # Create text object
    bpy.ops.object.text_add(location=location)
    
    # Get the created object
    text_obj = bpy.context.active_object
    text_obj.name = name
    
    # Set text properties
    text_obj.data.body = text
    text_obj.data.size = size
    text_obj.data.extrude = extrude
    text_obj.data.bevel_depth = bevel_depth
    text_obj.data.bevel_resolution = bevel_resolution
    
    return text_obj


def create_3d_text(text="3D", name="3DText", location=(0, 0, 0), 
                   size=1.0, extrude=0.25, bevel_depth=0.05, bevel_resolution=3):
    """Create a 3D text object with extrusion and beveling.
    
    Args:
        text: The text content.
        name: Name for the text object.
        location: (x, y, z) tuple for object location.
        size: Font size.
        extrude: Extrusion depth.
        bevel_depth: Bevel depth (for rounded edges).
        bevel_resolution: Bevel resolution (subdivisions).
        
    Returns:
        The created text object.
    """
    # Create text with extrude and bevel settings
    text_obj = create_text_object(
        text=text,
        name=name,
        location=location,
        size=size,
        extrude=extrude,
        bevel_depth=bevel_depth,
        bevel_resolution=bevel_resolution
    )
    
    return text_obj


def set_text_alignment(text_obj, align_x='CENTER', align_y='CENTER'):
    """Set the text alignment.
    
    Args:
        text_obj: The text object to modify.
        align_x: Horizontal alignment ('LEFT', 'CENTER', 'RIGHT', 'JUSTIFY', 'FLUSH').
        align_y: Vertical alignment ('TOP', 'CENTER', 'BOTTOM', 'TOP_BASELINE', 'BOTTOM_BASELINE').
    """
    text_obj.data.align_x = align_x
    text_obj.data.align_y = align_y


def set_text_font(text_obj, font_path=None):
    """Set the font for a text object.
    
    Args:
        text_obj: The text object to modify.
        font_path: Path to a font file. If None, uses the default font.
        
    Returns:
        True if successful, False otherwise.
    """
    if font_path is None:
        return True
    
    try:
        # Load the font
        font = bpy.data.fonts.load(font_path)
        # Assign it to the text object
        text_obj.data.font = font
        return True
    except Exception as e:
        print(f"Error loading font: {e}")
        return False


def create_text_on_curve(text="Text on Curve", curve_type='CIRCLE', name="CurvedText", 
                         location=(0, 0, 0), size=1.0, extrude=0.0, bevel_depth=0.0,
                         curve_radius=2.0):
    """Create text that follows a curve path.
    
    Args:
        text: The text content.
        curve_type: Type of curve ('CIRCLE', 'LINE', 'WAVE').
        name: Name for the text object.
        location: (x, y, z) tuple for object location.
        size: Font size.
        extrude: Extrusion depth.
        bevel_depth: Bevel depth (for rounded edges).
        curve_radius: Radius of the curve (for circle).
        
    Returns:
        The created text object.
    """
    # First create the curve to follow
    if curve_type == 'CIRCLE':
        bpy.ops.curve.primitive_bezier_circle_add(radius=curve_radius, location=location)
        curve_obj = bpy.context.active_object
        curve_obj.name = f"{name}Path"
    elif curve_type == 'LINE':
        bpy.ops.curve.primitive_bezier_curve_add(location=location)
        curve_obj = bpy.context.active_object
        curve_obj.name = f"{name}Path"
        # Adjust the curve points for a straight line
        curve_obj.data.splines[0].bezier_points[0].co = Vector((-curve_radius, 0, 0))
        curve_obj.data.splines[0].bezier_points[1].co = Vector((curve_radius, 0, 0))
    elif curve_type == 'WAVE':
        bpy.ops.curve.primitive_bezier_curve_add(location=location)
        curve_obj = bpy.context.active_object
        curve_obj.name = f"{name}Path"
        
        # Adjust to create a wave
        spline = curve_obj.data.splines[0]
        # Add more points for the wave
        spline.bezier_points.add(2)  # Add two more points (4 total)
        
        # Set the points for a wave shape
        points = spline.bezier_points
        points[0].co = Vector((-curve_radius, 0, 0))
        points[1].co = Vector((-curve_radius/3, curve_radius/2, 0))
        points[2].co = Vector((curve_radius/3, -curve_radius/2, 0))
        points[3].co = Vector((curve_radius, 0, 0))
        
        # Set handle types to AUTO for smooth wave
        for point in points:
            point.handle_left_type = 'AUTO'
            point.handle_right_type = 'AUTO'
    else:
        raise ValueError(f"Unknown curve type: {curve_type}")
    
    # Now create the text object
    bpy.ops.object.text_add(location=(0, 0, 0))  # Position will be determined by the curve
    text_obj = bpy.context.active_object
    text_obj.name = name
    
    # Set text properties
    text_obj.data.body = text
    text_obj.data.size = size
    text_obj.data.extrude = extrude
    text_obj.data.bevel_depth = bevel_depth
    
    # Add Follow Path constraint to the text
    follow_path = text_obj.constraints.new(type='FOLLOW_PATH')
    follow_path.target = curve_obj
    follow_path.use_curve_follow = True
    
    # Orient the text properly along the curve
    text_obj.data.align_x = 'CENTER'
    text_obj.rotation_euler[0] = math.pi/2  # Rotate 90 degrees around X
    
    # Return both objects
    return text_obj, curve_obj


def create_text_with_materials(text="Colorful", name="MaterialText", location=(0, 0, 0),
                              size=1.0, extrude=0.2, color=(1, 0, 0, 1)):
    """Create a text object with a material applied.
    
    Args:
        text: The text content.
        name: Name for the text object.
        location: (x, y, z) tuple for object location.
        size: Font size.
        extrude: Extrusion depth.
        color: (R, G, B, A) tuple for the material color.
        
    Returns:
        The created text object.
    """
    # Create the text object
    text_obj = create_text_object(
        text=text,
        name=name,
        location=location,
        size=size,
        extrude=extrude
    )
    
    # Create a new material
    mat = bpy.data.materials.new(name=f"{name}Material")
    mat.use_nodes = True
    
    # Get the Principled BSDF shader
    principled = mat.node_tree.nodes.get('Principled BSDF')
    if principled:
        # Set the base color
        principled.inputs['Base Color'].default_value = color
        # Optionally adjust other material properties
        principled.inputs['Metallic'].default_value = 0.3
        principled.inputs['Specular'].default_value = 0.5
        principled.inputs['Roughness'].default_value = 0.2
    
    # Assign the material to the text object
    if text_obj.data.materials:
        text_obj.data.materials[0] = mat
    else:
        text_obj.data.materials.append(mat)
    
    return text_obj


def create_multi_line_text(lines=None, name="MultiLineText", location=(0, 0, 0),
                          size=1.0, line_spacing=1.5):
    """Create a multi-line text object.
    
    Args:
        lines: List of text lines. If None, uses default text.
        name: Name for the text object.
        location: (x, y, z) tuple for object location.
        size: Font size.
        line_spacing: Vertical spacing factor between lines.
        
    Returns:
        The created text object.
    """
    if lines is None:
        lines = ["Line 1", "Line 2", "This is line 3"]
    
    # Join lines with newline characters
    text_content = "\n".join(lines)
    
    # Create the text object
    text_obj = create_text_object(
        text=text_content,
        name=name,
        location=location,
        size=size
    )
    
    # Set line spacing
    text_obj.data.space_line = line_spacing
    
    return text_obj


def create_text_to_mesh(text="Mesh", name="TextMesh", location=(0, 0, 0),
                       size=1.0, extrude=0.2, bevel_depth=0.05, shading='SMOOTH',
                       convert=True):
    """Create a text object and optionally convert it to a mesh.
    
    Args:
        text: The text content.
        name: Name for the text/mesh object.
        location: (x, y, z) tuple for object location.
        size: Font size.
        extrude: Extrusion depth.
        bevel_depth: Bevel depth (for rounded edges).
        shading: Shading type ('FLAT', 'SMOOTH').
        convert: Whether to convert to mesh (True) or leave as text (False).
        
    Returns:
        The created object (text or mesh).
    """
    # Create the text object
    text_obj = create_text_object(
        text=text,
        name=name,
        location=location,
        size=size,
        extrude=extrude,
        bevel_depth=bevel_depth
    )
    
    if not convert:
        return text_obj
    
    # Convert to mesh
    bpy.ops.object.convert(target='MESH')
    mesh_obj = bpy.context.active_object
    mesh_obj.name = name
    
    # Set shading
    if shading == 'SMOOTH':
        bpy.ops.object.shade_smooth()
    else:
        bpy.ops.object.shade_flat()
    
    return mesh_obj


def create_text_with_animation(text="Animated", name="AnimatedText", location=(0, 0, 0),
                              size=1.0, extrude=0.2, anim_type='ROTATE', frames=48):
    """Create a text object with a simple animation.
    
    Args:
        text: The text content.
        name: Name for the text object.
        location: (x, y, z) tuple for object location.
        size: Font size.
        extrude: Extrusion depth.
        anim_type: Animation type ('ROTATE', 'SCALE', 'FADE').
        frames: Number of frames for the animation cycle.
        
    Returns:
        The created text object.
    """
    # Create the text object
    text_obj = create_text_object(
        text=text,
        name=name,
        location=location,
        size=size,
        extrude=extrude
    )
    
    # Set up the animation
    scene = bpy.context.scene
    scene.frame_start = 1
    scene.frame_end = frames
    
    # Insert initial keyframe
    scene.frame_set(1)
    
    if anim_type == 'ROTATE':
        text_obj.rotation_euler = (0, 0, 0)
        text_obj.keyframe_insert(data_path="rotation_euler")
        
        # Insert final keyframe
        scene.frame_set(frames)
        text_obj.rotation_euler = (0, 0, math.pi * 2)  # 360 degrees
        text_obj.keyframe_insert(data_path="rotation_euler")
        
    elif anim_type == 'SCALE':
        text_obj.scale = (1, 1, 1)
        text_obj.keyframe_insert(data_path="scale")
        
        # Insert middle keyframe
        scene.frame_set(frames // 2)
        text_obj.scale = (1.5, 1.5, 1.5)
        text_obj.keyframe_insert(data_path="scale")
        
        # Insert final keyframe
        scene.frame_set(frames)
        text_obj.scale = (1, 1, 1)
        text_obj.keyframe_insert(data_path="scale")
        
    elif anim_type == 'FADE':
        # For fade animation, we need a material with transparency
        mat = bpy.data.materials.new(name=f"{name}Material")
        mat.use_nodes = True
        mat.blend_method = 'BLEND'  # Enable transparency
        
        # Assign material to the text object
        if text_obj.data.materials:
            text_obj.data.materials[0] = mat
        else:
            text_obj.data.materials.append(mat)
        
        # Get the Principled BSDF shader
        principled = mat.node_tree.nodes.get('Principled BSDF')
        
        # Set initial alpha value
        principled.inputs['Alpha'].default_value = 1.0
        principled.inputs['Alpha'].keyframe_insert('default_value', frame=1)
        
        # Set middle keyframe
        principled.inputs['Alpha'].default_value = 0.0
        principled.inputs['Alpha'].keyframe_insert('default_value', frame=frames // 2)
        
        # Set final keyframe
        principled.inputs['Alpha'].default_value = 1.0
        principled.inputs['Alpha'].keyframe_insert('default_value', frame=frames)
    
    # Make the animation cycle
    for fcurve in text_obj.animation_data.action.fcurves:
        fcurve.extrapolation = 'CYCLIC'
    
    return text_obj


def create_extruded_logo_text(text="LOGO", name="LogoText", location=(0, 0, 0),
                             size=1.0, extrude=0.5, bevel_depth=0.05, bevel_resolution=4,
                             material_color=(0.2, 0.6, 1.0, 1.0)):
    """Create an extruded text object suitable for a logo.
    
    Args:
        text: The text content.
        name: Name for the text object.
        location: (x, y, z) tuple for object location.
        size: Font size.
        extrude: Extrusion depth.
        bevel_depth: Bevel depth (for rounded edges).
        bevel_resolution: Bevel resolution (subdivisions).
        material_color: (R, G, B, A) tuple for the material color.
        
    Returns:
        The created text object.
    """
    # Create the text object with extrusion and bevel
    text_obj = create_text_object(
        text=text,
        name=name,
        location=location,
        size=size,
        extrude=extrude,
        bevel_depth=bevel_depth,
        bevel_resolution=bevel_resolution
    )
    
    # Center the text
    set_text_alignment(text_obj, align_x='CENTER', align_y='CENTER')
    
    # Add material
    mat = bpy.data.materials.new(name=f"{name}Material")
    mat.use_nodes = True
    
    # Get the Principled BSDF shader
    principled = mat.node_tree.nodes.get('Principled BSDF')
    if principled:
        # Set the base color
        principled.inputs['Base Color'].default_value = material_color
        # Set metallic look
        principled.inputs['Metallic'].default_value = 0.8
        principled.inputs['Specular'].default_value = 0.7
        principled.inputs['Roughness'].default_value = 0.1
    
    # Assign the material to the text object
    if text_obj.data.materials:
        text_obj.data.materials[0] = mat
    else:
        text_obj.data.materials.append(mat)
    
    return text_obj


def create_neon_text(text="NEON", name="NeonText", location=(0, 0, 0),
                    size=1.0, extrude=0.1, bevel_depth=0.03, bevel_resolution=3,
                    color=(0, 1, 0.8, 1)):
    """Create a text object with a neon glow effect.
    
    Args:
        text: The text content.
        name: Name for the text object.
        location: (x, y, z) tuple for object location.
        size: Font size.
        extrude: Extrusion depth.
        bevel_depth: Bevel depth (for rounded edges).
        bevel_resolution: Bevel resolution (subdivisions).
        color: (R, G, B, A) tuple for the neon color.
        
    Returns:
        The created text object.
    """
    # Create the text object with extrusion and bevel
    text_obj = create_text_object(
        text=text,
        name=name,
        location=location,
        size=size,
        extrude=extrude,
        bevel_depth=bevel_depth,
        bevel_resolution=bevel_resolution
    )
    
    # Add neon material
    mat = bpy.data.materials.new(name=f"{name}Material")
    mat.use_nodes = True
    
    # Create neon shader nodes
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    
    # Clear default nodes
    nodes.clear()
    
    # Create emission shader
    emission = nodes.new(type='ShaderNodeEmission')
    emission.inputs['Color'].default_value = color
    emission.inputs['Strength'].default_value = 5.0  # High emission strength
    
    # Create output node
    output = nodes.new(type='ShaderNodeOutputMaterial')
    
    # Connect nodes
    links.new(emission.outputs['Emission'], output.inputs['Surface'])
    
    # Assign the material to the text object
    if text_obj.data.materials:
        text_obj.data.materials[0] = mat
    else:
        text_obj.data.materials.append(mat)
    
    return text_obj


def save_blend_file(filepath, obj=None):
    """Save the current scene or specific object to a .blend file.
    
    Args:
        filepath: Path to save the .blend file.
        obj: Optional object to save. If None, saves the entire scene.
    """
    # Ensure the directory exists
    directory = os.path.dirname(filepath)
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    if obj is not None:
        # Deselect all objects
        bpy.ops.object.select_all(action='DESELECT')
        
        # Select only the desired object
        obj.select_set(True)
        
        # Set as active object
        bpy.context.view_layer.objects.active = obj
        
        # Save the file with only the selected object
        bpy.ops.wm.save_as_mainfile(filepath=filepath, copy=True)
    else:
        # Save the entire scene
        bpy.ops.wm.save_as_mainfile(filepath=filepath)


def create_all_text_types(save_dir="./blend_files/text_types/"):
    """Create all text object types and save them as individual .blend files.
    
    Args:
        save_dir: Directory to save the .blend files.
    """
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    # Dictionary of creation functions and their parameters
    text_types = {
        "basic_text": {"func": create_text_object, "params": {"text": "Basic Text"}},
        "3d_text": {"func": create_3d_text, "params": {}},
        "text_to_mesh": {"func": create_text_to_mesh, "params": {}},
        "multi_line_text": {"func": create_multi_line_text, "params": {}},
        "text_with_materials": {"func": create_text_with_materials, "params": {}},
        "extruded_logo_text": {"func": create_extruded_logo_text, "params": {}},
        "neon_text": {"func": create_neon_text, "params": {}}
    }
    
    # Special case for text on curve (returns multiple objects)
    try:
        clear_scene()
        text_obj, curve_obj = create_text_on_curve(text="Text On Path", curve_type='CIRCLE')
        filepath = os.path.join(save_dir, "text_on_curve.blend")
        save_blend_file(filepath)  # Save entire scene
        print(f"Created and saved text_on_curve to {filepath}")
    except Exception as e:
        print(f"Error creating text_on_curve: {e}")
    
    # Special case for animated text (has animation data)
    try:
        clear_scene()
        text_obj = create_text_with_animation(text="Animated", anim_type='ROTATE')
        filepath = os.path.join(save_dir, "animated_text.blend")
        save_blend_file(filepath)  # Save entire scene with animation
        print(f"Created and saved animated_text to {filepath}")
    except Exception as e:
        print(f"Error creating animated_text: {e}")
    
    # Create and save the rest of the text types
    for name, data in text_types.items():
        try:
            # Clear the scene
            clear_scene()
            
            # Create the text object
            obj = data["func"](**data["params"])
            
            # Save to a .blend file
            filepath = os.path.join(save_dir, f"{name}.blend")
            save_blend_file(filepath, obj)
            
            print(f"Created and saved {name} to {filepath}")
        except Exception as e:
            print(f"Error creating {name}: {e}")


# Example usage
if __name__ == "__main__":
    # Create and save all text object types
    create_all_text_types()
    
    # Or create and save individual text objects
    # clear_scene()
    # neon = create_neon_text(text="NEON GLOW", color=(1, 0.2, 0.8, 1))
    # save_blend_file("./blend_files/text_types/custom_neon.blend", neon)