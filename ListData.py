import arcpy

##arcpy.env.workspace = r"D:\My_Files\ArcPy_Course\LPA"
##wsList = arcpy.ListWorkspaces()
##gdbListAll = []
##for workspace in wsList:
##    arcpy.env.workspace = workspace
##    gdbList = arcpy.ListWorkspaces("","FileGDB")
##    #print("{0} contains {1}".format(workspace,gdbList))
##    gdbListAll+=gdbList
##print("List of file geodatabases:\n{0}".format(gdbListAll))

##for gdb in gdbListAll:
##    arcpy.env.workspace = gdb
##    print("\nFeature classes in {0}:\n{1}".format(
##        gdb,arcpy.ListFeatureClasses()))
##    print("Feature datasets in {0}:\n{1}".format(
##        gdb,arcpy.ListDatasets("","Feature")))
##    fdList = arcpy.ListDatasets("","Feature")
##    for fd in fdList:
##        arcpy.env.workspace = r"{0}\{1}".format(gdb,fd)
##        print("\nFeature classes in feature dataset {0}:\n{1}".format(
##            arcpy.env.workspace,arcpy.ListFeatureClasses()))
##        


##for gdb in gdbListAll:
##    arcpy.env.workspace = gdb
##    print("\nTables in {0}:\n{1}".format(gdb,arcpy.ListTables()))


arcpy.env.workspace = r"D:\My_Files\ArcPy_Course\LPA\Data\Sample.gdb"
for tbl in arcpy.ListTables():
    fieldObjectList = arcpy.ListFields(tbl)
    #fieldNameList = [x.name for x in fieldObjectList]
    fieldNameTypeList = [[x.name,x.type] for x in fieldObjectList]
    print("\nFields in {0}\{1}:\n{2}".format(
        arcpy.env.workspace,tbl,fieldNameTypeList))

print("\nScript completed!")
