# Blender Modular Object Creation Documentation

## Overview

This documentation provides detailed information about a collection of Python modules designed for Blender, each specializing in different object types and operations. These modules can be used independently or combined to create complex 3D assets and scenes programmatically.

Each module follows a consistent pattern:
- A main creation function for each specific object type
- Common utility functions (e.g., `clear_scene()`, `save_blend_file()`)
- An example function that creates samples of all object types in the module

## Table of Contents

1. [mesh_creator.py](#1-mesh_creatorpy) - Create mesh objects
2. [curve_creator.py](#2-curve_creatorpy) - Create curve objects
3. [surface_creator.py](#3-surface_creatorpy) - Create surface objects
4. [meta_creator.py](#4-meta_creatorpy) - Create meta objects
5. [text_creator.py](#5-text_creatorpy) - Create text objects
6. [empty_creator.py](#6-empty_creatorpy) - Create empty objects
7. [collection_creator.py](#7-collection_creatorpy) - Create collections
8. [armature_creator.py](#8-armature_creatorpy) - Create armatures for rigging
9. [import_model.py](#9-import_modelpy) - Import external models

---

## 1. mesh_creator.py

Creates various mesh primitives, allowing for customization of their parameters.

### Functions

#### `clear_scene()`
- **Description**: Removes all objects from the current scene
- **Parameters**: None
- **Returns**: None

#### `create_cube(size=2.0, location=(0, 0, 0))`
- **Description**: Creates a cube mesh object
- **Parameters**:
  - `size`: Size of the cube (float)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created cube object

#### `create_sphere(radius=1.0, segments=32, rings=16, location=(0, 0, 0))`
- **Description**: Creates a UV sphere mesh object
- **Parameters**:
  - `radius`: Radius of the sphere (float)
  - `segments`: Number of segments (longitude) (int)
  - `rings`: Number of rings (latitude) (int)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created sphere object

#### `create_cylinder(radius=1.0, depth=2.0, vertices=32, location=(0, 0, 0))`
- **Description**: Creates a cylinder mesh object
- **Parameters**:
  - `radius`: Radius of the cylinder (float)
  - `depth`: Height of the cylinder (float)
  - `vertices`: Number of vertices around the circumference (int)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created cylinder object

#### `create_cone(radius1=1.0, radius2=0.0, depth=2.0, vertices=32, location=(0, 0, 0))`
- **Description**: Creates a cone mesh object
- **Parameters**:
  - `radius1`: Radius of the base of the cone (float)
  - `radius2`: Radius of the top of the cone (float)
  - `depth`: Height of the cone (float)
  - `vertices`: Number of vertices around the circumference (int)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created cone object

#### `create_torus(major_radius=1.0, minor_radius=0.25, major_segments=48, minor_segments=12, location=(0, 0, 0))`
- **Description**: Creates a torus mesh object
- **Parameters**:
  - `major_radius`: Major radius of the torus (float)
  - `minor_radius`: Minor radius of the torus (float)
  - `major_segments`: Number of segments along the major circle (int)
  - `minor_segments`: Number of segments along the minor circle (int)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created torus object

#### `create_grid(x_subdivisions=10, y_subdivisions=10, size=2.0, location=(0, 0, 0))`
- **Description**: Creates a grid mesh object
- **Parameters**:
  - `x_subdivisions`: Number of subdivisions in the X direction (int)
  - `y_subdivisions`: Number of subdivisions in the Y direction (int)
  - `size`: Size of the grid (float)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created grid object

#### `create_icosphere(radius=1.0, subdivisions=2, location=(0, 0, 0))`
- **Description**: Creates an icosphere mesh object
- **Parameters**:
  - `radius`: Radius of the icosphere (float)
  - `subdivisions`: Number of subdivisions (int)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created icosphere object

#### `create_plane(size=2.0, location=(0, 0, 0))`
- **Description**: Creates a plane mesh object
- **Parameters**:
  - `size`: Size of the plane (float)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created plane object

#### `create_monkey(size=1.0, location=(0, 0, 0))`
- **Description**: Creates a monkey (Suzanne) mesh object
- **Parameters**:
  - `size`: Size of the monkey (float)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created monkey object

#### `save_blend_file(filepath, obj=None)`
- **Description**: Saves the current scene or specific object to a .blend file
- **Parameters**:
  - `filepath`: Path to save the .blend file (string)
  - `obj`: Optional object to save. If None, saves the entire scene
- **Returns**: None

#### `create_all_mesh_primitives(save_dir="./blend_files/mesh_primitives/")`
- **Description**: Creates all primitive mesh objects and saves them as individual .blend files
- **Parameters**:
  - `save_dir`: Directory to save the .blend files (string)
- **Returns**: None

---

## 2. curve_creator.py

Creates various curve objects, allowing for customization of their parameters.

### Functions

#### `clear_scene()`
- **Description**: Removes all objects from the current scene
- **Parameters**: None
- **Returns**: None

#### `create_bezier_curve(points=None, name="BezierCurve", location=(0, 0, 0))`
- **Description**: Creates a Bezier curve with specified points
- **Parameters**:
  - `points`: List of (x, y, z) tuples for curve points. Default creates a simple curve
  - `name`: Name for the curve object (string)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created curve object

#### `create_nurbs_curve(points=None, name="NurbsCurve", location=(0, 0, 0))`
- **Description**: Creates a NURBS curve with specified points
- **Parameters**:
  - `points`: List of (x, y, z) tuples for curve points. Default creates a simple curve
  - `name`: Name for the curve object (string)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created curve object

#### `create_path_curve(points=None, name="PathCurve", location=(0, 0, 0))`
- **Description**: Creates a path curve (specialized NURBS)
- **Parameters**:
  - `points`: List of (x, y, z) tuples for curve points. Default creates a simple path
  - `name`: Name for the curve object (string)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created curve object

#### `create_circle_curve(radius=1.0, vertices=32, name="CircleCurve", location=(0, 0, 0))`
- **Description**: Creates a circular curve
- **Parameters**:
  - `radius`: Radius of the circle (float)
  - `vertices`: Number of vertices/points (int)
  - `name`: Name for the curve object (string)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created curve object

#### `create_spiral_curve(turns=2, height=5.0, radius=1.0, points=64, name="SpiralCurve", location=(0, 0, 0))`
- **Description**: Creates a spiral curve
- **Parameters**:
  - `turns`: Number of full rotations in the spiral (int)
  - `height`: Total height of the spiral (float)
  - `radius`: Maximum radius of the spiral (float)
  - `points`: Number of points in the spiral (int)
  - `name`: Name for the curve object (string)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created curve object

#### `create_helix_curve(turns=2, height=5.0, radius=1.0, points=64, name="HelixCurve", location=(0, 0, 0))`
- **Description**: Creates a helix (coil) curve
- **Parameters**:
  - `turns`: Number of full rotations in the helix (int)
  - `height`: Total height of the helix (float)
  - `radius`: Radius of the helix (float)
  - `points`: Number of points in the helix (int)
  - `name`: Name for the curve object (string)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created curve object

#### `create_text_curve(text="Blender", font_size=1.0, extrude=0.0, name="TextCurve", location=(0, 0, 0))`
- **Description**: Creates a curve from text (converts text to curve)
- **Parameters**:
  - `text`: The text content (string)
  - `font_size`: Size of the font (float)
  - `extrude`: Extrusion depth (float)
  - `name`: Name for the curve object (string)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created curve object

#### `save_blend_file(filepath, obj=None)`
- **Description**: Saves the current scene or specific object to a .blend file
- **Parameters**:
  - `filepath`: Path to save the .blend file (string)
  - `obj`: Optional object to save. If None, saves the entire scene
- **Returns**: None

#### `create_all_curve_types(save_dir="./blend_files/curve_types/")`
- **Description**: Creates all curve types and saves them as individual .blend files
- **Parameters**:
  - `save_dir`: Directory to save the .blend files (string)
- **Returns**: None

---

## 3. surface_creator.py

Creates various surface objects, allowing for customization of their parameters.

### Functions

#### `clear_scene()`
- **Description**: Removes all objects from the current scene
- **Parameters**: None
- **Returns**: None

#### `create_nurbs_surface(size=2.0, u_res=4, v_res=4, name="NurbsSurface", location=(0, 0, 0))`
- **Description**: Creates a NURBS surface
- **Parameters**:
  - `size`: Size of the surface (float)
  - `u_res`: Number of control points in U direction (approximated) (int)
  - `v_res`: Number of control points in V direction (approximated) (int)
  - `name`: Name for the surface object (string)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created surface object

#### `create_nurbs_cylinder(radius=1.0, height=2.0, u_segments=8, v_segments=4, name="NurbsCylinder", location=(0, 0, 0))`
- **Description**: Creates a NURBS cylinder surface
- **Parameters**:
  - `radius`: Radius of the cylinder (float)
  - `height`: Height of the cylinder (float)
  - `u_segments`: Number of segments around the circumference (int)
  - `v_segments`: Number of segments along the height (int)
  - `name`: Name for the surface object (string)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created surface object

#### `create_nurbs_sphere(radius=1.0, u_segments=8, v_segments=8, name="NurbsSphere", location=(0, 0, 0))`
- **Description**: Creates a NURBS sphere surface
- **Parameters**:
  - `radius`: Radius of the sphere (float)
  - `u_segments`: Number of segments around the longitude (int)
  - `v_segments`: Number of segments around the latitude (int)
  - `name`: Name for the surface object (string)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created surface object

#### `create_custom_torus(major_radius=1.5, minor_radius=0.5, u_segments=16, v_segments=8, name="NurbsTorus", location=(0, 0, 0))`
- **Description**: Creates a torus surface by starting with a sphere and manipulating it
- **Parameters**:
  - `major_radius`: Major radius of the torus (float)
  - `minor_radius`: Minor radius of the torus (float)
  - `u_segments`: Number of segments around the major circle (int)
  - `v_segments`: Number of segments around the minor circle (int)
  - `name`: Name for the surface object (string)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created surface object

#### `create_nurbs_ring(radius=1.0, inner_radius=0.7, u_segments=16, rings=1, name="RingSurface", location=(0, 0, 0))`
- **Description**: Creates a ring surface mesh
- **Parameters**:
  - `radius`: Outer radius of the ring (float)
  - `inner_radius`: Inner radius of the ring (float)
  - `u_segments`: Number of segments around the circumference (int)
  - `rings`: Number of subdivisions between inner and outer radius (int)
  - `name`: Name for the surface object (string)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created surface object

#### `create_landscape_surface(width=10.0, height=10.0, x_res=32, y_res=32, height_scale=1.0, noise_scale=1.0, name="Landscape", location=(0, 0, 0))`
- **Description**: Creates a landscape surface mesh with procedural noise
- **Parameters**:
  - `width`: Width of the landscape (float)
  - `height`: Length of the landscape (float)
  - `x_res`: Resolution in X direction (int)
  - `y_res`: Resolution in Y direction (int)
  - `height_scale`: Scale factor for height variation (float)
  - `noise_scale`: Scale of the noise pattern (float)
  - `name`: Name for the landscape object (string)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created landscape object

#### `create_disk_surface(radius=1.0, inner_radius=0.0, sectors=32, rings=8, name="DiskSurface", location=(0, 0, 0))`
- **Description**: Creates a disk surface mesh
- **Parameters**:
  - `radius`: Outer radius of the disk (float)
  - `inner_radius`: Inner radius of the disk (0 for full disk, >0 for ring) (float)
  - `sectors`: Number of sectors (divisions around the circumference) (int)
  - `rings`: Number of rings (divisions between inner and outer radius) (int)
  - `name`: Name for the disk object (string)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created disk object

#### `create_nurbs_patch_4x4(name="NurbsPatch", location=(0, 0, 0))`
- **Description**: Creates a simple 4x4 NURBS patch surface
- **Parameters**:
  - `name`: Name for the surface object (string)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created surface object

#### `save_blend_file(filepath, obj=None)`
- **Description**: Saves the current scene or specific object to a .blend file
- **Parameters**:
  - `filepath`: Path to save the .blend file (string)
  - `obj`: Optional object to save. If None, saves the entire scene
- **Returns**: None

#### `create_all_surface_types(save_dir="./blend_files/surface_types/")`
- **Description**: Creates all surface types and saves them as individual .blend files
- **Parameters**:
  - `save_dir`: Directory to save the .blend files (string)
- **Returns**: None

---

## 4. meta_creator.py

Creates meta objects (also known as metaballs or implicit surfaces).

### Functions

#### `clear_scene()`
- **Description**: Removes all objects from the current scene
- **Parameters**: None
- **Returns**: None

#### `create_meta_ball(radius=1.0, name="MetaBall", location=(0, 0, 0))`
- **Description**: Creates a meta ball object
- **Parameters**:
  - `radius`: Radius of the meta ball (float)
  - `name`: Name for the meta object (string)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created meta object

#### `create_meta_capsule(radius=1.0, size_x=2.0, name="MetaCapsule", location=(0, 0, 0))`
- **Description**: Creates a meta capsule object
- **Parameters**:
  - `radius`: Radius of the meta capsule (float)
  - `size_x`: Length of the capsule (float)
  - `name`: Name for the meta object (string)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created meta object

#### `create_meta_plane(radius=1.0, size_x=2.0, name="MetaPlane", location=(0, 0, 0))`
- **Description**: Creates a meta plane object
- **Parameters**:
  - `radius`: Radius of the meta plane (float)
  - `size_x`: Size of the plane (float)
  - `name`: Name for the meta object (string)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created meta object

#### `create_meta_ellipsoid(radius=1.0, size_x=1.5, size_y=1.0, size_z=1.0, name="MetaEllipsoid", location=(0, 0, 0))`
- **Description**: Creates a meta ellipsoid object
- **Parameters**:
  - `radius`: Base radius of the meta ellipsoid (float)
  - `size_x`: X size of the ellipsoid (float)
  - `size_y`: Y size of the ellipsoid (float)
  - `size_z`: Z size of the ellipsoid (float)
  - `name`: Name for the meta object (string)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created meta object

#### `create_meta_cube(radius=1.0, size=1.5, name="MetaCube", location=(0, 0, 0))`
- **Description**: Creates a meta cube object
- **Parameters**:
  - `radius`: Base radius of the meta cube (float)
  - `size`: Size of the cube (float)
  - `name`: Name for the meta object (string)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created meta object

#### `create_meta_molecule(positions=None, radii=None, name="MetaMolecule", location=(0, 0, 0))`
- **Description**: Creates a molecule-like structure using multiple meta balls
- **Parameters**:
  - `positions`: List of (x, y, z) tuples for positions of each meta ball. If None, uses default positions
  - `radii`: List of radii for each meta ball. If None, uses default radii
  - `name`: Base name for the meta object (string)
  - `location`: (x, y, z) tuple for object's center location
- **Returns**: The created meta object

#### `create_meta_blob(name="MetaBlob", seed=42, num_elements=5, location=(0, 0, 0))`
- **Description**: Creates a random blob using multiple meta balls
- **Parameters**:
  - `name`: Name for the meta object (string)
  - `seed`: Random seed for reproducibility (int)
  - `num_elements`: Number of meta elements to create (int)
  - `location`: (x, y, z) tuple for object's center location
- **Returns**: The created meta object

#### `create_meta_tubes(num_rings=3, balls_per_ring=8, radius=0.5, ring_radius=2.0, name="MetaTubes", location=(0, 0, 0))`
- **Description**: Creates a set of interconnected meta ball tubes
- **Parameters**:
  - `num_rings`: Number of rings of meta balls (int)
  - `balls_per_ring`: Number of meta balls in each ring (int)
  - `radius`: Radius of each meta ball (float)
  - `ring_radius`: Radius of the rings (float)
  - `name`: Name for the meta object (string)
  - `location`: (x, y, z) tuple for object's center location
- **Returns**: The created meta object

#### `create_meta_dna(turns=3, bases_per_turn=10, radius=0.3, helix_radius=1.0, height=6.0, name="MetaDNA", location=(0, 0, 0))`
- **Description**: Creates a DNA-like structure using meta balls
- **Parameters**:
  - `turns`: Number of full turns in the helix (int)
  - `bases_per_turn`: Number of base pairs per turn (int)
  - `radius`: Radius of each meta ball (float)
  - `helix_radius`: Radius of the helix (float)
  - `height`: Total height of the helix (float)
  - `name`: Name for the meta object (string)
  - `location`: (x, y, z) tuple for object's center location
- **Returns**: The created meta object

#### `save_blend_file(filepath, obj=None)`
- **Description**: Saves the current scene or specific object to a .blend file
- **Parameters**:
  - `filepath`: Path to save the .blend file (string)
  - `obj`: Optional object to save. If None, saves the entire scene
- **Returns**: None

#### `create_all_meta_types(save_dir="./blend_files/meta_types/")`
- **Description**: Creates all meta object types and saves them as individual .blend files
- **Parameters**:
  - `save_dir`: Directory to save the .blend files (string)
- **Returns**: None

---

## 5. text_creator.py

Creates text objects with various styles and properties.

### Functions

#### `clear_scene()`
- **Description**: Removes all objects from the current scene
- **Parameters**: None
- **Returns**: None

#### `create_text_object(text="Blender", name="TextObject", location=(0, 0, 0), size=1.0, extrude=0.0, bevel_depth=0.0, bevel_resolution=0)`
- **Description**: Creates a basic text object
- **Parameters**:
  - `text`: The text content (string)
  - `name`: Name for the text object (string)
  - `location`: (x, y, z) tuple for object location
  - `size`: Font size (float)
  - `extrude`: Extrusion depth (float)
  - `bevel_depth`: Bevel depth (for rounded edges) (float)
  - `bevel_resolution`: Bevel resolution (subdivisions) (int)
- **Returns**: The created text object

#### `create_3d_text(text="3D", name="3DText", location=(0, 0, 0), size=1.0, extrude=0.25, bevel_depth=0.05, bevel_resolution=3)`
- **Description**: Creates a 3D text object with extrusion and beveling
- **Parameters**:
  - `text`: The text content (string)
  - `name`: Name for the text object (string)
  - `location`: (x, y, z) tuple for object location
  - `size`: Font size (float)
  - `extrude`: Extrusion depth (float)
  - `bevel_depth`: Bevel depth (for rounded edges) (float)
  - `bevel_resolution`: Bevel resolution (subdivisions) (int)
- **Returns**: The created text object

#### `set_text_alignment(text_obj, align_x='CENTER', align_y='CENTER')`
- **Description**: Sets the text alignment
- **Parameters**:
  - `text_obj`: The text object to modify
  - `align_x`: Horizontal alignment ('LEFT', 'CENTER', 'RIGHT', 'JUSTIFY', 'FLUSH') (string)
  - `align_y`: Vertical alignment ('TOP', 'CENTER', 'BOTTOM', 'TOP_BASELINE', 'BOTTOM_BASELINE') (string)
- **Returns**: None

#### `set_text_font(text_obj, font_path=None)`
- **Description**: Sets the font for a text object
- **Parameters**:
  - `text_obj`: The text object to modify
  - `font_path`: Path to a font file. If None, uses the default font (string)
- **Returns**: True if successful, False otherwise

#### `create_text_on_curve(text="Text on Curve", curve_type='CIRCLE', name="CurvedText", location=(0, 0, 0), size=1.0, extrude=0.0, bevel_depth=0.0, curve_radius=2.0)`
- **Description**: Creates text that follows a curve path
- **Parameters**:
  - `text`: The text content (string)
  - `curve_type`: Type of curve ('CIRCLE', 'LINE', 'WAVE') (string)
  - `name`: Name for the text object (string)
  - `location`: (x, y, z) tuple for object location
  - `size`: Font size (float)
  - `extrude`: Extrusion depth (float)
  - `bevel_depth`: Bevel depth (for rounded edges) (float)
  - `curve_radius`: Radius of the curve (for circle) (float)
- **Returns**: Tuple of (text_object, curve_object)

#### `create_text_with_materials(text="Colorful", name="MaterialText", location=(0, 0, 0), size=1.0, extrude=0.2, color=(1, 0, 0, 1))`
- **Description**: Creates a text object with a material applied
- **Parameters**:
  - `text`: The text content (string)
  - `name`: Name for the text object (string)
  - `location`: (x, y, z) tuple for object location
  - `size`: Font size (float)
  - `extrude`: Extrusion depth (float)
  - `color`: (R, G, B, A) tuple for the material color
- **Returns**: The created text object

#### `create_multi_line_text(lines=None, name="MultiLineText", location=(0, 0, 0), size=1.0, line_spacing=1.5)`
- **Description**: Creates a multi-line text object
- **Parameters**:
  - `lines`: List of text lines. If None, uses default text (list of strings)
  - `name`: Name for the text object (string)
  - `location`: (x, y, z) tuple for object location
  - `size`: Font size (float)
  - `line_spacing`: Vertical spacing factor between lines (float)
- **Returns**: The created text object

#### `create_text_to_mesh(text="Mesh", name="TextMesh", location=(0, 0, 0), size=1.0, extrude=0.2, bevel_depth=0.05, shading='SMOOTH', convert=True)`
- **Description**: Creates a text object and optionally converts it to a mesh
- **Parameters**:
  - `text`: The text content (string)
  - `name`: Name for the text/mesh object (string)
  - `location`: (x, y, z) tuple for object location
  - `size`: Font size (float)
  - `extrude`: Extrusion depth (float)
  - `bevel_depth`: Bevel depth (for rounded edges) (float)
  - `shading`: Shading type ('FLAT', 'SMOOTH') (string)
  - `convert`: Whether to convert to mesh (True) or leave as text (False) (bool)
- **Returns**: The created object (text or mesh)

#### `create_text_with_animation(text="Animated", name="AnimatedText", location=(0, 0, 0), size=1.0, extrude=0.2, anim_type='ROTATE', frames=48)`
- **Description**: Creates a text object with a simple animation
- **Parameters**:
  - `text`: The text content (string)
  - `name`: Name for the text object (string)
  - `location`: (x, y, z) tuple for object location
  - `size`: Font size (float)
  - `extrude`: Extrusion depth (float)
  - `anim_type`: Animation type ('ROTATE', 'SCALE', 'FADE') (string)
  - `frames`: Number of frames for the animation cycle (int)
- **Returns**: The created text object

#### `create_extruded_logo_text(text="LOGO", name="LogoText", location=(0, 0, 0), size=1.0, extrude=0.5, bevel_depth=0.05, bevel_resolution=4, material_color=(0.2, 0.6, 1.0, 1.0))`
- **Description**: Creates an extruded text object suitable for a logo
- **Parameters**:
  - `text`: The text content (string)
  - `name`: Name for the text object (string)
  - `location`: (x, y, z) tuple for object location
  - `size`: Font size (float)
  - `extrude`: Extrusion depth (float)
  - `bevel_depth`: Bevel depth (for rounded edges) (float)
  - `bevel_resolution`: Bevel resolution (subdivisions) (int)
  - `material_color`: (R, G, B, A) tuple for the material color
- **Returns**: The created text object

#### `create_neon_text(text="NEON", name="NeonText", location=(0, 0, 0), size=1.0, extrude=0.1, bevel_depth=0.03, bevel_resolution=3, color=(0, 1, 0.8, 1))`
- **Description**: Creates a text object with a neon glow effect
- **Parameters**:
  - `text`: The text content (string)
  - `name`: Name for the text object (string)
  - `location`: (x, y, z) tuple for object location
  - `size`: Font size (float)
  - `extrude`: Extrusion depth (float)
  - `bevel_depth`: Bevel depth (for rounded edges) (float)
  - `bevel_resolution`: Bevel resolution (subdivisions) (int)
  - `color`: (R, G, B, A) tuple for the neon color
- **Returns**: The created text object

#### `save_blend_file(filepath, obj=None)`
- **Description**: Saves the current scene or specific object to a .blend file
- **Parameters**:
  - `filepath`: Path to save the .blend file (string)
  - `obj`: Optional object to save. If None, saves the entire scene
- **Returns**: None

#### `create_all_text_types(save_dir="./blend_files/text_types/")`
- **Description**: Creates all text object types and saves them as individual .blend files
- **Parameters**:
  - `save_dir`: Directory to save the .blend files (string)
- **Returns**: None

---

## 6. empty_creator.py

Creates empty objects used for organization, constraints, and control.

### Functions

#### `clear_scene()`
- **Description**: Removes all objects from the current scene
- **Parameters**: None
- **Returns**: None

#### `create_empty_plain(name="EmptyPlain", location=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1))`
- **Description**: Creates a plain empty object
- **Parameters**:
  - `name`: Name for the empty object (string)
  - `location`: (x, y, z) tuple for object location
  - `rotation`: (x, y, z) tuple for object rotation in radians
  - `scale`: (x, y, z) tuple for object scale
- **Returns**: The created empty object

#### `create_empty_arrows(name="EmptyArrows", location=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1))`
- **Description**: Creates an empty object with arrows display
- **Parameters**:
  - `name`: Name for the empty object (string)
  - `location`: (x, y, z) tuple for object location
  - `rotation`: (x, y, z) tuple for object rotation in radians
  - `scale`: (x, y, z) tuple for object scale
- **Returns**: The created empty object

#### `create_empty_sphere(name="EmptySphere", location=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1), radius=1.0)`
- **Description**: Creates an empty object with sphere display
- **Parameters**:
  - `name`: Name for the empty object (string)
  - `location`: (x, y, z) tuple for object location
  - `rotation`: (x, y, z) tuple for object rotation in radians
  - `scale`: (x, y, z) tuple for object scale
  - `radius`: Radius of the sphere display (float)
- **Returns**: The created empty object

#### `create_empty_cube(name="EmptyCube", location=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1), size=1.0)`
- **Description**: Creates an empty object with cube display
- **Parameters**:
  - `name`: Name for the empty object (string)
  - `location`: (x, y, z) tuple for object location
  - `rotation`: (x, y, z) tuple for object rotation in radians
  - `scale`: (x, y, z) tuple for object scale
  - `size`: Size of the cube display (float)
- **Returns**: The created empty object

#### `create_empty_circle(name="EmptyCircle", location=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1), radius=1.0)`
- **Description**: Creates an empty object with circle display
- **Parameters**:
  - `name`: Name for the empty object (string)
  - `location`: (x, y, z) tuple for object location
  - `rotation`: (x, y, z) tuple for object rotation in radians
  - `scale`: (x, y, z) tuple for object scale
  - `radius`: Radius of the circle display (float)
- **Returns**: The created empty object

#### `create_empty_cone(name="EmptyCone", location=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1), radius=1.0)`
- **Description**: Creates an empty object with cone display
- **Parameters**:
  - `name`: Name for the empty object (string)
  - `location`: (x, y, z) tuple for object location
  - `rotation`: (x, y, z) tuple for object rotation in radians
  - `scale`: (x, y, z) tuple for object scale
  - `radius`: Radius of the cone display (float)
- **Returns**: The created empty object

#### `create_empty_image(name="EmptyImage", location=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1), image_path=None, size=5.0)`
- **Description**: Creates an empty object with an image display
- **Parameters**:
  - `name`: Name for the empty object (string)
  - `location`: (x, y, z) tuple for object location
  - `rotation`: (x, y, z) tuple for object rotation in radians
  - `scale`: (x, y, z) tuple for object scale
  - `image_path`: Path to the image file. If None, no image is used (string)
  - `size`: Size of the image display (float)
- **Returns**: The created empty object

#### `create_empty_single_arrow(name="EmptySingleArrow", location=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1), size=1.0)`
- **Description**: Creates an empty object with single arrow display
- **Parameters**:
  - `name`: Name for the empty object (string)
  - `location`: (x, y, z) tuple for object location
  - `rotation`: (x, y, z) tuple for object rotation in radians
  - `scale`: (x, y, z) tuple for object scale
  - `size`: Size of the arrow display (float)
- **Returns**: The created empty object

#### `create_empty_with_constraint(name="EmptyConstraint", empty_type='PLAIN_AXES', location=(0, 0, 0), constraint_type='COPY_LOCATION', target=None, influence=1.0)`
- **Description**: Creates an empty object with a constraint
- **Parameters**:
  - `name`: Name for the empty object (string)
  - `empty_type`: Type of empty ('PLAIN_AXES', 'ARROWS', 'SPHERE', 'CUBE', etc.) (string)
  - `location`: (x, y, z) tuple for object location
  - `constraint_type`: Type of constraint to add ('COPY_LOCATION', 'COPY_ROTATION', 'COPY_SCALE', etc.) (string)
  - `target`: Target object for the constraint. If None, no constraint is added
  - `influence`: Influence factor for the constraint (0.0 to 1.0) (float)
- **Returns**: The created empty object

#### `create_empty_parent(name="EmptyParent", children=None, location=(0, 0, 0), empty_type='PLAIN_AXES')`
- **Description**: Creates an empty object and makes it the parent of specified objects
- **Parameters**:
  - `name`: Name for the empty object (string)
  - `children`: List of objects to parent to the empty. If None, no parenting is done
  - `location`: (x, y, z) tuple for object location
  - `empty_type`: Type of empty ('PLAIN_AXES', 'ARROWS', 'SPHERE', 'CUBE', etc.) (string)
- **Returns**: The created empty object

#### `create_empty_hierarchy(name_prefix="Level", levels=3, branch_factor=2, base_location=(0, 0, 0), level_spacing=1.0, empty_type='PLAIN_AXES')`
- **Description**: Creates a hierarchy of empty objects
- **Parameters**:
  - `name_prefix`: Prefix for naming the empty objects (string)
  - `levels`: Number of hierarchy levels (int)
  - `branch_factor`: Number of children per parent (int)
  - `base_location`: (x, y, z) tuple for root location
  - `level_spacing`: Vertical spacing between hierarchy levels (float)
  - `empty_type`: Type of empty ('PLAIN_AXES', 'ARROWS', 'SPHERE', 'CUBE', etc.) (string)
- **Returns**: The root empty object

#### `create_empty_track(name="TrackEmpty", target=None, location=(0, 0, 0), empty_type='PLAIN_AXES')`
- **Description**: Creates an empty object with a Track To constraint
- **Parameters**:
  - `name`: Name for the empty object (string)
  - `target`: Target object to track. If None, no tracking is set up
  - `location`: (x, y, z) tuple for object location
  - `empty_type`: Type of empty ('PLAIN_AXES', 'ARROWS', 'SPHERE', 'CUBE', etc.) (string)
- **Returns**: The created empty object

#### `create_empty_path_animation(name="PathEmpty", path_object=None, location=(0, 0, 0), empty_type='PLAIN_AXES', frames=48)`
- **Description**: Creates an empty object that follows a path with animation
- **Parameters**:
  - `name`: Name for the empty object (string)
  - `path_object`: Curve object to follow. If None, creates a simple path
  - `location`: (x, y, z) tuple for object location
  - `empty_type`: Type of empty ('PLAIN_AXES', 'ARROWS', 'SPHERE', 'CUBE', etc.) (string)
  - `frames`: Number of frames for the animation (int)
- **Returns**: Tuple of (empty_object, path_object)

#### `save_blend_file(filepath, obj=None)`
- **Description**: Saves the current scene or specific object to a .blend file
- **Parameters**:
  - `filepath`: Path to save the .blend file (string)
  - `obj`: Optional object to save. If None, saves the entire scene
- **Returns**: None

#### `create_all_empty_types(save_dir="./blend_files/empty_types/")`
- **Description**: Creates all empty object types and saves them as individual .blend files
- **Parameters**:
  - `save_dir`: Directory to save the .blend files (string)
- **Returns**: None

---

## 7. collection_creator.py

Creates collections for organizing objects in the scene.

### Functions

#### `clear_scene()`
- **Description**: Removes all objects from the current scene
- **Parameters**: None
- **Returns**: None

#### `create_collection(name="NewCollection", parent_collection=None)`
- **Description**: Creates a new collection
- **Parameters**:
  - `name`: Name for the collection (string)
  - `parent_collection`: Parent collection. If None, adds to the scene collection
- **Returns**: The created collection

#### `add_object_to_collection(obj, collection)`
- **Description**: Adds an object to a collection
- **Parameters**:
  - `obj`: The object to add
  - `collection`: The collection to add to
- **Returns**: True if successful, False otherwise

#### `remove_object_from_collection(obj, collection)`
- **Description**: Removes an object from a collection
- **Parameters**:
  - `obj`: The object to remove
  - `collection`: The collection to remove from
- **Returns**: True if successful, False otherwise

#### `create_nested_collections(names, parent_collection=None)`
- **Description**: Creates a hierarchy of nested collections
- **Parameters**:
  - `names`: List of collection names, from parent to child (list of strings)
  - `parent_collection`: Parent collection for the first in the list. If None, uses scene collection
- **Returns**: The last created collection

#### `create_collection_instance(collection, name=None, location=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1))`
- **Description**: Creates an instance of a collection
- **Parameters**:
  - `collection`: The collection to instance
  - `name`: Name for the instance. If None, uses collection name + "Instance" (string)
  - `location`: (x, y, z) tuple for instance location
  - `rotation`: (x, y, z) tuple for instance rotation in radians
  - `scale`: (x, y, z) tuple for instance scale
- **Returns**: The created collection instance object

#### `create_collection_with_objects(name="ObjectCollection", objects=None)`
- **Description**: Creates a collection and adds objects to it
- **Parameters**:
  - `name`: Name for the collection (string)
  - `objects`: List of objects to add. If None, creates default objects
- **Returns**: The created collection

#### `organize_by_type(prefix="Type")`
- **Description**: Organizes existing objects into collections based on their type
- **Parameters**:
  - `prefix`: Prefix for collection names (string)
- **Returns**: Dictionary mapping object types to their collections

#### `create_layered_scene(base_name="Layer", layer_count=3)`
- **Description**: Creates a scene with multiple collection layers
- **Parameters**:
  - `base_name`: Base name for collections (string)
  - `layer_count`: Number of layers to create (int)
- **Returns**: List of created collections

#### `create_collection_instance_grid(collection, rows=3, columns=3, spacing=3.0, location=(0, 0, 0), variation=True)`
- **Description**: Creates a grid of collection instances
- **Parameters**:
  - `collection`: The collection to instance
  - `rows`: Number of rows in the grid (int)
  - `columns`: Number of columns in the grid (int)
  - `spacing`: Spacing between instances (float)
  - `location`: (x, y, z) tuple for the center of the grid
  - `variation`: If True, adds variation to rotation and scale (bool)
- **Returns**: List of created instance objects

#### `create_modular_building_collections()`
- **Description**: Creates a set of collections for modular building components
- **Parameters**: None
- **Returns**: Dictionary of collections categorized by building part

#### `set_collection_visibility(collection, visible=True)`
- **Description**: Sets the visibility of a collection in the viewport and render
- **Parameters**:
  - `collection`: The collection to modify
  - `visible`: Whether the collection should be visible (bool)
- **Returns**: None

#### `create_view_layers_with_collections(base_name="ViewLayer", collection_count=3)`
- **Description**: Creates multiple view layers with different collections visible
- **Parameters**:
  - `base_name`: Base name for view layers (string)
  - `collection_count`: Number of collections/layers to create (int)
- **Returns**: Dictionary mapping view layer names to their layer objects

#### `save_blend_file(filepath, obj=None)`
- **Description**: Saves the current scene or specific object to a .blend file
- **Parameters**:
  - `filepath`: Path to save the .blend file (string)
  - `obj`: Optional object to save. If None, saves the entire scene
- **Returns**: None

#### `create_example_collection_setups(save_dir="./blend_files/collection_examples/")`
- **Description**: Creates example collection setups and saves them
- **Parameters**:
  - `save_dir`: Directory to save the .blend files (string)
- **Returns**: None

---

## 8. armature_creator.py

Creates armatures for rigging and animation.

### Functions

#### `clear_scene()`
- **Description**: Removes all objects from the current scene
- **Parameters**: None
- **Returns**: None

#### `create_single_bone_armature(name="SimpleArmature", bone_name="Bone", location=(0, 0, 0), bone_length=1.0)`
- **Description**: Creates an armature with a single bone
- **Parameters**:
  - `name`: Name for the armature object (string)
  - `bone_name`: Name for the bone (string)
  - `location`: (x, y, z) tuple for armature location
  - `bone_length`: Length of the bone (float)
- **Returns**: The created armature object

#### `create_multi_bone_chain(name="ChainArmature", num_bones=3, bone_length=0.5, location=(0, 0, 0), bone_direction=(0, 0, 1))`
- **Description**: Creates an armature with a chain of connected bones
- **Parameters**:
  - `name`: Name for the armature object (string)
  - `num_bones`: Number of bones in the chain (int)
  - `bone_length`: Length of each bone (float)
  - `location`: (x, y, z) tuple for armature location
  - `bone_direction`: (x, y, z) tuple for bone direction
- **Returns**: The created armature object

#### `create_biped_armature(name="BipedArmature", height=2.0, location=(0, 0, 0))`
- **Description**: Creates a basic biped (humanoid) armature
- **Parameters**:
  - `name`: Name for the armature object (string)
  - `height`: Height of the biped (float)
  - `location`: (x, y, z) tuple for armature location
- **Returns**: The created armature object

#### `create_quadruped_armature(name="QuadrupedArmature", length=2.0, height=1.0, location=(0, 0, 0))`
- **Description**: Creates a basic quadruped (four-legged animal) armature
- **Parameters**:
  - `name`: Name for the armature object (string)
  - `length`: Length of the quadruped (float)
  - `height`: Height of the quadruped (float)
  - `location`: (x, y, z) tuple for armature location
- **Returns**: The created armature object

#### `create_armature_with_constraints(name="ConstraintedArmature", location=(0, 0, 0))`
- **Description**: Creates an armature with bone constraints
- **Parameters**:
  - `name`: Name for the armature object (string)
  - `location`: (x, y, z) tuple for armature location
- **Returns**: The created armature object

#### `create_armature_with_control_bones(name="ControlArmature", location=(0, 0, 0))`
- **Description**: Creates an armature with special control bones
- **Parameters**:
  - `name`: Name for the armature object (string)
  - `location`: (x, y, z) tuple for armature location
- **Returns**: The created armature object

#### `create_simple_rig_on_mesh(armature_name="MeshRig", mesh=None, location=(0, 0, 0))`
- **Description**: Creates a simple armature and attaches it to a mesh
- **Parameters**:
  - `armature_name`: Name for the armature object (string)
  - `mesh`: The mesh object to rig. If None, creates a simple cylinder
  - `location`: (x, y, z) tuple for armature and mesh location if mesh is created
- **Returns**: Tuple of (armature_object, mesh_object)

#### `create_sample_armature_animation(armature=None, name="ArmatureAnimation", location=(0, 0, 0), num_frames=48)`
- **Description**: Creates a simple animation for an armature
- **Parameters**:
  - `armature`: The armature to animate. If None, creates a simple chain armature
  - `name`: Name for the armature if created (string)
  - `location`: (x, y, z) tuple for armature location if created
  - `num_frames`: Number of frames for the animation (int)
- **Returns**: The armature object

#### `set_armature_display_options(armature, show_names=True, show_axes=False, show_in_front=True)`
- **Description**: Sets display options for an armature
- **Parameters**:
  - `armature`: The armature object to modify
  - `show_names`: Whether to show bone names (bool)
  - `show_axes`: Whether to show bone axes (bool)
  - `show_in_front`: Whether to show bones in front of other objects (bool)
- **Returns**: The modified armature object

#### `save_blend_file(filepath, obj=None)`
- **Description**: Saves the current scene or specific object to a .blend file
- **Parameters**:
  - `filepath`: Path to save the .blend file (string)
  - `obj`: Optional object to save. If None, saves the entire scene
- **Returns**: None

#### `create_all_armature_types(save_dir="./blend_files/armature_types/")`
- **Description**: Creates all armature types and saves them as individual .blend files
- **Parameters**:
  - `save_dir`: Directory to save the .blend files (string)
- **Returns**: None

---

## 9. import_model.py

Imports external 3D models into Blender.

### Functions

#### `clear_scene()`
- **Description**: Removes all objects from the current scene
- **Parameters**: None
- **Returns**: None

#### `import_obj(filepath, location=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1))`
- **Description**: Imports an OBJ file
- **Parameters**:
  - `filepath`: Path to the OBJ file (string)
  - `location`: (x, y, z) tuple for object location
  - `rotation`: (x, y, z) tuple for object rotation in radians
  - `scale`: (x, y, z) tuple for object scale
- **Returns**: List of imported objects

#### `import_fbx(filepath, location=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1), import_animations=True)`
- **Description**: Imports an FBX file
- **Parameters**:
  - `filepath`: Path to the FBX file (string)
  - `location`: (x, y, z) tuple for object location
  - `rotation`: (x, y, z) tuple for object rotation in radians
  - `scale`: (x, y, z) tuple for object scale
  - `import_animations`: Whether to import animations (bool)
- **Returns**: List of imported objects

#### `import_gltf(filepath, location=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1))`
- **Description**: Imports a glTF file
- **Parameters**:
  - `filepath`: Path to the glTF file (string)
  - `location`: (x, y, z) tuple for object location
  - `rotation`: (x, y, z) tuple for object rotation in radians
  - `scale`: (x, y, z) tuple for object scale
- **Returns**: List of imported objects

#### `import_stl(filepath, location=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1))`
- **Description**: Imports an STL file
- **Parameters**:
  - `filepath`: Path to the STL file (string)
  - `location`: (x, y, z) tuple for object location
  - `rotation`: (x, y, z) tuple for object rotation in radians
  - `scale`: (x, y, z) tuple for object scale
- **Returns**: The imported object

#### `import_ply(filepath, location=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1))`
- **Description**: Imports a PLY file
- **Parameters**:
  - `filepath`: Path to the PLY file (string)
  - `location`: (x, y, z) tuple for object location
  - `rotation`: (x, y, z) tuple for object rotation in radians
  - `scale`: (x, y, z) tuple for object scale
- **Returns**: The imported object

#### `import_dae(filepath, location=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1))`
- **Description**: Imports a Collada (DAE) file
- **Parameters**:
  - `filepath`: Path to the DAE file (string)
  - `location`: (x, y, z) tuple for object location
  - `rotation`: (x, y, z) tuple for object rotation in radians
  - `scale`: (x, y, z) tuple for object scale
- **Returns**: List of imported objects

#### `import_abc(filepath, location=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1))`
- **Description**: Imports an Alembic (ABC) file
- **Parameters**:
  - `filepath`: Path to the ABC file (string)
  - `location`: (x, y, z) tuple for object location
  - `rotation`: (x, y, z) tuple for object rotation in radians
  - `scale`: (x, y, z) tuple for object scale
- **Returns**: List of imported objects

#### `import_usd(filepath, location=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1))`
- **Description**: Imports a Universal Scene Description (USD) file
- **Parameters**:
  - `filepath`: Path to the USD file (string)
  - `location`: (x, y, z) tuple for object location
  - `rotation`: (x, y, z) tuple for object rotation in radians
  - `scale`: (x, y, z) tuple for object scale
- **Returns**: List of imported objects

#### `import_svg(filepath, location=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1), extrude=0.0, bevel_depth=0.0)`
- **Description**: Imports an SVG file as curves
- **Parameters**:
  - `filepath`: Path to the SVG file (string)
  - `location`: (x, y, z) tuple for object location
  - `rotation`: (x, y, z) tuple for object rotation in radians
  - `scale`: (x, y, z) tuple for object scale
  - `extrude`: Extrusion amount for the curves (float)
  - `bevel_depth`: Bevel depth for the curves (float)
- **Returns**: List of imported objects

#### `import_blend(filepath, data_types=None, link=False, relative_path=True)`
- **Description**: Imports objects from another .blend file
- **Parameters**:
  - `filepath`: Path to the .blend file (string)
  - `data_types`: List of data types to import ('OBJECT', 'MATERIAL', etc.). If None, imports objects (list of strings)
  - `link`: Whether to link (True) or append (False) the data (bool)
  - `relative_path`: Whether to use relative paths (bool)
- **Returns**: List of imported objects

#### `organize_imported_objects(objects, collection_name="Imported")`
- **Description**: Organizes imported objects into a collection
- **Parameters**:
  - `objects`: List of objects to organize
  - `collection_name`: Name for the collection (string)
- **Returns**: The created collection

#### `import_model_by_extension(filepath, location=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1))`
- **Description**: Imports a model based on its file extension
- **Parameters**:
  - `filepath`: Path to the model file (string)
  - `location`: (x, y, z) tuple for object location
  - `rotation`: (x, y, z) tuple for object rotation in radians
  - `scale`: (x, y, z) tuple for object scale
- **Returns**: List of imported objects

#### `save_blend_file(filepath, obj=None)`
- **Description**: Saves the current scene or specific object to a .blend file
- **Parameters**:
  - `filepath`: Path to save the .blend file (string)
  - `obj`: Optional object to save. If None, saves the entire scene
- **Returns**: None

#### `import_model_examples(models_dir="./example_models", save_dir="./blend_files/imported_models/")`
- **Description**: Imports example models and saves them
- **Parameters**:
  - `models_dir`: Directory with example model files (string)
  - `save_dir`: Directory to save the .blend files (string)
- **Returns**: None

---

## Combining Modules - Example Usage

Below are examples of how to combine the modules to create more complex assets:

### Example 1: Creating a Rigged Character

```python
import bpy
from mesh_creator import create_cylinder, create_sphere
from armature_creator import create_biped_armature, create_simple_rig_on_mesh
from collection_creator import create_collection, add_object_to_collection

# Clear scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Create a collection for the character
character_collection = create_collection("Character")

# Create a simple body from cylinders and spheres
torso = create_cylinder(radius=0.5, depth=1.5, location=(0, 0, 1.0))
head = create_sphere(radius=0.4, location=(0, 0, 2.0))
torso.name = "Torso"
head.name = "Head"

# Add objects to the collection
add_object_to_collection(torso, character_collection)
add_object_to_collection(head, character_collection)

# Create a biped armature
armature = create_biped_armature(height=2.0, location=(0, 0, 0))

# Rig the body parts
# (In a real example, you would join the mesh parts first or parent them individually)
body_parts = [torso, head]
for part in body_parts:
    part.select_set(True)
armature.select_set(True)
bpy.context.view_layer.objects.active = armature
bpy.ops.object.parent_set(type='ARMATURE_AUTO')

# Save the rigged character
bpy.ops.wm.save_as_mainfile(filepath="./rigged_character.blend")
```

### Example 2: Creating a Modular Building with Collections

```python
import bpy
from mesh_creator import create_cube, create_cone
from collection_creator import create_collection, create_collection_instance, add_object_to_collection
from empty_creator import create_empty_parent

# Clear scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Create building module collections
wall_collection = create_collection("Walls")
roof_collection = create_collection("Roofs")

# Create basic wall and add to collection
wall = create_cube(size=2.0, location=(0, 0, 1))
wall.scale = (1, 0.1, 1)
wall.name = "BasicWall"
add_object_to_collection(wall, wall_collection)

# Create basic roof and add to collection
roof = create_cone(radius1=1.5, depth=1.0, location=(0, 0, 2))
roof.name = "BasicRoof"
add_object_to_collection(roof, roof_collection)

# Create instances of walls to form a square building
wall_instances = []
positions = [(0, -2, 0), (0, 2, 0), (-2, 0, 0), (2, 0, 0)]
rotations = [(0, 0, 0), (0, 0, 0), (0, 0, math.pi/2), (0, 0, math.pi/2)]

for i, (pos, rot) in enumerate(zip(positions, rotations)):
    instance = create_collection_instance(
        wall_collection, 
        name=f"Wall_{i+1}", 
        location=pos, 
        rotation=rot
    )
    wall_instances.append(instance)

# Create a roof instance on top
roof_instance = create_collection_instance(
    roof_collection,
    name="Building_Roof",
    location=(0, 0, 2)
)

# Group everything under a parent empty
building_parts = wall_# Blender Modular Object Creation Documentation

## Overview

This documentation provides detailed information about a collection of Python modules designed for Blender, each specializing in different object types and operations. These modules can be used independently or combined to create complex 3D assets and scenes programmatically.

Each module follows a consistent pattern:
- A main creation function for each specific object type
- Common utility functions (e.g., `clear_scene()`, `save_blend_file()`)
- An example function that creates samples of all object types in the module

## Table of Contents

1. [mesh_creator.py](#1-mesh_creatorpy) - Create mesh objects
2. [curve_creator.py](#2-curve_creatorpy) - Create curve objects
3. [surface_creator.py](#3-surface_creatorpy) - Create surface objects
4. [meta_creator.py](#4-meta_creatorpy) - Create meta objects
5. [text_creator.py](#5-text_creatorpy) - Create text objects
6. [empty_creator.py](#6-empty_creatorpy) - Create empty objects
7. [collection_creator.py](#7-collection_creatorpy) - Create collections
8. [armature_creator.py](#8-armature_creatorpy) - Create armatures for rigging
9. [import_model.py](#9-import_modelpy) - Import external models

---

## 1. mesh_creator.py

Creates various mesh primitives, allowing for customization of their parameters.

### Functions

#### `clear_scene()`
- **Description**: Removes all objects from the current scene
- **Parameters**: None
- **Returns**: None

#### `create_cube(size=2.0, location=(0, 0, 0))`
- **Description**: Creates a cube mesh object
- **Parameters**:
  - `size`: Size of the cube (float)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created cube object

#### `create_sphere(radius=1.0, segments=32, rings=16, location=(0, 0, 0))`
- **Description**: Creates a UV sphere mesh object
- **Parameters**:
  - `radius`: Radius of the sphere (float)
  - `segments`: Number of segments (longitude) (int)
  - `rings`: Number of rings (latitude) (int)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created sphere object

#### `create_cylinder(radius=1.0, depth=2.0, vertices=32, location=(0, 0, 0))`
- **Description**: Creates a cylinder mesh object
- **Parameters**:
  - `radius`: Radius of the cylinder (float)
  - `depth`: Height of the cylinder (float)
  - `vertices`: Number of vertices around the circumference (int)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created cylinder object

#### `create_cone(radius1=1.0, radius2=0.0, depth=2.0, vertices=32, location=(0, 0, 0))`
- **Description**: Creates a cone mesh object
- **Parameters**:
  - `radius1`: Radius of the base of the cone (float)
  - `radius2`: Radius of the top of the cone (float)
  - `depth`: Height of the cone (float)
  - `vertices`: Number of vertices around the circumference (int)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created cone object

#### `create_torus(major_radius=1.0, minor_radius=0.25, major_segments=48, minor_segments=12, location=(0, 0, 0))`
- **Description**: Creates a torus mesh object
- **Parameters**:
  - `major_radius`: Major radius of the torus (float)
  - `minor_radius`: Minor radius of the torus (float)
  - `major_segments`: Number of segments along the major circle (int)
  - `minor_segments`: Number of segments along the minor circle (int)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created torus object

#### `create_grid(x_subdivisions=10, y_subdivisions=10, size=2.0, location=(0, 0, 0))`
- **Description**: Creates a grid mesh object
- **Parameters**:
  - `x_subdivisions`: Number of subdivisions in the X direction (int)
  - `y_subdivisions`: Number of subdivisions in the Y direction (int)
  - `size`: Size of the grid (float)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created grid object

#### `create_icosphere(radius=1.0, subdivisions=2, location=(0, 0, 0))`
- **Description**: Creates an icosphere mesh object
- **Parameters**:
  - `radius`: Radius of the icosphere (float)
  - `subdivisions`: Number of subdivisions (int)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created icosphere object

#### `create_plane(size=2.0, location=(0, 0, 0))`
- **Description**: Creates a plane mesh object
- **Parameters**:
  - `size`: Size of the plane (float)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created plane object

#### `create_monkey(size=1.0, location=(0, 0, 0))`
- **Description**: Creates a monkey (Suzanne) mesh object
- **Parameters**:
  - `size`: Size of the monkey (float)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created monkey object

#### `save_blend_file(filepath, obj=None)`
- **Description**: Saves the current scene or specific object to a .blend file
- **Parameters**:
  - `filepath`: Path to save the .blend file (string)
  - `obj`: Optional object to save. If None, saves the entire scene
- **Returns**: None

#### `create_all_mesh_primitives(save_dir="./blend_files/mesh_primitives/")`
- **Description**: Creates all primitive mesh objects and saves them as individual .blend files
- **Parameters**:
  - `save_dir`: Directory to save the .blend files (string)
- **Returns**: None

---

## 2. curve_creator.py

Creates various curve objects, allowing for customization of their parameters.

### Functions

#### `clear_scene()`
- **Description**: Removes all objects from the current scene
- **Parameters**: None
- **Returns**: None

#### `create_bezier_curve(points=None, name="BezierCurve", location=(0, 0, 0))`
- **Description**: Creates a Bezier curve with specified points
- **Parameters**:
  - `points`: List of (x, y, z) tuples for curve points. Default creates a simple curve
  - `name`: Name for the curve object (string)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created curve object

#### `create_nurbs_curve(points=None, name="NurbsCurve", location=(0, 0, 0))`
- **Description**: Creates a NURBS curve with specified points
- **Parameters**:
  - `points`: List of (x, y, z) tuples for curve points. Default creates a simple curve
  - `name`: Name for the curve object (string)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created curve object

#### `create_path_curve(points=None, name="PathCurve", location=(0, 0, 0))`
- **Description**: Creates a path curve (specialized NURBS)
- **Parameters**:
  - `points`: List of (x, y, z) tuples for curve points. Default creates a simple path
  - `name`: Name for the curve object (string)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created curve object

#### `create_circle_curve(radius=1.0, vertices=32, name="CircleCurve", location=(0, 0, 0))`
- **Description**: Creates a circular curve
- **Parameters**:
  - `radius`: Radius of the circle (float)
  - `vertices`: Number of vertices/points (int)
  - `name`: Name for the curve object (string)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created curve object

#### `create_spiral_curve(turns=2, height=5.0, radius=1.0, points=64, name="SpiralCurve", location=(0, 0, 0))`
- **Description**: Creates a spiral curve
- **Parameters**:
  - `turns`: Number of full rotations in the spiral (int)
  - `height`: Total height of the spiral (float)
  - `radius`: Maximum radius of the spiral (float)
  - `points`: Number of points in the spiral (int)
  - `name`: Name for the curve object (string)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created curve object

#### `create_helix_curve(turns=2, height=5.0, radius=1.0, points=64, name="HelixCurve", location=(0, 0, 0))`
- **Description**: Creates a helix (coil) curve
- **Parameters**:
  - `turns`: Number of full rotations in the helix (int)
  - `height`: Total height of the helix (float)
  - `radius`: Radius of the helix (float)
  - `points`: Number of points in the helix (int)
  - `name`: Name for the curve object (string)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created curve object

#### `create_text_curve(text="Blender", font_size=1.0, extrude=0.0, name="TextCurve", location=(0, 0, 0))`
- **Description**: Creates a curve from text (converts text to curve)
- **Parameters**:
  - `text`: The text content (string)
  - `font_size`: Size of the font (float)
  - `extrude`: Extrusion depth (float)
  - `name`: Name for the curve object (string)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created curve object

#### `save_blend_file(filepath, obj=None)`
- **Description**: Saves the current scene or specific object to a .blend file
- **Parameters**:
  - `filepath`: Path to save the .blend file (string)
  - `obj`: Optional object to save. If None, saves the entire scene
- **Returns**: None

#### `create_all_curve_types(save_dir="./blend_files/curve_types/")`
- **Description**: Creates all curve types and saves them as individual .blend files
- **Parameters**:
  - `save_dir`: Directory to save the .blend files (string)
- **Returns**: None

---

## 3. surface_creator.py

Creates various surface objects, allowing for customization of their parameters.

### Functions

#### `clear_scene()`
- **Description**: Removes all objects from the current scene
- **Parameters**: None
- **Returns**: None

#### `create_nurbs_surface(size=2.0, u_res=4, v_res=4, name="NurbsSurface", location=(0, 0, 0))`
- **Description**: Creates a NURBS surface
- **Parameters**:
  - `size`: Size of the surface (float)
  - `u_res`: Number of control points in U direction (approximated) (int)
  - `v_res`: Number of control points in V direction (approximated) (int)
  - `name`: Name for the surface object (string)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created surface object

#### `create_nurbs_cylinder(radius=1.0, height=2.0, u_segments=8, v_segments=4, name="NurbsCylinder", location=(0, 0, 0))`
- **Description**: Creates a NURBS cylinder surface
- **Parameters**:
  - `radius`: Radius of the cylinder (float)
  - `height`: Height of the cylinder (float)
  - `u_segments`: Number of segments around the circumference (int)
  - `v_segments`: Number of segments along the height (int)
  - `name`: Name for the surface object (string)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created surface object

#### `create_nurbs_sphere(radius=1.0, u_segments=8, v_segments=8, name="NurbsSphere", location=(0, 0, 0))`
- **Description**: Creates a NURBS sphere surface
- **Parameters**:
  - `radius`: Radius of the sphere (float)
  - `u_segments`: Number of segments around the longitude (int)
  - `v_segments`: Number of segments around the latitude (int)
  - `name`: Name for the surface object (string)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created surface object

#### `create_custom_torus(major_radius=1.5, minor_radius=0.5, u_segments=16, v_segments=8, name="NurbsTorus", location=(0, 0, 0))`
- **Description**: Creates a torus surface by starting with a sphere and manipulating it
- **Parameters**:
  - `major_radius`: Major radius of the torus (float)
  - `minor_radius`: Minor radius of the torus (float)
  - `u_segments`: Number of segments around the major circle (int)
  - `v_segments`: Number of segments around the minor circle (int)
  - `name`: Name for the surface object (string)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created surface object

#### `create_nurbs_ring(radius=1.0, inner_radius=0.7, u_segments=16, rings=1, name="RingSurface", location=(0, 0, 0))`
- **Description**: Creates a ring surface mesh
- **Parameters**:
  - `radius`: Outer radius of the ring (float)
  - `inner_radius`: Inner radius of the ring (float)
  - `u_segments`: Number of segments around the circumference (int)
  - `rings`: Number of subdivisions between inner and outer radius (int)
  - `name`: Name for the surface object (string)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created surface object

#### `create_landscape_surface(width=10.0, height=10.0, x_res=32, y_res=32, height_scale=1.0, noise_scale=1.0, name="Landscape", location=(0, 0, 0))`
- **Description**: Creates a landscape surface mesh with procedural noise
- **Parameters**:
  - `width`: Width of the landscape (float)
  - `height`: Length of the landscape (float)
  - `x_res`: Resolution in X direction (int)
  - `y_res`: Resolution in Y direction (int)
  - `height_scale`: Scale factor for height variation (float)
  - `noise_scale`: Scale of the noise pattern (float)
  - `name`: Name for the landscape object (string)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created landscape object

#### `create_disk_surface(radius=1.0, inner_radius=0.0, sectors=32, rings=8, name="DiskSurface", location=(0, 0, 0))`
- **Description**: Creates a disk surface mesh
- **Parameters**:
  - `radius`: Outer radius of the disk (float)
  - `inner_radius`: Inner radius of the disk (0 for full disk, >0 for ring) (float)
  - `sectors`: Number of sectors (divisions around the circumference) (int)
  - `rings`: Number of rings (divisions between inner and outer radius) (int)
  - `name`: Name for the disk object (string)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created disk object

#### `create_nurbs_patch_4x4(name="NurbsPatch", location=(0, 0, 0))`
- **Description**: Creates a simple 4x4 NURBS patch surface
- **Parameters**:
  - `name`: Name for the surface object (string)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created surface object

#### `save_blend_file(filepath, obj=None)`
- **Description**: Saves the current scene or specific object to a .blend file
- **Parameters**:
  - `filepath`: Path to save the .blend file (string)
  - `obj`: Optional object to save. If None, saves the entire scene
- **Returns**: None

#### `create_all_surface_types(save_dir="./blend_files/surface_types/")`
- **Description**: Creates all surface types and saves them as individual .blend files
- **Parameters**:
  - `save_dir`: Directory to save the .blend files (string)
- **Returns**: None

---

## 4. meta_creator.py

Creates meta objects (also known as metaballs or implicit surfaces).

### Functions

#### `clear_scene()`
- **Description**: Removes all objects from the current scene
- **Parameters**: None
- **Returns**: None

#### `create_meta_ball(radius=1.0, name="MetaBall", location=(0, 0, 0))`
- **Description**: Creates a meta ball object
- **Parameters**:
  - `radius`: Radius of the meta ball (float)
  - `name`: Name for the meta object (string)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created meta object

#### `create_meta_capsule(radius=1.0, size_x=2.0, name="MetaCapsule", location=(0, 0, 0))`
- **Description**: Creates a meta capsule object
- **Parameters**:
  - `radius`: Radius of the meta capsule (float)
  - `size_x`: Length of the capsule (float)
  - `name`: Name for the meta object (string)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created meta object

#### `create_meta_plane(radius=1.0, size_x=2.0, name="MetaPlane", location=(0, 0, 0))`
- **Description**: Creates a meta plane object
- **Parameters**:
  - `radius`: Radius of the meta plane (float)
  - `size_x`: Size of the plane (float)
  - `name`: Name for the meta object (string)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created meta object

#### `create_meta_ellipsoid(radius=1.0, size_x=1.5, size_y=1.0, size_z=1.0, name="MetaEllipsoid", location=(0, 0, 0))`
- **Description**: Creates a meta ellipsoid object
- **Parameters**:
  - `radius`: Base radius of the meta ellipsoid (float)
  - `size_x`: X size of the ellipsoid (float)
  - `size_y`: Y size of the ellipsoid (float)
  - `size_z`: Z size of the ellipsoid (float)
  - `name`: Name for the meta object (string)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created meta object

#### `create_meta_cube(radius=1.0, size=1.5, name="MetaCube", location=(0, 0, 0))`
- **Description**: Creates a meta cube object
- **Parameters**:
  - `radius`: Base radius of the meta cube (float)
  - `size`: Size of the cube (float)
  - `name`: Name for the meta object (string)
  - `location`: (x, y, z) tuple for object location
- **Returns**: The created meta object

#### `create_meta_molecule(positions=None, radii=None, name="MetaMolecule", location=(0, 0, 0))`
- **Description**: Creates a molecule-like structure using multiple meta balls
- **Parameters**:
  - `positions`: List of (x, y, z) tuples for positions of each meta ball. If None, uses default positions
  - `radii`: List of radii for each meta ball. If None, uses default radii
  - `name`: Base name for the meta object (string)
  - `location`: (x, y, z) tuple for object's center location
- **Returns**: The created meta object

#### `create_meta_blob(name="MetaBlob", seed=42, num_elements=5, location=(0, 0, 0))`
- **Description**: Creates a random blob using multiple meta balls
- **Parameters**:
  - `name`: Name for the meta object (string)
  - `seed`: Random seed for reproducibility (int)
  - `num_elements`: Number of meta elements to create (int)
  - `location`: (x, y, z) tuple for object's center location
- **Returns**: The created meta object

#### `create_meta_tubes(num_rings=3, balls_per_ring=8, radius=0.5, ring_radius=2.0, name="MetaTubes", location=(0, 0, 0))`
- **Description**: Creates a set of interconnected meta ball tubes
- **Parameters**:
  - `num_rings`: Number of rings of meta balls (int)
  - `balls_per_ring`: Number of meta balls in each ring (int)
  - `radius`: Radius of each meta ball (float)
  - `ring_radius`: Radius of the rings (float)
  - `name`: Name for the meta object (string)
  - `location`: (x, y, z) tuple for object's center location
- **Returns**: The created meta object

#### `create_meta_dna(turns=3, bases_per_turn=10, radius=0.3, helix_radius=1.0, height=6.0, name="MetaDNA", location=(0, 0, 0))`
- **Description**: Creates a DNA-like structure using meta balls
- **Parameters**:
  - `turns`: Number of full turns in the helix (int)
  - `bases_per_turn`: Number of base pairs per turn (int)
  - `radius`: Radius of each meta ball (float)
  - `helix_radius`: Radius of the helix (float)
  - `height`: Total height of the helix (float)
  - `name`: Name for the meta object (string)
  - `location`: (x, y, z) tuple for object's center location
- **Returns**: The created meta object

#### `save_blend_file(filepath, obj=None)`
- **Description**: Saves the current scene or specific object to a .blend file
- **Parameters**:
  - `filepath`: Path to save the .blend file (string)
  - `obj`: Optional object to save. If None, saves the entire scene
- **Returns**: None

#### `create_all_meta_types(save_dir="./blend_files/meta_types/")`
- **Description**: Creates all meta object types and saves them as individual .blend files
- **Parameters**:
  - `save_dir`: Directory to save the .blend files (string)
- **Returns**: None

---

## 5. text_creator.py

Creates text objects with various styles and properties.

### Functions

#### `clear_scene()`
- **Description**: Removes all objects from the current scene
- **Parameters**: None
- **Returns**: None

#### `create_text_object(text="Blender", name="TextObject", location=(0, 0, 0), size=1.0, extrude=0.0, bevel_depth=0.0, bevel_resolution=0)`
- **Description**: Creates a basic text object
- **Parameters**:
  - `text`: The text content (string)
  - `name`: Name for the text object (string)
  - `location`: (x, y, z) tuple for object location
  - `size`: Font size (float)
  - `extrude`: Extrusion depth (float)
  - `bevel_depth`: Bevel depth (for rounded edges) (float)
  - `bevel_resolution`: Bevel resolution (subdivisions) (int)
- **Returns**: The created text object

#### `create_3d_text(text="3D", name="3DText", location=(0, 0, 0), size=1.0, extrude=0.25, bevel_depth=0.05, bevel_resolution=3)`
- **Description**: Creates a 3D text object with extrusion and beveling
- **Parameters**:
  - `text`: The text content (string)
  - `name`: Name for the text object (string)
  - `location`: (x, y, z) tuple for object location
  - `size`: Font size (float)
  - `extrude`: Extrusion depth (float)
  - `bevel_depth`: Bevel depth (for rounded edges) (float)
  - `bevel_resolution`: Bevel resolution (subdivisions) (int)
- **Returns**: The created text object

#### `set_text_alignment(text_obj, align_x='CENTER', align_y='CENTER')`
- **Description**: Sets the text alignment
- **Parameters**:
  - `text_obj`: The text object to modify
  - `align_x`: Horizontal alignment ('LEFT', 'CENTER', 'RIGHT', 'JUSTIFY', 'FLUSH') (string)
  - `align_y`: Vertical alignment ('TOP', 'CENTER', 'BOTTOM', 'TOP_BASELINE', 'BOTTOM_BASELINE') (string)
- **Returns**: None

#### `set_text_font(text_obj, font_path=None)`
- **Description**: Sets the font for a text object
- **Parameters**:
  - `text_obj`: The text object to modify
  - `font_path`: Path to a font file. If None, uses the default font (string)
- **Returns**: True if successful, False otherwise

#### `create_text_on_curve(text="Text on Curve", curve_type='CIRCLE', name="CurvedText", location=(0, 0, 0), size=1.0, extrude=0.0, bevel_depth=0.0, curve_radius=2.0)`
- **Description**: Creates text that follows a curve path
- **Parameters**:
  - `text`: The text content (string)
  - `curve_type`: Type of curve ('CIRCLE', 'LINE', 'WAVE') (string)
  - `name`: Name for the text object (string)
  - `location`: (x, y, z) tuple for object location
  - `size`: Font size (float)
  - `extrude`: Extrusion depth (float)
  - `bevel_depth`: Bevel depth (for rounded edges) (float)
  - `curve_radius`: Radius of the curve (for circle) (float)
- **Returns**: Tuple of (text_object, curve_object)

#### `create_text_with_materials(text="Colorful", name="MaterialText", location=(0, 0, 0), size=1.0, extrude=0.2, color=(1, 0, 0, 1))`
- **Description**: Creates a text object with a material applied
- **Parameters**:
  - `text`: The text content (string)
  - `name`: Name for the text object (string)
  - `location`: (x, y, z) tuple for object location
  - `size`: Font size (float)
  - `extrude`: Extrusion depth (float)
  - `color`: (R, G, B, A) tuple for the material color
- **Returns**: The created text object

#### `create_multi_line_text(lines=None, name="MultiLineText", location=(0, 0, 0), size=1.0, line_spacing=1.5)`
- **Description**: Creates a multi-line text object
- **Parameters**:
  - `lines`: List of text lines. If None, uses default text (list of strings)
  - `name`: Name for the text object (string)
  - `location`: (x, y, z) tuple for object location
  - `size`: Font size (float)
  - `line_spacing`: Vertical spacing factor between lines (float)
- **Returns**: The created text object

#### `create_text_to_mesh(text="Mesh", name="TextMesh", location=(0, 0, 0), size=1.0, extrude=0.2, bevel_depth=0.05, shading='SMOOTH', convert=True)`
- **Description**: Creates a text object and optionally converts it to a mesh
- **Parameters**:
  - `text`: The text content (string)
  - `name`: Name for the text/mesh object (string)
  - `location`: (x, y, z) tuple for object location
  - `size`: Font size (float)
  - `extrude`: Extrusion depth (float)
  - `bevel_depth`: Bevel depth (for rounded edges) (float)
  - `shading`: Shading type ('FLAT', 'SMOOTH') (string)
  - `convert`: Whether to convert to mesh (True) or leave as text (False) (bool)
- **Returns**: The created object (text or mesh)

#### `create_text_with_animation(text="Animated", name="AnimatedText", location=(0, 0, 0), size=1.0, extrude=0.2, anim_type='ROTATE', frames=48)`
- **Description**: Creates a text object with a simple animation
- **Parameters**:
  - `text`: The text content (string)
  - `name`: Name for the text object (string)
  - `location`: (x, y, z) tuple for object location
  - `size`: Font size (float)
  - `extrude`: Extrusion depth (float)
  - `anim_type`: Animation type ('ROTATE', 'SCALE', 'FADE') (string)
  - `frames`: Number of frames for the animation cycle (int)
- **Returns**: The created text object

#### `create_extruded_logo_text(text="LOGO", name="LogoText", location=(0, 0, 0), size=1.0, extrude=0.5, bevel_depth=0.05, bevel_resolution=4, material_color=(0.2, 0.6, 1.0, 1.0))`
- **Description**: Creates an extruded text object suitable for a logo
- **Parameters**:
  - `text`: The text content (string)
  - `name`: Name for the text object (string)
  - `location`: (x, y, z) tuple for object location
  - `size`: Font size (float)
  - `extrude`: Extrusion depth (float)
  - `bevel_depth`: Bevel depth (for rounded edges) (float)
  - `bevel_resolution`: Bevel resolution (subdivisions) (int)
  - `material_color`: (R, G, B, A) tuple for the material color
- **Returns**: The created text object

#### `create_neon_text(text="NEON", name="NeonText", location=(0, 0, 0), size=1.0, extrude=0.1, bevel_depth=0.03, bevel_resolution=3, color=(0, 1, 0.8, 1))`
- **Description**: Creates a text object with a neon glow effect
- **Parameters**:
  - `text`: The text content (string)
  - `name`: Name for the text object (string)
  - `location`: (x, y, z) tuple for object location
  - `size`: Font size (float)
  - `extrude`: Extrusion depth (float)
  - `bevel_depth`: Bevel depth (for rounded edges) (float)
  - `bevel_resolution`: Bevel resolution (subdivisions) (int)
  - `color`: (R, G, B, A) tuple for the neon color
- **Returns**: