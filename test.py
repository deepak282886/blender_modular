import bpy
import math
import os
import sys
import random

# Add the directory containing the modules to Python's path
# Adjust this path to where your modules are located
script_dir = os.path.dirname(os.path.abspath(__file__))
if script_dir not in sys.path:
    sys.path.append(script_dir)

# Import all modules
from mesh_creator import create_cube, create_sphere, create_cylinder, create_plane, create_torus
from curve_creator import create_bezier_curve, create_spiral_curve, create_helix_curve
from surface_creator import create_nurbs_surface, create_landscape_surface
from meta_creator import create_meta_ball, create_meta_tubes, create_meta_dna
from text_creator import create_3d_text, create_neon_text, create_text_on_curve
from empty_creator import create_empty_parent, create_empty_track, create_empty_path_animation
from collection_creator import create_collection, add_object_to_collection, create_collection_instance
from armature_creator import create_biped_armature, create_simple_rig_on_mesh
from import_model import import_model_by_extension, organize_imported_objects


def clear_scene():
    """Clear the current Blender scene of all objects."""
    for obj in bpy.data.objects:
        bpy.data.objects.remove(obj, do_unlink=True)


def setup_environment():
    """Set up the basic environment with lighting and camera."""
    # Create a camera
    bpy.ops.object.camera_add(location=(12, -15, 10), rotation=(math.radians(60), 0, math.radians(60)))
    camera = bpy.context.active_object
    camera.name = "MainCamera"
    
    # Set as active camera
    bpy.context.scene.camera = camera
    
    # Create lights
    light_data = bpy.data.lights.new(name="SunLight", type='SUN')
    light_data.energy = 2.0
    light_object = bpy.data.objects.new(name="Sun", object_data=light_data)
    bpy.context.collection.objects.link(light_object)
    light_object.location = (5, 5, 15)
    light_object.rotation_euler = (math.radians(60), math.radians(30), 0)
    
    # Add area light for fill
    light_data2 = bpy.data.lights.new(name="FillLight", type='AREA')
    light_data2.energy = 3.0
    light_data2.size = 5.0
    light_object2 = bpy.data.objects.new(name="Fill", object_data=light_data2)
    bpy.context.collection.objects.link(light_object2)
    light_object2.location = (-5, -5, 8)
    light_object2.rotation_euler = (math.radians(45), math.radians(-30), 0)
    
    # Create ground plane
    ground = create_plane(size=30.0, location=(0, 0, -0.01))
    ground.name = "Ground"
    
    # Add a simple material to the ground
    mat = bpy.data.materials.new(name="GroundMaterial")
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes["Principled BSDF"]
    bsdf.inputs[0].default_value = (0.2, 0.2, 0.2, 1.0)  # Base color
    bsdf.inputs[7].default_value = 0.05  # Roughness
    
    if ground.data.materials:
        ground.data.materials[0] = mat
    else:
        ground.data.materials.append(mat)


def create_terrain_area():
    """Create a landscape terrain area with vegetation."""
    # Create main terrain collection
    terrain_collection = create_collection("Terrain")
    
    # Create landscape
    terrain = create_landscape_surface(
        width=20.0, height=20.0,
        x_res=50, y_res=50,
        height_scale=1.5,
        noise_scale=2.0,
        location=(-10, -10, -0.5)
    )
    terrain.name = "Landscape"
    
    # Add material to terrain
    terrain_mat = bpy.data.materials.new(name="TerrainMaterial")
    terrain_mat.use_nodes = True
    bsdf = terrain_mat.node_tree.nodes["Principled BSDF"]
    bsdf.inputs[0].default_value = (0.08, 0.28, 0.05, 1.0)  # Green
    
    if terrain.data.materials:
        terrain.data.materials[0] = terrain_mat
    else:
        terrain.data.materials.append(terrain_mat)
    
    add_object_to_collection(terrain, terrain_collection)
    
    # Create trees (simplified as cylinders with spheres)
    tree_collection = create_collection("Trees", terrain_collection)
    
    # Create a prototype tree
    tree_trunk = create_cylinder(radius=0.1, depth=1.2, location=(0, 0, 0.6))
    tree_trunk.name = "TreeTrunk"
    tree_leaves = create_sphere(radius=0.4, location=(0, 0, 1.2))
    tree_leaves.name = "TreeLeaves"
    
    # Add materials
    trunk_mat = bpy.data.materials.new(name="TrunkMaterial")
    trunk_mat.use_nodes = True
    trunk_bsdf = trunk_mat.node_tree.nodes["Principled BSDF"]
    trunk_bsdf.inputs[0].default_value = (0.35, 0.2, 0.1, 1.0)  # Brown
    
    leaves_mat = bpy.data.materials.new(name="LeavesMaterial")
    leaves_mat.use_nodes = True
    leaves_bsdf = leaves_mat.node_tree.nodes["Principled BSDF"]
    leaves_bsdf.inputs[0].default_value = (0.05, 0.3, 0.05, 1.0)  # Dark green
    
    tree_trunk.data.materials.append(trunk_mat)
    tree_leaves.data.materials.append(leaves_mat)
    
    # Group the tree parts
    tree_parts = [tree_trunk, tree_leaves]
    tree_parent = create_empty_parent("TreePrototype", tree_parts)
    
    add_object_to_collection(tree_parent, tree_collection)
    
    # Scatter trees randomly on terrain
    random.seed(42)  # For reproducible results
    for i in range(15):
        # Random position on terrain
        pos_x = random.uniform(-8, 8)
        pos_y = random.uniform(-8, 8)
        # Compute height at this point (simplified)
        pos_z = 0.5 + 0.5 * math.sin(pos_x * 0.2) * math.cos(pos_y * 0.2)
        
        scale = random.uniform(0.7, 1.3)
        rotation = (0, 0, random.uniform(0, math.pi * 2))
        
        tree_instance = create_collection_instance(
            tree_collection,
            name=f"Tree_{i}",
            location=(pos_x, pos_y, pos_z),
            rotation=rotation,
            scale=(scale, scale, scale)
        )


def create_futuristic_building():
    """Create a futuristic-looking building using primitives and curves."""
    # Create building collection
    building_collection = create_collection("FuturisticBuilding")
    
    # Base structure
    base = create_cube(size=5.0, location=(0, 0, 2.5))
    base.scale = (1, 1, 0.5)
    base.name = "BuildingBase"
    
    tower = create_cylinder(radius=1.5, depth=8.0, location=(0, 0, 7.0))
    tower.name = "BuildingTower"
    
    dome = create_sphere(radius=2.0, location=(0, 0, 11.0))
    dome.scale = (1, 1, 0.5)
    dome.name = "BuildingDome"
    
    # Add decorative elements
    ring = create_torus(major_radius=2.5, minor_radius=0.2, location=(0, 0, 3.5))
    ring.name = "DecorativeRing"
    
    # Create a spiral structure around the tower
    spiral = create_spiral_curve(
        turns=3, 
        height=8.0, 
        radius=2.0, 
        points=64, 
        name="TowerSpiral", 
        location=(0, 0, 3.0)
    )
    
    # Convert curve to mesh and add thickness
    bpy.context.view_layer.objects.active = spiral
    bpy.ops.object.convert(target='MESH')
    bpy.ops.object.modifier_add(type='SOLIDIFY')
    spiral.modifiers["Solidify"].thickness = 0.2
    
    # Create futuristic signage
    sign = create_neon_text(
        text="NEXUS",
        size=0.5,
        extrude=0.1,
        location=(0, -2.5, 5.0),
        color=(0, 1, 0.8, 1)
    )
    sign.rotation_euler = (0, 0, 0)
    
    # Create material for building parts
    building_mat = bpy.data.materials.new(name="BuildingMaterial")
    building_mat.use_nodes = True
    building_bsdf = building_mat.node_tree.nodes["Principled BSDF"]
    building_bsdf.inputs[0].default_value = (0.2, 0.3, 0.4, 1.0)  # Blue-gray
    building_bsdf.inputs[7].default_value = 0.1  # Roughness
    building_bsdf.inputs[6].default_value = 0.8  # Metallic
    
    # Apply material to building parts
    for obj in [base, tower, dome, ring]:
        obj.data.materials.append(building_mat)
        add_object_to_collection(obj, building_collection)
    
    # Add spiral and sign to collection
    add_object_to_collection(spiral, building_collection)
    add_object_to_collection(sign, building_collection)


def create_character():
    """Create a simple rigged character."""
    # Create character collection
    character_collection = create_collection("Character")
    
    # Create a cylindrical body for simplicity
    body = create_cylinder(radius=0.3, depth=1.5, location=(5, 5, 0.75))
    body.name = "CharacterBody"
    
    # Head
    head = create_sphere(radius=0.3, location=(5, 5, 1.8))
    head.name = "CharacterHead"
    
    # Arms (simplified)
    left_arm = create_cylinder(radius=0.1, depth=0.8, location=(5.4, 5, 1.2))
    left_arm.rotation_euler = (0, math.pi/2, 0)
    left_arm.name = "LeftArm"
    
    right_arm = create_cylinder(radius=0.1, depth=0.8, location=(4.6, 5, 1.2))
    right_arm.rotation_euler = (0, math.pi/2, 0)
    right_arm.name = "RightArm"
    
    # Legs (simplified)
    left_leg = create_cylinder(radius=0.1, depth=0.8, location=(5.15, 5, 0.15))
    left_leg.name = "LeftLeg"
    
    right_leg = create_cylinder(radius=0.1, depth=0.8, location=(4.85, 5, 0.15))
    right_leg.name = "RightLeg"
    
    # Create material for character
    character_mat = bpy.data.materials.new(name="CharacterMaterial")
    character_mat.use_nodes = True
    character_bsdf = character_mat.node_tree.nodes["Principled BSDF"]
    character_bsdf.inputs[0].default_value = (0.8, 0.2, 0.2, 1.0)  # Red
    
    # Apply material to all parts
    character_parts = [body, head, left_arm, right_arm, left_leg, right_leg]
    for part in character_parts:
        part.data.materials.append(character_mat)
    
    # Join all parts into a single mesh for rigging
    for part in character_parts:
        part.select_set(True)
    bpy.context.view_layer.objects.active = body
    bpy.ops.object.join()
    
    # The joined object is now the active object
    character_mesh = bpy.context.active_object
    character_mesh.name = "Character"
    
    # Create armature and rig the character
    armature = create_biped_armature(name="CharacterRig", height=2.0, location=(5, 5, 0))
    
    # Parent the mesh to the armature
    character_mesh.select_set(True)
    armature.select_set(True)
    bpy.context.view_layer.objects.active = armature
    bpy.ops.object.parent_set(type='ARMATURE')
    
    # Add objects to the collection
    add_object_to_collection(character_mesh, character_collection)
    add_object_to_collection(armature, character_collection)


def create_meta_organism():
    """Create an organic-looking structure using metaballs."""
    # Create metaball collection
    meta_collection = create_collection("MetaOrganism")
    
    # Create base DNA structure
    dna = create_meta_dna(
        turns=2,
        bases_per_turn=8,
        radius=0.3,
        helix_radius=1.0,
        height=4.0,
        name="OrganismDNA",
        location=(-5, 5, 2.0)
    )
    
    # Add circular tube structure
    tubes = create_meta_tubes(
        num_rings=2,
        balls_per_ring=12,
        radius=0.4,
        ring_radius=1.5,
        name="OrganismTubes",
        location=(-5, 5, 2.0)
    )
    
    # Create material for the metaballs
    meta_mat = bpy.data.materials.new(name="OrganismMaterial")
    meta_mat.use_nodes = True
    meta_bsdf = meta_mat.node_tree.nodes["Principled BSDF"]
    meta_bsdf.inputs[0].default_value = (0.0, 0.4, 0.6, 1.0)  # Blue
    meta_bsdf.inputs[7].default_value = 0.2  # Roughness
    
    # Apply material to metaballs
    for obj in [dna, tubes]:
        if obj.data.materials:
            obj.data.materials[0] = meta_mat
        else:
            obj.data.materials.append(meta_mat)
        add_object_to_collection(obj, meta_collection)
    
    # Create path for animation
    path = create_bezier_curve(
        points=[(-6, 4, 2), (-5, 6, 3), (-4, 4, 2)],
        name="OrganismPath",
        location=(0, 0, 0)
    )
    
    # Add tracking empty
    tracker_empty = create_empty_track(
        name="OrganismTracker",
        target=dna,
        location=(-7, 5, 3.0),
        empty_type='SPHERE'
    )
    
    # Add objects to collection
    add_object_to_collection(path, meta_collection)
    add_object_to_collection(tracker_empty, meta_collection)


def create_abstract_art():
    """Create an abstract art installation using curves and surfaces."""
    # Create art collection
    art_collection = create_collection("AbstractArt")
    
    # Create a NURBS surface base
    base_surface = create_nurbs_surface(
        size=3.0,
        u_res=8,
        v_res=8,
        name="ArtBase",
        location=(5, -5, 0.5)
    )
    
    # Create a helix structure
    helix = create_helix_curve(
        turns=5,
        height=4.0,
        radius=1.0,
        points=64,
        name="ArtHelix",
        location=(5, -5, 0.5)
    )
    
    # Create circular text
    text_obj, curve_obj = create_text_on_curve(
        text="ABSTRACT ART",
        curve_type='CIRCLE',
        name="ArtText",
        location=(5, -5, 3.0),
        size=0.3,
        curve_radius=1.5
    )
    
    # Create materials
    # Base surface material
    base_mat = bpy.data.materials.new(name="ArtBaseMaterial")
    base_mat.use_nodes = True
    base_bsdf = base_mat.node_tree.nodes["Principled BSDF"]
    base_bsdf.inputs[0].default_value = (0.9, 0.9, 0.9, 1.0)  # White
    base_bsdf.inputs[7].default_value = 0.05  # Roughness
    
    # Helix material
    helix_mat = bpy.data.materials.new(name="ArtHelixMaterial")
    helix_mat.use_nodes = True
    helix_bsdf = helix_mat.node_tree.nodes["Principled BSDF"]
    helix_bsdf.inputs[0].default_value = (0.8, 0.1, 0.8, 1.0)  # Purple
    helix_bsdf.inputs[7].default_value = 0.3  # Roughness
    
    # Apply materials
    base_surface.data.materials.append(base_mat)
    helix.data.materials.append(helix_mat)
    
    # Add objects to collection
    add_object_to_collection(base_surface, art_collection)
    add_object_to_collection(helix, art_collection)
    add_object_to_collection(text_obj, art_collection)
    add_object_to_collection(curve_obj, art_collection)


def import_external_model():
    """Import an external model if available, otherwise create a placeholder."""
    # Create a collection for the imported model
    import_collection = create_collection("ImportedModel")
    
    # Check if any example model exists (modify path as needed)
    model_files = [
        "./models/example.obj",
        "./models/example.fbx",
        "./models/example.gltf",
        "./models/example.stl"
    ]
    
    model_imported = False
    
    for model_path in model_files:
        if os.path.exists(model_path):
            # Import the model
            imported_objects = import_model_by_extension(
                filepath=model_path,
                location=(-5, -5, 0),
                rotation=(0, 0, 0),
                scale=(1, 1, 1)
            )
            
            # Organize imported objects
            if imported_objects:
                organize_imported_objects(imported_objects, "ImportedModel")
                model_imported = True
                break
    
    # If no model was imported, create a placeholder
    if not model_imported:
        # Create a simple placeholder (teapot-like shape using primitives)
        body = create_sphere(radius=1.0, location=(-5, -5, 1.0))
        body.scale = (1.2, 1.0, 0.8)
        body.name = "PlaceholderBody"
        
        spout = create_cylinder(radius=0.2, depth=1.0, location=(-3.8, -5, 1.0))
        spout.rotation_euler = (0, math.pi/2, 0)
        spout.name = "PlaceholderSpout"
        
        handle = create_torus(
            major_radius=0.5, 
            minor_radius=0.1, 
            location=(-5.8, -5, 1.2)
        )
        handle.rotation_euler = (math.pi/2, 0, 0)
        handle.name = "PlaceholderHandle"
        
        lid = create_sphere(radius=0.5, location=(-5, -5, 1.6))
        lid.scale = (0.8, 0.8, 0.3)
        lid.name = "PlaceholderLid"
        
        # Create material
        mat = bpy.data.materials.new(name="PlaceholderMaterial")
        mat.use_nodes = True
        bsdf = mat.node_tree.nodes["Principled BSDF"]
        bsdf.inputs[0].default_value = (0.7, 0.7, 0.7, 1.0)  # Gray
        bsdf.inputs[7].default_value = 0.1  # Roughness
        bsdf.inputs[6].default_value = 0.8  # Metallic
        
        # Apply material to all parts
        for obj in [body, spout, handle, lid]:
            obj.data.materials.append(mat)
            add_object_to_collection(obj, import_collection)
        
        # Group the placeholder parts
        placeholder_parts = [body, spout, handle, lid]
        create_empty_parent("PlaceholderModel", placeholder_parts, location=(-5, -5, 0))


def setup_scene_organization():
    """Create a main collection to organize the scene."""
    # Create a main collection for the entire scene
    main_collection = create_collection("ComplexScene")
    
    # Move all top-level collections under the main collection
    collections_to_move = [
        "Terrain", "FuturisticBuilding", "Character", 
        "MetaOrganism", "AbstractArt", "ImportedModel"
    ]
    
    for coll_name in collections_to_move:
        if coll_name in bpy.data.collections:
            coll = bpy.data.collections[coll_name]
            
            # Unlink from scene collection
            if coll.name in bpy.context.scene.collection.children:
                bpy.context.scene.collection.children.unlink(coll)
            
            # Link to main collection
            main_collection.children.link(coll)


def setup_render_settings():
    """Configure render settings for a nice output."""
    render = bpy.context.scene.render
    
    # Set resolution
    render.resolution_x = 1920
    render.resolution_y = 1080
    render.resolution_percentage = 100
    
    # Set samples for Cycles renderer
    bpy.context.scene.render.engine = 'CYCLES'
    bpy.context.scene.cycles.samples = 128
    bpy.context.scene.cycles.preview_samples = 32
    
    # Set background color
    world = bpy.data.worlds["World"]
    world.use_nodes = True
    bg_node = world.node_tree.nodes["Background"]
    bg_node.inputs[0].default_value = (0.05, 0.05, 0.05, 1.0)  # Dark gray
    
    # Set up a simple animation (orbit camera)
    bpy.context.scene.frame_start = 1
    bpy.context.scene.frame_end = 240
    
    camera = bpy.data.objects["MainCamera"]
    
    # Create an empty as a target for the camera
    bpy.ops.object.empty_add(type='PLAIN_AXES', location=(0, 0, 5))
    target = bpy.context.active_object
    target.name = "CameraTarget"
    
    # Make camera track the target
    track = camera.constraints.new(type='TRACK_TO')
    track.target = target
    track.track_axis = 'TRACK_NEGATIVE_Z'
    track.up_axis = 'UP_Y'
    
    # Create a circle path for camera
    circle_path = create_bezier_curve()
    bpy.ops.transform.resize(value=(15, 15, 0))
    
    # Make it a circle
    bpy.ops.object.editmode_toggle()
    bpy.ops.curve.cyclic_toggle()
    bpy.ops.object.editmode_toggle()
    
    # Add follow path constraint to the camera
    follow = camera.constraints.new(type='FOLLOW_PATH')
    follow.target = circle_path
    follow.use_curve_follow = True
    
    # Animate the path
    circle_path.data.path_duration = 240
    follow.offset_factor = 0.0
    follow.keyframe_insert(data_path="offset_factor", frame=1)
    follow.offset_factor = 1.0
    follow.keyframe_insert(data_path="offset_factor", frame=240)


def main():
    """Main function to create the entire complex scene."""
    # Clear the scene
    clear_scene()
    
    # Set up environment
    setup_environment()
    
    # Create the different parts of the scene
    create_terrain_area()
    create_futuristic_building()
    create_character()
    create_meta_organism()
    create_abstract_art()
    import_external_model()
    
    # Organize the scene
    setup_scene_organization()
    
    # Configure render settings
    setup_render_settings()
    
    # Save the result
    output_path = os.path.join(script_dir, "complex_asset.blend")
    bpy.ops.wm.save_as_mainfile(filepath=output_path)
    print(f"Complex asset created and saved to: {output_path}")


# Execute the main function
if __name__ == "__main__":
    main()