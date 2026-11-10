import bpy
import os
import math
from mathutils import Vector


def clear_scene():
    """Clear the current scene of all objects."""
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()


def create_empty_plain(name="EmptyPlain", location=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1)):
    """Create a plain empty object.
    
    Args:
        name: Name for the empty object.
        location: (x, y, z) tuple for object location.
        rotation: (x, y, z) tuple for object rotation in radians.
        scale: (x, y, z) tuple for object scale.
        
    Returns:
        The created empty object.
    """
    # Create an empty object of type 'PLAIN_AXES'
    bpy.ops.object.empty_add(type='PLAIN_AXES', location=location, rotation=rotation)
    
    # Get the created object
    empty_obj = bpy.context.active_object
    empty_obj.name = name
    
    # Set scale
    empty_obj.scale = scale
    
    return empty_obj


def create_empty_arrows(name="EmptyArrows", location=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1)):
    """Create an empty object with arrows display.
    
    Args:
        name: Name for the empty object.
        location: (x, y, z) tuple for object location.
        rotation: (x, y, z) tuple for object rotation in radians.
        scale: (x, y, z) tuple for object scale.
        
    Returns:
        The created empty object.
    """
    # Create an empty object of type 'ARROWS'
    bpy.ops.object.empty_add(type='ARROWS', location=location, rotation=rotation)
    
    # Get the created object
    empty_obj = bpy.context.active_object
    empty_obj.name = name
    
    # Set scale
    empty_obj.scale = scale
    
    return empty_obj


def create_empty_sphere(name="EmptySphere", location=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1), radius=1.0):
    """Create an empty object with sphere display.
    
    Args:
        name: Name for the empty object.
        location: (x, y, z) tuple for object location.
        rotation: (x, y, z) tuple for object rotation in radians.
        scale: (x, y, z) tuple for object scale.
        radius: Radius of the sphere display.
        
    Returns:
        The created empty object.
    """
    # Create an empty object of type 'SPHERE'
    bpy.ops.object.empty_add(type='SPHERE', radius=radius, location=location, rotation=rotation)
    
    # Get the created object
    empty_obj = bpy.context.active_object
    empty_obj.name = name
    
    # Set scale
    empty_obj.scale = scale
    
    return empty_obj


def create_empty_cube(name="EmptyCube", location=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1), size=1.0):
    """Create an empty object with cube display.
    
    Args:
        name: Name for the empty object.
        location: (x, y, z) tuple for object location.
        rotation: (x, y, z) tuple for object rotation in radians.
        scale: (x, y, z) tuple for object scale.
        size: Size of the cube display.
        
    Returns:
        The created empty object.
    """
    # Create an empty object of type 'CUBE'
    bpy.ops.object.empty_add(type='CUBE', location=location, rotation=rotation)
    
    # Get the created object
    empty_obj = bpy.context.active_object
    empty_obj.name = name
    
    # Set display size
    empty_obj.empty_display_size = size
    
    # Set scale
    empty_obj.scale = scale
    
    return empty_obj


def create_empty_circle(name="EmptyCircle", location=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1), radius=1.0):
    """Create an empty object with circle display.
    
    Args:
        name: Name for the empty object.
        location: (x, y, z) tuple for object location.
        rotation: (x, y, z) tuple for object rotation in radians.
        scale: (x, y, z) tuple for object scale.
        radius: Radius of the circle display.
        
    Returns:
        The created empty object.
    """
    # Create an empty object of type 'CIRCLE'
    bpy.ops.object.empty_add(type='CIRCLE', radius=radius, location=location, rotation=rotation)
    
    # Get the created object
    empty_obj = bpy.context.active_object
    empty_obj.name = name
    
    # Set scale
    empty_obj.scale = scale
    
    return empty_obj


def create_empty_cone(name="EmptyCone", location=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1), radius=1.0):
    """Create an empty object with cone display.
    
    Args:
        name: Name for the empty object.
        location: (x, y, z) tuple for object location.
        rotation: (x, y, z) tuple for object rotation in radians.
        scale: (x, y, z) tuple for object scale.
        radius: Radius of the cone display.
        
    Returns:
        The created empty object.
    """
    # Create an empty object of type 'CONE'
    bpy.ops.object.empty_add(type='CONE', radius=radius, location=location, rotation=rotation)
    
    # Get the created object
    empty_obj = bpy.context.active_object
    empty_obj.name = name
    
    # Set scale
    empty_obj.scale = scale
    
    return empty_obj


def create_empty_image(name="EmptyImage", location=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1), 
                       image_path=None, size=5.0):
    """Create an empty object with an image display.
    
    Args:
        name: Name for the empty object.
        location: (x, y, z) tuple for object location.
        rotation: (x, y, z) tuple for object rotation in radians.
        scale: (x, y, z) tuple for object scale.
        image_path: Path to the image file. If None, no image is used.
        size: Size of the image display.
        
    Returns:
        The created empty object.
    """
    # Create an empty object of type 'IMAGE'
    bpy.ops.object.empty_add(type='IMAGE', location=location, rotation=rotation)
    
    # Get the created object
    empty_obj = bpy.context.active_object
    empty_obj.name = name
    
    # Set display size
    empty_obj.empty_display_size = size
    
    # Set scale
    empty_obj.scale = scale
    
    # Load and assign image if path is provided
    if image_path and os.path.exists(image_path):
        try:
            image = bpy.data.images.load(image_path)
            empty_obj.data = image
        except Exception as e:
            print(f"Error loading image: {e}")
    
    return empty_obj


def create_empty_single_arrow(name="EmptySingleArrow", location=(0, 0, 0), rotation=(0, 0, 0), 
                             scale=(1, 1, 1), size=1.0):
    """Create an empty object with single arrow display.
    
    Args:
        name: Name for the empty object.
        location: (x, y, z) tuple for object location.
        rotation: (x, y, z) tuple for object rotation in radians.
        scale: (x, y, z) tuple for object scale.
        size: Size of the arrow display.
        
    Returns:
        The created empty object.
    """
    # Create an empty object of type 'SINGLE_ARROW'
    bpy.ops.object.empty_add(type='SINGLE_ARROW', location=location, rotation=rotation)
    
    # Get the created object
    empty_obj = bpy.context.active_object
    empty_obj.name = name
    
    # Set display size
    empty_obj.empty_display_size = size
    
    # Set scale
    empty_obj.scale = scale
    
    return empty_obj


def create_empty_with_constraint(name="EmptyConstraint", empty_type='PLAIN_AXES', 
                                location=(0, 0, 0), constraint_type='COPY_LOCATION', 
                                target=None, influence=1.0):
    """Create an empty object with a constraint.
    
    Args:
        name: Name for the empty object.
        empty_type: Type of empty ('PLAIN_AXES', 'ARROWS', 'SPHERE', 'CUBE', etc.).
        location: (x, y, z) tuple for object location.
        constraint_type: Type of constraint to add ('COPY_LOCATION', 'COPY_ROTATION', 'COPY_SCALE', etc.).
        target: Target object for the constraint. If None, no constraint is added.
        influence: Influence factor for the constraint (0.0 to 1.0).
        
    Returns:
        The created empty object.
    """
    # Create an empty object of specified type
    bpy.ops.object.empty_add(type=empty_type, location=location)
    
    # Get the created object
    empty_obj = bpy.context.active_object
    empty_obj.name = name
    
    # Add constraint if target is provided
    if target is not None:
        constraint = empty_obj.constraints.new(type=constraint_type)
        constraint.target = target
        constraint.influence = influence
    
    return empty_obj


def create_empty_parent(name="EmptyParent", children=None, location=(0, 0, 0), empty_type='PLAIN_AXES'):
    """Create an empty object and make it the parent of specified objects.
    
    Args:
        name: Name for the empty object.
        children: List of objects to parent to the empty. If None, no parenting is done.
        location: (x, y, z) tuple for object location.
        empty_type: Type of empty ('PLAIN_AXES', 'ARROWS', 'SPHERE', 'CUBE', etc.).
        
    Returns:
        The created empty object.
    """
    # Create an empty object
    bpy.ops.object.empty_add(type=empty_type, location=location)
    
    # Get the created object
    empty_obj = bpy.context.active_object
    empty_obj.name = name
    
    # Parent children to the empty
    if children:
        # Store the active object
        original_active = bpy.context.active_object
        
        # Deselect all objects
        bpy.ops.object.select_all(action='DESELECT')
        
        # Select all children
        for child in children:
            child.select_set(True)
        
        # Set the empty as active
        bpy.context.view_layer.objects.active = empty_obj
        empty_obj.select_set(True)
        
        # Parent objects to the empty (keep transforms)
        bpy.ops.object.parent_set(type='OBJECT', keep_transform=True)
        
        # Restore original selection
        bpy.ops.object.select_all(action='DESELECT')
        bpy.context.view_layer.objects.active = original_active
        original_active.select_set(True)
    
    return empty_obj


def create_empty_hierarchy(name_prefix="Level", levels=3, branch_factor=2, 
                          base_location=(0, 0, 0), level_spacing=1.0, 
                          empty_type='PLAIN_AXES'):
    """Create a hierarchy of empty objects.
    
    Args:
        name_prefix: Prefix for naming the empty objects.
        levels: Number of hierarchy levels.
        branch_factor: Number of children per parent.
        base_location: (x, y, z) tuple for root location.
        level_spacing: Vertical spacing between hierarchy levels.
        empty_type: Type of empty ('PLAIN_AXES', 'ARROWS', 'SPHERE', 'CUBE', etc.).
        
    Returns:
        The root empty object.
    """
    def create_level(parent, level, pos, index_path=()):
        """Recursively create hierarchy levels."""
        if level > levels:
            return
        
        # Create objects for this level
        level_objects = []
        for i in range(branch_factor):
            # Calculate position offset based on level and branch
            branch_spread = 1.0 + level * 0.5  # Wider spread for deeper levels
            offset_x = (i - (branch_factor - 1) / 2) * branch_spread
            offset_z = -level_spacing
            
            new_pos = (pos[0] + offset_x, pos[1], pos[2] + offset_z)
            
            # Create unique name with path indices
            current_path = index_path + (i,)
            obj_name = f"{name_prefix}_{level}" + "".join(f"_{idx}" for idx in current_path)
            
            # Create empty
            empty = create_empty_plain(name=obj_name, location=new_pos, 
                                    rotation=(0, 0, 0), scale=(1, 1, 1))
            
            # Change empty type if needed
            empty.empty_display_type = empty_type
            
            level_objects.append(empty)
            
            # Create children for this object
            create_level(empty, level + 1, new_pos, current_path)
        
        # Parent all created objects to the parent
        if parent is not None:
            for obj in level_objects:
                obj.parent = parent
    
    # Create root empty
    root = create_empty_plain(name=f"{name_prefix}_Root", location=base_location)
    root.empty_display_type = empty_type
    
    # Create the hierarchy
    create_level(root, 1, base_location)
    
    return root


def create_empty_track(name="TrackEmpty", target=None, location=(0, 0, 0), empty_type='PLAIN_AXES'):
    """Create an empty object with a Track To constraint.
    
    Args:
        name: Name for the empty object.
        target: Target object to track. If None, no tracking is set up.
        location: (x, y, z) tuple for object location.
        empty_type: Type of empty ('PLAIN_AXES', 'ARROWS', 'SPHERE', 'CUBE', etc.).
        
    Returns:
        The created empty object.
    """
    # Create an empty object
    bpy.ops.object.empty_add(type=empty_type, location=location)
    
    # Get the created object
    empty_obj = bpy.context.active_object
    empty_obj.name = name
    
    # Add Track To constraint if target is provided
    if target is not None:
        constraint = empty_obj.constraints.new(type='TRACK_TO')
        constraint.target = target
        constraint.track_axis = 'TRACK_Z'
        constraint.up_axis = 'UP_Y'
    
    return empty_obj


def create_empty_path_animation(name="PathEmpty", path_object=None, location=(0, 0, 0), 
                               empty_type='PLAIN_AXES', frames=48):
    """Create an empty object that follows a path with animation.
    
    Args:
        name: Name for the empty object.
        path_object: Curve object to follow. If None, creates a simple path.
        location: (x, y, z) tuple for object location.
        empty_type: Type of empty ('PLAIN_AXES', 'ARROWS', 'SPHERE', 'CUBE', etc.).
        frames: Number of frames for the animation.
        
    Returns:
        The created empty object and the path object.
    """
    # Create an empty object
    bpy.ops.object.empty_add(type=empty_type, location=location)
    
    # Get the created object
    empty_obj = bpy.context.active_object
    empty_obj.name = name
    
    # Create a path if none is provided
    if path_object is None:
        bpy.ops.curve.primitive_bezier_circle_add(radius=2.0, location=location)
        path_object = bpy.context.active_object
        path_object.name = f"{name}Path"
    
    # Make sure the path is set up for animation
    path_object.data.use_path = True
    path_object.data.path_duration = frames
    
    # Set up follow path constraint
    constraint = empty_obj.constraints.new(type='FOLLOW_PATH')
    constraint.target = path_object
    constraint.use_curve_follow = True
    
    # Set up animation
    constraint.offset_factor = 0.0
    constraint.keyframe_insert(data_path="offset_factor", frame=1)
    
    constraint.offset_factor = 1.0
    constraint.keyframe_insert(data_path="offset_factor", frame=frames)
    
    # Return both objects
    return empty_obj, path_object


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


def create_all_empty_types(save_dir="./blend_files/empty_types/"):
    """Create all empty object types and save them as individual .blend files.
    
    Args:
        save_dir: Directory to save the .blend files.
    """
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    # Dictionary of creation functions and their parameters
    empty_types = {
        "empty_plain": {"func": create_empty_plain, "params": {}},
        "empty_arrows": {"func": create_empty_arrows, "params": {}},
        "empty_sphere": {"func": create_empty_sphere, "params": {}},
        "empty_cube": {"func": create_empty_cube, "params": {}},
        "empty_circle": {"func": create_empty_circle, "params": {}},
        "empty_cone": {"func": create_empty_cone, "params": {}},
        "empty_single_arrow": {"func": create_empty_single_arrow, "params": {}}
    }
    
    # Create and save basic empty types
    for name, data in empty_types.items():
        try:
            # Clear the scene
            clear_scene()
            
            # Create the empty object
            obj = data["func"](**data["params"])
            
            # Save to a .blend file
            filepath = os.path.join(save_dir, f"{name}.blend")
            save_blend_file(filepath, obj)
            
            print(f"Created and saved {name} to {filepath}")
        except Exception as e:
            print(f"Error creating {name}: {e}")
    
    # Create and save empty hierarchy
    try:
        clear_scene()
        root = create_empty_hierarchy(levels=2, branch_factor=2)
        filepath = os.path.join(save_dir, "empty_hierarchy.blend")
        save_blend_file(filepath)  # Save entire scene
        print(f"Created and saved empty_hierarchy to {filepath}")
    except Exception as e:
        print(f"Error creating empty_hierarchy: {e}")
    
    # Create and save path animation empty
    try:
        clear_scene()
        empty_obj, path_obj = create_empty_path_animation()
        filepath = os.path.join(save_dir, "empty_path_animation.blend")
        save_blend_file(filepath)  # Save entire scene
        print(f"Created and saved empty_path_animation to {filepath}")
    except Exception as e:
        print(f"Error creating empty_path_animation: {e}")
    
    # Create parent-child relationship with empties and objects
    try:
        clear_scene()
        
        # Create some objects to parent
        bpy.ops.mesh.primitive_cube_add(size=0.5, location=(1, 0, 0))
        cube = bpy.context.active_object
        cube.name = "ChildCube"
        
        bpy.ops.mesh.primitive_uv_sphere_add(radius=0.5, location=(-1, 0, 0))
        sphere = bpy.context.active_object
        sphere.name = "ChildSphere"
        
        # Create parent empty
        parent_empty = create_empty_parent(name="ParentEmpty", children=[cube, sphere])
        
        filepath = os.path.join(save_dir, "empty_parent.blend")
        save_blend_file(filepath)  # Save entire scene
        print(f"Created and saved empty_parent to {filepath}")
    except Exception as e:
        print(f"Error creating empty_parent: {e}")


# Example usage
if __name__ == "__main__":
    # Create and save all empty object types
    create_all_empty_types()
    
    # Or create and save individual empty objects
    # clear_scene()
    # empty = create_empty_sphere(name="MySphere", radius=2.0)
    # save_blend_file("./blend_files/empty_types/my_sphere_empty.blend", empty)