import bpy
import os
import math


def clear_scene():
    """Clear the current scene of all objects."""
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()


def create_cube(size=2.0, location=(0, 0, 0)):
    """Create a cube mesh object.
    
    Args:
        size: Size of the cube.
        location: (x, y, z) tuple for object location.
    
    Returns:
        The created object.
    """
    bpy.ops.mesh.primitive_cube_add(size=size, location=location)
    cube = bpy.context.active_object
    cube.name = "Cube"
    return cube


def create_sphere(radius=1.0, segments=32, rings=16, location=(0, 0, 0)):
    """Create a UV sphere mesh object.
    
    Args:
        radius: Radius of the sphere.
        segments: Number of segments (longitude).
        rings: Number of rings (latitude).
        location: (x, y, z) tuple for object location.
    
    Returns:
        The created object.
    """
    bpy.ops.mesh.primitive_uv_sphere_add(
        radius=radius,
        segments=segments,
        ring_count=rings,
        location=location
    )
    sphere = bpy.context.active_object
    sphere.name = "Sphere"
    return sphere


def create_cylinder(radius=1.0, depth=2.0, vertices=32, location=(0, 0, 0)):
    """Create a cylinder mesh object.
    
    Args:
        radius: Radius of the cylinder.
        depth: Height of the cylinder.
        vertices: Number of vertices around the circumference.
        location: (x, y, z) tuple for object location.
    
    Returns:
        The created object.
    """
    bpy.ops.mesh.primitive_cylinder_add(
        radius=radius,
        depth=depth,
        vertices=vertices,
        location=location
    )
    cylinder = bpy.context.active_object
    cylinder.name = "Cylinder"
    return cylinder


def create_cone(radius1=1.0, radius2=0.0, depth=2.0, vertices=32, location=(0, 0, 0)):
    """Create a cone mesh object.
    
    Args:
        radius1: Radius of the base of the cone.
        radius2: Radius of the top of the cone (0 for a true cone).
        depth: Height of the cone.
        vertices: Number of vertices around the circumference.
        location: (x, y, z) tuple for object location.
    
    Returns:
        The created object.
    """
    bpy.ops.mesh.primitive_cone_add(
        radius1=radius1,
        radius2=radius2,
        depth=depth,
        vertices=vertices,
        location=location
    )
    cone = bpy.context.active_object
    cone.name = "Cone"
    return cone


def create_torus(major_radius=1.0, minor_radius=0.25, major_segments=48, minor_segments=12, location=(0, 0, 0)):
    """Create a torus mesh object.
    
    Args:
        major_radius: Major radius of the torus (from center to ring center).
        minor_radius: Minor radius of the torus (thickness of the ring).
        major_segments: Number of segments along the major circle.
        minor_segments: Number of segments along the minor circle.
        location: (x, y, z) tuple for object location.
    
    Returns:
        The created object.
    """
    bpy.ops.mesh.primitive_torus_add(
        major_radius=major_radius,
        minor_radius=minor_radius,
        major_segments=major_segments,
        minor_segments=minor_segments,
        location=location
    )
    torus = bpy.context.active_object
    torus.name = "Torus"
    return torus


def create_grid(x_subdivisions=10, y_subdivisions=10, size=2.0, location=(0, 0, 0)):
    """Create a grid mesh object.
    
    Args:
        x_subdivisions: Number of subdivisions in the X direction.
        y_subdivisions: Number of subdivisions in the Y direction.
        size: Size of the grid.
        location: (x, y, z) tuple for object location.
    
    Returns:
        The created object.
    """
    bpy.ops.mesh.primitive_grid_add(
        x_subdivisions=x_subdivisions,
        y_subdivisions=y_subdivisions,
        size=size,
        location=location
    )
    grid = bpy.context.active_object
    grid.name = "Grid"
    return grid


def create_icosphere(radius=1.0, subdivisions=2, location=(0, 0, 0)):
    """Create an icosphere mesh object.
    
    Args:
        radius: Radius of the icosphere.
        subdivisions: Number of subdivisions (affects smoothness).
        location: (x, y, z) tuple for object location.
    
    Returns:
        The created object.
    """
    bpy.ops.mesh.primitive_ico_sphere_add(
        radius=radius,
        subdivisions=subdivisions,
        location=location
    )
    icosphere = bpy.context.active_object
    icosphere.name = "Icosphere"
    return icosphere


def create_plane(size=2.0, location=(0, 0, 0)):
    """Create a plane mesh object.
    
    Args:
        size: Size of the plane.
        location: (x, y, z) tuple for object location.
    
    Returns:
        The created object.
    """
    bpy.ops.mesh.primitive_plane_add(
        size=size,
        location=location
    )
    plane = bpy.context.active_object
    plane.name = "Plane"
    return plane


def create_monkey(size=1.0, location=(0, 0, 0)):
    """Create a monkey (Suzanne) mesh object.
    
    Args:
        size: Size of the monkey.
        location: (x, y, z) tuple for object location.
    
    Returns:
        The created object.
    """
    bpy.ops.mesh.primitive_monkey_add(
        size=size,
        location=location
    )
    monkey = bpy.context.active_object
    monkey.name = "Suzanne"
    return monkey


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


def create_all_mesh_primitives(save_dir="./blend_files/mesh_primitives/"):
    """Create all primitive mesh objects and save them as individual .blend files.
    
    Args:
        save_dir: Directory to save the .blend files.
    """
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    # Dictionary of creation functions and their parameters
    primitives = {
        "cube": {"func": create_cube, "params": {}},
        "sphere": {"func": create_sphere, "params": {}},
        "cylinder": {"func": create_cylinder, "params": {}},
        "cone": {"func": create_cone, "params": {}},
        "torus": {"func": create_torus, "params": {}},
        "grid": {"func": create_grid, "params": {}},
        "icosphere": {"func": create_icosphere, "params": {}},
        "plane": {"func": create_plane, "params": {}},
        "monkey": {"func": create_monkey, "params": {}}
    }
    
    for name, data in primitives.items():
        # Clear the scene
        clear_scene()
        
        # Create the primitive
        obj = data["func"](**data["params"])
        
        # Save to a .blend file
        filepath = os.path.join(save_dir, f"{name}.blend")
        save_blend_file(filepath, obj)
        
        print(f"Created and saved {name} to {filepath}")


# Example usage
if __name__ == "__main__":
    # Create and save all primitive mesh objects
    create_all_mesh_primitives()
    
    # Or create and save individual primitives
    # clear_scene()
    # cube = create_cube()
    # save_blend_file("./blend_files/mesh_primitives/my_cube.blend", cube)