import arcpy

arcpy.env.overwriteOutput = True
#print(arcpy.env.workspace)
arcpy.env.workspace = r"D:\My_Files\ArcPy_Course\LPA\Data\test.gdb"
##if arcpy.Exists(r"D:\My_Files\ArcPy_Course\LPA\Data\test.gdb"):
##    arcpy.Delete_management(r"D:\My_Files\ArcPy_Course\LPA\Data\test.gdb")
arcpy.CreateFileGDB_management(r"D:\My_Files\ArcPy_Course\LPA\Data","test")
#arcpy.management.CreateFileGDB(r"D:\My_Files\ArcPy_Course\LPA\Data","test")

arcpy.FeatureClassToFeatureClass_conversion(
    r"D:\My_Files\ArcPy_Course\LPA\Data\ne_10m_admin_0_countries.shp",
    r"D:\My_Files\ArcPy_Course\LPA\Data\test.gdb","Countries")
    
print(arcpy.Exists(r"D:\My_Files\ArcPy_Course\LPA\Data\test.gdb\Countries"))
    
arcpy.Select_analysis("Countries","TrinidadTobago","NAME = 'Trinidad and Tobago'")
print(arcpy.Exists(r"D:\My_Files\ArcPy_Course\LPA\Data\test.gdb\TrinidadTobago"))

arcpy.Buffer_analysis("TrinidadTobago","TrinidadTobago_EEZ","200 NauticalMiles",method="GEODESIC")
print(arcpy.Exists(r"D:\My_Files\ArcPy_Course\LPA\Data\test.gdb\TrinidadTobago_EEZ"))

arcpy.FeatureClassToFeatureClass_conversion(
    r"D:\My_Files\ArcPy_Course\LPA\Data\ne_10m_admin_1_states_provinces.shp",
    r"D:\My_Files\ArcPy_Course\LPA\Data\test.gdb","States")
print(arcpy.GetCount_management("States"))

arcpy.env.extent = "TrinidadTobago_EEZ"
arcpy.CopyFeatures_management("States","StatesInExtent")
print(arcpy.GetCount_management("StatesInExtent"))


print("\nScript completed")
