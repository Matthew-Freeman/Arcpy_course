import arcpy

arcpy.env.overwriteOutput = True

aprx = arcpy.mp.ArcGISProject("D:\My_Files\ArcPy_Course\LPA\Projects\BookmarkProject\BookmarkProject.aprx")
mapx = aprx.listMaps()[0]
lyt = aprx.listLayouts()[0]
mf = lyt.listElements("MAPFRAME_ELEMENT","Map Frame")[0]

defaultGDB = aprx.defaultGeodatabase
bmFCName = "bmFC"
bmFC = r"{0}\{1}".format(defaultGDB,bmFCName)
sr = arcpy.SpatialReference("WGS 1984 Web Mercator (auxiliary sphere)")

arcpy.CreateFeatureclass_management(defaultGDB,bmFCName,"POLYGON",spatial_reference=sr)

arcpy.AddField_management(bmFC,"Name","TEXT","","",50)

cursor = arcpy.da.InsertCursor(bmFC,["SHAPE@","Name"])
array = arcpy.Array()
for bm in mapx.listBookmarks():
    print(bm.name)
    mf.zoomToBookmark(bm)
    extent = mf.camera.getExtent()
    array.add(arcpy.Point(extent.XMin,extent.YMin))
    array.add(arcpy.Point(extent.XMin,extent.YMax))
    array.add(arcpy.Point(extent.XMax,extent.YMax))
    array.add(arcpy.Point(extent.XMax,extent.YMin))
    # To close the polygon, add the first point again.
    array.add(arcpy.Point(extent.XMin,extent.YMin))
    cursor.insertRow([arcpy.Polygon(array),bm.name])
    array.removeAll()

del bm,array,cursor,aprx

print("Script complete")
