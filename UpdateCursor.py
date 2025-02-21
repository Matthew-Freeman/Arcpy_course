import arcpy


shp = r"D:\My_Files\ArcPy_Course\LPA\Data\ne_10m_admin_0_countries.shp"
fc = r"D:\My_Files\ArcPy_Course\LPA\Projects\CursorProject\CursorProject.gdb\Countries"
arcpy.env.overwriteOutput = True
arcpy.management.CopyFeatures(
    in_features=shp,
    out_feature_class=fc,
    config_keyword="",
    spatial_grid_1=None,
    spatial_grid_2=None,
    spatial_grid_3=None
)
##for field in arcpy.ListFields(shp):
##    print(field.name)
arcpy.management.AddField(fc,"GDPperPerson","FLOAT")
with arcpy.da.UpdateCursor(fc,["NAME","GDP_MD","POP_EST","GDPperPerson"]) as cursor:
    for row in cursor:
        row[0] = row[0].upper()
        if row[2] == 0:
            row[3] = 0
        else:     
            row[3] = (row[1]*1000000)/row[2]
        if row[3] >= 10000:
            cursor.deleteRow()
        else:
            cursor.updateRow(row)
            print("{0} GDPP: US${1}".format(row[0],int(row[3])))
        #print(row[0])



print("\nScript completed!")
