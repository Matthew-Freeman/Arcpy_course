import arcpy

#Solid stroke to Black 2pts
#Shape marker to Black, 1pt wide 10pt long hatch marks
#Space hatch marks 7.5,25.


aprx = arcpy.mp.ArcGISProject(r"D:\My_Files\ArcPy_Course\LPA\Projects\SymbologyProject\SymbologyProject.aprx")
mapx = aprx.listMaps("Map")[0]
lyrx = mapx.listLayers("Railroads")[0]
cim_def = lyrx.getDefinition("V2")

symLyr1 = cim_def.renderer.symbol.symbol.symbolLayers[0]  #shapeMarkerSymLyr
symLyr2 = cim_def.renderer.symbol.symbol.symbolLayers[1]  #solidStrokeSymLyr

symLyr2.width = 2
symLyr2.color.values = [0,0,0,100]

symLyr1.size = 10
symLyr1.markerGraphics[0].symbol.symbolLayers[0].width = 1    #lineMarkerSymLyr
symLyr1.markerGraphics[0].symbol.symbolLayers[0].color.values = [0,0,0,100]
symLyr1.markerPlacement.placementTemplate = [7.5,25]

lyrx.setDefinition(cim_def)

aprx.save()
del aprx
print("Script complete.")
