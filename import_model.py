import bpy
import os
import math
from mathutils import Vector


def clear_scene():
    """Clear the current scene of all objects."""
    # Deselect all objects first
    for obj in bpy.context.selected_objects:
        obj.select_set(False)
    
    # Delete all objects directly from data
    for obj in list(bpy.data.objects):
        bpy.data.objects.remove(obj, do_unlink=True)


def import_obj(filepath, location=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1)):
    """Import an OBJ file.
    
    Args:
        filepath: Path to the OBJ file.
        location: (x, y, z) tuple for object location.
        rotation: (x, y, z) tuple for object rotation in radians.
        scale: (x, y, z) tuple for object scale.
        
    Returns:
        List of imported objects.
    """
    # Check if the file exists
    if not os.path.exists(filepath):
        print(f"Error: File not found: {filepath}")
        return []
    
    # Import the OBJ file
    bpy.ops.import_scene.obj(
        filepath=filepath,
        use_edges=True,
        use_smooth_groups=True,
        split_mode='ON',
        axis_forward='-Z',
        axis_up='Y'
    )
    
    # Get the imported objects (all newly created objects)
    imported_objects = bpy.context.selected_objects
    
    # Group the objects if there are multiple
    if len(imported_objects) > 1:
        # Create an empty object as parent
        bpy.ops.object.empty_add(type='PLAIN_AXES', location=location)
        parent_empty = bpy.context.active_object
        parent_empty.name = os.path.basename(filepath).split('.')[0] + "_Group"
        
        # Parent all imported objects to the empty
        for obj in imported_objects:
            obj.parent = parent_empty
        
        # Set the transformation of the parent
        parent_empty.rotation_euler = rotation
        parent_empty.scale = scale
        
        # Add the parent to the list of imported objects
        imported_objects.append(parent_empty)
    else:
        # If only one object, apply transformations directly
        for obj in imported_objects:
            obj.location = location
            obj.rotation_euler = rotation
            obj.scale = scale
    
    return imported_objects


def import_fbx(filepath, location=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1), 
             import_animations=True):
    """Import an FBX file.
    
    Args:
        filepath: Path to the FBX file.
        location: (x, y, z) tuple for object location.
        rotation: (x, y, z) tuple for object rotation in radians.
        scale: (x, y, z) tuple for object scale.
        import_animations: Whether to import animations.
        
    Returns:
        List of imported objects.
    """
    # Check if the file exists
    if not os.path.exists(filepath):
        print(f"Error: File not found: {filepath}")
        return []
    
    # Import the FBX file
    bpy.ops.import_scene.fbx(
        filepath=filepath,
        use_anim=import_animations,
        axis_forward='-Z',
        axis_up='Y',
        global_scale=1.0
    )
    
    # Get the imported objects (all newly created objects)
    imported_objects = bpy.context.selected_objects
    
    # Group the objects if there are multiple
    if len(imported_objects) > 1:
        # Create an empty object as parent
        bpy.ops.object.empty_add(type='PLAIN_AXES', location=location)
        parent_empty = bpy.context.active_object
        parent_empty.name = os.path.basename(filepath).split('.')[0] + "_Group"
        
        # Parent all imported objects to the empty
        for obj in imported_objects:
            obj.parent = parent_empty
        
        # Set the transformation of the parent
        parent_empty.rotation_euler = rotation
        parent_empty.scale = scale
        
        # Add the parent to the list of imported objects
        imported_objects.append(parent_empty)
    else:
        # If only one object, apply transformations directly
        for obj in imported_objects:
            obj.location = location
            obj.rotation_euler = rotation
            obj.scale = scale
    
    return imported_objects


def import_gltf(filepath, location=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1)):
    """Import a glTF file.
    
    Args:
        filepath: Path to the glTF file.
        location: (x, y, z) tuple for object location.
        rotation: (x, y, z) tuple for object rotation in radians.
        scale: (x, y, z) tuple for object scale.
        
    Returns:
        List of imported objects.
    """
    # Check if the file exists
    if not os.path.exists(filepath):
        print(f"Error: File not found: {filepath}")
        return []
    
    # Import the glTF file
    bpy.ops.import_scene.gltf(
        filepath=filepath,
        import_pack_images=True
    )
    
    # Get the imported objects (all newly created objects)
    imported_objects = bpy.context.selected_objects
    
    # Group the objects if there are multiple
    if len(imported_objects) > 1:
        # Create an empty object as parent
        bpy.ops.object.empty_add(type='PLAIN_AXES', location=location)
        parent_empty = bpy.context.active_object
        parent_empty.name = os.path.basename(filepath).split('.')[0] + "_Group"
        
        # Parent all imported objects to the empty
        for obj in imported_objects:
            obj.parent = parent_empty
        
        # Set the transformation of the parent
        parent_empty.rotation_euler = rotation
        parent_empty.scale = scale
        
        # Add the parent to the list of imported objects
        imported_objects.append(parent_empty)
    else:
        # If only one object, apply transformations directly
        for obj in imported_objects:
            obj.location = location
            obj.rotation_euler = rotation
            obj.scale = scale
    
    return imported_objects


def import_stl(filepath, location=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1)):
    """Import an STL file.
    
    Args:
        filepath: Path to the STL file.
        location: (x, y, z) tuple for object location.
        rotation: (x, y, z) tuple for object rotation in radians.
        scale: (x, y, z) tuple for object scale.
        
    Returns:
        The imported object.
    """
    # Check if the file exists
    if not os.path.exists(filepath):
        print(f"Error: File not found: {filepath}")
        return None
    
    # Import the STL file
    bpy.ops.import_mesh.stl(
        filepath=filepath,
        global_scale=1.0,
        use_scene_unit=True,
        axis_forward='Y',
        axis_up='Z'
    )
    
    # Get the imported object (should be only one)
    obj = bpy.context.active_object
    
    # Set transformations
    obj.location = location
    obj.rotation_euler = rotation
    obj.scale = scale
    
    return obj


def import_ply(filepath, location=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1)):
    """Import a PLY file.
    
    Args:
        filepath: Path to the PLY file.
        location: (x, y, z) tuple for object location.
        rotation: (x, y, z) tuple for object rotation in radians.
        scale: (x, y, z) tuple for object scale.
        
    Returns:
        The imported object.
    """
    # Check if the file exists
    if not os.path.exists(filepath):
        print(f"Error: File not found: {filepath}")
        return None
    
    # Import the PLY file
    bpy.ops.import_mesh.ply(
        filepath=filepath
    )
    
    # Get the imported object (should be only one)
    obj = bpy.context.active_object
    
    # Set transformations
    obj.location = location
    obj.rotation_euler = rotation
    obj.scale = scale
    
    return obj


def import_dae(filepath, location=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1)):
    """Import a Collada (DAE) file.
    
    Args:
        filepath: Path to the DAE file.
        location: (x, y, z) tuple for object location.
        rotation: (x, y, z) tuple for object rotation in radians.
        scale: (x, y, z) tuple for object scale.
        
    Returns:
        List of imported objects.
    """
    # Check if the file exists
    if not os.path.exists(filepath):
        print(f"Error: File not found: {filepath}")
        return []
    
    # Import the DAE file
    bpy.ops.wm.collada_import(
        filepath=filepath,
        import_units=True
    )
    
    # Get the imported objects (all newly created objects)
    imported_objects = bpy.context.selected_objects
    
    # Group the objects if there are multiple
    if len(imported_objects) > 1:
        # Create an empty object as parent
        bpy.ops.object.empty_add(type='PLAIN_AXES', location=location)
        parent_empty = bpy.context.active_object
        parent_empty.name = os.path.basename(filepath).split('.')[0] + "_Group"
        
        # Parent all imported objects to the empty
        for obj in imported_objects:
            obj.parent = parent_empty
        
        # Set the transformation of the parent
        parent_empty.rotation_euler = rotation
        parent_empty.scale = scale
        
        # Add the parent to the list of imported objects
        imported_objects.append(parent_empty)
    else:
        # If only one object, apply transformations directly
        for obj in imported_objects:
            obj.location = location
            obj.rotation_euler = rotation
            obj.scale = scale
    
    return imported_objects


def import_abc(filepath, location=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1)):
    """Import an Alembic (ABC) file.
    
    Args:
        filepath: Path to the ABC file.
        location: (x, y, z) tuple for object location.
        rotation: (x, y, z) tuple for object rotation in radians.
        scale: (x, y, z) tuple for object scale.
        
    Returns:
        List of imported objects.
    """
    # Check if the file exists
    if not os.path.exists(filepath):
        print(f"Error: File not found: {filepath}")
        return []
    
    # Import the ABC file
    bpy.ops.wm.alembic_import(
        filepath=filepath,
        scale=1.0
    )
    
    # Get the imported objects (all newly created objects)
    imported_objects = bpy.context.selected_objects
    
    # Group the objects if there are multiple
    if len(imported_objects) > 1:
        # Create an empty object as parent
        bpy.ops.object.empty_add(type='PLAIN_AXES', location=location)
        parent_empty = bpy.context.active_object
        parent_empty.name = os.path.basename(filepath).split('.')[0] + "_Group"
        
        # Parent all imported objects to the empty
        for obj in imported_objects:
            obj.parent = parent_empty
        
        # Set the transformation of the parent
        parent_empty.rotation_euler = rotation
        parent_empty.scale = scale
        
        # Add the parent to the list of imported objects
        imported_objects.append(parent_empty)
    else:
        # If only one object, apply transformations directly
        for obj in imported_objects:
            obj.location = location
            obj.rotation_euler = rotation
            obj.scale = scale
    
    return imported_objects


def import_usd(filepath, location=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1)):
    """Import a Universal Scene Description (USD) file.
    
    Args:
        filepath: Path to the USD file.
        location: (x, y, z) tuple for object location.
        rotation: (x, y, z) tuple for object rotation in radians.
        scale: (x, y, z) tuple for object scale.
        
    Returns:
        List of imported objects.
    """
    # Check if the file exists
    if not os.path.exists(filepath):
        print(f"Error: File not found: {filepath}")
        return []
    
    try:
        # Import the USD file
        bpy.ops.wm.usd_import(
            filepath=filepath,
            scale=1.0
        )
        
        # Get the imported objects (all newly created objects)
        imported_objects = bpy.context.selected_objects
        
        # Group the objects if there are multiple
        if len(imported_objects) > 1:
            # Create an empty object as parent
            bpy.ops.object.empty_add(type='PLAIN_AXES', location=location)
            parent_empty = bpy.context.active_object
            parent_empty.name = os.path.basename(filepath).split('.')[0] + "_Group"
            
            # Parent all imported objects to the empty
            for obj in imported_objects:
                obj.parent = parent_empty
            
            # Set the transformation of the parent
            parent_empty.rotation_euler = rotation
            parent_empty.scale = scale
            
            # Add the parent to the list of imported objects
            imported_objects.append(parent_empty)
        else:
            # If only one object, apply transformations directly
            for obj in imported_objects:
                obj.location = location
                obj.rotation_euler = rotation
                obj.scale = scale
        
        return imported_objects
    except AttributeError:
        print("Warning: USD import not supported in this version of Blender.")
        return []


def import_svg(filepath, location=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1), 
               extrude=0.0, bevel_depth=0.0):
    """Import an SVG file as curves.
    
    Args:
        filepath: Path to the SVG file.
        location: (x, y, z) tuple for object location.
        rotation: (x, y, z) tuple for object rotation in radians.
        scale: (x, y, z) tuple for object scale.
        extrude: Extrusion amount for the curves.
        bevel_depth: Bevel depth for the curves.
        
    Returns:
        List of imported objects.
    """
    # Check if the file exists
    if not os.path.exists(filepath):
        print(f"Error: File not found: {filepath}")
        return []
    
    # Import the SVG file
    bpy.ops.import_curve.svg(
        filepath=filepath
    )
    
    # Get the imported objects (all newly created objects)
    imported_objects = bpy.context.selected_objects
    
    # Group the objects under a parent empty
    bpy.ops.object.empty_add(type='PLAIN_AXES', location=location)
    parent_empty = bpy.context.active_object
    parent_empty.name = os.path.basename(filepath).split('.')[0] + "_Group"
    
    # Set the transformation of the parent
    parent_empty.rotation_euler = rotation
    parent_empty.scale = scale
    
    # Parent all imported objects to the empty and apply extrude/bevel
    for obj in imported_objects:
        if obj.type == 'CURVE':
            obj.data.extrude = extrude
            obj.data.bevel_depth = bevel_depth
        obj.parent = parent_empty
    
    # Add the parent to the list of imported objects
    imported_objects.append(parent_empty)
    
    return imported_objects


def import_blend(filepath, data_types=None, link=False, relative_path=True):
    """Import objects from another .blend file.
    
    Args:
        filepath: Path to the .blend file.
        data_types: List of data types to import ('OBJECT', 'MATERIAL', etc.). If None, imports objects.
        link: Whether to link (True) or append (False) the data.
        relative_path: Whether to use relative paths.
        
    Returns:
        List of imported objects.
    """
    # Check if the file exists
    if not os.path.exists(filepath):
        print(f"Error: File not found: {filepath}")
        return []
    
    # Set default data types if none provided
    if data_types is None:
        data_types = ['OBJECT']
    
    # Get original object count to determine what's new
    original_objects = set(bpy.data.objects)
    
    # Import from the .blend file
    with bpy.data.libraries.load(filepath, link=link, relative=relative_path) as (data_from, data_to):
        # For each data type, copy all data
        for data_type in data_types:
            if hasattr(data_from, data_type.lower()):
                setattr(data_to, data_type.lower(), getattr(data_from, data_type.lower()))
    
    # Find newly added objects
    new_objects = set(bpy.data.objects) - original_objects
    
    # Link the new objects to the scene if they aren't already
    for obj in new_objects:
        if obj.name not in bpy.context.scene.objects:
            bpy.context.scene.collection.objects.link(obj)
    
    return list(new_objects)


def organize_imported_objects(objects, collection_name="Imported"):
    """Organize imported objects into a collection.
    
    Args:
        objects: List of objects to organize.
        collection_name: Name for the collection.
        
    Returns:
        The created collection.
    """
    # Check if the collection already exists
    if collection_name in bpy.data.collections:
        collection = bpy.data.collections[collection_name]
    else:
        # Create a new collection
        collection = bpy.data.collections.new(collection_name)
        bpy.context.scene.collection.children.link(collection)
    
    # Add the objects to the collection
    for obj in objects:
        # Check if the object is already in the collection
        if obj.name not in collection.objects:
            # Link the object to the collection
            collection.objects.link(obj)
            
            # Optionally, remove from other collections
            for other_coll in obj.users_collection:
                if other_coll != collection:
                    other_coll.objects.unlink(obj)
    
    return collection


def import_model_by_extension(filepath, location=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1)):
    """Import a model based on its file extension.
    
    Args:
        filepath: Path to the model file.
        location: (x, y, z) tuple for object location.
        rotation: (x, y, z) tuple for object rotation in radians.
        scale: (x, y, z) tuple for object scale.
        
    Returns:
        List of imported objects.
    """
    # Check if the file exists
    if not os.path.exists(filepath):
        print(f"Error: File not found: {filepath}")
        return []
    
    # Get the file extension
    ext = os.path.splitext(filepath)[1].lower()
    
    # Import based on extension
    if ext == '.obj':
        return import_obj(filepath, location, rotation, scale)
    elif ext == '.fbx':
        return import_fbx(filepath, location, rotation, scale)
    elif ext in ['.gltf', '.glb']:
        return import_gltf(filepath, location, rotation, scale)
    elif ext == '.stl':
        obj = import_stl(filepath, location, rotation, scale)
        return [obj] if obj else []
    elif ext == '.ply':
        obj = import_ply(filepath, location, rotation, scale)
        return [obj] if obj else []
    elif ext == '.dae':
        return import_dae(filepath, location, rotation, scale)
    elif ext == '.abc':
        return import_abc(filepath, location, rotation, scale)
    elif ext in ['.usd', '.usda', '.usdc', '.usdz']:
        return import_usd(filepath, location, rotation, scale)
    elif ext == '.svg':
        return import_svg(filepath, location, rotation, scale)
    elif ext == '.blend':
        return import_blend(filepath)
    else:
        print(f"Error: Unsupported file format: {ext}")
        return []


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
        # Deselect all objects first
        for sel_obj in bpy.context.selected_objects:
            sel_obj.select_set(False)
        
        # Select only the desired object
        obj.select_set(True)
        
        # Set as active object
        bpy.context.view_layer.objects.active = obj
        
        # Save the file with only the selected object
        bpy.ops.wm.save_as_mainfile(filepath=filepath, copy=True)
    else:
        # Save the entire scene
        bpy.ops.wm.save_as_mainfile(filepath=filepath)


def import_model_examples(models_dir="./example_models", save_dir="./blend_files/imported_models/"):
    """Import example models and save them.
    
    Args:
        models_dir: Directory with example model files.
        save_dir: Directory to save the .blend files.
    """
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    # Check if the models directory exists
    if not os.path.exists(models_dir):
        print(f"Warning: Models directory not found: {models_dir}")
        print("Creating example outputs with dummy data.")
        
        # Create a few primitive objects in lieu of imports
        primitive_types = ["cube", "sphere", "cylinder", "cone", "torus"]
        
        for prim_type in primitive_types:
            clear_scene()
            
            # Create primitive
            if prim_type == "cube":
                bpy.ops.mesh.primitive_cube_add(size=2.0)
            elif prim_type == "sphere":
                bpy.ops.mesh.primitive_uv_sphere_add(radius=1.0)
            elif prim_type == "cylinder":
                bpy.ops.mesh.primitive_cylinder_add(radius=1.0, depth=2.0)
            elif prim_type == "cone":
                bpy.ops.mesh.primitive_cone_add(radius1=1.0, radius2=0.0)
            elif prim_type == "torus":
                bpy.ops.mesh.primitive_torus_add(major_radius=1.0, minor_radius=0.25)
            
            obj = bpy.context.active_object
            obj.name = f"Example_{prim_type}"
            
            # Save to blend file
            filepath = os.path.join(save_dir, f"example_{prim_type}.blend")
            save_blend_file(filepath, obj)
            print(f"Created and saved example_{prim_type} to {filepath}")
        
        return
    
    # List of example model files
    model_files = []
    for root, dirs, files in os.walk(models_dir):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in ['.obj', '.fbx', '.gltf', '.glb', '.stl', '.ply', '.dae', '.abc', '.usd', '.usda', '.usdc', '.usdz', '.svg']:
                model_files.append(os.path.join(root, file))
    
    # If no models found, create a message
    if not model_files:
        print(f"No model files found in {models_dir}")
        print("Please place model files in this directory or specify a different directory.")
        return
    
    # Import and save each model
    for model_file in model_files:
        try:
            # Clear the scene
            clear_scene()
            
            # Import the model
            imported_objects = import_model_by_extension(model_file)
            
            if imported_objects:
                # Organize into a collection
                base_name = os.path.basename(model_file).split('.')[0]
                collection = organize_imported_objects(imported_objects, collection_name=f"Import_{base_name}")
                
                # Save to a blend file
                filepath = os.path.join(save_dir, f"imported_{base_name}.blend")
                save_blend_file(filepath)
                print(f"Imported and saved {base_name} to {filepath}")
            else:
                print(f"No objects imported from {model_file}")
        except Exception as e:
            print(f"Error importing {model_file}: {e}")


# Example usage
if __name__ == "__main__":
    # Import example models from a directory
    import_model_examples()
    
    # Or import a specific model
    # clear_scene()
    # model_file = "./example_models/cube.obj"  # Replace with your model file
    # imported_objects = import_model_by_extension(model_file)
    # save_blend_file("./blend_files/imported_models/my_import.blend")