import arcpy, os
arcpy.env.overwriteOutput = True

# Project object
aprx = arcpy.mp.ArcGISProject(r"D:\My_Files\ArcPy_Course\LPA\Projects\MGAZonesProject\MGAZonesProject.aprx")

# Map objects
map54 = aprx.listMaps("Map54")[0]
map55 = aprx.listMaps("Map55")[0]
map56 = aprx.listMaps("Map56")[0]

# Layer object
placesLayer = map54.listLayers("Queensland Places")[0]

# Layout object
lyt = aprx.listLayouts()[0]

# Map Frame objects
mapFrame54 = lyt.listElements("MAPFRAME_ELEMENT","Map Frame 54")[0]
mapFrame55 = lyt.listElements("MAPFRAME_ELEMENT","Map Frame 55")[0]
mapFrame56 = lyt.listElements("MAPFRAME_ELEMENT","Map Frame 56")[0]

# Spatial Reference Text objects
srText54 = lyt.listElements("TEXT_ELEMENT","Spatial Reference Text 54")[0]
srText55 = lyt.listElements("TEXT_ELEMENT","Spatial Reference Text 55")[0]
srText56 = lyt.listElements("TEXT_ELEMENT","Spatial Reference Text 56")[0]

# Create PDF document object
finalPDF = r"D:\My_Files\ArcPy_Course\LPA\PDFs\MGAZones.pdf"
if arcpy.Exists(finalPDF):
    arcpy.Delete_management(finalPDF)
pdfDoc = arcpy.mp.PDFDocumentCreate(finalPDF)

# Create list of place names sorted alphabetically
placesSortedByNameList = sorted([row[0] for row in arcpy.da.SearchCursor(placesLayer,"NAME")])

# Create dictionary of X, Y coordinates for each place
placesCoordsDict = {row[0]:row[1] for row in arcpy.da.SearchCursor(placesLayer,["NAME","SHAPE@XY"])}

# Create Spatial Reference object for the places layer which will be the Geographic Coordinate System of the source feature class
srPlacesLayer = arcpy.Describe(placesLayer).spatialReference

# Write one PDF page for each place in the sorted list
for pageCount, placeName in enumerate(placesSortedByNameList[:10]):
    xCoord, yCoord = placesCoordsDict[placeName]
    mgaZone = 1 + int((xCoord+180)/6)
    print("{0} is in zone {1}".format(placeName,mgaZone))
    srMGA = arcpy.SpatialReference("GDA2020 MGA Zone {0}".format(mgaZone))

    geogFC = r"{0}\geogFC".format(aprx.defaultGeodatabase)
    projFC = r"{0}\projFC".format(aprx.defaultGeodatabase)
    
    arcpy.CreateFishnet_management(geogFC,
                                   "{0} {1}".format(xCoord-0.25, yCoord-0.25),
                                   "{0} {1}".format(xCoord-0.25, yCoord+0.25),
                                   0.5,0.5,1,1,geometry_type="POLYGON",labels="NO_LABELS")

    arcpy.DefineProjection_management(geogFC,srPlacesLayer)
    arcpy.Project_management(geogFC,projFC,srMGA)
    projFCExtent = arcpy.Describe(projFC).extent

    if mgaZone == 54:
        mapFrame54.visible = True
        mapFrame55.visible = False
        mapFrame56.visible = False
        
        mapFrame54.camera.setExtent(projFCExtent)
        mapFrame54.camera.scale = mapFrame54.camera.scale *1.05
        
        srText54.visible = True
        srText55.visible = False
        srText56.visible = False
    elif mgaZone == 55:
        mapFrame54.visible = False
        mapFrame55.visible = True
        mapFrame56.visible = False
        
        mapFrame55.camera.setExtent(projFCExtent)
        mapFrame55.camera.scale = mapFrame55.camera.scale *1.05
        
        srText54.visible = False
        srText55.visible = True
        srText56.visible = False
    elif mgaZone == 56:
        mapFrame54.visible = False
        mapFrame55.visible = False
        mapFrame56.visible = True
        
        mapFrame56.camera.setExtent(projFCExtent)
        mapFrame56.camera.scale = mapFrame56.camera.scale *1.05
        
        srText54.visible = False
        srText55.visible = False
        srText56.visible = True
    else:
        print("Unexpected zone number of {0} encountered".format(mgaZone))

    #Title text object
    titleText = lyt.listElements("TEXT_ELEMENT","Title")[0]
    titleText.text = placeName

    #Export PDF for this countries page
    lyt.exportToPDF(r"D:\My_Files\ArcPy_Course\LPA\PDFs\test{0}.pdf".format(pageCount))
    pdfDoc.appendPages(r"D:\My_Files\ArcPy_Course\LPA\PDFs\test{0}.pdf".format(pageCount))

# Save and close PDF and open in Acrobat Reader
pdfDoc.saveAndClose()
del pdfDoc
os.startfile(finalPDF)

# Delete project object
del aprx
        

print("\nScript Completed!")
