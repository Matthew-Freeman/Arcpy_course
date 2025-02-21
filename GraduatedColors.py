import arcpy

#graduated colors
#field to POP_EST
#classed to 8
#color scheme black to white
#save

aprx = arcpy.mp.ArcGISProject(r"D:\My_Files\ArcPy_Course\LPA\Projects\SymbologyProject\SymbologyProject.aprx")
mapx = aprx.listMaps("Map")[0]
lyr = mapx.listLayers("Countries coloured by")[0]

sym = lyr.symbology

sym.updateRenderer("GraduatedColorsRenderer")
sym.renderer.classificationField = "POP_EST"
sym.renderer.breakCount = 8
sym.renderer.colorRamp = aprx.listColorRamps("White to Black")[0]

lyr.symbology = sym

aprx.save()
del aprx
print("Script complete.")
