import arcpy

arcpy.env.overwriteOutput = True
fGDB = r"D:\My_Files\ArcPy_Course\LPA\Projects\CursorProject\CursorProject.gdb"
##tableName = "TestTable"
##fgdbTable = r"{0}\{1}".format(fGDB,tableName)
##arcpy.management.CreateTable(fGDB,tableName)
##arcpy.management.AddField(fgdbTable,"TextField","TEXT",field_length=5)
##arcpy.management.AddField(fgdbTable,"IntField","SHORT")
##arcpy.management.AddField(fgdbTable,"FloatField","FLOAT")
##
##fieldList = ["TextField","IntField","FloatField"]
##cursor = arcpy.da.InsertCursor(fgdbTable,fieldList)
##cursor.insertRow(["A",1,0.0])
##cursor.insertRow(["B",2,5.5])
##cursor.insertRow(["C",3,9.9])
##del cursor
##
##with arcpy.da.SearchCursor(fgdbTable,fieldList) as cursor:
##    for row in cursor:
##        print(row)


shp = r"D:\My_Files\ArcPy_Course\LPA\Data\ne_10m_admin_0_countries.shp"
##fc = r"D:\My_Files\ArcPy_Course\LPA\Projects\CursorProject\CursorProject.gdb\Countries"
##arcpy.management.CopyFeatures(shp,fc)
##
##cursor = arcpy.da.InsertCursor(fc,["SHAPE@","NAME"])
##
##srWGS84 = arcpy.SpatialReference("WGS 1984")
##nullIslandPoint = arcpy.Point(0,0)
##nullIslandGeom = arcpy.PointGeometry(nullIslandPoint,srWGS84).buffer(5)
##cursor.insertRow([nullIslandGeom,"Null Island"])
##del cursor

fieldList = ["NAME","CONTINENT","POP_EST"]#,"GDP_MD"]

fieldLengthList = []
for field in fieldList:
    fieldLengthList.append(
        max([len(str(row[0])) for row in arcpy.da.SearchCursor(shp,[field])]))
print(fieldLengthList)
maxFieldLength = max(fieldLengthList)
print(maxFieldLength)

tableFCName = "TableFC"
tableFC = r"{0}\{1}".format(fGDB,tableFCName)
arcpy.management.CreateFeatureclass(fGDB,tableFCName,"POLYGON")
arcpy.management.AddField(tableFC,"TextField","TEXT",field_length=maxFieldLength)

cursor = arcpy.da.InsertCursor(tableFC,["SHAPE@","TextField"])
accumWidth = 0.0
headerHeight = 3.0
for i in range(0,len(fieldList)):
    tableCellText = fieldList[i]
    tableCellGeom = arcpy.Polygon(
        arcpy.Array([arcpy.Point(accumWidth,0.0),
                     arcpy.Point(accumWidth,headerHeight),
                     arcpy.Point(accumWidth+fieldLengthList[i],headerHeight),
                     arcpy.Point(accumWidth+fieldLengthList[i],0.0)]))
    cursor.insertRow([tableCellGeom,tableCellText])
    accumWidth+=fieldLengthList[i]
##del cursor

fidFieldList = ["FID"] + fieldList
fidDataDict = {row[0]:[row[n] for n in range(
    1,len(fieldList)+1)] for row in arcpy.da.SearchCursor(
        shp,fidFieldList,"FID < 25")}
print(fidDataDict)


accumWidth = 0.0
cellHeight = -1.5
for i in range(0,len(fieldList)):
    for j in range(0,len(fidDataDict)):
        tableCellText = fidDataDict[j][i]
        tableCellGeom = arcpy.Polygon(
        arcpy.Array([arcpy.Point(accumWidth,cellHeight*j),
                     arcpy.Point(accumWidth,cellHeight*(j+1)),
                     arcpy.Point(accumWidth+fieldLengthList[i],cellHeight*(j+1)),
                     arcpy.Point(accumWidth+fieldLengthList[i],cellHeight*j)]))
        cursor.insertRow([tableCellGeom,tableCellText])
    accumWidth+=fieldLengthList[i]
del cursor


print("\nScript completed!")
