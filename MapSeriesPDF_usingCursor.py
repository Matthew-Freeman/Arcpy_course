import arcpy, os

arcpy.env.overwriteOutput = True



# Project object
aprx = arcpy.mp.ArcGISProject(r"D:\My_Files\ArcPy_Course\LPA\Projects\MapSeriesProject\MapSeriesProject.aprx")

# Map objects
mainMap = aprx.listMaps("Main Map")[0]
overviewMap = aprx.listMaps("Overview Map")[0]

# Layer objects
countriesLayer = mainMap.listLayers("Countries")[0]

# Layout object
lyt = aprx.listLayouts()[0]

# Map Frame objects
mainMapFrame = lyt.listElements("MAPFRAME_ELEMENT","Main Map Frame")[0]
overviewMapFrame = lyt.listElements("MAPFRAME_ELEMENT","Overview Map Frame")[0]

finalPDF = r"D:\My_Files\ArcPy_Course\LPA\PDFs\LayoutFromCursor.pdf"
if arcpy.Exists(finalPDF):
    arcpy.Delete_management(finalPDF)
pdfDoc = arcpy.mp.PDFDocumentCreate(finalPDF)

countriesSortedByNameList = sorted([row[0] for row in arcpy.da.SearchCursor(countriesLayer,"NAME")])
for pageCount, countryName in enumerate(countriesSortedByNameList[0:10]):
##with arcpy.da.SearchCursor(countriesLayer,["FID","NAME"],"FID < 10") as rows:
##    for row in rows:
        
    #countryName = "Austria"
    #countryName = row[1]
                
    # Set zoom
    countriesLayer.definitionQuery = r"NAME = '{0}'".format(countryName)
    #countriesLayer.definitionQuery = "NAME = 'Austria'"
    selCountryExtent = mainMapFrame.getLayerExtent(countriesLayer)
    mainMapFrame.camera.setExtent(selCountryExtent)
    mainMapFrame.camera.scale = mainMapFrame.camera.scale * 1.05
    countriesLayer.definitionQuery = ""  #turn of filter, display all countries.
    print(countryName)

    # Title text object (works without this?)
    titleText = lyt.listElements("TEXT_ELEMENT","Page Name")[0]
    titleText.text = countryName

    # Export to pdf
    lyt.exportToPDF(r"D:\My_Files\ArcPy_Course\LPA\PDFs\test{0}.pdf".format(pageCount))
    pdfDoc.appendPages(r"D:\My_Files\ArcPy_Course\LPA\PDFs\test{0}.pdf".format(pageCount))

# Save and close pdf, open in Adobe
pdfDoc.saveAndClose()
del pdfDoc
os.startfile(finalPDF)
