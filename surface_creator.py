import bpy
import os
import math
import bmesh
from mathutils import Vector


def clear_scene():
    """Clear the current scene of all objects."""
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()


def create_nurbs_surface(size=2.0, u_res=4, v_res=4, name="NurbsSurface", location=(0, 0, 0)):
    """Create a NURBS surface.
    
    Args:
        size: Size of the surface.
        u_res: Number of control points in U direction (approximated).
        v_res: Number of control points in V direction (approximated).
        name: Name for the surface object.
        location: (x, y, z) tuple for object location.
        
    Returns:
        The created surface object.
    """
    # Create a NURBS surface using the built-in operator
    bpy.ops.surface.primitive_nurbs_surface_surface_add(
        radius=size/2,
        location=location
    )
    
    # Get the created surface
    surface_obj = bpy.context.active_object
    surface_obj.name = name
    
    # Adjust resolution settings
    for spline in surface_obj.data.splines:
        spline.resolution_u = u_res
        spline.resolution_v = v_res
    
    return surface_obj


def create_nurbs_cylinder(radius=1.0, height=2.0, u_segments=8, v_segments=4, name="NurbsCylinder", location=(0, 0, 0)):
    """Create a NURBS cylinder surface.
    
    Args:
        radius: Radius of the cylinder.
        height: Height of the cylinder.
        u_segments: Number of segments around the circumference.
        v_segments: Number of segments along the height.
        name: Name for the surface object.
        location: (x, y, z) tuple for object location.
        
    Returns:
        The created surface object.
    """
    # Create a NURBS cylinder using the built-in operator
    bpy.ops.surface.primitive_nurbs_surface_cylinder_add(
        radius=radius,
        location=location
    )
    
    # Get the created surface
    surface_obj = bpy.context.active_object
    surface_obj.name = name
    
    # Adjust resolution settings
    for spline in surface_obj.data.splines:
        spline.resolution_u = u_segments
        spline.resolution_v = v_segments
    
    # Scale to match height
    surface_obj.scale[2] = height / 2.0
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    
    return surface_obj


def create_nurbs_sphere(radius=1.0, u_segments=8, v_segments=8, name="NurbsSphere", location=(0, 0, 0)):
    """Create a NURBS sphere surface.
    
    Args:
        radius: Radius of the sphere.
        u_segments: Number of segments around the longitude.
        v_segments: Number of segments around the latitude.
        name: Name for the surface object.
        location: (x, y, z) tuple for object location.
        
    Returns:
        The created surface object.
    """
    # Create a NURBS sphere using the built-in operator
    bpy.ops.surface.primitive_nurbs_surface_sphere_add(
        radius=radius,
        location=location
    )
    
    # Get the created surface
    surface_obj = bpy.context.active_object
    surface_obj.name = name
    
    # Adjust resolution settings
    for spline in surface_obj.data.splines:
        spline.resolution_u = u_segments
        spline.resolution_v = v_segments
    
    return surface_obj


def create_custom_torus(major_radius=1.5, minor_radius=0.5, u_segments=16, v_segments=8, name="NurbsTorus", location=(0, 0, 0)):
    """Create a torus surface using a mesh approach.
    
    Args:
        major_radius: Major radius of the torus (distance from center to ring center).
        minor_radius: Minor radius of the torus (thickness of the ring).
        u_segments: Number of segments around the major circle.
        v_segments: Number of segments around the minor circle.
        name: Name for the surface object.
        location: (x, y, z) tuple for object location.
        
    Returns:
        The created surface object.
    """
    # Create a torus mesh
    bpy.ops.mesh.primitive_torus_add(
        align='WORLD',
        location=location,
        rotation=(0, 0, 0),
        major_segments=u_segments,
        minor_segments=v_segments,
        major_radius=major_radius,
        minor_radius=minor_radius
    )
    
    # Get the created mesh
    torus_obj = bpy.context.active_object
    torus_obj.name = name
    
    # Convert to NURBS surface if possible
    try:
        bpy.ops.object.convert(target='CURVE')
        bpy.context.object.data.bevel_depth = 0.01
        bpy.ops.object.shade_smooth()
    except Exception as e:
        print(f"Note: Could not convert to curve: {e}")
    
    return torus_obj


def create_nurbs_ring(radius=1.0, inner_radius=0.7, u_segments=16, rings=1, name="RingSurface", location=(0, 0, 0)):
    """Create a ring surface mesh.
    
    Args:
        radius: Outer radius of the ring.
        inner_radius: Inner radius of the ring.
        u_segments: Number of segments around the circumference.
        rings: Number of subdivisions between inner and outer radius.
        name: Name for the surface object.
        location: (x, y, z) tuple for object location.
        
    Returns:
        The created surface object.
    """
    # Create a mesh ring first
    bpy.ops.mesh.primitive_circle_add(
        vertices=u_segments,
        radius=radius,
        fill_type='NGON',
        location=location
    )
    
    # Get the circle mesh
    ring_obj = bpy.context.active_object
    ring_obj.name = name
    
    # Create a hole with the inner radius
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.inset(thickness=(radius - inner_radius), depth=0)
    bpy.ops.mesh.select_all(action='DESELECT')
    
    # Select the inner face
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.mesh.select_all(action='INVERT')
    
    # Delete the inner face to create a hole
    bpy.ops.mesh.delete(type='FACE')
    
    # Add rings if requested
    if rings > 1:
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.subdivide(number_cuts=rings-1)
    
    # Return to object mode
    bpy.ops.object.mode_set(mode='OBJECT')
    
    # Optional: smooth shading
    bpy.ops.object.shade_smooth()
    
    return ring_obj


def create_landscape_surface(width=10.0, height=10.0, x_res=32, y_res=32, height_scale=1.0, 
                             noise_scale=1.0, name="Landscape", location=(0, 0, 0)):
    """Create a landscape surface mesh with procedural noise.
    
    Args:
        width: Width of the landscape.
        height: Length of the landscape.
        x_res: Resolution in X direction.
        y_res: Resolution in Y direction.
        height_scale: Scale factor for height variation.
        noise_scale: Scale of the noise pattern.
        name: Name for the landscape object.
        location: (x, y, z) tuple for object location.
        
    Returns:
        The created landscape object.
    """
    # Create a grid mesh
    bpy.ops.mesh.primitive_grid_add(
        x_subdivisions=x_res-1,
        y_subdivisions=y_res-1,
        size=min(width, height)/2,
        location=location
    )
    
    grid_obj = bpy.context.active_object
    grid_obj.name = name
    
    # Scale to match requested width and height
    scale_x = width / min(width, height)
    scale_y = height / min(width, height)
    
    grid_obj.scale[0] = scale_x
    grid_obj.scale[1] = scale_y
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    
    # Apply displacement using Displace modifier with procedural texture
    # Create a noise texture
    noise_tex = bpy.data.textures.new(name=f"{name}Noise", type='CLOUDS')
    noise_tex.noise_scale = noise_scale
    
    # Add displacement modifier
    displace_mod = grid_obj.modifiers.new(name="Landscape", type='DISPLACE')
    displace_mod.texture = noise_tex
    displace_mod.strength = height_scale
    
    # Apply the modifier
    bpy.ops.object.modifier_apply(modifier="Landscape")
    
    return grid_obj


def create_disk_surface(radius=1.0, inner_radius=0.0, sectors=32, rings=8, name="DiskSurface", location=(0, 0, 0)):
    """Create a disk surface mesh.
    
    Args:
        radius: Outer radius of the disk.
        inner_radius: Inner radius of the disk (0 for full disk, >0 for ring).
        sectors: Number of sectors (divisions around the circumference).
        rings: Number of rings (divisions between inner and outer radius).
        name: Name for the disk object.
        location: (x, y, z) tuple for object location.
        
    Returns:
        The created disk object.
    """
    # Create a circle mesh (Blender doesn't have a built-in disk primitive)
    bpy.ops.mesh.primitive_circle_add(
        vertices=sectors,
        radius=radius,
        fill_type='NGON',
        location=location
    )
    
    disk_obj = bpy.context.active_object
    disk_obj.name = name
    
    # If inner_radius > 0, create a hole
    if inner_radius > 0:
        # Enter edit mode
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        
        # Inset the face
        bpy.ops.mesh.inset(thickness=radius-inner_radius, depth=0)
        
        # Select the inner face
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.mesh.select_all(action='INVERT')
        
        # Delete the inner face to create a hole
        bpy.ops.mesh.delete(type='FACE')
        
        # Return to object mode
        bpy.ops.object.mode_set(mode='OBJECT')
    
    # Add multiple rings if requested
    if rings > 1 and inner_radius < radius:
        # Enter edit mode
        bpy.ops.object.mode_set(mode='EDIT')
        
        # Select all faces
        bpy.ops.mesh.select_all(action='SELECT')
        
        # Subdivide to create rings
        bpy.ops.mesh.subdivide(number_cuts=rings-1)
        
        # Return to object mode
        bpy.ops.object.mode_set(mode='OBJECT')
    
    return disk_obj


def create_nurbs_patch_4x4(name="NurbsPatch", location=(0, 0, 0)):
    """Create a simple 4x4 NURBS patch surface.
    
    Args:
        name: Name for the surface object.
        location: (x, y, z) tuple for object location.
        
    Returns:
        The created surface object.
    """
    # Create a NURBS surface using the built-in operator
    bpy.ops.surface.primitive_nurbs_surface_surface_add(
        location=location
    )
    
    # Get the created surface
    surface_obj = bpy.context.active_object
    surface_obj.name = name
    
    # Modify some control points to create an interesting shape
    if len(surface_obj.data.splines) > 0:
        spline = surface_obj.data.splines[0]
        
        # Assuming it's a 4x4 patch (16 points)
        if len(spline.points) == 16:
            # Modify the middle points to create a bump
            spline.points[5].co[2] = 0.5  # Raise point
            spline.points[6].co[2] = 0.5  # Raise point
            spline.points[9].co[2] = 0.5  # Raise point
            spline.points[10].co[2] = 0.5  # Raise point
    
    return surface_obj


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


def create_all_surface_types(save_dir="./blend_files/surface_types/"):
    """Create all surface types and save them as individual .blend files.
    
    Args:
        save_dir: Directory to save the .blend files.
    """
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    # Dictionary of creation functions and their parameters
    surface_types = {
        "nurbs_surface": {"func": create_nurbs_surface, "params": {}},
        "nurbs_cylinder": {"func": create_nurbs_cylinder, "params": {}},
        "nurbs_sphere": {"func": create_nurbs_sphere, "params": {}},
        "torus_mesh": {"func": create_custom_torus, "params": {}},
        "ring_mesh": {"func": create_nurbs_ring, "params": {}},
        "landscape_surface": {"func": create_landscape_surface, "params": {}},
        "disk_surface": {"func": create_disk_surface, "params": {}},
        "nurbs_patch_4x4": {"func": create_nurbs_patch_4x4, "params": {}}
    }
    
    for name, data in surface_types.items():
        # Clear the scene
        clear_scene()
        
        try:
            # Create the surface
            obj = data["func"](**data["params"])
            
            # Save to a .blend file
            filepath = os.path.join(save_dir, f"{name}.blend")
            save_blend_file(filepath, obj)
            
            print(f"Created and saved {name} to {filepath}")
        except Exception as e:
            print(f"Error creating {name}: {e}")


# Example usage
if __name__ == "__main__":
    # Create and save all surface types
    create_all_surface_types()
    
    # Or create and save individual surfaces
    # clear_scene()
    # torus = create_custom_torus(major_radius=2.0, minor_radius=0.5)
    # save_blend_file("./blend_files/surface_types/my_torus.blend", torus)