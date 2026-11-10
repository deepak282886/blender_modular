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


def create_single_bone_armature(name="SimpleArmature", bone_name="Bone", 
                              location=(0, 0, 0), bone_length=1.0):
    """Create an armature with a single bone.
    
    Args:
        name: Name for the armature object.
        bone_name: Name for the bone.
        location: (x, y, z) tuple for armature location.
        bone_length: Length of the bone.
        
    Returns:
        The created armature object.
    """
    # Create armature object
    bpy.ops.object.armature_add(location=location)
    
    # Get the created armature object
    armature_obj = bpy.context.active_object
    armature_obj.name = name
    
    # Get the bone and set its name and length
    bone = armature_obj.data.bones[0]
    bone.name = bone_name
    
    # Enter edit mode to adjust the bone
    bpy.ops.object.mode_set(mode='EDIT')
    
    # Get the edit bone
    edit_bone = armature_obj.data.edit_bones[bone.name]
    
    # Set bone head and tail
    edit_bone.head = (0, 0, 0)
    edit_bone.tail = (0, 0, bone_length)
    
    # Return to object mode
    bpy.ops.object.mode_set(mode='OBJECT')
    
    return armature_obj


def create_multi_bone_chain(name="ChainArmature", num_bones=3, bone_length=0.5, 
                           location=(0, 0, 0), bone_direction=(0, 0, 1)):
    """Create an armature with a chain of connected bones.
    
    Args:
        name: Name for the armature object.
        num_bones: Number of bones in the chain.
        bone_length: Length of each bone.
        location: (x, y, z) tuple for armature location.
        bone_direction: (x, y, z) tuple for bone direction.
        
    Returns:
        The created armature object.
    """
    # Create armature object
    bpy.ops.object.armature_add(location=location)
    
    # Get the created armature object
    armature_obj = bpy.context.active_object
    armature_obj.name = name
    
    # Normalize the direction vector
    from mathutils import Vector
    direction = Vector(bone_direction)
    if direction.length > 0:
        direction.normalize()
    else:
        direction = Vector((0, 0, 1))
    
    # Enter edit mode to adjust the bones
    bpy.ops.object.mode_set(mode='EDIT')
    
    # Get the edit bones
    edit_bones = armature_obj.data.edit_bones
    
    # Rename the first bone
    first_bone = edit_bones[0]
    first_bone.name = f"{name}_Bone_1"
    
    # Set first bone position and direction
    first_bone.head = (0, 0, 0)
    first_bone.tail = direction * bone_length
    
    # Create additional bones
    prev_bone = first_bone
    for i in range(2, num_bones+1):
        # Create a new bone
        new_bone = edit_bones.new(f"{name}_Bone_{i}")
        
        # Connect to previous bone
        new_bone.head = prev_bone.tail
        new_bone.tail = new_bone.head + direction * bone_length
        new_bone.parent = prev_bone
        new_bone.use_connect = True
        
        prev_bone = new_bone
    
    # Return to object mode
    bpy.ops.object.mode_set(mode='OBJECT')
    
    return armature_obj


def create_biped_armature(name="BipedArmature", height=2.0, location=(0, 0, 0)):
    """Create a basic biped (humanoid) armature.
    
    Args:
        name: Name for the armature object.
        height: Height of the biped.
        location: (x, y, z) tuple for armature location.
        
    Returns:
        The created armature object.
    """
    # Create armature object
    bpy.ops.object.armature_add(location=location)
    
    # Get the created armature object
    armature_obj = bpy.context.active_object
    armature_obj.name = name
    
    # Enter edit mode to build the skeleton
    bpy.ops.object.mode_set(mode='EDIT')
    
    # Get the edit bones
    edit_bones = armature_obj.data.edit_bones
    
    # Clear default bone
    edit_bones.remove(edit_bones[0])
    
    # Calculate bone lengths based on height
    spine_length = height * 0.2
    leg_length = height * 0.3
    arm_length = height * 0.25
    
    # Create spine bones
    root = edit_bones.new("Root")
    root.head = (0, 0, 0)
    root.tail = (0, 0, spine_length * 0.5)
    
    spine = edit_bones.new("Spine")
    spine.head = root.tail
    spine.tail = (0, 0, spine_length * 1.5)
    spine.parent = root
    
    neck = edit_bones.new("Neck")
    neck.head = spine.tail
    neck.tail = (0, 0, spine_length * 2)
    neck.parent = spine
    
    head = edit_bones.new("Head")
    head.head = neck.tail
    head.tail = (0, 0, spine_length * 2.5)
    head.parent = neck
    
    # Create left leg
    l_thigh = edit_bones.new("L_Thigh")
    l_thigh.head = (0.2, 0, spine_length * 0.5)
    l_thigh.tail = (0.2, 0, -leg_length)
    l_thigh.parent = root
    
    l_shin = edit_bones.new("L_Shin")
    l_shin.head = l_thigh.tail
    l_shin.tail = (0.2, 0, -leg_length * 2)
    l_shin.parent = l_thigh
    
    l_foot = edit_bones.new("L_Foot")
    l_foot.head = l_shin.tail
    l_foot.tail = (0.2, 0.3, -leg_length * 2)
    l_foot.parent = l_shin
    
    # Create right leg (mirror of left)
    r_thigh = edit_bones.new("R_Thigh")
    r_thigh.head = (-0.2, 0, spine_length * 0.5)
    r_thigh.tail = (-0.2, 0, -leg_length)
    r_thigh.parent = root
    
    r_shin = edit_bones.new("R_Shin")
    r_shin.head = r_thigh.tail
    r_shin.tail = (-0.2, 0, -leg_length * 2)
    r_shin.parent = r_thigh
    
    r_foot = edit_bones.new("R_Foot")
    r_foot.head = r_shin.tail
    r_foot.tail = (-0.2, 0.3, -leg_length * 2)
    r_foot.parent = r_shin
    
    # Create left arm
    l_collar = edit_bones.new("L_Collar")
    l_collar.head = (0, 0, spine_length * 1.5)
    l_collar.tail = (0.3, 0, spine_length * 1.5)
    l_collar.parent = spine
    
    l_upper_arm = edit_bones.new("L_UpperArm")
    l_upper_arm.head = l_collar.tail
    l_upper_arm.tail = (0.3 + arm_length * 0.5, 0, spine_length)
    l_upper_arm.parent = l_collar
    
    l_forearm = edit_bones.new("L_Forearm")
    l_forearm.head = l_upper_arm.tail
    l_forearm.tail = (0.3 + arm_length, 0, spine_length)
    l_forearm.parent = l_upper_arm
    
    l_hand = edit_bones.new("L_Hand")
    l_hand.head = l_forearm.tail
    l_hand.tail = (0.3 + arm_length + 0.1, 0, spine_length)
    l_hand.parent = l_forearm
    
    # Create right arm (mirror of left)
    r_collar = edit_bones.new("R_Collar")
    r_collar.head = (0, 0, spine_length * 1.5)
    r_collar.tail = (-0.3, 0, spine_length * 1.5)
    r_collar.parent = spine
    
    r_upper_arm = edit_bones.new("R_UpperArm")
    r_upper_arm.head = r_collar.tail
    r_upper_arm.tail = (-0.3 - arm_length * 0.5, 0, spine_length)
    r_upper_arm.parent = r_collar
    
    r_forearm = edit_bones.new("R_Forearm")
    r_forearm.head = r_upper_arm.tail
    r_forearm.tail = (-0.3 - arm_length, 0, spine_length)
    r_forearm.parent = r_upper_arm
    
    r_hand = edit_bones.new("R_Hand")
    r_hand.head = r_forearm.tail
    r_hand.tail = (-0.3 - arm_length - 0.1, 0, spine_length)
    r_hand.parent = r_forearm
    
    # Return to object mode
    bpy.ops.object.mode_set(mode='OBJECT')
    
    # Scale the armature to match the desired height
    armature_obj.scale = (1, 1, 1)  # Reset scale first
    actual_height = head.tail.z - l_foot.head.z
    scale_factor = height / actual_height
    armature_obj.scale = (scale_factor, scale_factor, scale_factor)
    
    return armature_obj


def create_quadruped_armature(name="QuadrupedArmature", length=2.0, height=1.0, location=(0, 0, 0)):
    """Create a basic quadruped (four-legged animal) armature.
    
    Args:
        name: Name for the armature object.
        length: Length of the quadruped.
        height: Height of the quadruped.
        location: (x, y, z) tuple for armature location.
        
    Returns:
        The created armature object.
    """
    # Create armature object
    bpy.ops.object.armature_add(location=location)
    
    # Get the created armature object
    armature_obj = bpy.context.active_object
    armature_obj.name = name
    
    # Enter edit mode to build the skeleton
    bpy.ops.object.mode_set(mode='EDIT')
    
    # Get the edit bones
    edit_bones = armature_obj.data.edit_bones
    
    # Clear default bone
    edit_bones.remove(edit_bones[0])
    
    # Calculate bone lengths based on dimensions
    spine_length = length / 4
    leg_length = height * 0.8
    
    # Create spine bones (from tail to head)
    spine1 = edit_bones.new("Spine1")
    spine1.head = (-spine_length * 1.5, 0, height * 0.5)
    spine1.tail = (-spine_length * 0.5, 0, height * 0.6)
    
    spine2 = edit_bones.new("Spine2")
    spine2.head = spine1.tail
    spine2.tail = (spine_length * 0.5, 0, height * 0.7)
    spine2.parent = spine1
    
    neck = edit_bones.new("Neck")
    neck.head = spine2.tail
    neck.tail = (spine_length * 1, 0, height * 0.9)
    neck.parent = spine2
    
    head = edit_bones.new("Head")
    head.head = neck.tail
    head.tail = (spine_length * 1.5, 0, height * 0.9)
    head.parent = neck
    
    tail1 = edit_bones.new("Tail1")
    tail1.head = (-spine_length * 1.5, 0, height * 0.5)
    tail1.tail = (-spine_length * 2, 0, height * 0.6)
    tail1.parent = spine1
    
    tail2 = edit_bones.new("Tail2")
    tail2.head = tail1.tail
    tail2.tail = (-spine_length * 2.5, 0, height * 0.5)
    tail2.parent = tail1
    
    # Create front legs (back from head)
    fr_thigh = edit_bones.new("FR_Thigh")
    fr_thigh.head = (spine_length * 0.5, -0.2, height * 0.5)
    fr_thigh.tail = (spine_length * 0.5, -0.2, height * 0.25)
    fr_thigh.parent = spine2
    
    fr_shin = edit_bones.new("FR_Shin")
    fr_shin.head = fr_thigh.tail
    fr_shin.tail = (spine_length * 0.5, -0.2, 0)
    fr_shin.parent = fr_thigh
    
    fl_thigh = edit_bones.new("FL_Thigh")
    fl_thigh.head = (spine_length * 0.5, 0.2, height * 0.5)
    fl_thigh.tail = (spine_length * 0.5, 0.2, height * 0.25)
    fl_thigh.parent = spine2
    
    fl_shin = edit_bones.new("FL_Shin")
    fl_shin.head = fl_thigh.tail
    fl_shin.tail = (spine_length * 0.5, 0.2, 0)
    fl_shin.parent = fl_thigh
    
    # Create back legs
    br_thigh = edit_bones.new("BR_Thigh")
    br_thigh.head = (-spine_length * 1, -0.2, height * 0.5)
    br_thigh.tail = (-spine_length * 1, -0.2, height * 0.25)
    br_thigh.parent = spine1
    
    br_shin = edit_bones.new("BR_Shin")
    br_shin.head = br_thigh.tail
    br_shin.tail = (-spine_length * 1, -0.2, 0)
    br_shin.parent = br_thigh
    
    bl_thigh = edit_bones.new("BL_Thigh")
    bl_thigh.head = (-spine_length * 1, 0.2, height * 0.5)
    bl_thigh.tail = (-spine_length * 1, 0.2, height * 0.25)
    bl_thigh.parent = spine1
    
    bl_shin = edit_bones.new("BL_Shin")
    bl_shin.head = bl_thigh.tail
    bl_shin.tail = (-spine_length * 1, 0.2, 0)
    bl_shin.parent = bl_thigh
    
    # Return to object mode
    bpy.ops.object.mode_set(mode='OBJECT')
    
    return armature_obj


def create_armature_with_constraints(name="ConstraintedArmature", location=(0, 0, 0)):
    """Create an armature with bone constraints.
    
    Args:
        name: Name for the armature object.
        location: (x, y, z) tuple for armature location.
        
    Returns:
        The created armature object.
    """
    # Create a simple armature with multiple bones
    armature_obj = create_multi_bone_chain(name=name, num_bones=4, 
                                        bone_length=0.5, location=location)
    
    # Enter pose mode to add constraints
    bpy.ops.object.mode_set(mode='POSE')
    
    # Get the pose bones
    pose_bones = armature_obj.pose.bones
    
    # Add constraint to second bone (bone 2) - Limit Rotation
    if f"{name}_Bone_2" in pose_bones:
        bone2 = pose_bones[f"{name}_Bone_2"]
        limit_rot = bone2.constraints.new('LIMIT_ROTATION')
        limit_rot.use_limit_x = True
        limit_rot.min_x = math.radians(-30)
        limit_rot.max_x = math.radians(30)
        limit_rot.owner_space = 'LOCAL'
    
    # Add constraint to third bone (bone 3) - Copy Rotation from first bone
    if f"{name}_Bone_3" in pose_bones and f"{name}_Bone_1" in pose_bones:
        bone3 = pose_bones[f"{name}_Bone_3"]
        copy_rot = bone3.constraints.new('COPY_ROTATION')
        copy_rot.target = armature_obj
        copy_rot.subtarget = f"{name}_Bone_1"
        copy_rot.use_x = True
        copy_rot.use_y = True
        copy_rot.use_z = True
        copy_rot.target_space = 'LOCAL'
        copy_rot.owner_space = 'LOCAL'
        copy_rot.influence = 0.5  # 50% influence
    
    # Add constraint to fourth bone (bone 4) - IK constraint
    if f"{name}_Bone_4" in pose_bones:
        bone4 = pose_bones[f"{name}_Bone_4"]
        ik = bone4.constraints.new('IK')
        ik.chain_count = 2  # 2 bones in IK chain
    
    # Return to object mode
    bpy.ops.object.mode_set(mode='OBJECT')
    
    return armature_obj


def create_armature_with_control_bones(name="ControlArmature", location=(0, 0, 0)):
    """Create an armature with special control bones.
    
    Args:
        name: Name for the armature object.
        location: (x, y, z) tuple for armature location.
        
    Returns:
        The created armature object.
    """
    # Create a base armature
    armature_obj = create_single_bone_armature(name=name, bone_name="Deform_Bone", 
                                            location=location, bone_length=1.0)
    
    # Enter edit mode to add the control bone
    bpy.ops.object.mode_set(mode='EDIT')
    
    # Get the edit bones
    edit_bones = armature_obj.data.edit_bones
    
    # Create a control bone
    control_bone = edit_bones.new("Control_Bone")
    control_bone.head = (0, 0.5, 0)
    control_bone.tail = (0, 0.5, 1.0)
    
    # Return to object mode, then enter pose mode to set up constraints
    bpy.ops.object.mode_set(mode='OBJECT')
    bpy.ops.object.mode_set(mode='POSE')
    
    # Add constraint to the deform bone to copy transforms from the control bone
    deform_bone = armature_obj.pose.bones["Deform_Bone"]
    copy_trans = deform_bone.constraints.new('COPY_TRANSFORMS')
    copy_trans.target = armature_obj
    copy_trans.subtarget = "Control_Bone"
    
    # Set the control bone's custom shape (use a primitive mesh)
    bpy.ops.mesh.primitive_cube_add(size=0.2, location=(0, 0, 0))
    custom_shape = bpy.context.active_object
    custom_shape.name = "ControlShape"
    custom_shape.display_type = 'WIRE'  # Show as wireframe
    
    # Hide custom shape from renders
    custom_shape.hide_render = True
    
    # Assign the custom shape to the control bone
    control_bone_pose = armature_obj.pose.bones["Control_Bone"]
    control_bone_pose.custom_shape = custom_shape
    
    # Return to object mode
    bpy.ops.object.mode_set(mode='OBJECT')
    
    # Hide the custom shape from viewport
    custom_shape.hide_viewport = True
    
    return armature_obj


def create_simple_rig_on_mesh(armature_name="MeshRig", mesh=None, location=(0, 0, 0)):
    """Create a simple armature and attach it to a mesh.
    
    Args:
        armature_name: Name for the armature object.
        mesh: The mesh object to rig. If None, creates a simple cylinder.
        location: (x, y, z) tuple for armature and mesh location if mesh is created.
        
    Returns:
        Tuple of (armature_object, mesh_object).
    """
    # Create a simple mesh if none is provided
    if mesh is None:
        bpy.ops.mesh.primitive_cylinder_add(vertices=16, radius=0.5, depth=2.0, location=location)
        mesh = bpy.context.active_object
        mesh.name = "RiggedCylinder"
    
    # Create an armature with a chain of bones
    armature_obj = create_multi_bone_chain(name=armature_name, num_bones=3, 
                                        bone_length=0.6, location=mesh.location)
    
    # Deselect all objects using direct data manipulation instead of operators
    for obj in bpy.context.selected_objects:
        obj.select_set(False)
    
    # Select the mesh and armature
    mesh.select_set(True)
    armature_obj.select_set(True)
    bpy.context.view_layer.objects.active = armature_obj
    
    # Parent mesh to armature with automatic weights
    try:
        bpy.ops.object.parent_set(type='ARMATURE_AUTO')
    except Exception as e:
        print(f"Warning: Could not set automatic weights, using vertex groups instead: {e}")
        # Alternative method if automatic weights fail
        # Add armature modifier directly
        mod = mesh.modifiers.new(name="Armature", type='ARMATURE')
        mod.object = armature_obj
    
    return armature_obj, mesh


def create_sample_armature_animation(armature=None, name="ArmatureAnimation", location=(0, 0, 0), 
                                  num_frames=48):
    """Create a simple animation for an armature.
    
    Args:
        armature: The armature to animate. If None, creates a simple chain armature.
        name: Name for the armature if created.
        location: (x, y, z) tuple for armature location if created.
        num_frames: Number of frames for the animation.
        
    Returns:
        The armature object.
    """
    # Create an armature if none is provided
    if armature is None:
        armature = create_multi_bone_chain(name=name, num_bones=3, bone_length=0.5, location=location)
    
    # Set up the scene for animation
    scene = bpy.context.scene
    scene.frame_start = 1
    scene.frame_end = num_frames
    
    # Make sure the armature is selected and active
    for obj in bpy.context.selected_objects:
        obj.select_set(False)
    
    armature.select_set(True)
    bpy.context.view_layer.objects.active = armature
    
    try:
        # Enter pose mode
        bpy.ops.object.mode_set(mode='POSE')
        
        # Get the pose bones
        pose_bones = armature.pose.bones
        
        # Simple rotation animation for each bone
        for i, bone in enumerate(pose_bones):
            # Set initial keyframe at frame 1
            scene.frame_set(1)
            bone.rotation_mode = 'XYZ'
            bone.rotation_euler = (0, 0, 0)
            bone.keyframe_insert(data_path="rotation_euler")
            
            # Set keyframe at 1/4 of the timeline
            scene.frame_set(int(num_frames * 0.25))
            bone.rotation_euler = (math.radians(45) * (i+1), 0, 0)
            bone.keyframe_insert(data_path="rotation_euler")
            
            # Set keyframe at 1/2 of the timeline
            scene.frame_set(int(num_frames * 0.5))
            bone.rotation_euler = (0, math.radians(45) * (i+1), 0)
            bone.keyframe_insert(data_path="rotation_euler")
            
            # Set keyframe at 3/4 of the timeline
            scene.frame_set(int(num_frames * 0.75))
            bone.rotation_euler = (0, 0, math.radians(45) * (i+1))
            bone.keyframe_insert(data_path="rotation_euler")
            
            # Set final keyframe at the end
            scene.frame_set(num_frames)
            bone.rotation_euler = (0, 0, 0)
            bone.keyframe_insert(data_path="rotation_euler")
        
        # Return to object mode
        bpy.ops.object.mode_set(mode='OBJECT')
    
    except Exception as e:
        print(f"Warning: Could not create animation: {e}")
        # Alternative direct method if pose mode is not accessible
        # This is less ideal but can work in background mode
        for bone_name in armature.pose.bones.keys():
            fcurve = armature.animation_data.action.fcurves.new(
                data_path=f'pose.bones["{bone_name}"].rotation_euler', index=0)
            fcurve.keyframe_points.insert(1, 0)
            fcurve.keyframe_points.insert(num_frames, 0)
    
    # Reset timeline to first frame
    scene.frame_set(1)
    
    return armature


def set_armature_display_options(armature, show_names=True, show_axes=False, show_in_front=True):
    """Set display options for an armature.
    
    Args:
        armature: The armature object to modify.
        show_names: Whether to show bone names.
        show_axes: Whether to show bone axes.
        show_in_front: Whether to show bones in front of other objects.
        
    Returns:
        The modified armature object.
    """
    # Set armature properties
    armature.show_names = show_names
    armature.show_axes = show_axes
    armature.show_in_front = show_in_front
    
    return armature


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


def create_all_armature_types(save_dir="./blend_files/armature_types/"):
    """Create all armature types and save them as individual .blend files.
    
    Args:
        save_dir: Directory to save the .blend files.
    """
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    # Dictionary of creation functions and their parameters
    armature_types = {
        "single_bone": {"func": create_single_bone_armature, "params": {}},
        "bone_chain": {"func": create_multi_bone_chain, "params": {"num_bones": 5}},
        "biped": {"func": create_biped_armature, "params": {}},
        "quadruped": {"func": create_quadruped_armature, "params": {}},
        "constrained_armature": {"func": create_armature_with_constraints, "params": {}},
        "control_armature": {"func": create_armature_with_control_bones, "params": {}}
    }
    
    # Create and save armature types
    for name, data in armature_types.items():
        try:
            # Clear the scene
            clear_scene()
            
            # Create the armature
            obj = data["func"](**data["params"])
            
            # Save to a .blend file
            filepath = os.path.join(save_dir, f"{name}.blend")
            save_blend_file(filepath, obj)
            
            print(f"Created and saved {name} to {filepath}")
        except Exception as e:
            print(f"Error creating {name}: {e}")
    
    # Create and save a rigged mesh
    try:
        clear_scene()
        armature, mesh = create_simple_rig_on_mesh()
        
        filepath = os.path.join(save_dir, "rigged_mesh.blend")
        
        # Make sure we save the entire scene since we have multiple objects
        # Deselect using direct data manipulation instead of operators
        for obj in bpy.context.selected_objects:
            obj.select_set(False)
            
        # Save the file with both objects
        save_blend_file(filepath)
        print(f"Created and saved rigged_mesh to {filepath}")
    except Exception as e:
        print(f"Error creating rigged_mesh: {e}")
    
    # Create and save an animated armature
    try:
        clear_scene()
        
        # Make sure the animation data exists before saving
        bpy.context.scene.frame_start = 1
        bpy.context.scene.frame_end = 48
        
        armature = create_sample_armature_animation()
        
        # Ensure animation data exists
        if not armature.animation_data:
            armature.animation_data_create()
        
        filepath = os.path.join(save_dir, "animated_armature.blend")
        save_blend_file(filepath)  # Save entire scene with animation
        print(f"Created and saved animated_armature to {filepath}")
    except Exception as e:
        print(f"Error creating animated_armature: {e}")


# Example usage
if __name__ == "__main__":
    # Create and save all armature types
    create_all_armature_types()
    
    # Or create individual armature objects
    # clear_scene()
    # biped = create_biped_armature()
    # save_blend_file("./blend_files/armature_types/my_biped.blend", biped)