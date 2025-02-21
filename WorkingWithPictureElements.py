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

# Picture object
python_logo = lyt.listElements('PICTURE_ELEMENT',"python_logo")[0]
#python_logo.elementWidth = lyt.pageWidth - 20
python_logo.elementHeight = 25
python_logo.elementPositionX = 25
python_logo.elementPositionY = lyt.pageHeight -15
python_logo.sourceImage = r"D:\My_Files\ArcPy_Course\LPA\Images\python-powered-w-200x80.png"
python_logo.elementWidth = 25

# Export to PDF and open in Adobe Acrobat Reader
lyt.exportToPDF(r"D:\My_Files\ArcPy_Course\LPA\PDFs\test.pdf")
os.startfile(r"D:\My_Files\ArcPy_Course\LPA\PDFs\test.pdf")

# Delete project object
del aprx

