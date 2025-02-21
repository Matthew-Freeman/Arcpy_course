import arcpy,os

countryName = "Malaysia"

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

#Set zoom area
countriesLayer.definitionQuery = "NAME = '{0}'".format(countryName)
selCountryExtent = mapFrame.getLayerExtent(countriesLayer)
#selCountryExtent = mapx.getLayerExtent(countriesLayer) #doesn't work, have to get extent from mapframe element
mapFrame.camera.setExtent(selCountryExtent)
mapFrame.camera.scale = mapFrame.camera.scale * 1.05

#Text Objects
titleText = lyt.listElements("TEXT_ELEMENT","title_text")[0]
titleText.textSize = 20
titleText.elementPositionX = lyt.pageWidth/2
titleText.elementPositionY = lyt.pageHeight - 10
titleText.text = "<BOL>{0}</BOL>".format(countryName)

subtitleText = titleText.clone()
subtitleText.textSize = 14
subtitleText.text = "Map of Country with Topographic Background"
subtitleText.elementPositionY = lyt.pageHeight - 20

datePathText = titleText.clone()
datePathText.text = 'PDF created <dyn type="date" format="long"/> from <dyn type="project" property="path"/>'
datePathText.textSize = 7
datePathText.elementPositionY = 5
#<dyn type="time" format=""/>

# Export to PDF and open in Adobe Acrobat Reader
lyt.exportToPDF(r"D:\My_Files\ArcPy_Course\LPA\PDFs\test.pdf")
os.startfile(r"D:\My_Files\ArcPy_Course\LPA\PDFs\test.pdf")

# Delete project object
del aprx

