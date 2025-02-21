import arcpy,os

# Enable overwriting of outputs
arcpy.env.overwriteOutput = True

# Project object
aprx = arcpy.mp.ArcGISProject(
    r"D:\My_Files\ArcPy_Course\LPA\Projects\LayoutProject\LayoutProject.aprx")

# Map object
mapx = aprx.listMaps("Map")[0]

# Layer object
countriesLayer = mapx.listLayers("Countries")[0]

# Layout object
lyt = aprx.listLayouts()[0]

# Map Frame object
mapFrame = lyt.listElements('MAPFRAME_ELEMENT',"Map Frame")[0]
mapFrame.elementWidth = lyt.pageWidth - 20
mapFrame.elementHeight = mapFrame.elementWidth
mapFrame.elementPositionX = 10
mapFrame.elementPositionY = lyt.pageHeight / 4
mapFrame.camera.heading = -25
mapFrame.camera.scale = 15000000
print(mapFrame.camera.scale)

# Mapsurround objects
northArrow = lyt.listElements('MAPSURROUND_ELEMENT',"North Arrow")[0]
#northArrow.elementWidth = lyt.pageWidth - 20
northArrow.elementHeight = 30
northArrow.elementPositionX = lyt.pageWidth - 40
northArrow.elementPositionY = 40

scaleBar = lyt.listElements('MAPSURROUND_ELEMENT',"Scale Bar")[0]
#scaleBar.elementHeight = 30
scaleBar.elementPositionX = lyt.pageWidth/2
scaleBar.elementPositionY = 60

# Export to PDF and open in Adobe Acrobat Reader
lyt.exportToPDF(r"D:\My_Files\ArcPy_Course\LPA\PDFs\test.pdf")
os.startfile(r"D:\My_Files\ArcPy_Course\LPA\PDFs\test.pdf")

# Delete project object
del aprx

