import unreal

def listAssetPaths():

    EAL = unreal.EditorAssetLibrary

    assetPaths = EAL.list_assets('/Game')

    for assetPath in assetPaths: print (assetPath)

def getSelectionContentBrowser():

    EUL = unreal.EditorUtilityLibrary

    selectedAssets = EUL.get_selected_assets()

    for selectedAsset in selectedAssets: print(selectedAsset.get_outer().get_name())

def getAllActors():

    EAS = unreal.EditorActorSubsystem()

    actors = EAS.get_all_level_actors()

    for actor in actors: print(actor)

def getSelectedActors():
    
    EAS = unreal.EditorActorSubsystem()

    selectedActors = EAS.get_selected_level_actors()

    for selectedActor in selectedActors: print(selectedActor)

def getAssetClass(classType):
    EAL = unreal.EditorAssetLibrary
    assetPaths = EAL.list_assets('/Game')
    assets = []
    
    for assetPath in assetPaths:
        assetData = EAL.find_asset_data(assetPath)
        assetClass = assetData.asset_class_path
        if assetClass.asset_name == classType:
            assets.append(assetData.get_asset())
               
    for asset in assets: print(asset)
    return assets

def getStaticMeshData():
    staticMeshes = getAssetClass('StaticMesh')
    for staticMesh in staticMeshes:
        #assetImportData = staticMesh.get_editor_property('asset_import_data')
        #fbxFilePath = assetImportData.extract_filenames()
        #print(fbxFilePath)

        lodGroupInfo = staticMesh.get_editor_property('lod_group')
        #print(lodGroupInfo)

        if lodGroupInfo == None:
            print()
            #staticMesh.set_editor_property('lod_group')