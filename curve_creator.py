import bpy
import os
import math
from mathutils import Vector


def clear_scene():
    """Clear the current scene of all objects."""
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()


def create_bezier_curve(points=None, name="BezierCurve", location=(0, 0, 0)):
    """Create a Bezier curve with specified points.
    
    Args:
        points: List of (x, y, z) tuples for curve points. Default creates a simple curve.
        name: Name for the curve object.
        location: (x, y, z) tuple for object location.
        
    Returns:
        The created curve object.
    """
    # Create default points if none provided
    if points is None:
        points = [
            (-1, 0, 0),    # First point
            (-0.5, 1, 0),  # First handle
            (0.5, -1, 0),  # Second handle
            (1, 0, 0)      # Second point
        ]
    
    # Create the curve data
    curve_data = bpy.data.curves.new(name=name, type='CURVE')
    curve_data.dimensions = '3D'
    curve_data.resolution_u = 12
    
    # Create a new spline in the curve
    spline = curve_data.splines.new(type='BEZIER')
    
    # Adjust point count (need to have at least 2 points)
    point_count = max(2, len(points) // 3)
    if len(spline.bezier_points) < point_count:
        spline.bezier_points.add(point_count - len(spline.bezier_points))
    
    # Set the points
    for i in range(min(point_count, len(points) // 3)):
        bp = spline.bezier_points[i]
        idx = i * 3
        
        # Set the point coordinates
        bp.co = points[idx]
        
        # Set handle positions if available
        if idx + 1 < len(points):
            bp.handle_right = points[idx + 1]
        if idx + 2 < len(points):
            if i + 1 < point_count:  # Check if next point exists
                spline.bezier_points[i + 1].handle_left = points[idx + 2]
    
    # Create the object
    curve_obj = bpy.data.objects.new(name, curve_data)
    
    # Set the location
    curve_obj.location = location
    
    # Link it to the scene
    bpy.context.collection.objects.link(curve_obj)
    
    # Select the curve
    bpy.context.view_layer.objects.active = curve_obj
    curve_obj.select_set(True)
    
    return curve_obj


def create_nurbs_curve(points=None, name="NurbsCurve", location=(0, 0, 0)):
    """Create a NURBS curve with specified points.
    
    Args:
        points: List of (x, y, z) tuples for curve points. Default creates a simple curve.
        name: Name for the curve object.
        location: (x, y, z) tuple for object location.
        
    Returns:
        The created curve object.
    """
    # Create default points if none provided
    if points is None:
        points = [
            (-1.5, 0, 0),
            (-0.5, 0.5, 0),
            (0.5, -0.5, 0),
            (1.5, 0, 0)
        ]
    
    # Create the curve data
    curve_data = bpy.data.curves.new(name=name, type='CURVE')
    curve_data.dimensions = '3D'
    curve_data.resolution_u = 12
    
    # Create a new spline in the curve
    spline = curve_data.splines.new(type='NURBS')
    
    # Adjust point count
    if len(spline.points) < len(points):
        spline.points.add(len(points) - len(spline.points))
    
    # Set the points
    for i, point in enumerate(points):
        x, y, z = point
        spline.points[i].co = (x, y, z, 1)  # NURBS points are 4D (x, y, z, w)
    
    # Set NURBS attributes
    spline.use_endpoint_u = True
    spline.order_u = min(4, len(points))  # Order must be <= point count
    
    # Create the object
    curve_obj = bpy.data.objects.new(name, curve_data)
    
    # Set the location
    curve_obj.location = location
    
    # Link it to the scene
    bpy.context.collection.objects.link(curve_obj)
    
    # Select the curve
    bpy.context.view_layer.objects.active = curve_obj
    curve_obj.select_set(True)
    
    return curve_obj


def create_path_curve(points=None, name="PathCurve", location=(0, 0, 0)):
    """Create a Path curve (specialized NURBS).
    
    Args:
        points: List of (x, y, z) tuples for curve points. Default creates a simple path.
        name: Name for the curve object.
        location: (x, y, z) tuple for object location.
        
    Returns:
        The created curve object.
    """
    # Create default points if none provided
    if points is None:
        points = [
            (-2, 0, 0),
            (-1, 1, 0),
            (0, -1, 0),
            (1, 1, 0),
            (2, 0, 0)
        ]
    
    # Create the curve data
    curve_data = bpy.data.curves.new(name=name, type='CURVE')
    curve_data.dimensions = '3D'
    
    # Create a new spline in the curve
    spline = curve_data.splines.new(type='NURBS')
    
    # Adjust point count
    if len(spline.points) < len(points):
        spline.points.add(len(points) - len(spline.points))
    
    # Set the points
    for i, point in enumerate(points):
        x, y, z = point
        spline.points[i].co = (x, y, z, 1)  # NURBS points are 4D (x, y, z, w)
    
    # Set NURBS attributes for a path
    spline.use_endpoint_u = True
    spline.order_u = min(4, len(points))
    spline.resolution_u = 24  # Higher resolution for smoother path
    
    # Set up the curve as a path
    curve_data.use_path = True
    curve_data.use_path_follow = True
    
    # Create the object
    curve_obj = bpy.data.objects.new(name, curve_data)
    
    # Set the location
    curve_obj.location = location
    
    # Link it to the scene
    bpy.context.collection.objects.link(curve_obj)
    
    # Select the curve
    bpy.context.view_layer.objects.active = curve_obj
    curve_obj.select_set(True)
    
    return curve_obj


def create_circle_curve(radius=1.0, vertices=32, name="CircleCurve", location=(0, 0, 0)):
    """Create a circular curve.
    
    Args:
        radius: Radius of the circle.
        vertices: Number of vertices/points.
        name: Name for the curve object.
        location: (x, y, z) tuple for object location.
        
    Returns:
        The created curve object.
    """
    bpy.ops.curve.primitive_bezier_circle_add(radius=radius, location=location)
    circle = bpy.context.active_object
    circle.name = name
    
    # Adjust the number of points
    if vertices != 4:  # Default Bezier circle has 4 points
        # Get the curve data
        curve_data = circle.data
        spline = curve_data.splines[0]
        
        # Store the current points
        current_count = len(spline.bezier_points)
        
        # Calculate how many points to add or remove
        diff = vertices - current_count
        
        if diff > 0:
            # Add more points
            spline.bezier_points.add(diff)
            
            # Recalculate positions
            for i in range(len(spline.bezier_points)):
                angle = 2.0 * math.pi * i / vertices
                x = radius * math.cos(angle)
                y = radius * math.sin(angle)
                
                # Set the control point
                spline.bezier_points[i].co = (x, y, 0)
                
                # Calculate handle positions (tangent to circle)
                handle_factor = radius * 0.55  # Magic number for Bezier approximation of circle
                handle_x = handle_factor * math.sin(angle)
                handle_y = -handle_factor * math.cos(angle)
                
                spline.bezier_points[i].handle_left = (x - handle_x, y - handle_y, 0)
                spline.bezier_points[i].handle_right = (x + handle_x, y + handle_y, 0)
    
    return circle


def create_spiral_curve(turns=2, height=5.0, radius=1.0, points=64, name="SpiralCurve", location=(0, 0, 0)):
    """Create a spiral curve.
    
    Args:
        turns: Number of full rotations in the spiral.
        height: Total height of the spiral.
        radius: Maximum radius of the spiral.
        points: Number of points in the spiral.
        name: Name for the curve object.
        location: (x, y, z) tuple for object location.
        
    Returns:
        The created curve object.
    """
    # Create points for a spiral
    spiral_points = []
    for i in range(points):
        angle = (i / (points - 1)) * turns * 2.0 * math.pi
        z = (i / (points - 1)) * height
        r = (i / (points - 1)) * radius
        x = r * math.cos(angle)
        y = r * math.sin(angle)
        spiral_points.append((x, y, z))
    
    # Create the curve data
    curve_data = bpy.data.curves.new(name=name, type='CURVE')
    curve_data.dimensions = '3D'
    
    # Create a new spline in the curve
    spline = curve_data.splines.new(type='NURBS')
    
    # Adjust point count
    if len(spline.points) < len(spiral_points):
        spline.points.add(len(spiral_points) - len(spline.points))
    
    # Set the points
    for i, point in enumerate(spiral_points):
        x, y, z = point
        spline.points[i].co = (x, y, z, 1)  # NURBS points are 4D (x, y, z, w)
    
    # Set NURBS attributes
    spline.use_endpoint_u = True
    spline.order_u = 3
    spline.resolution_u = 24
    
    # Create the object
    curve_obj = bpy.data.objects.new(name, curve_data)
    
    # Set the location
    curve_obj.location = location
    
    # Link it to the scene
    bpy.context.collection.objects.link(curve_obj)
    
    # Select the curve
    bpy.context.view_layer.objects.active = curve_obj
    curve_obj.select_set(True)
    
    return curve_obj


def create_helix_curve(turns=2, height=5.0, radius=1.0, points=64, name="HelixCurve", location=(0, 0, 0)):
    """Create a helix (coil) curve.
    
    Args:
        turns: Number of full rotations in the helix.
        height: Total height of the helix.
        radius: Radius of the helix.
        points: Number of points in the helix.
        name: Name for the curve object.
        location: (x, y, z) tuple for object location.
        
    Returns:
        The created curve object.
    """
    # Create points for a helix
    helix_points = []
    for i in range(points):
        angle = (i / (points - 1)) * turns * 2.0 * math.pi
        z = (i / (points - 1)) * height
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        helix_points.append((x, y, z))
    
    # Create the curve data
    curve_data = bpy.data.curves.new(name=name, type='CURVE')
    curve_data.dimensions = '3D'
    
    # Create a new spline in the curve
    spline = curve_data.splines.new(type='NURBS')
    
    # Adjust point count
    if len(spline.points) < len(helix_points):
        spline.points.add(len(helix_points) - len(spline.points))
    
    # Set the points
    for i, point in enumerate(helix_points):
        x, y, z = point
        spline.points[i].co = (x, y, z, 1)  # NURBS points are 4D (x, y, z, w)
    
    # Set NURBS attributes
    spline.use_endpoint_u = True
    spline.order_u = 3
    spline.resolution_u = 24
    
    # Create the object
    curve_obj = bpy.data.objects.new(name, curve_data)
    
    # Set the location
    curve_obj.location = location
    
    # Link it to the scene
    bpy.context.collection.objects.link(curve_obj)
    
    # Select the curve
    bpy.context.view_layer.objects.active = curve_obj
    curve_obj.select_set(True)
    
    return curve_obj


def create_text_curve(text="Blender", font_size=1.0, extrude=0.0, name="TextCurve", location=(0, 0, 0)):
    """Create a curve from text (converts text to curve).
    
    Args:
        text: The text content.
        font_size: Size of the font.
        extrude: Extrusion depth.
        name: Name for the curve object.
        location: (x, y, z) tuple for object location.
        
    Returns:
        The created curve object.
    """
    # Create text object first
    bpy.ops.object.text_add(location=location)
    text_obj = bpy.context.active_object
    text_obj.name = name
    
    # Set text properties
    text_obj.data.body = text
    text_obj.data.size = font_size
    text_obj.data.extrude = extrude
    
    # Convert to curve
    bpy.ops.object.convert(target='CURVE')
    curve_obj = bpy.context.active_object
    curve_obj.name = name
    
    return curve_obj


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


def create_all_curve_types(save_dir="./blend_files/curve_types/"):
    """Create all curve types and save them as individual .blend files.
    
    Args:
        save_dir: Directory to save the .blend files.
    """
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    # Dictionary of creation functions and their parameters
    curve_types = {
        "bezier_curve": {"func": create_bezier_curve, "params": {}},
        "nurbs_curve": {"func": create_nurbs_curve, "params": {}},
        "path_curve": {"func": create_path_curve, "params": {}},
        "circle_curve": {"func": create_circle_curve, "params": {}},
        "spiral_curve": {"func": create_spiral_curve, "params": {}},
        "helix_curve": {"func": create_helix_curve, "params": {}},
        "text_curve": {"func": create_text_curve, "params": {}}
    }
    
    for name, data in curve_types.items():
        # Clear the scene
        clear_scene()
        
        # Create the curve
        obj = data["func"](**data["params"])
        
        # Save to a .blend file
        filepath = os.path.join(save_dir, f"{name}.blend")
        save_blend_file(filepath, obj)
        
        print(f"Created and saved {name} to {filepath}")


# Example usage
if __name__ == "__main__":
    # Create and save all curve types
    create_all_curve_types()
    
    # Or create and save individual curves
    # clear_scene()
    # spiral = create_spiral_curve(turns=3, height=8.0)
    # save_blend_file("./blend_files/curve_types/my_spiral.blend", spiral)