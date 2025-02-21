import arcpy

#workspace = r"D:\My_Files\ArcPy_Course\LPA\Data"
workspace = r"D:\My_Files\ArcPy_Course\LPA"

dataList = []
for dirpath, dirnames, filenames in arcpy.da.Walk(workspace,datatype="FeatureClass",type=["Point","Polyline"]):
    for filename in filenames:
        dataList.append(r"{0}\{1}".format(dirpath,filename))
        
print(dataList)
print("/nFound {0} data elements in {1}".format(len(dataList),workspace))


print("\nScript completed!")
