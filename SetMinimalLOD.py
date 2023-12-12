# For unreal python api, get selected assets and set min LOD for mobile platform if the selected assets are static mesh.

import unreal

# Get selected assets
selected_assets = unreal.EditorUtilityLibrary.get_selected_assets()

# Set min LOD for mobile platform
for asset in selected_assets:
    # Check if the asset is static mesh
    if isinstance(asset, unreal.StaticMesh):
        
        # Set min LOD for mobile platform
        asset.set_minimum_lod_for_platform("Windows", 3)
        # Save asset
        unreal.EditorAssetLibrary.save_loaded_asset(asset)
        # Print asset name
        print(asset.get_name() + ' set min LOD for mobile platform.')
    else:
        # Print asset name
        print(asset.get_name() + ' is not static mesh.')