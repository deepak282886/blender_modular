import bpy
import os
import math
from mathutils import Vector


def clear_scene():
    """Clear the current scene of all objects."""
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()


def create_collection(name="NewCollection", parent_collection=None):
    """Create a new collection.
    
    Args:
        name: Name for the collection.
        parent_collection: Parent collection. If None, adds to the scene collection.
        
    Returns:
        The created collection.
    """
    # Create a new collection
    new_collection = bpy.data.collections.new(name)
    
    # Add to parent collection or scene collection
    if parent_collection:
        parent_collection.children.link(new_collection)
    else:
        bpy.context.scene.collection.children.link(new_collection)
    
    return new_collection


def add_object_to_collection(obj, collection):
    """Add an object to a collection.
    
    Args:
        obj: The object to add.
        collection: The collection to add to.
        
    Returns:
        True if successful, False otherwise.
    """
    try:
        # Check if object is already in the collection
        if obj.name in collection.objects:
            print(f"Object {obj.name} is already in collection {collection.name}")
            return True
        
        # Add the object to the collection
        collection.objects.link(obj)
        
        # Optionally remove from other collections
        # for other_coll in obj.users_collection:
        #     if other_coll != collection:
        #         other_coll.objects.unlink(obj)
        
        return True
    except Exception as e:
        print(f"Error adding object to collection: {e}")
        return False


def remove_object_from_collection(obj, collection):
    """Remove an object from a collection.
    
    Args:
        obj: The object to remove.
        collection: The collection to remove from.
        
    Returns:
        True if successful, False otherwise.
    """
    try:
        # Check if object is in the collection
        if obj.name not in collection.objects:
            print(f"Object {obj.name} is not in collection {collection.name}")
            return False
        
        # Remove the object from the collection
        collection.objects.unlink(obj)
        
        return True
    except Exception as e:
        print(f"Error removing object from collection: {e}")
        return False


def create_nested_collections(names, parent_collection=None):
    """Create a hierarchy of nested collections.
    
    Args:
        names: List of collection names, from parent to child.
        parent_collection: Parent collection for the first in the list. If None, uses scene collection.
        
    Returns:
        The last created collection.
    """
    current_parent = parent_collection
    last_collection = None
    
    for name in names:
        new_collection = create_collection(name, current_parent)
        current_parent = new_collection
        last_collection = new_collection
    
    return last_collection


def create_collection_instance(collection, name=None, location=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1)):
    """Create an instance of a collection.
    
    Args:
        collection: The collection to instance.
        name: Name for the instance. If None, uses collection name + "Instance".
        location: (x, y, z) tuple for instance location.
        rotation: (x, y, z) tuple for instance rotation in radians.
        scale: (x, y, z) tuple for instance scale.
        
    Returns:
        The created collection instance object.
    """
    if name is None:
        name = collection.name + "Instance"
    
    # Create a collection instance
    bpy.ops.object.collection_instance_add(collection=collection.name, location=location, rotation=rotation)
    
    # Get the created object
    instance_obj = bpy.context.active_object
    instance_obj.name = name
    
    # Set scale
    instance_obj.scale = scale
    
    return instance_obj


def create_collection_with_objects(name="ObjectCollection", objects=None):
    """Create a collection and add objects to it.
    
    Args:
        name: Name for the collection.
        objects: List of objects to add. If None, creates default objects.
        
    Returns:
        The created collection.
    """
    # Create a new collection
    new_collection = create_collection(name)
    
    # Create default objects if none provided
    if objects is None:
        # Create a cube
        bpy.ops.mesh.primitive_cube_add(size=1, location=(1, 0, 0))
        cube = bpy.context.active_object
        cube.name = "CollectionCube"
        
        # Create a sphere
        bpy.ops.mesh.primitive_uv_sphere_add(radius=0.5, location=(-1, 0, 0))
        sphere = bpy.context.active_object
        sphere.name = "CollectionSphere"
        
        objects = [cube, sphere]
    
    # Add objects to the collection
    for obj in objects:
        add_object_to_collection(obj, new_collection)
    
    return new_collection


def organize_by_type(prefix="Type"):
    """Organize existing objects into collections based on their type.
    
    Args:
        prefix: Prefix for collection names.
        
    Returns:
        Dictionary mapping object types to their collections.
    """
    # Create a dictionary to hold type collections
    type_collections = {}
    
    # Iterate through all objects in the scene
    for obj in bpy.data.objects:
        obj_type = obj.type  # MESH, CURVE, LIGHT, etc.
        
        # Create a collection for this type if it doesn't exist
        if obj_type not in type_collections:
            coll_name = f"{prefix}_{obj_type}"
            type_collections[obj_type] = create_collection(coll_name)
        
        # Add the object to its type collection
        add_object_to_collection(obj, type_collections[obj_type])
    
    return type_collections


def create_layered_scene(base_name="Layer", layer_count=3):
    """Create a scene with multiple collection layers.
    
    Args:
        base_name: Base name for collections.
        layer_count: Number of layers to create.
        
    Returns:
        List of created collections.
    """
    collections = []
    
    # Create background collection with a plane
    bg_collection = create_collection(f"{base_name}_Background")
    collections.append(bg_collection)
    
    bpy.ops.mesh.primitive_plane_add(size=10, location=(0, 0, -0.5))
    bg_plane = bpy.context.active_object
    bg_plane.name = "BackgroundPlane"
    add_object_to_collection(bg_plane, bg_collection)
    
    # Create middle layers with various objects
    for i in range(1, layer_count):
        layer_collection = create_collection(f"{base_name}_{i}")
        collections.append(layer_collection)
        
        # Create different objects for each layer
        if i == 1:
            # Create some cubes
            for j in range(3):
                bpy.ops.mesh.primitive_cube_add(size=0.5, location=(j-1, -1, 0))
                cube = bpy.context.active_object
                cube.name = f"Cube_{j}"
                add_object_to_collection(cube, layer_collection)
        elif i == 2:
            # Create some spheres
            for j in range(3):
                bpy.ops.mesh.primitive_uv_sphere_add(radius=0.3, location=(j-1, 0, 0))
                sphere = bpy.context.active_object
                sphere.name = f"Sphere_{j}"
                add_object_to_collection(sphere, layer_collection)
        else:
            # Create some cylinders
            for j in range(3):
                bpy.ops.mesh.primitive_cylinder_add(radius=0.2, depth=0.6, location=(j-1, 1, 0))
                cylinder = bpy.context.active_object
                cylinder.name = f"Cylinder_{j}"
                add_object_to_collection(cylinder, layer_collection)
    
    # Create foreground collection with a camera and light
    fg_collection = create_collection(f"{base_name}_Foreground")
    collections.append(fg_collection)
    
    # Add a camera
    bpy.ops.object.camera_add(location=(0, -5, 2), rotation=(math.radians(60), 0, 0))
    camera = bpy.context.active_object
    camera.name = "SceneCamera"
    add_object_to_collection(camera, fg_collection)
    
    # Add a light
    bpy.ops.object.light_add(type='SUN', location=(2, -2, 4))
    light = bpy.context.active_object
    light.name = "SunLight"
    add_object_to_collection(light, fg_collection)
    
    return collections


def create_collection_instance_grid(collection, rows=3, columns=3, spacing=3.0, 
                                   location=(0, 0, 0), variation=True):
    """Create a grid of collection instances.
    
    Args:
        collection: The collection to instance.
        rows: Number of rows in the grid.
        columns: Number of columns in the grid.
        spacing: Spacing between instances.
        location: (x, y, z) tuple for the center of the grid.
        variation: If True, adds variation to rotation and scale.
        
    Returns:
        List of created instance objects.
    """
    import random
    random.seed(42)  # For reproducibility
    
    instances = []
    
    # Calculate grid offset
    offset_x = (columns - 1) * spacing / 2
    offset_y = (rows - 1) * spacing / 2
    
    for row in range(rows):
        for col in range(columns):
            # Calculate position
            x = col * spacing - offset_x + location[0]
            y = row * spacing - offset_y + location[1]
            z = location[2]
            
            # Calculate rotation and scale with variation if enabled
            if variation:
                rotation = (
                    random.uniform(0, 0.2),
                    random.uniform(0, 0.2),
                    random.uniform(0, math.pi * 2)
                )
                scale = (
                    random.uniform(0.8, 1.2),
                    random.uniform(0.8, 1.2),
                    random.uniform(0.8, 1.2)
                )
            else:
                rotation = (0, 0, 0)
                scale = (1, 1, 1)
            
            # Create instance
            instance = create_collection_instance(
                collection,
                name=f"{collection.name}_Instance_{row}_{col}",
                location=(x, y, z),
                rotation=rotation,
                scale=scale
            )
            
            instances.append(instance)
    
    return instances


def create_modular_building_collections():
    """Create a set of collections for modular building components.
    
    Returns:
        Dictionary of collections categorized by building part.
    """
    # Create a main container collection
    building_collection = create_collection("ModularBuilding")
    
    # Create subcollections for different building parts
    walls_collection = create_collection("Walls", building_collection)
    floors_collection = create_collection("Floors", building_collection)
    roofs_collection = create_collection("Roofs", building_collection)
    details_collection = create_collection("Details", building_collection)
    
    # Create a basic wall
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 0.5))
    wall = bpy.context.active_object
    wall.name = "BasicWall"
    wall.scale = (2, 0.2, 1)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    add_object_to_collection(wall, walls_collection)
    
    # Create a basic floor
    bpy.ops.mesh.primitive_cube_add(size=1, location=(0, 0, 0))
    floor = bpy.context.active_object
    floor.name = "BasicFloor"
    floor.scale = (2, 2, 0.1)
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    add_object_to_collection(floor, floors_collection)
    
    # Create a basic roof
    bpy.ops.mesh.primitive_cone_add(radius1=1.5, radius2=0, depth=1, location=(0, 0, 1.5))
    roof = bpy.context.active_object
    roof.name = "BasicRoof"
    add_object_to_collection(roof, roofs_collection)
    
    # Create a window detail
    bpy.ops.mesh.primitive_cube_add(size=0.5, location=(0, 0, 0.5))
    window = bpy.context.active_object
    window.name = "Window"
    add_object_to_collection(window, details_collection)
    
    collections = {
        "main": building_collection,
        "walls": walls_collection,
        "floors": floors_collection,
        "roofs": roofs_collection,
        "details": details_collection
    }
    
    return collections


def set_collection_visibility(collection, visible=True):
    """Set the visibility of a collection in the viewport and render.
    
    Args:
        collection: The collection to modify.
        visible: Whether the collection should be visible.
        
    Returns:
        None
    """
    # If collection is stored as a name string, get the actual collection
    if isinstance(collection, str):
        collection = bpy.data.collections.get(collection)
        if not collection:
            print(f"Collection {collection} not found")
            return
    
    # Set visibility in viewport
    collection.hide_viewport = not visible
    
    # Set visibility in render
    collection.hide_render = not visible


def create_view_layers_with_collections(base_name="ViewLayer", collection_count=3):
    """Create multiple view layers with different collections visible.
    
    Args:
        base_name: Base name for view layers.
        collection_count: Number of collections/layers to create.
        
    Returns:
        Dictionary mapping view layer names to their layer objects.
    """
    # Create collections
    collections = []
    scene = bpy.context.scene
    
    for i in range(collection_count):
        coll_name = f"Collection_{i+1}"
        coll = create_collection(coll_name)
        collections.append(coll)
        
        # Add some objects to the collection
        bpy.ops.mesh.primitive_cube_add(size=1, location=(i-1, 0, 0))
        cube = bpy.context.active_object
        cube.name = f"Cube_{i+1}"
        add_object_to_collection(cube, coll)
    
    # Create view layers
    view_layers = {}
    
    # Create a view layer with all collections
    all_layer_name = f"{base_name}_All"
    if all_layer_name not in scene.view_layers:
        all_layer = scene.view_layers.new(all_layer_name)
        view_layers[all_layer_name] = all_layer
    
    # Create individual view layers for each collection
    for i, coll in enumerate(collections):
        layer_name = f"{base_name}_{i+1}"
        
        # Create new view layer if it doesn't exist
        if layer_name not in scene.view_layers:
            layer = scene.view_layers.new(layer_name)
            view_layers[layer_name] = layer
            
            # Hide other collections in this view layer
            for j, other_coll in enumerate(collections):
                if j != i:
                    # This is a simplified approach - in a full implementation
                    # you would need to handle the view layer collection hierarchy properly
                    try:
                        layer.layer_collection.children[other_coll.name].exclude = True
                    except (KeyError, AttributeError) as e:
                        print(f"Error setting collection visibility: {e}")
    
    return view_layers


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


def create_example_collection_setups(save_dir="./blend_files/collection_examples/"):
    """Create example collection setups and save them.
    
    Args:
        save_dir: Directory to save the .blend files.
    """
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    # Example 1: Nested Collections
    try:
        clear_scene()
        nested = create_nested_collections(["Level1", "Level2", "Level3"])
        
        # Add an object to the deepest collection
        bpy.ops.mesh.primitive_cube_add(size=1)
        cube = bpy.context.active_object
        add_object_to_collection(cube, nested)
        
        filepath = os.path.join(save_dir, "nested_collections.blend")
        save_blend_file(filepath)
        print(f"Created and saved nested_collections to {filepath}")
    except Exception as e:
        print(f"Error creating nested_collections: {e}")
    
    # Example 2: Collection with Objects
    try:
        clear_scene()
        collection = create_collection_with_objects("MixedObjects")
        
        filepath = os.path.join(save_dir, "collection_with_objects.blend")
        save_blend_file(filepath)
        print(f"Created and saved collection_with_objects to {filepath}")
    except Exception as e:
        print(f"Error creating collection_with_objects: {e}")
    
    # Example 3: Instance Grid
    try:
        clear_scene()
        
        # Create a source collection with objects
        source_collection = create_collection_with_objects("SourceCollection")
        
        # Create a grid of instances
        instances = create_collection_instance_grid(source_collection, rows=2, columns=2)
        
        filepath = os.path.join(save_dir, "collection_instance_grid.blend")
        save_blend_file(filepath)
        print(f"Created and saved collection_instance_grid to {filepath}")
    except Exception as e:
        print(f"Error creating collection_instance_grid: {e}")
    
    # Example 4: Layered Scene
    try:
        clear_scene()
        collections = create_layered_scene()
        
        filepath = os.path.join(save_dir, "layered_scene.blend")
        save_blend_file(filepath)
        print(f"Created and saved layered_scene to {filepath}")
    except Exception as e:
        print(f"Error creating layered_scene: {e}")
    
    # Example 5: Modular Building Collections
    try:
        clear_scene()
        building_collections = create_modular_building_collections()
        
        filepath = os.path.join(save_dir, "modular_building.blend")
        save_blend_file(filepath)
        print(f"Created and saved modular_building to {filepath}")
    except Exception as e:
        print(f"Error creating modular_building: {e}")
    
    # Example 6: View Layers with Collections
    try:
        clear_scene()
        view_layers = create_view_layers_with_collections()
        
        filepath = os.path.join(save_dir, "view_layers.blend")
        save_blend_file(filepath)
        print(f"Created and saved view_layers to {filepath}")
    except Exception as e:
        print(f"Error creating view_layers: {e}")


# Example usage
if __name__ == "__main__":
    # Create and save example collection setups
    create_example_collection_setups()
    
    # Or create individual collection setups
    # clear_scene()
    # collections = create_modular_building_collections()
    # save_blend_file("./blend_files/collection_examples/my_modular_building.blend")