import arcpy

#Make state capitals
#airport symbol
#size 20
#bright red, 75% opacity
#angle 45 degrees

aprx = arcpy.mp.ArcGISProject(r"D:\My_Files\ArcPy_Course\LPA\Projects\SymbologyProject\SymbologyProject.aprx")
mapx = aprx.listMaps()[0]
lyr = mapx.listLayers("State Capitals")[0]
sym = lyr.symbology

sym.renderer.symbol.applySymbolFromGallery("Airport")
sym.renderer.symbol.color = {"RGB":[255,0,0,75]}
sym.renderer.symbol.size = 20
sym.renderer.symbol.angle = 45
lyr.symbology = sym

aprx.save()
del aprx
print("Script complete.")
