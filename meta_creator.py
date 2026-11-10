import bpy
import os
import math
from mathutils import Vector


def clear_scene():
    """Clear the current scene of all objects."""
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()


def create_meta_ball(radius=1.0, name="MetaBall", location=(0, 0, 0)):
    """Create a meta ball object.
    
    Args:
        radius: Radius of the meta ball.
        name: Name for the meta object.
        location: (x, y, z) tuple for object location.
        
    Returns:
        The created meta object.
    """
    # Create meta ball
    bpy.ops.object.metaball_add(type='BALL', radius=radius, location=location)
    
    # Get the created object
    meta_obj = bpy.context.active_object
    meta_obj.name = name
    
    return meta_obj


def create_meta_capsule(radius=1.0, size_x=2.0, name="MetaCapsule", location=(0, 0, 0)):
    """Create a meta capsule object.
    
    Args:
        radius: Radius of the meta capsule.
        size_x: Length of the capsule.
        name: Name for the meta object.
        location: (x, y, z) tuple for object location.
        
    Returns:
        The created meta object.
    """
    # Create meta capsule
    bpy.ops.object.metaball_add(type='CAPSULE', radius=radius, location=location)
    
    # Get the created object
    meta_obj = bpy.context.active_object
    meta_obj.name = name
    
    # Get the active element
    meta_element = meta_obj.data.elements[-1]
    meta_element.size_x = size_x
    
    return meta_obj


def create_meta_plane(radius=1.0, size_x=2.0, name="MetaPlane", location=(0, 0, 0)):
    """Create a meta plane object.
    
    Args:
        radius: Radius of the meta plane.
        size_x: Size of the plane.
        name: Name for the meta object.
        location: (x, y, z) tuple for object location.
        
    Returns:
        The created meta object.
    """
    # Create meta plane
    bpy.ops.object.metaball_add(type='PLANE', radius=radius, location=location)
    
    # Get the created object
    meta_obj = bpy.context.active_object
    meta_obj.name = name
    
    # Get the active element
    meta_element = meta_obj.data.elements[-1]
    meta_element.size_x = size_x
    
    return meta_obj


def create_meta_ellipsoid(radius=1.0, size_x=1.5, size_y=1.0, size_z=1.0, name="MetaEllipsoid", location=(0, 0, 0)):
    """Create a meta ellipsoid object.
    
    Args:
        radius: Base radius of the meta ellipsoid.
        size_x: X size of the ellipsoid.
        size_y: Y size of the ellipsoid.
        size_z: Z size of the ellipsoid.
        name: Name for the meta object.
        location: (x, y, z) tuple for object location.
        
    Returns:
        The created meta object.
    """
    # Create meta ellipsoid
    bpy.ops.object.metaball_add(type='ELLIPSOID', radius=radius, location=location)
    
    # Get the created object
    meta_obj = bpy.context.active_object
    meta_obj.name = name
    
    # Get the active element
    meta_element = meta_obj.data.elements[-1]
    meta_element.size_x = size_x
    meta_element.size_y = size_y
    meta_element.size_z = size_z
    
    return meta_obj


def create_meta_cube(radius=1.0, size=1.5, name="MetaCube", location=(0, 0, 0)):
    """Create a meta cube object.
    
    Args:
        radius: Base radius of the meta cube.
        size: Size of the cube.
        name: Name for the meta object.
        location: (x, y, z) tuple for object location.
        
    Returns:
        The created meta object.
    """
    # Create meta cube
    bpy.ops.object.metaball_add(type='CUBE', radius=radius, location=location)
    
    # Get the created object
    meta_obj = bpy.context.active_object
    meta_obj.name = name
    
    # Get the active element
    meta_element = meta_obj.data.elements[-1]
    meta_element.size_x = size
    meta_element.size_y = size
    meta_element.size_z = size
    
    return meta_obj


def create_meta_molecule(positions=None, radii=None, name="MetaMolecule", location=(0, 0, 0)):
    """Create a molecule-like structure using multiple meta balls.
    
    Args:
        positions: List of (x, y, z) tuples for positions of each meta ball.
                   If None, uses default positions.
        radii: List of radii for each meta ball. If None, uses default radii.
        name: Base name for the meta object.
        location: (x, y, z) tuple for object's center location.
        
    Returns:
        The created meta object.
    """
    # Default positions if none provided
    if positions is None:
        positions = [
            (0, 0, 0),         # Center
            (1.2, 0, 0),        # +X
            (-1.2, 0, 0),       # -X
            (0, 1.2, 0),        # +Y
            (0, -1.2, 0),       # -Y
            (0, 0, 1.2),        # +Z
            (0, 0, -1.2),       # -Z
            (0.8, 0.8, 0.8),    # +X+Y+Z
            (-0.8, -0.8, -0.8)  # -X-Y-Z
        ]
    
    # Default radii if none provided
    if radii is None:
        radii = [1.0] + [0.7] * 8  # First ball bigger, rest smaller
    
    # Ensure we have a radius for each position
    if len(radii) < len(positions):
        radii.extend([0.7] * (len(positions) - len(radii)))
    
    # Create the first meta ball
    bpy.ops.object.metaball_add(
        type='BALL', 
        radius=radii[0], 
        location=Vector(positions[0]) + Vector(location)
    )
    
    # Get the meta object
    meta_obj = bpy.context.active_object
    meta_obj.name = name
    
    # Add additional meta elements to the same meta object
    for i in range(1, len(positions)):
        # Add a new element
        element = meta_obj.data.elements.new()
        element.co = Vector(positions[i])  # Local coordinates
        element.radius = radii[i]
        element.type = 'BALL'
    
    return meta_obj


def create_meta_blob(name="MetaBlob", seed=42, num_elements=5, location=(0, 0, 0)):
    """Create a random blob using multiple meta balls.
    
    Args:
        name: Name for the meta object.
        seed: Random seed for reproducibility.
        num_elements: Number of meta elements to create.
        location: (x, y, z) tuple for object's center location.
        
    Returns:
        The created meta object.
    """
    import random
    random.seed(seed)
    
    # Create the first meta ball at the center
    bpy.ops.object.metaball_add(type='BALL', radius=1.0, location=location)
    
    # Get the meta object
    meta_obj = bpy.context.active_object
    meta_obj.name = name
    
    # Add additional meta elements to create a blob
    for i in range(1, num_elements):
        # Random position offset from center
        offset = (
            random.uniform(-1.5, 1.5),
            random.uniform(-1.5, 1.5),
            random.uniform(-1.5, 1.5)
        )
        
        # Random radius
        radius = random.uniform(0.3, 1.0)
        
        # Random type
        element_type = random.choice(['BALL', 'ELLIPSOID', 'CAPSULE'])
        
        # Add a new element
        element = meta_obj.data.elements.new()
        element.co = offset
        element.radius = radius
        element.type = element_type
        
        # If ellipsoid or capsule, set random sizes
        if element_type in ['ELLIPSOID', 'CAPSULE']:
            element.size_x = random.uniform(0.5, 2.0)
            if element_type == 'ELLIPSOID':
                element.size_y = random.uniform(0.5, 2.0)
                element.size_z = random.uniform(0.5, 2.0)
    
    return meta_obj


def create_meta_tubes(num_rings=3, balls_per_ring=8, radius=0.5, ring_radius=2.0, name="MetaTubes", location=(0, 0, 0)):
    """Create a set of interconnected meta ball tubes.
    
    Args:
        num_rings: Number of rings of meta balls.
        balls_per_ring: Number of meta balls in each ring.
        radius: Radius of each meta ball.
        ring_radius: Radius of the rings.
        name: Name for the meta object.
        location: (x, y, z) tuple for object's center location.
        
    Returns:
        The created meta object.
    """
    # Create the first meta ball
    bpy.ops.object.metaball_add(type='BALL', radius=radius, location=location)
    
    # Get the meta object
    meta_obj = bpy.context.active_object
    meta_obj.name = name
    
    # Generate positions for meta balls in rings
    positions = []
    for ring in range(num_rings):
        z_offset = (ring - (num_rings - 1) / 2) * radius * 4
        for i in range(balls_per_ring):
            angle = 2 * math.pi * i / balls_per_ring
            x = ring_radius * math.cos(angle)
            y = ring_radius * math.sin(angle)
            z = z_offset
            positions.append((x, y, z))
    
    # Add meta elements for each position
    for pos in positions:
        element = meta_obj.data.elements.new()
        element.co = Vector(pos)
        element.radius = radius
        element.type = 'BALL'
    
    # Adjust meta object settings for better tubes
    meta_obj.data.threshold = 0.4  # Adjust for better connections
    
    return meta_obj


def create_meta_dna(turns=3, bases_per_turn=10, radius=0.3, helix_radius=1.0, height=6.0, name="MetaDNA", location=(0, 0, 0)):
    """Create a DNA-like structure using meta balls.
    
    Args:
        turns: Number of full turns in the helix.
        bases_per_turn: Number of base pairs per turn.
        radius: Radius of each meta ball.
        helix_radius: Radius of the helix.
        height: Total height of the helix.
        name: Name for the meta object.
        location: (x, y, z) tuple for object's center location.
        
    Returns:
        The created meta object.
    """
    # Create the first meta ball
    bpy.ops.object.metaball_add(type='BALL', radius=radius, location=location)
    
    # Get the meta object
    meta_obj = bpy.context.active_object
    meta_obj.name = name
    
    # Generate positions for the two strands of DNA
    positions = []
    total_bases = int(turns * bases_per_turn)
    
    for i in range(total_bases):
        t = i / (total_bases - 1)  # Parameter from 0 to 1
        
        # Calculate height along the helix
        z = t * height - height / 2
        
        # Calculate angles for the two strands (offset by 180 degrees)
        angle1 = 2 * math.pi * turns * t
        angle2 = angle1 + math.pi  # 180 degrees offset
        
        # First strand
        x1 = helix_radius * math.cos(angle1)
        y1 = helix_radius * math.sin(angle1)
        positions.append((x1, y1, z))
        
        # Second strand
        x2 = helix_radius * math.cos(angle2)
        y2 = helix_radius * math.sin(angle2)
        positions.append((x2, y2, z))
        
        # Optional: add "base pairs" connecting the strands
        if i % 2 == 0:  # Add base pair every other position
            # Multiple points to form a "bar" between the strands
            for j in range(3):
                frac = (j + 1) / 4  # Points at 0.25, 0.5, 0.75 along the bar
                x_base = x1 * (1 - frac) + x2 * frac
                y_base = y1 * (1 - frac) + y2 * frac
                positions.append((x_base, y_base, z))
    
    # Add meta elements for each position
    for pos in positions:
        element = meta_obj.data.elements.new()
        element.co = Vector(pos)
        element.radius = radius
        element.type = 'BALL'
    
    # Adjust meta object settings for better connections
    meta_obj.data.threshold = 0.6
    meta_obj.data.resolution = 0.1
    
    return meta_obj


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


def create_all_meta_types(save_dir="./blend_files/meta_types/"):
    """Create all meta object types and save them as individual .blend files.
    
    Args:
        save_dir: Directory to save the .blend files.
    """
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    # Dictionary of creation functions and their parameters
    meta_types = {
        "meta_ball": {"func": create_meta_ball, "params": {}},
        "meta_capsule": {"func": create_meta_capsule, "params": {}},
        "meta_plane": {"func": create_meta_plane, "params": {}},
        "meta_ellipsoid": {"func": create_meta_ellipsoid, "params": {}},
        "meta_cube": {"func": create_meta_cube, "params": {}},
        "meta_molecule": {"func": create_meta_molecule, "params": {}},
        "meta_blob": {"func": create_meta_blob, "params": {}},
        "meta_tubes": {"func": create_meta_tubes, "params": {}},
        "meta_dna": {"func": create_meta_dna, "params": {}}
    }
    
    for name, data in meta_types.items():
        try:
            # Clear the scene
            clear_scene()
            
            # Create the meta object
            obj = data["func"](**data["params"])
            
            # Save to a .blend file
            filepath = os.path.join(save_dir, f"{name}.blend")
            save_blend_file(filepath, obj)
            
            print(f"Created and saved {name} to {filepath}")
        except Exception as e:
            print(f"Error creating {name}: {e}")


# Example usage
if __name__ == "__main__":
    # Create and save all meta object types
    create_all_meta_types()
    
    # Or create and save individual meta objects
    # clear_scene()
    # dna = create_meta_dna(turns=2, height=5.0)
    # save_blend_file("./blend_files/meta_types/my_dna.blend", dna)