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

#Graphic objects
borderLineLeft = lyt.listElements("GRAPHIC_ELEMENT","border_line")[0]
borderLineLeft.name = "border_line_left"
borderLineLeft.elementWidth = 0
borderLineLeft.elementHeight = lyt.pageHeight
borderLineLeft.elementPositionX = 5
borderLineLeft.elementPositionY = lyt.pageHeight / 2

borderLineRight = borderLineLeft.clone()
borderLineRight.name = "border_line_right"
borderLineRight.elementPositionX = lyt.pageWidth -5

borderLineTop = borderLineLeft.clone()
borderLineTop.name = "border_line_top"
borderLineTop.elementWidth = lyt.pageWidth
borderLineTop.elementHeight = 0
borderLineTop.elementPositionX = lyt.pageWidth/2
borderLineTop.elementPositionY = lyt.pageHeight -5

borderLineBottom = borderLineTop.clone()
borderLineTop.name = "border_line_bottom"
borderLineBottom.elementPositionY = 5

borderPointTopLeft = lyt.listElements("GRAPHIC_ELEMENT","border_point")[0]
borderPointTopLeft.name = "border_point_top_left"
borderPointTopLeft.elementPositionX = 2.5
borderPointTopLeft.elementPositionY = lyt.pageHeight - 2.5

borderPointTopRight = borderPointTopLeft.clone() 
borderPointTopRight.name = "border_point_top_right"
borderPointTopRight.elementPositionX = lyt.pageWidth - 2.5
borderPointTopRight.elementPositionY = lyt.pageHeight - 2.5

borderPointBottomRight = borderPointTopLeft.clone() 
borderPointBottomRight.name = "border_point_bottom_right"
borderPointBottomRight.elementPositionX = lyt.pageWidth - 2.5
borderPointBottomRight.elementPositionY = 2.5

borderPointBottomLeft = borderPointTopLeft.clone() 
borderPointBottomLeft.name = "border_point_bottom_left"
borderPointBottomLeft.elementPositionX = 2.5
borderPointBottomLeft.elementPositionY = 2.5

# Export to PDF and open in Adobe Acrobat Reader
lyt.exportToPDF(r"D:\My_Files\ArcPy_Course\LPA\PDFs\test.pdf")
os.startfile(r"D:\My_Files\ArcPy_Course\LPA\PDFs\test.pdf")

# Delete project object
del aprx

